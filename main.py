#!/usr/bin/env python3
"""Write the make.fun bounty entry text to disk.

Bounty: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610

The entry is one short line roasting a gadget. This program writes exactly
those bytes (no trailing newline) into the directory named by
MAKEFUN_OUTPUT_DIR when it is set, else /output, creating the directory if
needed, and reports the character count on stderr.

Python 3.13, standard library only, no network access.
"""

import os
import sys
from pathlib import Path

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def output_dir() -> Path:
    """Directory to write into.

    MAKEFUN_OUTPUT_DIR wins when set; OUTPUT_DIR is accepted as a fallback;
    /output is used when neither is set.
    """
    chosen = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    return Path(chosen)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)

    entry = target / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
