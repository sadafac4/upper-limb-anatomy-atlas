#!/usr/bin/env python3
"""Pelvis/perine düzeyleri: VHP-M ve VHP-F kriyokesit + aynı NLM numaralı donmuş BT.
Kırpım: gövde maskesinin merkezinde, pelvis/perine bölgesini kapsayan kutu.
Çıktı: perine/images/vhp/{M|F}{n}_{cryo|ct|ctbone}.*, meta, /tmp/grid_pe/g_{M|F}{n}.jpg"""
import json, pathlib, sys, numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import vhp_fetch as V, vhp_register as R
from vhp_basboyun import hizala, kirp

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "perine" / "images" / "vhp"; OUT.mkdir(parents=True, exist_ok=True)
GRID = pathlib.Path("/tmp/grid_pe"); GRID.mkdir(exist_ok=True)
ROL = {"M": ("cryo", "frozenCT"), "F": ("cryoF", "frozenCT_F")}

def govde(c):
    m = R.cryo_mask(c); m = ndi.binary_opening(m, iterations=2)
    lab, n = ndi.label(m); sz = ndi.sum(m, lab, range(1, n + 1))
    keep = np.isin(lab, [i + 1 for i, s in enumerate(sz) if s > 0.15 * sz.max()])
    return ndi.binary_fill_holes(keep)

def make(sex, n, yarim=330):
    rc, rct = ROL[sex]
    c, ds, row = V.load(rc, n); c = np.ascontiguousarray(np.flipud(c))
    m = govde(c); ys, xs = np.nonzero(m)
    cx = int((xs.min() + xs.max()) / 2)
    box = [cx - yarim, max(0, ys.min() - 20), cx + yarim, min(1216, ys.max() + 20)]
    crop = Image.fromarray(c[box[1]:box[3], box[0]:box[2]]); size = crop.size
    tag = f"{sex}{n}"
    crop.save(OUT / f"{tag}_cryo.jpg", quality=92)
    meta = dict(sex=sex, slice=n, cryo_file=str(ds[(0x0009, 0x1001)].value), box=[int(b) for b in box])
    f, dsc, rowc = V.load(rct, n)
    T = hizala(m, f > -400, R.CRYO_PX / float(dsc.PixelSpacing[0]))
    kirp(V.window(f, 40, 400), T, box, size).save(OUT / f"{tag}_ct.png")
    kirp(V.window(f, 500, 2000), T, box, size).save(OUT / f"{tag}_ctbone.png")
    meta.update(ct_file=str(dsc[(0x0009, 0x1001)].value), ct_slice=float(rowc.slice), ct_reg=T)
    (OUT / f"{tag}_meta.json").write_text(json.dumps(meta, indent=1))
    g = crop.copy(); d = ImageDraw.Draw(g)
    for gx in range(0, size[0], 50):
        d.line([(gx, 0), (gx, size[1])], fill=(0, 255, 0) if gx % 100 == 0 else (0, 110, 0))
        if gx % 100 == 0: d.text((gx + 2, 2), str(gx), fill=(255, 255, 0))
    for gy in range(0, size[1], 50):
        d.line([(0, gy), (size[0], gy)], fill=(0, 255, 0) if gy % 100 == 0 else (0, 110, 0))
        if gy % 100 == 0: d.text((2, gy + 2), str(gy), fill=(255, 255, 0))
    b = Image.open(OUT / f"{tag}_ctbone.png").convert("RGB")
    sh = Image.new("RGB", (size[0] * 2, size[1])); sh.paste(g, (0, 0)); sh.paste(b, (size[0], 0)); sh.save(GRID / f"g_{tag}.jpg", quality=88)
    return meta

DUZEY = {"M": [1866, 1878, 1890, 1900, 1912, 1924, 1934], "F": [1845, 1860, 1875, 1890, 1905]}

if __name__ == "__main__":
    for sex, lv in DUZEY.items():
        for n in lv:
            m = make(sex, n); print(sex, n, m["box"], m["ct_reg"], m["ct_slice"])
