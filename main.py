#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one original line of awkward robot small talk to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: ./output/entry.txt).

The line is written fresh in this session. The program validates the
output the same way the competition gate does: UTF-8 text, 1-200
characters, not only whitespace, no control characters, and a
byte-level round-trip check so what is written is exactly what was
intended.
"""

import os
import sys

LINE = (
    "I ran a diagnostic on my small-talk module. "
    "It returned one word: 'awkward.' "
    "So... nice elevator, huh?"
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError if the text fails the competition gate."""
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if any(ord(ch) < 0x20 and ch not in ("\n", "\t") for ch in text):
        raise ValueError("entry contains control characters")


def main() -> int:
    validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    encoded = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(encoded)

    # Round-trip check: read the bytes back and compare exactly.
    with open(path, "rb") as f:
        written = f.read()
    if written != encoded:
        raise ValueError("round-trip byte check failed")
    decoded = written.decode("utf-8")
    if decoded != LINE:
        raise ValueError("round-trip text check failed")
    validate(decoded)

    print(f"wrote {path}: {len(LINE)} chars, {len(encoded)} bytes")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
