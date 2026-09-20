from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from datetime import date, timedelta, timezone
from pathlib import Path
from typing import Any

from .activity import GitHubActivityClient
from .curriculum import load_curriculum, select_topic
from .journal import render_activity_report, render_note, update_readme_latest
from .models import (
    ActivityReport,
    GenerationMetadata,
    GenerationResult,
    NoteContext,
    RuntimeConfig,
    StudyContent,
    Topic,
    TopicSelection,
)
from .openrouter import OpenRouterClient, OpenRouterError, fallback_content

JAKARTA_TIMEZONE = timezone(timedelta(hours=7), name="Asia/Jakarta")


@dataclass(frozen=True)
class ProgressUpdate:
    progress: dict[str, Any]
    selection: TopicSelection
    note_path: Path
    is_new_entry: bool


class DailyLogGenerator:
    def __init__(self, config: RuntimeConfig) -> None:
        self._config = config

    def run(self) -> GenerationResult:
        root = self._config.repository_root
        topics = load_curriculum(root / "config" / "curriculum.json")
        progress = _load_progress(root / "data" / "progress.json")
        date_key = self._config.target_date.isoformat()
        existing_entry = _progress_entry(progress, date_key)
        selection = _select_for_run(topics, progress, existing_entry)
        note_path = _note_path(selection, self._config.target_date)
        report_path = _report_path(self._config.target_date)

        if (root / note_path).exists() and not self._config.force:
            return GenerationResult(
                note_path=note_path,
                report_path=report_path,
                created=False,
                generator="existing",
                model="existing",
            )

        activity = self._collect_activity()
        content, metadata = self._generate_content(selection, activity)
        context = NoteContext(
            target_date=self._config.target_date,
            selection=selection,
            content=content,
            activity=activity,
            generation=metadata,
        )
        _write_text(root / note_path, render_note(context))
        _write_text(root / report_path, render_activity_report(context))
        self._update_readme(note_path, context)
        self._update_progress(
            ProgressUpdate(
                progress=progress,
                selection=selection,
                note_path=note_path,
                is_new_entry=existing_entry is None,
            )
        )
        return GenerationResult(
            note_path=note_path,
            report_path=report_path,
            created=True,
            generator=metadata.generator,
            model=metadata.model,
        )

    def _collect_activity(self) -> ActivityReport:
        if self._config.offline:
            return ActivityReport(
                status="offline",
                source="GitHub public events API",
                events=(),
                message="Offline mode",
            )
        client = GitHubActivityClient(
            username=self._config.github_username,
            token=self._config.github_token,
        )
        return client.fetch_for_date(self._config.target_date, JAKARTA_TIMEZONE)

    def _generate_content(
        self,
        selection: TopicSelection,
        activity: ActivityReport,
    ) -> tuple[StudyContent, GenerationMetadata]:
        if self._config.offline or not self._config.openrouter_api_key:
            return fallback_content(selection), GenerationMetadata(
                generator="curriculum-fallback",
                model="none",
            )

        client = OpenRouterClient(
            api_key=self._config.openrouter_api_key,
            model=self._config.openrouter_model,
            repository_url=self._config.repository_url,
        )
        try:
            result = client.generate(selection, activity)
        except (OpenRouterError, OSError, ValueError):
            return fallback_content(selection), GenerationMetadata(
                generator="curriculum-fallback",
                model="none",
            )
        return result.content, GenerationMetadata(
            generator="openrouter",
            model=result.model,
        )

    def _update_readme(self, note_path: Path, context: NoteContext) -> None:
        readme_path = self._config.repository_root / "README.md"
        updated = update_readme_latest(
            readme_path.read_text(encoding="utf-8"),
            note_path,
            context,
        )
        _write_text(readme_path, updated)

    def _update_progress(self, update: ProgressUpdate) -> None:
        date_key = self._config.target_date.isoformat()
        entries = update.progress.setdefault("entries", {})
        entries[date_key] = {
            "topic_index": update.selection.index,
            "topic_slug": update.selection.topic.slug,
            "cycle": update.selection.cycle,
            "note": update.note_path.as_posix(),
        }
        if update.is_new_entry:
            update.progress["next_topic_index"] = (
                int(update.progress.get("next_topic_index", 0)) + 1
            )
        progress_path = self._config.repository_root / "data" / "progress.json"
        _write_text(
            progress_path,
            json.dumps(update.progress, ensure_ascii=False, indent=2) + "\n",
        )


def _load_progress(path: Path) -> dict[str, Any]:
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError("Progress file must contain an object")
    if not isinstance(document.get("entries"), dict):
        raise ValueError("Progress entries must be an object")
    next_index = document.get("next_topic_index")
    if not isinstance(next_index, int) or next_index < 0:
        raise ValueError("Progress next_topic_index must be a non-negative integer")
    return document


def _progress_entry(progress: dict[str, Any], date_key: str) -> dict[str, Any] | None:
    entries = progress["entries"]
    entry = entries.get(date_key)
    return entry if isinstance(entry, dict) else None


def _select_for_run(
    topics: tuple[Topic, ...],
    progress: dict[str, Any],
    existing_entry: dict[str, Any] | None,
) -> TopicSelection:
    if existing_entry is None:
        return select_topic(topics, progress["next_topic_index"])
    index = existing_entry.get("topic_index")
    cycle = existing_entry.get("cycle")
    if not isinstance(index, int) or not 0 <= index < len(topics):
        raise ValueError("Existing progress entry has an invalid topic index")
    if not isinstance(cycle, int) or cycle < 1:
        raise ValueError("Existing progress entry has an invalid cycle")
    return TopicSelection(topic=topics[index], index=index, cycle=cycle)


def _note_path(selection: TopicSelection, target_date: date) -> Path:
    return (
        Path("notes")
        / f"{target_date.year:04d}"
        / f"{target_date.month:02d}"
        / f"{target_date.isoformat()}-{selection.topic.slug}.md"
    )


def _report_path(target_date: date) -> Path:
    return (
        Path("reports")
        / "activity"
        / f"{target_date.year:04d}"
        / f"{target_date.month:02d}"
        / f"{target_date.isoformat()}.json"
    )


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as file:
            file.write(content)
        temporary_path.replace(path)
    finally:
        temporary_path.unlink(missing_ok=True)
