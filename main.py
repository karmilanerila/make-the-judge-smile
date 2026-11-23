#!/usr/bin/env python3
"""Make the Judge Smile (u-gentle-badger-68).

Writes one original line about a small good thing that happened today
to /output/entry.txt. Stdlib only, fully deterministic: the same line
is written on every run.
"""

import os
import tempfile


def validate_entry(text: str) -> str:
    """Enforce the competition gate before anything is written.

    The line must be valid UTF-8, 1-200 chars, and non-whitespace-only.
    Fails loudly instead of writing a bad entry.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid
    return text


def write_entry(path: str, text: str) -> None:
    """Write atomically: temp file in the same dir, then rename.

    A crash mid-write never leaves a half-written entry.txt behind,
    and the written bytes are verified against the validated line.
    """
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=directory, delete=False
    ) as handle:
        handle.write(text)
        temp_path = handle.name
    with open(temp_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        os.unlink(temp_path)
        raise IOError("written bytes do not match the validated entry")
    os.replace(temp_path, path)


def main() -> None:
    write_entry("/output/entry.txt", validate_entry(LINE))

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
