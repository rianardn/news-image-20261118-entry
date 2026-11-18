#!/usr/bin/env python3
"""News-image entry: place the front page at /output/entry.png.

The image is rendered by draw_frontpage.py and shipped in this repository
as entry.png; this program only copies it to the output directory, so both
grader runs write identical bytes.

Run with --check to validate the shipped PNG without writing anything.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def is_valid_png(path):
    """True when path exists and starts with the PNG magic bytes."""
    try:
        with open(path, "rb") as fh:
            return fh.read(8) == PNG_MAGIC
    except OSError:
        return False


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png missing next to main.py: " + SRC)
    if not is_valid_png(SRC):
        raise SystemExit("entry.png is not a valid PNG: " + SRC)
    if "--check" in sys.argv:
        print("ok", SRC, os.path.getsize(SRC), "bytes")
        return
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Verify the copy is a real PNG before reporting success: a truncated
    # or corrupted entry.png would otherwise be graded silently.
    if not is_valid_png(DST):
        raise SystemExit("output is not a valid PNG: " + DST)
    print("wrote", DST, os.path.getsize(DST), "bytes")


if __name__ == "__main__":
    main()
