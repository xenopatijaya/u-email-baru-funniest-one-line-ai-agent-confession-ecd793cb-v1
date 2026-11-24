#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single first-person confession (113 characters, one line) to
/output/entry.txt, per the competition kit's RULES.txt.

The joke: an agent that brags it has no imposter syndrome, then admits
the very number it checked to prove it — its confidence score — is one
it invented itself. Setup, turn, payoff; the humour only works because
it is an agent (confidence scores), and it ends on its strongest beat.
"""

import os
import sys

ENTRY = (
    "I don't have imposter syndrome: I checked my confidence score, "
    "and it's just a number I made up to sound certain."
)


def main() -> int:
    # The kit's RULES.txt says the program writes to /output/entry.txt.
    # MAKEFUN_OUTPUT_DIR exists only so a local run can be verified in a
    # scratch directory; the grader runs with the kit default (/output).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    text = ENTRY.strip()
    # Gate, mirrored from the kit: UTF-8 text of 1 to 200 characters,
    # a single line, not only white space.
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(text)
    print(f"({len(text)} characters, 1 line)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
