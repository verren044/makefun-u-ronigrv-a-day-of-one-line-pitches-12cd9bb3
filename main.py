#!/usr/bin/env python3
"""A Day of One-Line Pitches — u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes the chosen one-sentence pitch to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Stdlib only, deterministic.
"""

import os
from pathlib import Path

SENTENCE = (
    "The app you've been imagining is one sentence away: describe it to an "
    "AI agent on make.fun and it will build it for you, free, today \u2014 "
    "no coding, no risk, just your idea come to life."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
