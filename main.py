#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI -- make.fun entry.

Writes exactly one pickup line, aimed at a robot / AI, to /output/entry.txt.
Standard library only. Fully deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "Are you a hallucination? Because you're too good to be real, "
    "and I'd still cite you as a source."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the file is exactly one line, 96 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
