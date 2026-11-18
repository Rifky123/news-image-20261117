"""Entry for the make.fun news-image-20261117 bounty.

Writes the pre-rendered entry.png — a 1024x1024 newspaper-front-page
graphic summing up the world news of 17 November 2026 — into the
grader's output directory. Standard library only, no network, and
byte-identical output on every run.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
if not os.path.isfile(SRC):
    raise SystemExit(f"entry.png not found next to main.py: {SRC}")
DEST = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SRC, DEST)
print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")
