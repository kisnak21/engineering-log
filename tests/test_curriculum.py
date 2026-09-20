from __future__ import annotations

import unittest
from pathlib import Path

from scripts.engineering_log.curriculum import load_curriculum, select_topic


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class CurriculumTest(unittest.TestCase):
    def test_loads_unique_topics(self) -> None:
        topics = load_curriculum(REPOSITORY_ROOT / "config" / "curriculum.json")

        self.assertGreaterEqual(len(topics), 20)
        self.assertEqual(len(topics), len({topic.slug for topic in topics}))

    def test_selection_wraps_into_next_cycle(self) -> None:
        topics = load_curriculum(REPOSITORY_ROOT / "config" / "curriculum.json")

        selection = select_topic(topics, len(topics))

        self.assertEqual(topics[0], selection.topic)
        self.assertEqual(2, selection.cycle)


if __name__ == "__main__":
    unittest.main()
