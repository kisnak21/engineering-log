from __future__ import annotations

import unittest

from scripts.engineering_log.openrouter import OpenRouterError, _parse_study_content


class OpenRouterParsingTest(unittest.TestCase):
    def test_parses_json_inside_markdown_fence(self) -> None:
        raw_content = """```json
        {
          "focus": "Memahami jalur request.",
          "concepts": [
            {"name": "Request", "description": "Pesan dari client."},
            {"name": "Response", "description": "Balasan dari server."}
          ],
          "exercise_steps": ["Periksa request.", "Catat status response."],
          "review_questions": ["Apa itu header?", "Apa arti status 404?"],
          "next_step": "Bandingkan dua request."
        }
        ```"""

        content = _parse_study_content(raw_content)

        self.assertEqual("Memahami jalur request.", content.focus)
        self.assertEqual(2, len(content.concepts))

    def test_rejects_unsupported_personal_claim(self) -> None:
        raw_content = """{
          "focus": "Saya sudah menguasai Docker.",
          "concepts": [
            {"name": "Image", "description": "Template container."},
            {"name": "Container", "description": "Instance image."}
          ],
          "exercise_steps": ["Periksa image.", "Periksa container."],
          "review_questions": ["Apa itu image?", "Apa itu container?"],
          "next_step": "Ulangi latihan."
        }"""

        with self.assertRaises(OpenRouterError):
            _parse_study_content(raw_content)


if __name__ == "__main__":
    unittest.main()
