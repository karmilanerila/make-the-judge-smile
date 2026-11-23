#!/usr/bin/env python3
"""Make the Judge Smile (u-gentle-badger-68).

Writes one original line about a small good thing that happened today
to /output/entry.txt. Stdlib only, fully deterministic: the same line
is written on every run.
"""

import os

LINE = (
    "My neighbour left a mango on my doorstep with a note: "
    "'the tree's too generous \u2014 help yourself.' "
    "I ate it standing up, juice on my chin, grinning like a kid."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
