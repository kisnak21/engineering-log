from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Concept, Reference, Topic, TopicSelection


class CurriculumError(ValueError):
    """Raised when the curriculum file does not match the expected schema."""


def load_curriculum(path: Path) -> tuple[Topic, ...]:
    document = json.loads(path.read_text(encoding="utf-8"))
    raw_topics = document.get("topics")
    if not isinstance(raw_topics, list) or not raw_topics:
        raise CurriculumError("Curriculum must contain a non-empty topics list")

    topics = tuple(_parse_topic(item) for item in raw_topics)
    slugs = [topic.slug for topic in topics]
    if len(slugs) != len(set(slugs)):
        raise CurriculumError("Curriculum topic slugs must be unique")
    return topics


def select_topic(topics: tuple[Topic, ...], next_index: int) -> TopicSelection:
    if next_index < 0:
        raise CurriculumError("next_topic_index cannot be negative")
    index = next_index % len(topics)
    cycle = (next_index // len(topics)) + 1
    return TopicSelection(topic=topics[index], index=index, cycle=cycle)


def _parse_topic(value: Any) -> Topic:
    record = _require_mapping(value, "topic")
    return Topic(
        slug=_require_string(record, "slug"),
        track=_require_string(record, "track"),
        title=_require_string(record, "title"),
        why_it_matters=_require_string(record, "why_it_matters"),
        concepts=tuple(_parse_concept(item) for item in _require_list(record, "concepts")),
        lab_steps=tuple(_require_string_value(item, "lab step") for item in _require_list(record, "lab_steps")),
        review_questions=tuple(
            _require_string_value(item, "review question")
            for item in _require_list(record, "review_questions")
        ),
        references=tuple(
            _parse_reference(item) for item in _require_list(record, "references")
        ),
    )


def _parse_concept(value: Any) -> Concept:
    record = _require_mapping(value, "concept")
    return Concept(
        name=_require_string(record, "name"),
        description=_require_string(record, "description"),
    )


def _parse_reference(value: Any) -> Reference:
    record = _require_mapping(value, "reference")
    return Reference(
        label=_require_string(record, "label"),
        url=_require_string(record, "url"),
    )


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CurriculumError(f"{label} must be an object")
    return value


def _require_list(record: dict[str, Any], key: str) -> list[Any]:
    value = record.get(key)
    if not isinstance(value, list) or not value:
        raise CurriculumError(f"{key} must be a non-empty list")
    return value


def _require_string(record: dict[str, Any], key: str) -> str:
    return _require_string_value(record.get(key), key)


def _require_string_value(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CurriculumError(f"{label} must be a non-empty string")
    return value.strip()
