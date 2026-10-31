#!/usr/bin/env python3
"""Make full-resolution crops of the patient's RIGHT upper limb (image left after vertical flip to
radiological convention) from VHP-M cryosections, plus the registered frozen-CT crop of the same region.
Also writes a gridded preview used for manual structure identification (QA only, not for slides)."""
import sys, json, pathlib, numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import vhp_fetch as V, vhp_register as R

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "kesitsel" / "images" / "vhp"; OUT.mkdir(parents=True, exist_ok=True)
GRID = pathlib.Path("/tmp/grid"); GRID.mkdir(exist_ok=True)

def arm_bbox(c, xmax=1000, pad=40):
    m = R.cryo_mask(c); m[:, xmax:] = False
    m = ndi.binary_opening(m, iterations=3)
    lab, n = ndi.label(m)
    if n == 0: return None
    sizes = ndi.sum(m, lab, range(1, n + 1))
    # choose the component whose centroid is left-most among big components (the arm), unless arm merges with trunk
    comps = [(i + 1, s) for i, s in enumerate(sizes) if s > 15000]
    cents = {i: ndi.center_of_mass(m, lab, i)[1] for i, _ in comps}
    i = min(cents, key=cents.get)
    ys, xs = np.nonzero(lab == i)
    return [max(0, xs.min() - pad), max(0, ys.min() - pad), min(2048, xs.max() + pad), min(1216, ys.max() + pad)]

def make(slice_no, box=None):
    c, ds, row = V.load("cryo", slice_no); c = np.ascontiguousarray(np.flipud(c))
    f, dsc, rowc = V.load("frozenCT", slice_no)
    T = R.register(c, f)
    box = box or arm_bbox(c)
    T, _ = R.refine_local(c, f, T, box)
    x0, y0, x1, y1 = box
    crop = Image.fromarray(c[y0:y1, x0:x1])
    crop.save(OUT / f"cryo_{slice_no}_R.jpg", quality=92)
    # CT crop of same physical region, resampled to cryo pixel grid for side-by-side display
    X0, Y0 = R.cryo_to_ct((x0, y0), T); X1, Y1 = R.cryo_to_ct((x1, y1), T)
    ctimg = Image.fromarray(V.window(f, 60, 500))
    ctc = ctimg.crop((round(X0), round(Y0), round(X1), round(Y1))).resize(crop.size, Image.BICUBIC)
    ctc.save(OUT / f"ct_{slice_no}_R.png")
    ctb = Image.fromarray(V.window(f, 500, 2000)).crop((round(X0), round(Y0), round(X1), round(Y1))).resize(crop.size, Image.BICUBIC)
    ctb.save(OUT / f"ctbone_{slice_no}_R.png")
    # gridded preview for identification
    g = crop.copy(); d = ImageDraw.Draw(g)
    for gx in range(0, crop.size[0], 50):
        d.line([(gx, 0), (gx, crop.size[1])], fill=(0, 255, 0) if gx % 100 == 0 else (0, 120, 0), width=1)
        if gx % 100 == 0: d.text((gx + 2, 2), str(gx), fill=(255, 255, 0))
    for gy in range(0, crop.size[1], 50):
        d.line([(0, gy), (crop.size[0], gy)], fill=(0, 255, 0) if gy % 100 == 0 else (0, 120, 0), width=1)
        if gy % 100 == 0: d.text((2, gy + 2), str(gy), fill=(255, 255, 0))
    sc = 2 if max(crop.size) < 600 else 1
    g.resize((crop.size[0] * sc, crop.size[1] * sc), Image.LANCZOS).save(GRID / f"g_{slice_no}.jpg", quality=90)
    meta = dict(slice=slice_no, cryo_key=row.key, cryo_file=str(ds.get((0x0009, 0x1001)).value if (0x0009, 0x1001) in ds else ""),
                ct_key=rowc.key, ct_slice=float(rowc.slice), ct_file=str(dsc.get((0x0009, 0x1001)).value if (0x0009, 0x1001) in dsc else ""),
                box_cryo_px=[int(v) for v in box], reg=T, mm_per_px_crop=0.33)
    (OUT / f"meta_{slice_no}.json").write_text(json.dumps(meta, indent=1))
    return meta

# Final pilot levels: NLM slice number -> crop box (x0,y0,x1,y1) in flipped full-res cryo px (right limb)
LEVELS = {1320: (200, 440, 1000, 1110), 1360: (150, 380, 900, 1140), 1490: (150, 560, 520, 990),
          1560: (125, 574, 529, 996), 1615: (130, 470, 560, 960), 1645: (140, 460, 560, 960),
          1740: (380, 250, 720, 650), 1785: (440, 120, 980, 540), 1830: (560, 80, 980, 450)}

if __name__ == "__main__":
    lv = [int(a) for a in sys.argv[1:]] or list(LEVELS)
    for s in lv:
        m = make(s, LEVELS.get(s)); print(s, m["box_cryo_px"], m["reg"], m["ct_file"])
