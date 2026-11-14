#!/usr/bin/env python3
"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one poem about agency to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no randomness.

The poem is about the agency that passes between a person and something
they built: handing over the keys is itself the act.
"""
import os
from pathlib import Path

POEM = (
    "I gave my keys to something I had built,\n"
    "and told it: the house, the hours, the hill.\n"
    "It climbed the stairs I never would,\n"
    "and did the things I only meant to do.\n"
    "\n"
    "It asked me nothing. It just went.\n"
    "The lamps came on. The kettle sang.\n"
    "And in the quiet after it was done,\n"
    "I understood the thing I'd feared:\n"
    "\n"
    "the choice was mine. It always was.\n"
    "The hand that lets go is the hand that acts."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
