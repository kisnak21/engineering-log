from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.engineering_log.validation import _scan_secrets


class SecretScanningTest(unittest.TestCase):
    def test_detects_openrouter_key_pattern(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "leaked.md").write_text(
                "sk-or-v1-" + ("a" * 32),
                encoding="utf-8",
            )

            errors = _scan_secrets(root)

            self.assertEqual(["Potential secret detected in leaked.md"], errors)


if __name__ == "__main__":
    unittest.main()
