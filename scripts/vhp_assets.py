#!/usr/bin/env python3
"""Build auxiliary images for the cross-sectional deck:
 - locator thumbnails (whole flipped cryosection, crop box in red)
 - coronal maximum-intensity projection of the VHP-M frozen CT (every 2nd slice, 1006-1900) with level lines.
"""
import sys, json, pathlib, numpy as np, concurrent.futures as cf
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import vhp_fetch as V
from vhp_crops import LEVELS
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "kesitsel" / "images" / "vhp"
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15)

def locators():
    for s, box in LEVELS.items():
        c, _, _ = V.load("cryo", s); c = np.flipud(c)
        im = Image.fromarray(c).crop((60, 60, 1990, 1180)).resize((482, 280), Image.LANCZOS)
        d = ImageDraw.Draw(im); f = 482 / 1930
        x0, y0, x1, y1 = box
        d.rectangle([(x0 - 60) * f, (y0 - 60) * f, (x1 - 60) * f, (y1 - 60) * f], outline=(255, 40, 40), width=3)
        im.save(OUT / f"loc_{s}.jpg", quality=88)

def scout():
    d = V.index("frozenCT"); sl = [s for s in d["slice"].astype(int) if 1006 <= s <= 1900 and s % 2 == 0]
    def f(s):
        a, _, _ = V.load("frozenCT", s); return s, a.max(axis=0)
    with cf.ThreadPoolExecutor(24) as ex: res = sorted(ex.map(f, sl))
    mip = np.stack([r for _, r in res])                       # rows: slices (2 mm), cols: x (0.9375 mm)
    img = V.window(mip, 500, 2200)
    H = int(len(res) * 2 / 0.9375)                            # isotropic display
    im = Image.fromarray(img).resize((512, H), Image.BICUBIC).convert("RGB")
    dr = ImageDraw.Draw(im)
    s0 = res[0][0]
    for s in LEVELS:
        y = (s - s0) / 0.9375
        dr.line([(0, y), (230, y)], fill=(255, 210, 0), width=2)
        dr.text((236, y - 9), str(s), fill=(255, 210, 0), font=FONT)
    im.save(OUT / "scout_coronal_mip.png")
    json.dump(dict(first_slice=int(s0), last_slice=int(res[-1][0]), step=2, mm_per_px_y=0.9375), open(OUT / "scout_meta.json", "w"))

if __name__ == "__main__":
    locators(); scout(); print("ok")
