from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, tzinfo

from .models import ActivityEvent, ActivityReport

GITHUB_API_URL = "https://api.github.com"
MAX_EVENTS = 100
REQUEST_TIMEOUT_SECONDS = 20
SAFE_TEXT_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


@dataclass(frozen=True)
class ActivityWindow:
    target_date: date
    timezone: tzinfo


class GitHubActivityClient:
    def __init__(self, username: str, token: str = "") -> None:
        self._username = username
        self._token = token

    def fetch_for_date(self, target_date: date, timezone: tzinfo) -> ActivityReport:
        window = ActivityWindow(target_date=target_date, timezone=timezone)
        try:
            events = self._request_events()
        except (OSError, ValueError) as error:
            return ActivityReport(
                status="unavailable",
                source="GitHub public events API",
                events=(),
                message=_safe_error_message(error),
            )

        normalized = tuple(
            event
            for raw_event in events
            if (event := self._normalize_event(raw_event, window)) is not None
        )
        return ActivityReport(
            status="ok",
            source="GitHub public events API",
            events=normalized,
        )

    def _request_events(self) -> list[dict[str, object]]:
        username = urllib.parse.quote(self._username, safe="")
        url = f"{GITHUB_API_URL}/users/{username}/events/public?per_page={MAX_EVENTS}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "engineering-log-generator",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"

        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not isinstance(payload, list):
            raise ValueError("GitHub events response was not a list")
        return [event for event in payload if isinstance(event, dict)]

    def _normalize_event(
        self,
        raw_event: dict[str, object],
        window: ActivityWindow,
    ) -> ActivityEvent | None:
        created_at = raw_event.get("created_at")
        repository = _nested_string(raw_event, "repo", "name")
        event_type = raw_event.get("type")
        if not isinstance(created_at, str) or not repository or not isinstance(event_type, str):
            return None
        if repository.lower() == f"{self._username}/engineering-log".lower():
            return None

        occurred_at = datetime.fromisoformat(created_at.replace("Z", "+00:00")).astimezone(
            window.timezone
        )
        if occurred_at.date() != window.target_date:
            return None

        summary, url = _describe_event(event_type, raw_event, repository)
        if not summary:
            return None
        return ActivityEvent(
            occurred_at=occurred_at.isoformat(timespec="seconds"),
            repository=repository,
            kind=event_type,
            summary=_clean_text(summary),
            url=url,
        )


def _describe_event(
    event_type: str,
    raw_event: dict[str, object],
    repository: str,
) -> tuple[str, str]:
    payload = raw_event.get("payload")
    details = payload if isinstance(payload, dict) else {}
    repository_url = f"https://github.com/{repository}"

    if event_type == "PushEvent":
        count = details.get("distinct_size", details.get("size", 0))
        ref = str(details.get("ref", "")).removeprefix("refs/heads/")
        return f"Push {count} commit ke branch {ref or 'unknown'}", repository_url
    if event_type == "PullRequestEvent":
        action = str(details.get("action", "updated"))
        number = details.get("number", "?")
        url = f"{repository_url}/pull/{number}" if str(number).isdigit() else repository_url
        return f"Pull request #{number} {action}", url
    if event_type == "IssuesEvent":
        action = str(details.get("action", "updated"))
        issue = details.get("issue")
        number = issue.get("number", "?") if isinstance(issue, dict) else "?"
        url = f"{repository_url}/issues/{number}" if str(number).isdigit() else repository_url
        return f"Issue #{number} {action}", url
    if event_type == "CreateEvent":
        ref_type = str(details.get("ref_type", "resource"))
        ref = details.get("ref")
        suffix = f" {ref}" if ref else ""
        return f"Membuat {ref_type}{suffix}", repository_url
    if event_type == "ReleaseEvent":
        action = str(details.get("action", "published"))
        return f"Release {action}", f"{repository_url}/releases"
    return "", repository_url


def _nested_string(record: dict[str, object], parent: str, child: str) -> str:
    nested = record.get(parent)
    if not isinstance(nested, dict):
        return ""
    value = nested.get(child)
    return value if isinstance(value, str) else ""


def _clean_text(value: str) -> str:
    without_controls = SAFE_TEXT_PATTERN.sub("", value)
    return without_controls.replace("\n", " ").replace("\r", " ").strip()[:300]


def _safe_error_message(error: Exception) -> str:
    if isinstance(error, urllib.error.HTTPError):
        return f"GitHub API returned HTTP {error.code}"
    return error.__class__.__name__
