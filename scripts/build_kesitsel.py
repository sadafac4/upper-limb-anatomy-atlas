#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kesitsel anatomi sunumu (uzun, bölümlü): Giriş → Omuz → Kol → Önkol → El.
Her bölüm: kapak → kesitsel okuma rehberi → VHP-M kriyokesit + aynı kesit numaralı donmuş BT düzeyleri →
literatürden MR/BT/US görselleri → görüntüleme varyasyonları literatür taraması → çalışmalar.
Önce: vhp_index_headers.py, vhp_crops.py, vhp_assets.py, vhp_bulk_slices.py + vhp_cpr.py.
Çıktı: kesitsel/Kesitsel_Anatomi.pptx, kesitsel/qa/label_qa.json"""
import json, pathlib, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from slayt_tipleri import *
import icerik_kesitsel as IK
import icerik_anlatim as AN

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "kesitsel" / "images" / "vhp"
QA = ROOT / "kesitsel" / "qa"; QA.mkdir(exist_ok=True)
SRC_VHP = ("Kaynak: NLM Visible Human Project – Visible Human Male (kriyokesit a_vm{n}, donmuş BT c_vm{n}.fro); NCI Imaging Data Commons "
           "(doi:10.5281/zenodo.12690049); NLM Terms and Conditions (2019). Yönelim: radyolojik (ön yukarıda, hastanın sağı solda); sağ üst ekstremite.")

def bone_like(rgb):
    r, g, b = [rgb[..., i].astype(int) for i in range(3)]
    return (r > 170) & (g > 135) & (b > 115) & ((r - b) < 72)

def snap_bone(img, pt, radius=30):
    a = np.asarray(img); m = ndi.binary_opening(bone_like(a), iterations=1)
    x, y = pt; H, W = m.shape
    y0, y1, x0, x1 = max(0, y - radius), min(H, y + radius), max(0, x - radius), min(W, x + radius)
    ys, xs = np.nonzero(m[y0:y1, x0:x1])
    if len(xs) == 0: return pt, None
    i = ((xs + x0 - x) ** 2 + (ys + y0 - y) ** 2).argmin()
    nx, ny = int(xs[i] + x0), int(ys[i] + y0)
    lab, _ = ndi.label(m); comp = lab == lab[ny, nx]
    if 30 < comp.sum() < 40000:
        dist = ndi.distance_transform_edt(comp); yy, xx = np.nonzero(comp)
        near = (xx - nx) ** 2 + (yy - ny) ** 2 < 25 ** 2
        j = np.argmax(np.where(near, dist[yy, xx], -1)); nx, ny = int(xx[j]), int(yy[j])
    return (nx, ny), float(np.hypot(nx - x, ny - y))

def ct_bone_points(ct_path, istek):
    a = np.asarray(Image.open(ct_path).convert("L")).astype(int)
    lab, n = ndi.label(a > 110); out = []
    for name, p in istek:
        best = None
        for i in range(1, n + 1):
            yy, xx = np.nonzero(lab == i)
            if len(xx) < 25: continue
            d2 = (xx - p[0]) ** 2 + (yy - p[1]) ** 2; k = d2.argmin()
            if best is None or d2[k] < best[0]: best = (d2[k], (int(xx[k]), int(yy[k])))
        out.append((name, best[1] if best and best[0] ** 0.5 < 70 else None))
    return out

def duzey(prs, n, sayfa, bolum, qa):
    L = IK.L[n]
    s = yeni_slayt(prs)
    title_bar(s, f"{L['baslik']}", f"{L['alt']} – NLM kesit no. {n}"); bolum_seridi(s, bolum); etiket(s, "KESİT")
    cryo = Image.open(IMG / f"cryo_{n}_R.jpg"); meta = json.loads((IMG / f"meta_{n}.json").read_text())
    pts, rec = [], []
    for t, p, side, snap in L["etiketler"]:
        q, sh = snap_bone(cryo, p) if snap == "bone" else (p, None)
        pts.append((t, q, side)); rec.append(dict(label=t, given=p, used=q, snap_shift_px=sh))
    g = picture_fit(s, IMG / f"cryo_{n}_R.jpg", 2.4, 1.35, 4.1, 4.45)
    text(s, g["x"] - 0.2, g["y"] + g["h"] + 0.02, g["w"] + 0.4, 0.3, "Kriyokesit (renkli fotoğraf)", size=11, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    labels(s, g, [(t, q) for t, q, sd in pts if sd == "L"], 0.1, 2.2, "L", 1.35, 5.85, size=13, box_h=0.5)
    labels(s, g, [(t, q) for t, q, sd in pts if sd == "R"], 6.6, 2.3, "R", 1.35, 5.85, size=13, box_h=0.5)
    gc = picture_fit(s, IMG / f"ct_{n}_R.png", 9.0, 1.35, 2.45, 4.45)
    text(s, gc["x"] - 0.2, gc["y"] + gc["h"] + 0.02, gc["w"] + 0.4, 0.3, "Donmuş BT, aynı kesit no.", size=11, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    istek = []
    for name in L["ct"]:
        q = next(q for t, q, sd in pts if t.split(" (")[0] == name.split(" (")[0] or t.startswith(name.split(" (")[0]))
        istek.append((name, q))
    ctp = ct_bone_points(IMG / f"ctbone_{n}_R.png", istek)
    labels(s, gc, [(t, q) for t, q in ctp if q is not None], 11.55, 1.6, "R", 2.6, 5.85, size=12.5, box_h=0.5)
    rec.append(dict(ct_labels=[dict(label=t, point=q) for t, q in ctp]))
    if L.get("ct_not"):
        text(s, gc["x"] - 0.3, gc["y"] + gc["h"] + 0.32, gc["w"] + 0.6, 0.7, L["ct_not"], size=11, color=ACCENT, italic=True)
    picture_fit(s, IMG / f"loc_{n}.jpg", 11.5, 1.35, 1.7, 1.0)
    text(s, 11.45, 2.35, 1.8, 0.3, "Konum (kırmızı kutu)", size=10, color=GREY, italic=True)
    bullets(s, 0.3, 6.15, 12.8, 0.85, L["notlar"], size=sigdir(L["notlar"], 12.8, 0.85, 15, 12) or 12)
    footer(s, SRC_VHP.format(n=n), sayfa); fix_runs(s)
    notes(s, f"Kriyokesit: {meta['cryo_file']}\nBT: {meta['ct_file']} (kesit no. {meta['ct_slice']})\nKırpma kutusu: {meta['box_cryo_px']}\nKayıt: {meta['reg']}")
    qa[str(n)] = dict(meta=meta, labels=rec)

def locator_eksik():
    for n in IK.L:
        if not (IMG / f"loc_{n}.jpg").exists():
            raise SystemExit(f"loc_{n}.jpg yok – önce scripts/vhp_assets.py çalıştırın")

def build():
    locator_eksik()
    prs = new_deck(); sayfa = 1; qa = {}; kullanilan = []
    kapak(prs, "Membrum Superius – Kesitsel Anatomi",
          "Gerçek kadavra kriyokesitleri, aynı kadavranın aynı düzeydeki BT'si ve literatürden MR/BT/US görüntüleri",
          ["Bölümler: Omuz → Kol → Önkol → El (18 VHP düzeyi + boylamsal reformat)",
           "Her bölümün sonunda görüntüleme tabanlı varyasyonların literatür taraması",
           "Tüm görüntüler gerçek kadavra/radyoloji verisidir; sentetik görüntü kullanılmamıştır."],
          [("vhp_crop", 1320), ("vhp", "cpr_coronal_levels.jpg", ""), ("vhp_crop", 1740), ("vhp_crop", 1830)])
    sayfa += 1
    icindekiler(prs, IK.BOLUMLER, "Giriş: düzlemler ve yönelim, dokuların görüntüleme özellikleri, veri kaynağı, boylamsal reformat", sayfa); sayfa += 1
    for d in AN.KESIT["giris"] + IK.GIRIS:
        sayfa += {"anlatim": anlatim, "tablo": tablo, "gorsel": gorsel, "duzyazi": duzyazi}[d.get("tip", "duzyazi")](prs, d, sayfa, "GİRİŞ")
    for no, b in enumerate(IK.BOLUMLER, 1):
        v = b["veri"]; etk = f"BÖLÜM {no} · {b['ad']}"
        refs = [("vhp_crop", v["duzeyler"][len(v["duzeyler"]) // 2])] + [v["lit"][0]["figs"][0]]
        sayfa += bolum_kapak(prs, no, b, refs, sayfa)
        for d in AN.KESIT[b["kod"]]:
            sayfa += duzyazi(prs, d, sayfa, etk)
        for d in v["anlatim"]:
            sayfa += anlatim(prs, d, sayfa, etk); kullanilan += [r[1] for r in d.get("figs", []) if r[0] == "pmc"]
        for n in v["duzeyler"]:
            duzey(prs, n, sayfa, etk, qa); sayfa += 1
        for d in v["lit"]:
            sayfa += gorsel(prs, d, sayfa, etk); kullanilan += [r[1] for r in d["figs"] if r[0] == "pmc"]
        sayfa += lit_tablo(prs, f"{b['ad'].capitalize() if b['kod'] != 'onkol' else 'Önkol'} – görüntüleme tabanlı varyasyonlar: literatür taraması",
                           "MR, BT, ultrason ve grafi çalışmaları (PMC açık erişim)", v["var_tablo"], sayfa, etk)
        for d in v["var_cal"]:
            sayfa += gorsel(prs, d, sayfa, etk); kullanilan += [r[1] for r in d["figs"] if r[0] == "pmc"]
    s = yeni_slayt(prs); title_bar(s, "Sınırlılıklar ve kalite kontrol")
    bullets(s, 0.4, 1.2, 12.5, 5.6, [
        "**Düzey eşleştirme** NLM kesit numarasına dayanır (Ackerman 1995; Spitzer ve ark. 1996); yalnız düzlem içi hizalama hesaplanmıştır.",
        "**BT görüş alanı** (480 mm) kol ortasından dirseğe kadar kolu kısmen dışarıda bırakır: 1490–1645 düzeylerinde BT etiketlenmemiştir.",
        "**MR:** VHP-M aksiyel MR yalnız başı kapsar; ekstremite MR/US örnekleri farklı bireylerden alınmış literatür görselleridir (aynı kişi değildir).",
        "**Etiketler:** kaynak piksel koordinatında tanımlanmış, kemik etiketleri kemik maskesine yapıştırılmış, slaytlar PNG'ye dönüştürülüp görsel olarak denetlenmiştir (kesitsel/qa/). Tek tek karpal kemikler, ayrı sinirler ve yüzeyel venler bilinçli olarak etiketlenmemiştir.",
        "**Önkol ve el kesitleri** kadavranın pozisyonu (pronasyon, el uyluğa yaslı) nedeniyle eğiktir.",
        "**Boylamsal reformat** doğrulanmış kemik merkezleri arasında enterpolasyonla çizilmiş bir yol boyunca örneklenmiştir; blok sınırlarında süreksizlik vardır.",
        "Tüm etiketler ve özetler eğitim amaçlıdır; bir anatomi öğretim üyesince gözden geçirilmesi önerilir."], size=15)
    footer(s, "Spitzer V, et al. J Am Med Inform Assoc 1996;3(2):118–130 • Ackerman MJ. D-Lib Magazine 1995 • Fedorov A, et al. RadioGraphics 2023;43(12):e230180.", sayfa); fix_runs(s); sayfa += 1
    sayfa = kaynakca(prs, kullanilan, "Kaynakça ve görsel lisansları", sayfa)
    out = ROOT / "kesitsel" / "Kesitsel_Anatomi.pptx"; prs.save(out)
    (QA / "label_qa.json").write_text(json.dumps(qa, indent=1, ensure_ascii=False, default=str))
    print(out, len(prs.slides), "slayt")

if __name__ == "__main__":
    build()
