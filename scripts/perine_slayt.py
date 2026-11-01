# -*- coding: utf-8 -*-
"""Perine sunumu için slayt tipleri (büyük punto). deck_common üzerine kuruludur.

Punto standardı (ders salonunda okunabilirlik): başlık 28, alt başlık 15, gövde metni 17–18,
görsel üzeri Latince etiketler 13–14, altyazı 11, dipnot/atıf ≥ 9.

Görsel referansı: ("pmc", PMCID, dosya-anahtarı) ; etiket noktaları JSON'daki label_points'ten
(özgün görüntü pikseli) okunur ve yerleştirilen resmin gerçek geometrisine göre slayta çevrilir.
"""
import pathlib, re
from PIL import Image
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
import deck_common as D
from deck_common import NAVY, ACCENT, GREY, LIGHT, WHITE, YELLOW, text, fix_runs, picture_fit, img2slide, notes, new_deck
import kaynak_kayit as K

ROOT = pathlib.Path(__file__).resolve().parent.parent
SW, SH = 13.333, 7.5
SOLUK = RGBColor(0xC8, 0xD1, 0xE6)
ETIKET_RENK = {"KONU ANLATIMI": RGBColor(0x1F, 0x5F, 0x9E), "KLİNİK BAĞLANTI": RGBColor(0xC2, 0x6A, 0x00),
               "KADAVRA": RGBColor(0x2E, 0x7D, 0x32), "ŞEMA": RGBColor(0x45, 0x5A, 0x64),
               "TABLO": RGBColor(0x45, 0x5A, 0x64), "VARYASYON": ACCENT, "LİTERATÜR": ACCENT,
               "İLLÜSTRASYON": RGBColor(0x5E, 0x35, 0xB1), "GÖRÜNTÜLEME": RGBColor(0x5E, 0x35, 0xB1),
               "KEMİK": RGBColor(0x79, 0x55, 0x48), "ÖZET": NAVY}


def yeni(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def baslik(s, t, alt=None, etiket=None, bolum=None):
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(SW), Inches(1.0))
    bar.fill.solid(); bar.fill.fore_color.rgb = NAVY; bar.line.fill.background()
    text(s, 0.35, 0.07, 10.2, 0.55, t, size=28, color=WHITE, bold=True)
    if alt:
        text(s, 0.35, 0.6, 10.4, 0.36, alt, size=15, color=SOLUK, italic=True)
    if etiket:
        text(s, 10.85, 0.12, 2.25, 0.34, etiket, size=11, color=WHITE, bold=True, align=PP_ALIGN.CENTER,
             fill=ETIKET_RENK.get(etiket, ACCENT), anchor=MSO_ANCHOR.MIDDLE)
    if bolum:
        text(s, 10.85, 0.52, 2.25, 0.36, bolum, size=10, color=SOLUK, bold=True, align=PP_ALIGN.CENTER)


def dipnot(s, atif, sayfa):
    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(0.3), Inches(7.0), Inches(13.03), Inches(7.0))
    ln.line.color.rgb = RGBColor(0xBB, 0xBB, 0xBB); ln.line.width = Pt(0.75)
    if atif:
        text(s, 0.3, 7.02, 11.9, 0.45, atif, size=9, color=GREY)
    if sayfa is not None:
        text(s, 12.3, 7.06, 0.75, 0.3, str(sayfa), size=11, color=GREY, align=PP_ALIGN.RIGHT)


def maddeler(s, x, y, w, h, items, size=18, color=NAVY, aralik=6):
    """'• ' madde; '  - ' ile başlayan satır alt madde (daha küçük punto)."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        alt = it.startswith("  - ")
        D._add_runs(p, ("– " + it[4:]) if alt else ("• " + it))
        p.space_after = Pt(aralik)
        if alt:
            p.level = 1
        for r in p.runs:
            r.font.size = Pt(size - 2 if alt else size); r.font.color.rgb = color; r.font.name = D.FONT
    return tb


# ---------- görsel çözümleme ----------
def sekil(ref):
    _, pmc, key = ref[:3]
    f = K.sekil(pmc, key)
    return ROOT / f["local_path"], f


def kisa_atif(pmc):
    return K.atif(pmc, kisa=True)


def _kirp(path, crop):
    """crop=(x0,y0,x1,y1) özgün pikselde → scratch'e değil repo'daki perine/images/crop'a yazılır (tekrar üretilebilir)."""
    if not crop:
        return path, (0, 0)
    out = ROOT / "perine" / "images" / "crop" / f"{path.stem}_{'_'.join(map(str, crop))}.jpg"
    if not out.exists():
        out.parent.mkdir(parents=True, exist_ok=True)
        Image.open(path).convert("RGB").crop(crop).save(out, quality=92)
    return out, (crop[0], crop[1])


def etiketler(s, geo, items, sol_x, sol_w, sag_x, sag_w, y0, y1, size=13.5, renk=YELLOW, kutu_h=0.34):
    """items: [(etiket, (px,py))] özgün piksel. Görüntünün sol yarısındaki noktalar sol sütuna, sağdakiler sağ sütuna."""
    orta = geo["x"] + geo["w"] / 2
    pts = [(t, img2slide(geo, p)) for t, p in items]
    sol = [p for p in pts if p[1][0] < orta]; sag = [p for p in pts if p[1][0] >= orta]
    for grup, cx, cw, yon in ((sol, sol_x, sol_w, "L"), (sag, sag_x, sag_w, "R")):
        if not grup:
            continue
        grup.sort(key=lambda a: a[1][1])
        n = len(grup); gap = kutu_h + 0.08
        ys = [min(max(p[1][1] - kutu_h / 2, y0), y1 - kutu_h) for p in grup]
        for i in range(1, n):
            ys[i] = max(ys[i], ys[i - 1] + gap)
        if ys[-1] > y1 - kutu_h:
            ys[-1] = y1 - kutu_h
            for i in range(n - 2, -1, -1):
                ys[i] = min(ys[i], ys[i + 1] - gap)
        for (t, (sx, sy)), ty in zip(grup, ys):
            text(s, cx, ty, cw, kutu_h, t, size=size, color=NAVY, bold=True,
                 align=PP_ALIGN.RIGHT if yon == "L" else PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)
            lx = cx + cw if yon == "L" else cx
            ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(lx), Inches(ty + kutu_h / 2), Inches(sx), Inches(sy))
            ln.line.color.rgb = renk; ln.line.width = Pt(1.75)
            r = 0.05
            dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(sx - r), Inches(sy - r), Inches(2 * r), Inches(2 * r))
            dot.fill.solid(); dot.fill.fore_color.rgb = renk; dot.line.color.rgb = NAVY; dot.line.width = Pt(0.75)


def _icinde(pts, kirp):
    """Kırpma kutusu dışındaki noktaları atar, kalanları kırpma orijinine kaydırır."""
    if not kirp:
        return pts
    x0, y0, x1, y1 = kirp
    return [(t, (x - x0, y - y0)) for t, (x, y) in pts if x0 + 3 <= x <= x1 - 3 and y0 + 3 <= y <= y1 - 3]


def _noktalar(f, d):
    """Slayt etiketleri: d['etiket'] varsa [(latince, xy)], yoksa JSON label_points'in tamamı."""
    if d.get("etiketler") is not None:
        return d["etiketler"]
    out = []
    for lp in f.get("label_points") or []:
        out.append((lp["latin"], tuple(lp["xy"])))
    return out


def _lisans_notu(s, pmc, x, y, w):
    lc = K.makale(pmc)["license_code"]
    if "NC" in lc or "ND" in lc:
        text(s, x, y, w, 0.3, f"Lisans: {lc} – yalnızca ticari olmayan eğitim amaçlı; görsel değiştirilmeden kullanılmıştır.",
             size=9, color=ACCENT, italic=True)


# ---------- slayt tipleri ----------
def kapak(prs, b, alt, satirlar, refs):
    s = yeni(prs)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
    text(s, 0.7, 1.0, 7.3, 1.6, b, size=42, color=WHITE, bold=True)
    text(s, 0.7, 2.75, 7.3, 1.1, alt, size=20, color=SOLUK)
    maddeler(s, 0.7, 4.0, 7.3, 2.6, satirlar, size=16, color=WHITE)
    for i, r in enumerate(refs[:2]):
        p, _ = sekil(r)
        picture_fit(s, p, 8.4, 0.5 + i * 3.4, 4.6, 3.2)
    text(s, 0.7, 6.8, 7.6, 0.4, "Türkçe anlatım · Latince terminoloji (Terminologia Anatomica, TA2 2019)", size=13, color=SOLUK, italic=True)
    fix_runs(s)


def bolum_kapak(prs, no, ad, alt, konular, ref, sayfa):
    s = yeni(prs)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(7.0), prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
    text(s, 0.6, 0.8, 6.0, 0.5, f"BÖLÜM {no}", size=20, color=SOLUK, bold=True)
    text(s, 0.6, 1.35, 6.2, 1.5, ad, size=40, color=WHITE, bold=True)
    text(s, 0.6, 2.95, 6.0, 0.7, alt, size=17, color=SOLUK, italic=True)
    maddeler(s, 0.6, 3.75, 6.1, 3.2, konular, size=17, color=WHITE)
    if ref:
        p, f = sekil(ref)
        g = picture_fit(s, p, 7.3, 0.5, 5.75, 6.1)
        text(s, 7.3, 6.65, 5.75, 0.3, kisa_atif(ref[1]), size=9, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    text(s, 12.3, 7.06, 0.75, 0.3, str(sayfa), size=11, color=GREY, align=PP_ALIGN.RIGHT)
    fix_runs(s)


def anlatim(prs, d, sayfa):
    """Metin slaytı; isteğe bağlı sağda tek görsel (etiketli veya etiketsiz)."""
    s = yeni(prs)
    baslik(s, d["baslik"], d.get("alt"), d.get("etiket", "KONU ANLATIMI"), d.get("bolum"))
    atif = d.get("kaynak", "")
    if d.get("fig"):
        maddeler(s, 0.35, 1.25, 6.6, 5.7, d["metin"], size=d.get("boyut", 17))
        p, f = sekil(d["fig"])
        p2, off = _kirp(p, d.get("kirp"))
        g = picture_fit(s, p2, 7.15, 1.25, 5.9, 5.25)
        text(s, 7.15, g["y"] + g["h"] + 0.02, 5.9, 0.3, d.get("altyazi") or f"{f['label']} – {kisa_atif(d['fig'][1])}",
             size=11, color=GREY, italic=True, align=PP_ALIGN.CENTER)
        atif = (atif + "  •  " if atif else "") + K.atif(d["fig"][1])
        _lisans_notu(s, d["fig"][1], 7.15, 6.68, 5.9)
        notes(s, (d.get("not", "") + "\n\nŞekil altyazısı (özgün): " + f["caption"]).strip())
    else:
        maddeler(s, 0.45, 1.3, 12.4, 5.6, d["metin"], size=d.get("boyut", 19))
        if d.get("not"): notes(s, d["not"])
    dipnot(s, atif, sayfa); fix_runs(s)
    return s


def kadavra(prs, d, sayfa):
    """Büyük görsel + iki yanda Latince etiketler + altta kısa anlatım şeridi."""
    s = yeni(prs)
    baslik(s, d["baslik"], d.get("alt"), d.get("etiket", "KADAVRA"), d.get("bolum"))
    p, f = sekil(d["fig"])
    p2, off = _kirp(p, d.get("kirp"))
    alt_h = 1.05 if d.get("metin") else 0.0
    y0, y1 = 1.2, 6.62 - alt_h
    sol_w = d.get("sol_w", 2.9); sag_w = d.get("sag_w", 2.9)
    ix = 0.3 + sol_w + 0.25; iw = SW - ix - sag_w - 0.55
    g = picture_fit(s, p2, ix, y0, iw, y1 - y0 - 0.28)
    pts = _icinde(_noktalar(f, d), d.get("kirp"))
    etiketler(s, g, pts, 0.3, sol_w, SW - 0.3 - sag_w, sag_w, y0, y1 - 0.28, size=d.get("eboyut", 13.5))
    text(s, ix, g["y"] + g["h"] + 0.02, iw, 0.28, d.get("altyazi") or f"{f['label']} – {kisa_atif(d['fig'][1])}",
         size=11, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    if d.get("metin"):
        kutu = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.3), Inches(y1 + 0.05), Inches(SW - 0.6), Inches(alt_h))
        kutu.fill.solid(); kutu.fill.fore_color.rgb = LIGHT; kutu.line.fill.background()
        maddeler(s, 0.4, y1 + 0.08, SW - 0.8, alt_h, d["metin"], size=d.get("boyut", 15), aralik=2)
    _lisans_notu(s, d["fig"][1], 0.3, 6.68, 8.0)
    dipnot(s, K.atif(d["fig"][1]), sayfa)
    notes(s, (d.get("not", "") + "\n\nŞekil altyazısı (özgün, " + f["label"] + "): " + f["caption"] +
              "\nGörüntüdeki özgün etiketler: " + str(f.get("labels_visible_in_image", ""))).strip())
    fix_runs(s)
    return s


def iki_gorsel(prs, d, sayfa):
    """İki görsel yan yana (karşılaştırma) + altta kısa metin; etiketler görsel içinde yerel sütunlarda."""
    s = yeni(prs)
    baslik(s, d["baslik"], d.get("alt"), d.get("etiket", "KADAVRA"), d.get("bolum"))
    alt_h = 1.0 if d.get("metin") else 0.0
    y0, y1 = 1.2, 6.62 - alt_h
    atiflar = []
    for i, fd in enumerate(d["figler"]):
        bx = 0.3 + i * 6.4; bw = 6.3
        p, f = sekil(fd["fig"]); p2, off = _kirp(p, fd.get("kirp"))
        lw = fd.get("lw", 1.75)
        g = picture_fit(s, p2, bx + lw + 0.12, y0, bw - 2 * lw - 0.24, y1 - y0 - 0.3)
        pts = _icinde(_noktalar(f, fd), fd.get("kirp"))
        etiketler(s, g, pts, bx, lw, bx + bw - lw, lw, y0, y1 - 0.3, size=fd.get("eboyut", 12))
        text(s, bx, g["y"] + g["h"] + 0.02, bw, 0.28, fd.get("altyazi") or f"{f['label']} – {kisa_atif(fd['fig'][1])}",
             size=10.5, color=GREY, italic=True, align=PP_ALIGN.CENTER)
        atiflar.append(K.atif(fd["fig"][1]))
    if d.get("metin"):
        kutu = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.3), Inches(y1 + 0.05), Inches(SW - 0.6), Inches(alt_h))
        kutu.fill.solid(); kutu.fill.fore_color.rgb = LIGHT; kutu.line.fill.background()
        maddeler(s, 0.4, y1 + 0.08, SW - 0.8, alt_h, d["metin"], size=d.get("boyut", 15), aralik=2)
    dipnot(s, "  •  ".join(dict.fromkeys(atiflar)), sayfa)
    if d.get("not"): notes(s, d["not"])
    fix_runs(s)
    return s


def tablo(prs, d, sayfa):
    s = yeni(prs)
    baslik(s, d["baslik"], d.get("alt"), d.get("etiket", "TABLO"), d.get("bolum"))
    rows, cols = len(d["satirlar"]) + 1, len(d["sutunlar"])
    H = min(5.55, 0.5 + d.get("satir_h", 0.8) * (rows - 1))
    gt = s.shapes.add_table(rows, cols, Inches(0.3), Inches(1.25), Inches(12.73), Inches(H)).table
    gen = d.get("genislik") or [1] * cols; tot = sum(gen)
    for j, gg in enumerate(gen):
        gt.columns[j].width = Inches(12.73 * gg / tot)
    for j, h in enumerate(d["sutunlar"]):
        c = gt.cell(0, j); c.text = h; c.fill.solid(); c.fill.fore_color.rgb = NAVY
        for p in c.text_frame.paragraphs:
            for r in p.runs: r.font.size = Pt(15); r.font.bold = True; r.font.color.rgb = WHITE; r.font.name = D.FONT
    for i, row in enumerate(d["satirlar"], 1):
        for j, v in enumerate(row):
            c = gt.cell(i, j); c.text = ""
            c.fill.solid(); c.fill.fore_color.rgb = LIGHT if i % 2 else WHITE
            c.margin_top = c.margin_bottom = Inches(0.03)
            D._add_runs(c.text_frame.paragraphs[0], v)
            for p in c.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(d.get("boyut", 14)); r.font.color.rgb = NAVY; r.font.name = D.FONT
                    if j == 0: r.font.bold = True
                    if getattr(r, "_bold", False): r.font.bold = True
                    if getattr(r, "_ital", False): r.font.italic = True
    if d.get("dip"):
        text(s, 0.3, 6.6, 12.7, 0.38, d["dip"], size=12, color=GREY, italic=True)
    dipnot(s, d.get("kaynak", ""), sayfa); fix_runs(s)
    if d.get("not"): notes(s, d["not"])
    return s


def calisma(prs, d, sayfa):
    """Literatür/varyasyon çalışması: solda görsel (etiketli), sağda yöntem–bulgu–önem özeti."""
    s = yeni(prs)
    baslik(s, d["baslik"], d.get("alt"), d.get("etiket", "VARYASYON"), d.get("bolum"))
    p, f = sekil(d["fig"]); p2, off = _kirp(p, d.get("kirp"))
    pts = _icinde(_noktalar(f, d), d.get("kirp")) if d.get("etiketli", True) else []
    lw = d.get("lw", 1.75 if pts else 0.0)
    g = picture_fit(s, p2, 0.3 + lw, 1.25, 6.9 - 2 * lw, 5.1)
    if pts:
        etiketler(s, g, pts, 0.25, lw - 0.05, 0.3 + 6.9 - lw + 0.05, lw - 0.05, 1.25, 6.35, size=12)
    text(s, 0.3, g["y"] + g["h"] + 0.02, 6.9, 0.3, d.get("altyazi") or f"{f['label']} – {kisa_atif(d['fig'][1])}",
         size=10.5, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    y = 1.25
    for ad, icerik in (("Çalışma", d["calisma"]), ("Bulgular", d["bulgu"]), ("Klinik / cerrahi önem", d["onem"])):
        text(s, 7.45, y, 5.6, 0.34, ad, size=15, color=ACCENT, bold=True); y += 0.36
        tb = maddeler(s, 7.45, y, 5.6, 1.6, icerik if isinstance(icerik, list) else [icerik], size=d.get("boyut", 14), aralik=2)
        y += d.get("bosluk", {}).get(ad, 1.55)
    _lisans_notu(s, d["fig"][1], 7.45, 6.68, 5.6)
    dipnot(s, K.atif(d["fig"][1]), sayfa)
    notes(s, "Şekil altyazısı (özgün): " + f["caption"])
    fix_runs(s)
    return s


def kaynakca(prs, pmcler, ek, sayfa):
    pmcler = list(dict.fromkeys(pmcler))
    items = []
    for p in pmcler:
        e = K.makale(p)
        items.append(f"{e['authors']} {K.baslik_noktali(e)} ~{e['journal']}~ {e['year']}. doi:{e['doi']} – {p} – **{e['license_code']}**")
    items += ek
    n = 9
    for i in range(0, len(items), n):
        s = yeni(prs)
        baslik(s, "Kaynakça ve görsel lisansları" + (f" ({i // n + 1})" if len(items) > n else ""), etiket="LİTERATÜR")
        maddeler(s, 0.35, 1.2, 12.6, 5.75, items[i:i + n], size=13, aralik=5)
        dipnot(s, "PMC görselleri AWS PMC Open Access deposundan (pmc-oa-opendata) indirilmiştir; lisans, md5 ve özgün altyazılar sources/perine_*.json içinde.", sayfa)
        fix_runs(s); sayfa += 1
    return sayfa
