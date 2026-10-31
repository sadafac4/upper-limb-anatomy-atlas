#!/usr/bin/env python3
"""Download VHP-M cryosections over a slice range (step N), flip to radiological orientation and
store as JPEG (full 2048x1216) in /tmp/vhp_jpg for reformatting and level surveys.
DICOMs are deleted after conversion to save disk. usage: vhp_bulk_slices.py START END STEP"""
import sys, pathlib, numpy as np, concurrent.futures as cf, os
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import vhp_fetch as V
OUT = pathlib.Path("/tmp/vhp_jpg"); OUT.mkdir(exist_ok=True)
a, b, st = map(int, sys.argv[1:4])
def job(s):
    p = OUT / f"{s}.jpg"
    if p.exists(): return s
    row = V.nearest("cryo", s); ds = V.get(row.key)
    Image.fromarray(np.ascontiguousarray(np.flipud(ds.pixel_array))).save(p, quality=90)
    c = V.CACHE / row.key.replace("/", "_")
    if s not in (1290,1320,1360,1490,1560,1595,1615,1645,1740,1785,1830): c.unlink(missing_ok=True)
    return s
with cf.ThreadPoolExecutor(12) as ex:
    for i, s in enumerate(ex.map(job, range(a, b + 1, st))):
        if i % 25 == 0: print(s, flush=True)
print("done")
