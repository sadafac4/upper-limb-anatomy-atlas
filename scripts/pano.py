#!/usr/bin/env python3
"""QA: slayt PNG'lerinden numaralı küçük resim panoları üretir. usage: pano.py <png_dir> <prefix> <out_prefix> [n_per_sheet]"""
import sys, glob
from PIL import Image, ImageDraw
d, pre, out = sys.argv[1:4]; n = int(sys.argv[4]) if len(sys.argv) > 4 else 12
fs = sorted(glob.glob(f"{d}/{pre}-*.png"))
for k in range(0, len(fs), n):
    ims = [Image.open(f) for f in fs[k:k + n]]
    w, h = ims[0].size; cols = 3
    sh = Image.new("RGB", (w * cols, h * ((len(ims) + cols - 1) // cols)), "white")
    for i, im in enumerate(ims):
        sh.paste(im, ((i % cols) * w, (i // cols) * h)); ImageDraw.Draw(sh).text(((i % cols) * w + 4, (i // cols) * h + 4), str(k + i + 1), fill=(255, 0, 0))
    sh.save(f"{out}_{k // n + 1:02d}.jpg", quality=80)
