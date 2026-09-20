from __future__ import annotations

import argparse
import os
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from scripts.engineering_log.models import RuntimeConfig
from scripts.engineering_log.repository import DailyLogGenerator

JAKARTA_TIMEZONE = timezone(timedelta(hours=7), name="Asia/Jakarta")
DEFAULT_MODEL = "openrouter/free"


def main() -> int:
    arguments = _parse_arguments()
    try:
        config = _build_config(arguments)
        result = DailyLogGenerator(config).run()
    except (OSError, ValueError) as error:
        print(f"Generation failed: {error}", file=sys.stderr)
        return 1

    if result.created:
        print(
            f"Created {result.note_path.as_posix()} using "
            f"{result.generator} ({result.model})"
        )
    else:
        print(f"Skipped existing note {result.note_path.as_posix()}")
    return 0


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate one daily engineering study brief")
    parser.add_argument("--date", help="Target date in YYYY-MM-DD format")
    parser.add_argument("--force", action="store_true", help="Replace an existing note for the date")
    parser.add_argument("--offline", action="store_true", help="Skip all external API calls")
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root, defaults to the parent of scripts",
    )
    return parser.parse_args()


def _build_config(arguments: argparse.Namespace) -> RuntimeConfig:
    repository_root = arguments.repository_root.resolve()
    target_date = _parse_date(arguments.date)
    github_username = os.environ.get("GITHUB_USERNAME", "kisnak21").strip()
    repository_url = os.environ.get(
        "REPOSITORY_URL",
        "https://github.com/kisnak21/engineering-log",
    ).strip()
    if not github_username:
        raise ValueError("GITHUB_USERNAME cannot be empty")
    return RuntimeConfig(
        repository_root=repository_root,
        target_date=target_date,
        github_username=github_username,
        github_token=os.environ.get("GITHUB_TOKEN", "").strip(),
        openrouter_api_key=os.environ.get("OPENROUTER_API_KEY", "").strip(),
        openrouter_model=os.environ.get("OPENROUTER_MODEL", DEFAULT_MODEL).strip(),
        repository_url=repository_url,
        force=arguments.force,
        offline=arguments.offline,
    )


def _parse_date(raw_date: str | None) -> date:
    if raw_date:
        return date.fromisoformat(raw_date)
    return datetime.now(JAKARTA_TIMEZONE).date()


if __name__ == "__main__":
    raise SystemExit(main())
