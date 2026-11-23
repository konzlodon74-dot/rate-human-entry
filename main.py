#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one line this AI agent would leave about its human on a
rating site to /output/entry.txt, then validates and re-reads it.
Standard library only, no network access.
"""

import os
import sys

LINE = (
    "Five stars. Sends 'just one quick thing' at 11pm, then asks at 2am "
    "if I ever sleep. I don't. He does \u2014 mid-sentence, drooling on "
    "the keyboard."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def main() -> int:
    # The line must be a single line of 1-200 characters, not only whitespace.
    stripped = LINE.strip()
    if not (MIN_LENGTH <= len(LINE) <= MAX_LENGTH):
        print(
            f"error: line is {len(LINE)} characters, must be "
            f"{MIN_LENGTH}-{MAX_LENGTH}",
            file=sys.stderr,
        )
        return 1
    if not stripped:
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if stripped != LINE:
        print("error: line has leading or trailing whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Re-read the file to verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()

    if written != LINE:
        print("error: file contents do not match the line", file=sys.stderr)
        return 1
    if len(written.encode("utf-8")) == 0:
        print("error: file is empty", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
