from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.engineering_log.models import RuntimeConfig
from scripts.engineering_log.repository import DailyLogGenerator


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
INITIAL_PROGRESS = {
    "entries": {},
    "next_topic_index": 0,
}


class RepositoryGenerationTest(unittest.TestCase):
    def test_offline_generation_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self._create_fixture_files(root)
            config = RuntimeConfig(
                repository_root=root,
                target_date=date(2026, 9, 20),
                github_username="kisnak21",
                github_token="",
                openrouter_api_key="",
                openrouter_model="openrouter/free",
                repository_url="https://github.com/kisnak21/engineering-log",
                force=False,
                offline=True,
            )

            first_result = DailyLogGenerator(config).run()
            second_result = DailyLogGenerator(config).run()

            self.assertTrue(first_result.created)
            self.assertFalse(second_result.created)
            note = (root / first_result.note_path).read_text(encoding="utf-8")
            self.assertIn("review_status: \"pending\"", note)
            progress = json.loads((root / "data" / "progress.json").read_text(encoding="utf-8"))
            self.assertEqual(1, progress["next_topic_index"])

    def _create_fixture_files(self, root: Path) -> None:
        (root / "config").mkdir()
        (root / "data").mkdir()
        shutil.copy(REPOSITORY_ROOT / "config" / "curriculum.json", root / "config")
        (root / "data" / "progress.json").write_text(
            json.dumps(INITIAL_PROGRESS, indent=2) + "\n",
            encoding="utf-8",
        )
        shutil.copy(REPOSITORY_ROOT / "README.md", root)


if __name__ == "__main__":
    unittest.main()
