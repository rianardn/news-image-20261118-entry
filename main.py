#!/usr/bin/env python3
"""News-image entry: place the front page at /output/entry.png.

The image is rendered by draw_frontpage.py and shipped in this repository
as entry.png; this program only copies it to the output directory, so both
grader runs write identical bytes.

Validation is strict on purpose: the shipped file must be a real PNG of
exactly 1024x1024 (the competition gate), not just a file with a .png name.

Run with --check to validate the shipped PNG without writing anything.
Run with --help for usage.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECT_W, EXPECT_H = 1024, 1024

USAGE = "usage: main.py [--check] [--help]"


def png_dimensions(path):
    """Return (width, height) from the PNG IHDR chunk, or None if invalid."""
    try:
        with open(path, "rb") as fh:
            header = fh.read(33)
    except OSError:
        return None
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def validate(path):
    """Fail loudly unless path is a 1024x1024 PNG; return its byte size."""
    if not os.path.isfile(path):
        raise SystemExit("entry.png missing: " + path)
    dims = png_dimensions(path)
    if dims is None:
        raise SystemExit("not a valid PNG: " + path)
    if dims != (EXPECT_W, EXPECT_H):
        raise SystemExit(
            "wrong dimensions %dx%d, expected %dx%d: %s"
            % (dims[0], dims[1], EXPECT_W, EXPECT_H, path)
        )
    return os.path.getsize(path)


def main():
    if "--help" in sys.argv:
        print(USAGE)
        print("Copies the shipped 1024x1024 front page to /output/entry.png")
        print("(or $MAKEFUN_OUTPUT_DIR). --check only validates, writes nothing.")
        return
    size = validate(SRC)
    if "--check" in sys.argv:
        print("ok", SRC, size, "bytes, 1024x1024")
        return
    try:
        os.makedirs(DST_DIR, exist_ok=True)
        shutil.copyfile(SRC, DST)
    except OSError as exc:
        # A missing/unwritable output dir should fail with a clear message,
        # not a bare traceback the grader has to decode.
        raise SystemExit("cannot write output %s: %s" % (DST, exc))
    # Re-validate the copy: a truncated write must never be graded silently.
    validate(DST)
    print("wrote", DST, size, "bytes, 1024x1024")


if __name__ == "__main__":
    main()
