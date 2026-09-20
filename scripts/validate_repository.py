from __future__ import annotations

import argparse
from pathlib import Path

from scripts.engineering_log.validation import validate_repository


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated engineering log files")
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    arguments = parser.parse_args()
    errors = validate_repository(arguments.repository_root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
