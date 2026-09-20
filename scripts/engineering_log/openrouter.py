from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from .models import ActivityReport, Concept, StudyContent, TopicSelection

OPENROUTER_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
REQUEST_TIMEOUT_SECONDS = 60
MAX_ATTEMPTS = 3
MAX_TEXT_LENGTH = 600
FIRST_PERSON_CLAIM = re.compile(
    r"\b(?:saya|aku)\s+(?:telah|sudah|berhasil|mempelajari|menguasai)\b",
    re.IGNORECASE,
)


class OpenRouterError(RuntimeError):
    """Raised when OpenRouter cannot produce a valid study brief."""


@dataclass(frozen=True)
class OpenRouterResult:
    content: StudyContent
    model: str


@dataclass(frozen=True)
class ListBounds:
    minimum: int
    maximum: int


EXERCISE_BOUNDS = ListBounds(minimum=2, maximum=6)
QUESTION_BOUNDS = ListBounds(minimum=2, maximum=5)


class OpenRouterClient:
    def __init__(self, api_key: str, model: str, repository_url: str) -> None:
        self._api_key = api_key
        self._model = model
        self._repository_url = repository_url

    def generate(
        self,
        selection: TopicSelection,
        activity: ActivityReport,
    ) -> OpenRouterResult:
        payload = self._build_payload(selection, activity)
        response = self._post_with_retry(payload)
        content = _extract_message_content(response)
        study_content = _parse_study_content(content)
        model = response.get("model")
        return OpenRouterResult(
            content=study_content,
            model=model if isinstance(model, str) else self._model,
        )

    def _build_payload(
        self,
        selection: TopicSelection,
        activity: ActivityReport,
    ) -> dict[str, object]:
        topic = selection.topic
        evidence = [
            {
                "repository": event.repository,
                "kind": event.kind,
                "summary": event.summary,
            }
            for event in activity.events
        ]
        curriculum = {
            "title": topic.title,
            "track": topic.track,
            "cycle": selection.cycle,
            "why_it_matters": topic.why_it_matters,
            "concepts": [
                {"name": concept.name, "description": concept.description}
                for concept in topic.concepts
            ],
            "lab_steps": list(topic.lab_steps),
            "review_questions": list(topic.review_questions),
        }
        user_prompt = (
            "Buat daily study brief berbahasa Indonesia dari data JSON berikut. "
            "Gunakan hanya fakta di input. Jangan menyatakan bahwa pengguna sudah belajar, "
            "mencoba, berhasil, atau menguasai sesuatu. Jangan menciptakan statistik, aktivitas, "
            "URL, command output, atau pengalaman pribadi. Tulis jelas dan ringkas. "
            "Kembalikan tepat satu object JSON tanpa markdown fence dengan schema: "
            '{"focus":"string","concepts":[{"name":"string","description":"string"}],'
            '"exercise_steps":["string"],"review_questions":["string"],"next_step":"string"}. '
            "Berikan 2 sampai 4 concepts, 2 sampai 6 exercise_steps, dan 2 sampai 5 "
            "review_questions. Aktivitas GitHub hanya boleh memengaruhi konteks, bukan menjadi "
            "klaim pembelajaran.\n\n"
            f"INPUT:\n{json.dumps({'curriculum': curriculum, 'github_activity': evidence}, ensure_ascii=False)}"
        )
        return {
            "model": self._model,
            "temperature": 0.3,
            "max_tokens": 1600,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Anda menulis study brief berbasis bukti. Kejujuran lebih penting "
                        "daripada terdengar produktif. Output harus berupa JSON valid."
                    ),
                },
                {"role": "user", "content": user_prompt},
            ],
        }

    def _post_with_retry(self, payload: dict[str, object]) -> dict[str, Any]:
        request_body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self._repository_url,
            "X-OpenRouter-Title": "Engineering Log",
        }
        for attempt in range(1, MAX_ATTEMPTS + 1):
            request = urllib.request.Request(
                OPENROUTER_ENDPOINT,
                data=request_body,
                headers=headers,
                method="POST",
            )
            try:
                with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                    document = json.loads(response.read().decode("utf-8"))
                if not isinstance(document, dict):
                    raise OpenRouterError("OpenRouter response was not an object")
                return document
            except urllib.error.HTTPError as error:
                if not _is_retryable(error.code) or attempt == MAX_ATTEMPTS:
                    raise OpenRouterError(f"OpenRouter returned HTTP {error.code}") from error
                time.sleep(_retry_delay_seconds(error, attempt))
            except (urllib.error.URLError, TimeoutError) as error:
                if attempt == MAX_ATTEMPTS:
                    raise OpenRouterError("OpenRouter request failed") from error
                time.sleep(attempt * 2)
        raise OpenRouterError("OpenRouter request exhausted all attempts")


def fallback_content(selection: TopicSelection) -> StudyContent:
    topic = selection.topic
    cycle_note = (
        "Gunakan putaran ini untuk membangun dasar yang dapat diuji."
        if selection.cycle == 1
        else f"Ini putaran ke-{selection.cycle}; cari perbedaan dari pemahaman pada putaran sebelumnya."
    )
    return StudyContent(
        focus=f"{topic.why_it_matters} {cycle_note}",
        concepts=topic.concepts,
        exercise_steps=topic.lab_steps,
        review_questions=topic.review_questions,
        next_step="Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.",
    )


def _extract_message_content(response: dict[str, Any]) -> str:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        raise OpenRouterError("OpenRouter response did not contain choices")
    first_choice = choices[0]
    if not isinstance(first_choice, dict):
        raise OpenRouterError("OpenRouter choice was not an object")
    message = first_choice.get("message")
    if not isinstance(message, dict) or not isinstance(message.get("content"), str):
        raise OpenRouterError("OpenRouter response did not contain message content")
    return message["content"]


def _parse_study_content(raw_content: str) -> StudyContent:
    document = _extract_json_object(raw_content)
    focus = _required_text(document, "focus")
    concepts = _parse_concepts(document.get("concepts"))
    exercise_steps = _parse_text_list(document, "exercise_steps", EXERCISE_BOUNDS)
    review_questions = _parse_text_list(document, "review_questions", QUESTION_BOUNDS)
    next_step = _required_text(document, "next_step")
    generated_text = [
        focus,
        next_step,
        *exercise_steps,
        *review_questions,
        *(concept.description for concept in concepts),
    ]
    if any(FIRST_PERSON_CLAIM.search(text) for text in generated_text):
        raise OpenRouterError("Generated content made an unsupported first-person claim")
    return StudyContent(
        focus=focus,
        concepts=concepts,
        exercise_steps=exercise_steps,
        review_questions=review_questions,
        next_step=next_step,
    )


def _extract_json_object(raw_content: str) -> dict[str, Any]:
    cleaned = raw_content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, count=1, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned, count=1)
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start < 0 or end <= start:
        raise OpenRouterError("Generated content did not contain a JSON object")
    try:
        document = json.loads(cleaned[start : end + 1])
    except json.JSONDecodeError as error:
        raise OpenRouterError("Generated content was not valid JSON") from error
    if not isinstance(document, dict):
        raise OpenRouterError("Generated JSON was not an object")
    return document


def _parse_concepts(value: Any) -> tuple[Concept, ...]:
    if not isinstance(value, list) or not 2 <= len(value) <= 4:
        raise OpenRouterError("Generated concepts must contain 2 to 4 items")
    concepts: list[Concept] = []
    for item in value:
        if not isinstance(item, dict):
            raise OpenRouterError("Generated concept must be an object")
        concepts.append(
            Concept(
                name=_required_text(item, "name"),
                description=_required_text(item, "description"),
            )
        )
    return tuple(concepts)


def _parse_text_list(
    document: dict[str, Any],
    key: str,
    bounds: ListBounds,
) -> tuple[str, ...]:
    value = document.get(key)
    if not isinstance(value, list) or not bounds.minimum <= len(value) <= bounds.maximum:
        raise OpenRouterError(
            f"{key} must contain {bounds.minimum} to {bounds.maximum} items"
        )
    return tuple(_clean_generated_text(item, key) for item in value)


def _required_text(document: dict[str, Any], key: str) -> str:
    return _clean_generated_text(document.get(key), key)


def _clean_generated_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise OpenRouterError(f"{label} must be a non-empty string")
    cleaned = value.replace("—", "-").replace("–", "-").replace("\r", " ").replace("\n", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if len(cleaned) > MAX_TEXT_LENGTH:
        raise OpenRouterError(f"{label} exceeded the maximum length")
    return cleaned


def _is_retryable(status_code: int) -> bool:
    return status_code == 429 or status_code >= 500


def _retry_delay_seconds(error: urllib.error.HTTPError, attempt: int) -> int:
    retry_after = error.headers.get("Retry-After", "") if error.headers else ""
    if retry_after.isdigit():
        return min(int(retry_after), 15)
    return attempt * 2
