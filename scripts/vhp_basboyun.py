#!/usr/bin/env python3
"""Baş–boyun düzeyleri: VHP-M kriyokesit + aynı NLM numaralı donmuş BT + (varsa) MR T1 / PD / T2.

MR dosyaları m_vm####.t1/.pd/.t2 (özgün NLM adları, DICOM 0009,1001) aynı numaralandırmayı kullanır;
5 mm aralıkla 1005–1165. Her modalite, kriyokesitteki baş/boyun maskesine çapraz korelasyonla
(ölçek = piksel boyutu oranı, yalnız öteleme) hizalanır ve kriyokesit kırpımıyla aynı alana yeniden örneklenir.
Çıktı: basboyun/images/vhp/{cryo,ct,ctbone,t1,pd,t2}_<n>.(jpg|png), meta_<n>.json, /tmp/grid_bb/g_<n>.jpg"""
import io, json, pathlib, sys, functools, numpy as np, requests, pydicom
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import vhp_fetch as V, vhp_register as R

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "basboyun" / "images" / "vhp"; OUT.mkdir(parents=True, exist_ok=True)
GRID = pathlib.Path("/tmp/grid_bb"); GRID.mkdir(exist_ok=True)
MR_SERIES = {"t1": "a83c457a-d8c9-4290-b657-d1570d99fbef", "t2pd": "342d9e2a-7c85-4de3-bb7b-baf6246ba537"}

@functools.lru_cache(None)
def mr_tablo():
    """NLM numarası → {t1/pd/t2: key}"""
    import pandas as pd
    tab = {}
    for role, uid in MR_SERIES.items():
        d = pd.read_csv(V.IDX / f"{uid}.csv")
        for k in d.key:
            r = requests.get(f"{V.BUCKET}/{k}", headers={"Range": "bytes=0-20000"}, timeout=60)
            ds = pydicom.dcmread(io.BytesIO(r.content), stop_before_pixels=True, force=True)
            fn = str(ds[(0x0009, 0x1001)].value)
            num = int(fn.split("m_vm")[1][:4]); ext = fn.rsplit(".", 1)[1]
            tab.setdefault(num, {})[ext] = k
    return tab

def mask_cryo(c):
    m = R.cryo_mask(c); m = ndi.binary_opening(m, iterations=2)
    lab, n = ndi.label(m)
    if n == 0: return m
    sz = ndi.sum(m, lab, range(1, n + 1)); i = int(np.argmax(sz)) + 1
    return ndi.binary_fill_holes(lab == i)

def bbox(m, pad=40):
    ys, xs = np.nonzero(m)
    return [max(0, xs.min() - pad), max(0, ys.min() - pad), min(m.shape[1], xs.max() + pad), min(m.shape[0], ys.max() + pad)]

def hizala(mc, img_mask, scale):
    """kriyo maskesi (mc) ↔ başka modalite maskesi; kriyo px → modalite px: X = x*scale + dx"""
    h, w = mc.shape
    ms = np.array(Image.fromarray(mc.astype(np.uint8) * 255).resize((round(w * scale), round(h * scale)), Image.BILINEAR)) > 127
    H = max(ms.shape[0], img_mask.shape[0]) * 2; W = max(ms.shape[1], img_mask.shape[1]) * 2
    A = np.zeros((H, W)); A[:img_mask.shape[0], :img_mask.shape[1]] = img_mask
    B = np.zeros((H, W)); B[:ms.shape[0], :ms.shape[1]] = ms
    cc = np.real(np.fft.ifft2(np.fft.fft2(A) * np.conj(np.fft.fft2(B))))
    dy, dx = np.unravel_index(np.argmax(cc), cc.shape)
    if dy > H // 2: dy -= H
    if dx > W // 2: dx -= W
    Bs = np.roll(np.roll(B, dy, 0), dx, 1)[:img_mask.shape[0], :img_mask.shape[1]] > 0
    dice = 2 * (Bs & img_mask).sum() / (Bs.sum() + img_mask.sum())
    return dict(scale=scale, dx=int(dx), dy=int(dy), dice=round(float(dice), 3))

def kirp(arr8, T, box, size):
    x0, y0, x1, y1 = box
    X0, Y0 = x0 * T["scale"] + T["dx"], y0 * T["scale"] + T["dy"]
    X1, Y1 = x1 * T["scale"] + T["dx"], y1 * T["scale"] + T["dy"]
    return Image.fromarray(arr8).crop((round(X0), round(Y0), round(X1), round(Y1))).resize(size, Image.BICUBIC)

def mr_yukle(key):
    p = V.CACHE / key.replace("/", "_")
    if not p.exists():
        p.write_bytes(requests.get(f"{V.BUCKET}/{key}", timeout=120).content)
    ds = pydicom.dcmread(p); a = ds.pixel_array.astype(float)
    return a, ds

def norm(a, lo=1, hi=99.5):
    v = a[a > np.percentile(a, 5)]
    l, h = np.percentile(v, lo), np.percentile(v, hi)
    return (np.clip((a - l) / (h - l + 1e-6), 0, 1) * 255).astype(np.uint8)

def make(n, ct_pencere=(40, 120)):
    c, ds, row = V.load("cryo", n); c = np.ascontiguousarray(np.flipud(c))
    mc = mask_cryo(c); box = bbox(mc)
    crop = Image.fromarray(c[box[1]:box[3], box[0]:box[2]]); size = crop.size
    crop.save(OUT / f"cryo_{n}.jpg", quality=92)
    meta = dict(slice=n, cryo_file=str(ds[(0x0009, 0x1001)].value), box=[int(b) for b in box])
    f, dsc, rowc = V.load("frozenCT", n)
    Tct = hizala(mc, f > -400, R.CRYO_PX / float(dsc.PixelSpacing[0]))
    kirp(V.window(f, *ct_pencere), Tct, box, size).save(OUT / f"ct_{n}.png")
    kirp(V.window(f, 500, 2000), Tct, box, size).save(OUT / f"ctbone_{n}.png")
    meta.update(ct_file=str(dsc[(0x0009, 0x1001)].value), ct_reg=Tct)
    mr = mr_tablo().get(n)
    if mr:
        for ext, key in mr.items():
            a, dm = mr_yukle(key)
            px = float(dm.PixelSpacing[0])
            mm = a > np.percentile(a, 60) * 0.5
            mm = ndi.binary_fill_holes(ndi.binary_opening(mm, iterations=2))
            T = hizala(mc, mm, R.CRYO_PX / px)
            kirp(norm(a), T, box, size).save(OUT / f"{ext}_{n}.png")
            meta[f"mr_{ext}"] = dict(file=str(dm[(0x0009, 0x1001)].value), reg=T, px=px)
    (OUT / f"meta_{n}.json").write_text(json.dumps(meta, indent=1))
    # ızgaralı önizleme (QA)
    g = crop.copy(); d = ImageDraw.Draw(g)
    for gx in range(0, size[0], 50):
        d.line([(gx, 0), (gx, size[1])], fill=(0, 255, 0) if gx % 100 == 0 else (0, 110, 0))
        if gx % 100 == 0: d.text((gx + 2, 2), str(gx), fill=(255, 255, 0))
    for gy in range(0, size[1], 50):
        d.line([(0, gy), (size[0], gy)], fill=(0, 255, 0) if gy % 100 == 0 else (0, 110, 0))
        if gy % 100 == 0: d.text((2, gy + 2), str(gy), fill=(255, 255, 0))
    panels = [g] + [Image.open(OUT / f"{k}_{n}.png").convert("RGB") for k in ("ctbone", "t1", "t2", "pd") if (OUT / f"{k}_{n}.png").exists()]
    W = sum(p.size[0] for p in panels); sh = Image.new("RGB", (W, size[1])); x = 0
    for p in panels: sh.paste(p, (x, 0)); x += p.size[0]
    sh.save(GRID / f"g_{n}.jpg", quality=88)
    return meta

def kirp_1260():
    from PIL import Image
    for f in ["cryo_1260.jpg", "ct_1260.png", "ctbone_1260.png"]:
        p = OUT / f; im = Image.open(p)
        if im.size[0] > 700: im.crop((250, 0, 850, im.size[1])).save(p)

DUZEYLER = [1045, 1060, 1080, 1095, 1110, 1125, 1140, 1155, 1165, 1185, 1200, 1215, 1230, 1245, 1260]

if __name__ == "__main__":
    lv = [int(a) for a in sys.argv[1:]] or DUZEYLER
    for n in lv:
        m = make(n)
        print(n, m["box"], m["ct_reg"], {k: v["reg"]["dice"] for k, v in m.items() if k.startswith("mr_")})
    kirp_1260()
# 1260 kesiti build sonrası x=250..850 aralığına kırpılır (build_basboyun ile uyumlu)
