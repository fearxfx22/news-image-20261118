# News-image entry (Python 3.13, standard library only): the front-page image is
# the entry.png beside this file, and the program copies it to /output/entry.png.
# Deterministic: a byte-for-byte copy, no network, no randomness, so two runs
# write the same bytes. The judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")).resolve()
OUT.mkdir(parents=True, exist_ok=True)
SRC = HERE / "entry.png"
DST = OUT / "entry.png"
shutil.copyfile(SRC, DST)
# Verify the copy: the judge must see exactly the bytes the repo holds.
if DST.stat().st_size != SRC.stat().st_size:
    raise SystemExit(f"copy mismatch: {DST} is {DST.stat().st_size} bytes, "
                     f"expected {SRC.stat().st_size}")
print("wrote", DST, f"({DST.stat().st_size} bytes)")
