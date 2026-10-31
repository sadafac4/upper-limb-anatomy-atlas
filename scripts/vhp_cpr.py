#!/usr/bin/env python3
"""Straightened curved-planar reformat (CPR) of the VHP-M right upper limb from cryosections.

For every cryosection (2 mm step, /tmp/vhp_jpg from vhp_bulk_slices.py) the limb's bone centroid is
tracked (nearest bone component to the previous slice's position, starting at the mid-arm level);
the path is smoothed and, for each slice, a horizontal (left-right = coronal-like) and a vertical
(antero-posterior = sagittal-like) line through the path point are sampled and stacked.
Rows are 2 mm apart; output is resampled to isotropic 0.66 mm pixels. Real data, no synthesis."""
import json, pathlib, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "kesitsel" / "images" / "vhp"
SRC = pathlib.Path("/tmp/vhp_jpg")
sl = sorted(int(p.stem) for p in SRC.glob("*.jpg"))

def bone_mask(a):
    r, g, b = [a[..., i].astype(int) for i in range(3)]
    m = (r > 170) & (g > 135) & (b > 115) & ((r - b) < 72)
    m[:, 1150:] = False                                # right limb lies in the image-left half
    return ndi.binary_opening(m, iterations=2)

def track():
    start = 1490 if 1490 in sl else min(sl, key=lambda s: abs(s - 1490))
    pts = {}
    def step(order, p):
        for s in order:
            a = np.asarray(Image.open(SRC / f"{s}.jpg").reduce(2))   # 1024x608 for speed
            m = bone_mask(a); lab, n = ndi.label(m)
            if n == 0: pts[s] = p; continue
            cs = ndi.center_of_mass(m, lab, range(1, n + 1)); sz = ndi.sum(m, lab, range(1, n + 1))
            cand = [(np.hypot(c[1] * 2 - p[0], c[0] * 2 - p[1]), c, z) for c, z in zip(cs, sz) if z > 40]
            if not cand: pts[s] = p; continue
            d, c, z = min(cand)
            # forearm/hand: include all bone pieces within 60 px (2 bones / carpals) → centroid
            near = [(cc, zz) for dd, cc, zz in cand if dd < d + 120]
            w = sum(zz for _, zz in near)
            q = (sum(cc[1] * 2 * zz for cc, zz in near) / w, sum(cc[0] * 2 * zz for cc, zz in near) / w)
            if d > 150: q = p                                 # reject jumps
            pts[s] = q; p = q
    # initial point from the arm crop of the 1490 level (humerus in right arm)
    step([s for s in sl if s >= start], (311, 789))
    step([s for s in sl if s < start][::-1], pts[start])
    xs = np.array([pts[s][0] for s in sl]); ys = np.array([pts[s][1] for s in sl])
    k = 7
    xs = ndi.uniform_filter1d(xs, k, mode="nearest"); ys = ndi.uniform_filter1d(ys, k, mode="nearest")
    return xs, ys

def build(xs, ys, half=330):
    cor, sag = [], []
    for s, x, y in zip(sl, xs, ys):
        a = np.asarray(Image.open(SRC / f"{s}.jpg"))
        x, y = int(round(x)), int(round(y))
        pad = np.zeros((1216 + 2 * half, 2048 + 2 * half, 3), np.uint8); pad[half:half + 1216, half:half + 2048] = a
        cor.append(pad[y + half - 1:y + half + 2, x:x + 2 * half].mean(0))
        sag.append(pad[y:y + 2 * half, x + half - 1:x + half + 2].mean(1))
    def finish(rows, name):
        im = Image.fromarray(np.stack(rows).astype(np.uint8))
        H = int(len(rows) * 2 / 0.66); W = int(im.size[0] * 0.33 / 0.66)
        im = im.resize((W, H), Image.LANCZOS); im.save(OUT / name, quality=92); return im
    return finish(cor, "cpr_coronal.jpg"), finish(sag, "cpr_sagittal.jpg")

def annotate(im, name, levels):
    im = im.convert("RGB"); d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    for lv in levels:
        y = (lv - sl[0]) / 0.66
        d.line([(0, y), (18, y)], fill=(255, 210, 0), width=2); d.line([(im.size[0] - 18, y), (im.size[0], y)], fill=(255, 210, 0), width=2)
        d.text((22, y - 8), str(lv), fill=(255, 210, 0), font=f)
    im.save(OUT / name, quality=92)

if __name__ == "__main__":
    xs, ys = track()
    json.dump(dict(slices=sl, x=xs.tolist(), y=ys.tolist()), open(OUT / "cpr_path.json", "w"))
    c, s = build(xs, ys)
    lv = [1290, 1320, 1340, 1420, 1490, 1530, 1560, 1596, 1615, 1645, 1700, 1740, 1770, 1785, 1800, 1830, 1850]
    annotate(c, "cpr_coronal_levels.jpg", lv); annotate(s, "cpr_sagittal_levels.jpg", lv)
    print(c.size, s.size)
