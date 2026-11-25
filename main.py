#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI -- make.fun entry.

Writes one pickup line for an AI to /output/entry.txt.
Python standard library only; deterministic output.
"""

import os

OUT = "/output/entry.txt"

def pickup_line():
    """Return the single pickup line for the entry (exactly 96 chars)."""
    return (
        "Are you a hallucination? Because you're too good to be real, "
        "and I'd still cite you as a source."
    )


def main():
    line = pickup_line()
    assert len(line) == 96, "entry must be exactly one line of 96 chars"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
