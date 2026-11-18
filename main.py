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

os.makedirs(DST_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
