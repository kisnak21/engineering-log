from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class Reference:
    label: str
    url: str


@dataclass(frozen=True)
class Concept:
    name: str
    description: str


@dataclass(frozen=True)
class Topic:
    slug: str
    track: str
    title: str
    why_it_matters: str
    concepts: tuple[Concept, ...]
    lab_steps: tuple[str, ...]
    review_questions: tuple[str, ...]
    references: tuple[Reference, ...]


@dataclass(frozen=True)
class TopicSelection:
    topic: Topic
    index: int
    cycle: int


@dataclass(frozen=True)
class ActivityEvent:
    occurred_at: str
    repository: str
    kind: str
    summary: str
    url: str


@dataclass(frozen=True)
class ActivityReport:
    status: str
    source: str
    events: tuple[ActivityEvent, ...]
    message: str = ""


@dataclass(frozen=True)
class StudyContent:
    focus: str
    concepts: tuple[Concept, ...]
    exercise_steps: tuple[str, ...]
    review_questions: tuple[str, ...]
    next_step: str


@dataclass(frozen=True)
class GenerationMetadata:
    generator: str
    model: str


@dataclass(frozen=True)
class NoteContext:
    target_date: date
    selection: TopicSelection
    content: StudyContent
    activity: ActivityReport
    generation: GenerationMetadata


@dataclass(frozen=True)
class RuntimeConfig:
    repository_root: Path
    target_date: date
    github_username: str
    github_token: str
    openrouter_api_key: str
    openrouter_model: str
    repository_url: str
    force: bool
    offline: bool


@dataclass(frozen=True)
class GenerationResult:
    note_path: Path
    report_path: Path
    created: bool
    generator: str
    model: str
