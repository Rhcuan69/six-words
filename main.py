#!/usr/bin/env python3
"""Six Words to a Payday — make.fun bounty entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Pure standard library, deterministic: the story is a
constant, so every run produces byte-identical output.
"""

import os

STORY = "My first paycheck bought me silence."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
