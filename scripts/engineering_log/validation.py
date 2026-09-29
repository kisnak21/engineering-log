from __future__ import annotations

import json
import re
from pathlib import Path

from .curriculum import load_curriculum
from .journal import LATEST_ENTRY_END, LATEST_ENTRY_START

SECRET_PATTERNS = (
    re.compile(r"sk-or-v1-[A-Za-z0-9_-]{16,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{16,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{16,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
)
TEXT_SUFFIXES = {".json", ".md", ".py", ".yml", ".yaml"}
IGNORED_DIRECTORIES = {".git", "__pycache__", ".venv", "venv"}


def scan_generated_content(note: str, report: str) -> bool:
    generated_content = f"{note}\n{report}"
    return any(pattern.search(generated_content) for pattern in SECRET_PATTERNS)


def scan_repository_secrets(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*"):
        if not _is_scannable_file(path):
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        if any(pattern.search(content) for pattern in SECRET_PATTERNS):
            errors.append(f"Potential secret detected in {path.relative_to(root)}")
    return errors


def _is_scannable_file(path: Path) -> bool:
    return (
        path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not any(part in IGNORED_DIRECTORIES for part in path.parts)
    )


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(_validate_curriculum(root))
    errors.extend(_validate_progress(root))
    errors.extend(_validate_readme(root))
    errors.extend(_validate_notes(root))
    errors.extend(scan_repository_secrets(root))
    return errors


def _validate_curriculum(root: Path) -> list[str]:
    try:
        load_curriculum(root / "config" / "curriculum.json")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [f"Invalid curriculum: {error}"]
    return []


def _validate_progress(root: Path) -> list[str]:
    try:
        progress = json.loads((root / "data" / "progress.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"Invalid progress file: {error}"]
    if not isinstance(progress, dict):
        return ["Progress file must contain an object"]
    entries = progress.get("entries", {})
    if not isinstance(entries, dict):
        return ["Progress entries must contain an object"]
    next_index = progress.get("next_topic_index")
    if not isinstance(next_index, int) or next_index < 0:
        return ["Progress next_topic_index must be a non-negative integer"]
    return []


def _validate_readme(root: Path) -> list[str]:
    try:
        readme = (root / "README.md").read_text(encoding="utf-8")
    except OSError as error:
        return [f"README cannot be read: {error}"]
    if readme.count(LATEST_ENTRY_START) != 1 or readme.count(LATEST_ENTRY_END) != 1:
        return ["README must contain exactly one latest-entry marker pair"]
    return []


def _validate_notes(root: Path) -> list[str]:
    required_fields = (
        "generated: true",
        "reviewed:",
        "review_status:",
        "generator:",
        "model:",
    )
    errors: list[str] = []
    for note in (root / "notes").rglob("*.md"):
        content = note.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append(f"{note.relative_to(root)} is missing YAML front matter")
        for field in required_fields:
            if field not in content:
                errors.append(f"{note.relative_to(root)} is missing {field}")
        if "—" in content:
            errors.append(f"{note.relative_to(root)} contains an em dash")
    return errors


