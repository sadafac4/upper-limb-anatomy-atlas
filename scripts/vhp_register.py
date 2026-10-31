#!/usr/bin/env python3
"""In-plane rigid (translation-only, fixed scale) registration of a VHP-M cryosection to the
frozen CT image with the SAME NLM slice number.

Level correspondence is NOT computed here: it is taken from NLM's numbering (cryosection a_vm####
and frozen CT c_vm####.fro share the slice number; Ackerman 1995, D-Lib Magazine). Only the in-plane
offset between the photo and the CT matrix is estimated, so that crops/labels refer to the same tissue.

scale  = cryo pixel (0.33 mm) / CT pixel (0.9375 mm)
offset = argmax cross-correlation of binary body masks (tissue vs. blue gel / air)
"""
import numpy as np
from PIL import Image

CRYO_PX, CT_PX = 0.33, 0.9375

def cryo_mask(rgb):
    r, g, b = [rgb[..., i].astype(int) for i in range(3)]
    tissue = (r > b + 25) & (r > 60)          # red muscle / yellow fat; gel is blue, background black
    return tissue

def ct_mask(hu):
    return hu > -400

def register(cryo_rgb_flipped, ct_hu):
    s = CRYO_PX / CT_PX
    m = cryo_mask(cryo_rgb_flipped).astype(np.uint8) * 255
    h, w = m.shape
    ms = np.array(Image.fromarray(m).resize((round(w * s), round(h * s)), Image.BILINEAR)) > 127
    mc = ct_mask(ct_hu)
    H = max(ms.shape[0], mc.shape[0]) * 2; W = max(ms.shape[1], mc.shape[1]) * 2
    A = np.zeros((H, W)); A[:mc.shape[0], :mc.shape[1]] = mc
    B = np.zeros((H, W)); B[:ms.shape[0], :ms.shape[1]] = ms
    cc = np.real(np.fft.ifft2(np.fft.fft2(A) * np.conj(np.fft.fft2(B))))
    dy, dx = np.unravel_index(np.argmax(cc), cc.shape)
    if dy > H // 2: dy -= H
    if dx > W // 2: dx -= W
    # dice for QA
    Bs = np.roll(np.roll(B, dy, 0), dx, 1)[:mc.shape[0], :mc.shape[1]] > 0
    dice = 2 * (Bs & mc).sum() / (Bs.sum() + mc.sum())
    return dict(scale=s, dx=int(dx), dy=int(dy), dice=float(dice))

def cryo_to_ct(pt, T):
    x, y = pt
    return (x * T["scale"] + T["dx"], y * T["scale"] + T["dy"])

def ct_to_cryo(pt, T):
    x, y = pt
    return ((x - T["dx"]) / T["scale"], (y - T["dy"]) / T["scale"])

def refine_local(cryo_rgb_flipped, ct_hu, T, box, search=12):
    """Refine translation using only the limb region (box in cryo px): maximise overlap of the
    limb soft-tissue mask, then the bone mask (CT>300 HU vs pale cryo bone). Returns new T + scores."""
    from PIL import Image
    x0, y0, x1, y1 = box
    s = T["scale"]
    sub = cryo_rgb_flipped[y0:y1, x0:x1]
    w, h = round((x1 - x0) * s), round((y1 - y0) * s)
    def rs(mask): return np.array(Image.fromarray(mask.astype(np.uint8) * 255).resize((w, h), Image.BILINEAR)) > 127
    r, g, b = [sub[..., i].astype(int) for i in range(3)]
    bone_c = rs((r > 175) & (g > 140) & (b > 125) & ((r - b) < 75))
    tis_c = rs(cryo_mask(sub))
    best = None
    X0, Y0 = x0 * s + T["dx"], y0 * s + T["dy"]
    for ddy in range(-search, search + 1):
        for ddx in range(-search, search + 1):
            X, Y = round(X0 + ddx), round(Y0 + ddy)
            if X < 0 or Y < 0 or X + w > ct_hu.shape[1] or Y + h > ct_hu.shape[0]:
                continue
            ct = ct_hu[Y:Y + h, X:X + w]
            bone_t, tis_t = ct > 300, ct > -400
            sb = 2 * (bone_c & bone_t).sum() / max(1, bone_c.sum() + bone_t.sum())
            st = 2 * (tis_c & tis_t).sum() / max(1, tis_c.sum() + tis_t.sum())
            score = st + 2 * sb
            if best is None or score > best[0]:
                best = (score, ddx, ddy, sb, st)
    if best is None:
        return T, None
    T2 = dict(T, dx=T["dx"] + best[1], dy=T["dy"] + best[2], local_shift_ctpx=[best[1], best[2]],
              local_bone_dice=round(best[3], 3), local_tissue_dice=round(best[4], 3))
    return T2, best
