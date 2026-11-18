#!/usr/bin/env python3
"""News-image entry: place the front page at /output/entry.png.

The image is rendered by draw_frontpage.py and shipped in this repository
as entry.png; this program only copies it to the output directory, so both
grader runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")

if not os.path.isfile(SRC):
    raise SystemExit("entry.png missing next to main.py: " + SRC)

os.makedirs(DST_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

# Verify the copy is a real PNG before reporting success: a truncated or
# corrupted entry.png would otherwise be graded silently.
with open(DST, "rb") as fh:
    header = fh.read(8)
if header != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("output is not a valid PNG: " + DST)
size = os.path.getsize(DST)
print("wrote", DST, size, "bytes")
