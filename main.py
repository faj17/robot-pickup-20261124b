#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one original pickup line, written for a robot to say out
loud, to /output/entry.txt (1-200 characters, UTF-8, a single line).
Standard library only, no network, no input.

The line is built from two fragments: a setup (the robot scans the
whole room with its sensors — a machine act, the kind of thing only
a robot would do while trying to charm someone) and a punch (the
turn: the sensors keep returning one error, and the error is that
the person is standing too far away, so the machine's fault report
becomes the flirt).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I scanned the whole room and my sensors kept returning one error:"
PUNCH = "you were standing too far away."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one pickup line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
