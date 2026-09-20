from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .models import ActivityReport, NoteContext

LATEST_ENTRY_START = "<!-- latest-entry:start -->"
LATEST_ENTRY_END = "<!-- latest-entry:end -->"


def render_note(context: NoteContext) -> str:
    topic = context.selection.topic
    lines = [
        "---",
        f'date: "{context.target_date.isoformat()}"',
        f'track: "{topic.track}"',
        f'topic: "{topic.slug}"',
        f'cycle: {context.selection.cycle}',
        "generated: true",
        "reviewed: false",
        'review_status: "pending"',
        f'generator: "{_yaml_text(context.generation.generator)}"',
        f'model: "{_yaml_text(context.generation.model)}"',
        f'evidence_count: {len(context.activity.events)}',
        "---",
        "",
        f"# Daily Study Brief: {topic.title}",
        "",
        "> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. "
        "Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.",
        "",
        "## Fokus",
        "",
        context.content.focus,
        "",
        "## Konsep inti",
        "",
    ]
    for concept in context.content.concepts:
        lines.extend([f"### {concept.name}", "", concept.description, ""])

    lines.extend(["## Latihan", ""])
    lines.extend(
        f"{number}. {step}"
        for number, step in enumerate(context.content.exercise_steps, start=1)
    )
    lines.extend(["", "## Aktivitas GitHub publik", ""])
    lines.extend(_activity_lines(context.activity))
    lines.extend(["", "## Pertanyaan review", ""])
    lines.extend(f"- [ ] {question}" for question in context.content.review_questions)
    lines.extend(
        [
            "",
            "## Langkah berikutnya",
            "",
            context.content.next_step,
            "",
            "## Referensi",
            "",
        ]
    )
    lines.extend(f"- [{reference.label}]({reference.url})" for reference in topic.references)
    lines.extend(
        [
            "",
            "## Review manual",
            "",
            "Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, "
            "ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.",
            "",
        ]
    )
    return "\n".join(lines)


def render_activity_report(context: NoteContext) -> str:
    document = {
        "date": context.target_date.isoformat(),
        "source": context.activity.source,
        "status": context.activity.status,
        "message": context.activity.message,
        "events": [asdict(event) for event in context.activity.events],
    }
    return json.dumps(document, ensure_ascii=False, indent=2) + "\n"


def update_readme_latest(readme: str, note_path: Path, context: NoteContext) -> str:
    if readme.count(LATEST_ENTRY_START) != 1 or readme.count(LATEST_ENTRY_END) != 1:
        raise ValueError("README latest-entry markers are missing or duplicated")
    relative_note = note_path.as_posix()
    topic = context.selection.topic
    replacement = "\n".join(
        [
            LATEST_ENTRY_START,
            f"[{context.target_date.isoformat()}: {topic.title}]({relative_note})",
            "",
            f"Track: `{topic.track}` | Review: `pending` | Generator: `{context.generation.generator}`",
            LATEST_ENTRY_END,
        ]
    )
    prefix, remainder = readme.split(LATEST_ENTRY_START, maxsplit=1)
    _, suffix = remainder.split(LATEST_ENTRY_END, maxsplit=1)
    return f"{prefix}{replacement}{suffix}"


def _activity_lines(report: ActivityReport) -> list[str]:
    if report.status != "ok":
        return [
            "Pengambilan aktivitas GitHub tidak tersedia pada run ini. "
            "Bagian ini tidak digunakan sebagai bukti aktivitas."
        ]
    if not report.events:
        return [
            "Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. "
            "Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan."
        ]
    return [
        f"- {event.occurred_at}: [{event.repository}]({event.url}) - {event.summary}"
        for event in report.events
    ]


def _yaml_text(value: str) -> str:
    value = value.replace(chr(13), ' ').replace(chr(10), ' ')
    return value.replace("\\", "\\\\").replace('"', '\\"')
