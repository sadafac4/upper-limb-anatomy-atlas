# -*- coding: utf-8 -*-
"""Uzun (bölümlü) sunumlar için ortak slayt tipleri – okunabilirlik odaklı (v3).

* Metin kutuları için punto, içerik miktarına göre otomatik seçilir (sigdir); en küçük punto
  sınırına rağmen sığmayan içerik otomatik olarak '(devam)' slaytlarına bölünür.
* Alt sınırlar: anlatım 15 pt, düzyazı 16 pt, lejant/önemli noktalar 13 pt, tablo 13 pt.
"""
import math, pathlib
from PIL import Image
from pptx.util import Inches, Pt
from deck_common import *
import kaynak_kayit as K

ROOT = pathlib.Path(__file__).resolve().parent.parent
VHP = ROOT / "kesitsel" / "images" / "vhp"
ETIKET_RENK = {"KONU ANLATIMI": RGBColor(0x1F, 0x5F, 0x9E), "KLİNİK BAĞLANTI": RGBColor(0xC2, 0x6A, 0x00),
               "DİSEKSİYON": RGBColor(0x2E, 0x7D, 0x32), "GÖRÜNTÜLEME": RGBColor(0x5E, 0x35, 0xB1),
               "VARYASYON": ACCENT, "LİTERATÜR TARAMASI": ACCENT, "KESİT": RGBColor(0x00, 0x69, 0x7C),
               "ŞEMA": RGBColor(0x45, 0x5A, 0x64), "TABLO": RGBColor(0x45, 0x5A, 0x64),
               "ANLATIM": RGBColor(0x1F, 0x5F, 0x9E), "HİSTOLOJİ": RGBColor(0x8E, 0x24, 0xAA)}

# ---------------- metin ölçümü ----------------
def _temiz(s):
    return s.replace("**", "").replace("~", "")

def yukseklik(items, w, size, bullet=True, ara=4):
    """Metnin kutu genişliği w (inç) ve punto size ile kaplayacağı yaklaşık yükseklik (inç)."""
    cw = size * 0.50 / 72          # Calibri ortalama karakter genişliği
    lh = size * 1.18 / 72
    h = 0
    for it in items:
        n = len(_temiz(it)) + (2 if bullet else 0)
        lines = max(1, math.ceil(n * cw / max(w - 0.15, 0.5)))
        h += lines * lh + ara / 72
    return h + 0.1

def sigdir(items, w, h, maxp, minp, bullet=True):
    p = maxp
    while p >= minp:
        if yukseklik(items, w, p, bullet) <= h: return p
        p -= 0.5
    return None

def bol(items, w, h, minp, bullet=True):
    """minp puntoda h yüksekliğine sığan parçalara böler."""
    out, cur = [], []
    for it in items:
        if cur and yukseklik(cur + [it], w, minp, bullet) > h:
            out.append(cur); cur = []
        cur.append(it)
    if cur: out.append(cur)
    return out

def yeni_slayt(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def etiket(s, ad):
    text(s, 10.55, 0.9, 2.55, 0.32, ad, size=11, color=WHITE, bold=True, align=PP_ALIGN.CENTER,
         fill=ETIKET_RENK.get(ad, NAVY), anchor=MSO_ANCHOR.MIDDLE)

def bolum_seridi(s, bolum):
    if bolum:
        text(s, 0.3, 0.9, 6.0, 0.32, bolum, size=11, color=GREY, bold=True)

def baslik(s, t, alt=None, devam=False):
    title_bar(s, t + (" (devam)" if devam else ""), alt)

# ---------------- görsel referans çözümleme ----------------
def cozumle(ref):
    """ref → (yol, kısa altyazı, tam atıf veya None)"""
    tip = ref[0]
    if tip == "pmc":
        _, pmc, key = ref[:3]
        f = K.sekil(pmc, key)
        alt = ref[3] if len(ref) > 3 else f"{f['label']} – {K.atif(pmc, kisa=True)}"
        return ROOT / f["local_path"], alt, K.atif(pmc)
    if tip == "vhp":
        return VHP / ref[1], ref[2], None
    if tip == "vhp_crop":
        return VHP / f"cryo_{ref[1]}_R.jpg", ref[2] if len(ref) > 2 else f"VHP-M kriyokesit {ref[1]}", None
    if tip == "img":                       # ("img", repo-göreli yol, altyazı)
        return ROOT / ref[1], ref[2], None
    raise ValueError(ref)

VHP_ATIF = ("Görüntü: NLM Visible Human Project (NCI Imaging Data Commons, doi:10.5281/zenodo.12690049; "
            "NLM Terms and Conditions 2019). İşleme/kırpma: bu proje.")

def gorselleri_yerlestir(s, refs, X, Y, W, H, yatay=None, alt_boyut=9.5):
    items = [cozumle(r) for r in refs]
    sizes = [Image.open(p).size for p, _, _ in items]
    ar = [w / h for w, h in sizes]
    n = len(items); cap = 0.3
    if n == 1:
        boxes = [(X, Y, W, H - cap)]
    else:
        if yatay is None:
            hs = min(H - cap, (W - 0.15 * (n - 1)) / sum(ar))
            vs = min(W, (H - cap * n) / sum(1 / a for a in ar))
            yatay = hs * hs * sum(ar) >= vs * vs * sum(1 / a for a in ar) * 0.9
        if yatay:
            h = min(H - cap, (W - 0.15 * (n - 1)) / sum(ar)); x = X + (W - (sum(ar) * h + 0.15 * (n - 1))) / 2
            boxes = []
            for a in ar:
                boxes.append((x, Y, a * h, h)); x += a * h + 0.15
        else:
            w = min(W, (H - cap * n) / sum(1 / a for a in ar)); y = Y
            boxes = []
            for a in ar:
                boxes.append((X + (W - w) / 2, y, w, w / a)); y += w / a + cap
    atiflar = []
    for (p, alt, atf), b in zip(items, boxes):
        g = picture_fit(s, p, *b)
        text(s, g["x"] - 0.2, g["y"] + g["h"], g["w"] + 0.4, cap, alt, size=alt_boyut, color=GREY, italic=True, align=PP_ALIGN.CENTER)
        atiflar.append(atf or VHP_ATIF)
    return list(dict.fromkeys(atiflar))

def dipnot(s, atiflar, sayfa):
    footer(s, "  •  ".join(atiflar) if atiflar else "", sayfa)

# ---------------- slayt tipleri ----------------
def kapak(prs, baslik_, alt, satirlar, refs):
    s = yeni_slayt(prs)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height); bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
    text(s, 0.7, 1.0, 7.4, 1.6, baslik_, size=38, color=WHITE, bold=True)
    text(s, 0.7, 2.75, 7.4, 1.1, alt, size=19, color=RGBColor(0xC8, 0xD1, 0xE6))
    text(s, 0.7, 4.0, 7.4, 2.6, satirlar, size=16, color=WHITE)
    for i, r in enumerate(refs[:4]):
        p, _, _ = cozumle(r)
        picture_fit(s, p, 8.4 + (i % 2) * 2.35, 0.45 + (i // 2) * 3.45, 2.25, 3.3)
    text(s, 0.7, 6.75, 7.6, 0.4, "Sunum dili Türkçe; anatomik terimler Terminologia Anatomica (Latince).", size=13, color=RGBColor(0xC8, 0xD1, 0xE6), italic=True)
    fix_runs(s)

def icindekiler(prs, bolumler, ek=None, sayfa=None):
    s = yeni_slayt(prs); title_bar(s, "İçindekiler", "Her bölüm: konu anlatımı → görseller → klinik bağlantılar → varyasyon literatür taraması")
    n = len(bolumler); w = (12.4 - 0.2 * (n - 1)) / n
    for i, b in enumerate(bolumler):
        x = 0.45 + i * (w + 0.2)
        kutu = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.15), Inches(w), Inches(5.4))
        kutu.fill.solid(); kutu.fill.fore_color.rgb = LIGHT; kutu.line.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
        text(s, x + 0.1, 1.25, w - 0.2, 0.55, f"{i + 1}. {b['ad']}", size=22, color=ACCENT, bold=True)
        text(s, x + 0.1, 1.85, w - 0.2, 0.6, b["alt"], size=12.5, color=GREY, italic=True)
        p = sigdir(b["konular"], w - 0.2, 3.9, 15, 11.5) or 11.5
        bullets(s, x + 0.1, 2.5, w - 0.2, 3.95, b["konular"], size=p)
    if ek:
        text(s, 0.5, 6.6, 12.3, 0.38, ek, size=13, color=GREY, italic=True)
    footer(s, "", sayfa); fix_runs(s)

def bolum_kapak(prs, no, b, refs, sayfa):
    s = yeni_slayt(prs)
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(7.2), prs.slide_height); bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
    text(s, 0.6, 0.8, 6.3, 0.6, f"BÖLÜM {no}", size=20, color=RGBColor(0xC8, 0xD1, 0xE6), bold=True)
    text(s, 0.6, 1.35, 6.3, 1.0, b["ad"], size=48, color=WHITE, bold=True)
    text(s, 0.6, 2.5, 6.3, 1.0, [b["baslik"], b["alt"]], size=18, color=RGBColor(0xC8, 0xD1, 0xE6))
    p = sigdir(b["konular"], 6.3, 3.4, 17, 13) or 13
    bullets(s, 0.6, 3.7, 6.3, 3.5, b["konular"], size=p, color=WHITE)
    atif = gorselleri_yerlestir(s, refs, 7.45, 0.4, 5.6, 6.3)
    text(s, 7.45, 6.9, 5.6, 0.55, "  •  ".join(atif), size=7.5, color=GREY)
    text(s, 12.4, 7.05, 0.65, 0.3, str(sayfa), size=11, color=GREY, align=PP_ALIGN.RIGHT); fix_runs(s)
    return 1

def anlatim(prs, d, sayfa, bolum=None):
    """Madde işaretli anlatım; gerekirse devam slaytlarına bölünür. Döner: üretilen slayt sayısı."""
    figs = d.get("figs") or []
    if figs:
        X, W = 0.3, 7.0; minp, maxp = 15, 19
    else:
        X, W = 0.45, 12.4; minp, maxp = 16, 22
    H = 5.55
    p = sigdir(d["metin"], W, H, maxp, minp)
    parcalar = [d["metin"]] if p else bol(d["metin"], W, H, minp)
    for i, parca in enumerate(parcalar):
        s = yeni_slayt(prs)
        baslik(s, d["baslik"], d.get("alt"), devam=i > 0); bolum_seridi(s, bolum)
        etiket(s, "KLİNİK BAĞLANTI" if d["tip"] == "klinik" else d.get("etiket", "KONU ANLATIMI"))
        pp = p or sigdir(parca, W, H, maxp, minp) or minp
        bullets(s, X, 1.35, W, H, parca, size=pp)
        atif = []
        if figs:
            atif = gorselleri_yerlestir(s, figs, 7.55, 1.35, 5.5, 5.5)
        dipnot(s, atif, sayfa + i); fix_runs(s)
        if d.get("not"): notes(s, d["not"])
    return len(parcalar)

def duzyazi(prs, d, sayfa, bolum=None):
    """Paragraf tarzı konu anlatımı (madde işareti yok). d: baslik, alt, paragraflar, figs(ops.)"""
    figs = d.get("figs") or []
    X, W = (0.45, 7.1) if figs else (0.6, 12.1)
    H = 5.5; minp, maxp = 16, 20
    pars = d["paragraflar"]
    p = sigdir(pars, W, H, maxp, minp, bullet=False)
    parcalar = [pars] if p else bol(pars, W, H, minp, bullet=False)
    for i, parca in enumerate(parcalar):
        s = yeni_slayt(prs)
        baslik(s, d["baslik"], d.get("alt"), devam=i > 0); bolum_seridi(s, bolum); etiket(s, "ANLATIM")
        pp = p or sigdir(parca, W, H, maxp, minp, bullet=False) or minp
        tb = text(s, X, 1.35, W, H, parca, size=pp, color=NAVY)
        for para in tb.text_frame.paragraphs:
            para.space_after = Pt(9); para.line_spacing = 1.08
        atif = []
        if figs:
            atif = gorselleri_yerlestir(s, figs, 7.75, 1.35, 5.3, 5.5)
        dipnot(s, atif, sayfa + i); fix_runs(s)
    return len(parcalar)

def tablo(prs, d, sayfa, bolum=None, et="TABLO"):
    """Tablo; satır yüksekliği metne göre hesaplanır, sığmayan satırlar devam slaytına geçer."""
    cols = len(d["sutunlar"]); gen = d.get("genislik") or [1] * cols; tot = sum(gen)
    W = 12.73; ws = [W * g / tot for g in gen]
    fs = d.get("boyut", 13.5)
    def satir_h(row):
        return max(yukseklik([v], w, fs, bullet=False, ara=0) for v, w in zip(row, ws)) + 0.08
    hh = 0.5; maxH = 5.25
    gruplar, cur, h = [], [], hh
    for r in d["satirlar"]:
        rh = satir_h(r)
        if cur and h + rh > maxH:
            gruplar.append(cur); cur, h = [], hh
        cur.append(r); h += rh
    if cur: gruplar.append(cur)
    for gi, grup in enumerate(gruplar):
        s = yeni_slayt(prs)
        baslik(s, d["baslik"], d.get("alt"), devam=gi > 0); bolum_seridi(s, bolum); etiket(s, et)
        H = hh + sum(satir_h(r) for r in grup)
        gt = s.shapes.add_table(len(grup) + 1, cols, Inches(0.3), Inches(1.35), Inches(W), Inches(H)).table
        for j, w in enumerate(ws): gt.columns[j].width = Inches(w)
        gt.rows[0].height = Inches(hh)
        for j, hd in enumerate(d["sutunlar"]):
            c = gt.cell(0, j); c.text = hd; c.fill.solid(); c.fill.fore_color.rgb = NAVY
            for p in c.text_frame.paragraphs:
                for r in p.runs: r.font.size = Pt(fs + 0.5); r.font.bold = True; r.font.color.rgb = WHITE; r.font.name = FONT
        for i, row in enumerate(grup, 1):
            gt.rows[i].height = Inches(satir_h(row))
            for j, v in enumerate(row):
                c = gt.cell(i, j); c.text = v; c.fill.solid(); c.fill.fore_color.rgb = LIGHT if i % 2 else WHITE
                for p in c.text_frame.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(fs); r.font.color.rgb = NAVY; r.font.name = FONT; r.font.bold = (j == 0)
        if d.get("dip") and gi == len(gruplar) - 1:
            text(s, 0.3, 6.62, 12.7, 0.38, d["dip"], size=12, color=GREY, italic=True)
        footer(s, d.get("kaynak", "Kaynak: standart anatomi bilgisi (Terminologia Anatomica)."), sayfa + gi); fix_runs(s)
    return len(gruplar)

def _kutu(s, x, y, w, h, t, renk, yazi=WHITE, boyut=13):
    k = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    k.fill.solid(); k.fill.fore_color.rgb = renk; k.line.color.rgb = WHITE
    tf = k.text_frame; tf.margin_left = tf.margin_right = Inches(0.03); tf.word_wrap = True
    tf.text = t
    for p in tf.paragraphs:
        p.alignment = PP_ALIGN.CENTER
        for r in p.runs: r.font.size = Pt(boyut); r.font.bold = True; r.font.color.rgb = yazi; r.font.name = FONT
    return (x, y, w, h)

def _bag(s, a, b, renk=GREY, kalin=1.5):
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(ax + aw), Inches(ay + ah / 2), Inches(bx), Inches(by + bh / 2))
    ln.line.color.rgb = renk; ln.line.width = Pt(kalin)

def _sema_metin(s, metin, X, W):
    p = sigdir(metin, W, 5.55, 16, 13) or 13
    bullets(s, X, 1.35, W, 5.55, metin, size=p)

def sema_plexus(prs, d, sayfa, bolum=None):
    s = yeni_slayt(prs)
    baslik(s, d["baslik"], d.get("alt")); bolum_seridi(s, bolum); etiket(s, "ŞEMA")
    SAR = RGBColor(0xE0, 0xA1, 0x00); YES = RGBColor(0x2E, 0x7D, 0x32); MAV = RGBColor(0x1F, 0x5F, 0x9E)
    xs = [0.3, 1.75, 3.25, 4.85, 6.5]; w = 1.3; h = 0.46
    for x, t in zip(xs, ["Radices", "Trunci", "Divisiones", "Fasciculi", "Rami terminales"]):
        text(s, x - 0.05, 1.3, w + 0.35, 0.32, t, size=13, color=GREY, bold=True, align=PP_ALIGN.CENTER)
    R = {k: _kutu(s, xs[0], 1.7 + i * 0.95, w, h, k, MAV) for i, k in enumerate(["C5", "C6", "C7", "C8", "T1"])}
    TR = {"sup": _kutu(s, xs[1], 2.15, w, h, "T. superior", MAV, boyut=12), "med": _kutu(s, xs[1], 3.6, w, h, "T. medius", MAV, boyut=12),
          "inf": _kutu(s, xs[1], 5.05, w, h, "T. inferior", MAV, boyut=12)}
    for r, t in [("C5", "sup"), ("C6", "sup"), ("C7", "med"), ("C8", "inf"), ("T1", "inf")]: _bag(s, R[r], TR[t])
    DV = {}
    for t, y in [("sup", 1.85), ("med", 3.3), ("inf", 4.75)]:
        DV[t + "A"] = _kutu(s, xs[2], y, w, 0.4, "ön", SAR, NAVY, 12); DV[t + "P"] = _kutu(s, xs[2], y + 0.52, w, 0.4, "arka", YES, WHITE, 12)
        _bag(s, TR[t], DV[t + "A"]); _bag(s, TR[t], DV[t + "P"])
    F = {"lat": _kutu(s, xs[3], 2.1, w, h, "F. lateralis", SAR, NAVY, 12), "post": _kutu(s, xs[3], 3.65, w, h, "F. posterior", YES, boyut=12),
         "med": _kutu(s, xs[3], 5.2, w, h, "F. medialis", SAR, NAVY, 12)}
    for a, f in [("supA", "lat"), ("medA", "lat"), ("supP", "post"), ("medP", "post"), ("infP", "post"), ("infA", "med")]: _bag(s, DV[a], F[f])
    TT = {"mc": _kutu(s, xs[4], 1.65, w + 0.3, h, "N. musculocutaneus", SAR, NAVY, 11), "ax": _kutu(s, xs[4], 2.95, w + 0.3, h, "N. axillaris", YES, WHITE, 12),
          "rad": _kutu(s, xs[4], 3.65, w + 0.3, h, "N. radialis", YES, WHITE, 12), "med": _kutu(s, xs[4], 4.55, w + 0.3, h, "N. medianus", SAR, NAVY, 12),
          "uln": _kutu(s, xs[4], 5.6, w + 0.3, h, "N. ulnaris", SAR, NAVY, 12)}
    for f, t in [("lat", "mc"), ("lat", "med"), ("post", "ax"), ("post", "rad"), ("med", "med"), ("med", "uln")]: _bag(s, F[f], TT[t])
    text(s, 0.3, 6.3, 7.9, 0.6, "Sarı: ön divisiolar → fleksör sinirler; yeşil: arka divisiolar → ekstensör sinirler.", size=12, color=GREY, italic=True)
    _sema_metin(s, d["metin"], 8.35, 4.75)
    footer(s, "Şema: bu projede standart anatomi bilgisinden çizilmiştir (gerçek görüntü değildir).", sayfa); fix_runs(s)
    return 1

def sema_arter(prs, d, sayfa, bolum=None):
    s = yeni_slayt(prs)
    baslik(s, d["baslik"], d.get("alt")); bolum_seridi(s, bolum); etiket(s, "ŞEMA")
    KIR = RGBColor(0xB7, 0x1C, 0x1C)
    zinc = [("A. subclavia", "kosta I lateral kenarı"), ("A. axillaris", "m. teres major alt kenarı"), ("A. brachialis", "fossa cubiti (collum radii)")]
    y = 1.4; prev = None
    for ad, sinir in zinc:
        b = _kutu(s, 0.6, y, 2.4, 0.52, ad, KIR)
        if prev:
            ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1.8), Inches(prev[1] + 0.52), Inches(1.8), Inches(y)); ln.line.color.rgb = KIR; ln.line.width = Pt(2.5)
        text(s, 3.1, y + 0.55, 4.2, 0.32, f"↓ sınır: {sinir}", size=12, color=GREY, italic=True)
        prev = b; y += 1.05
    text(s, 3.1, 2.35, 4.4, 0.7, "1: a. thoracica sup. • 2: a. thoracoacromialis, a. thoracica lat. • 3: a. subscapularis, aa. circumflexae humeri", size=11.5, color=NAVY)
    text(s, 3.1, 3.4, 4.4, 0.6, "a. profunda brachii • aa. collaterales ulnares • a. nutricia humeri", size=11.5, color=NAVY)
    r = _kutu(s, 0.2, y + 0.1, 1.7, 0.52, "A. radialis", KIR); u = _kutu(s, 2.1, y + 0.1, 1.7, 0.52, "A. ulnaris", KIR)
    for b in (r, u):
        ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1.8), Inches(prev[1] + 0.52), Inches(b[0] + b[2] / 2), Inches(b[1])); ln.line.color.rgb = KIR; ln.line.width = Pt(2.5)
    text(s, 3.95, y + 0.1, 3.5, 0.7, "a. interossea communis; rekürren dallar → dirsek anastomozu", size=11.5, color=NAVY)
    y2 = y + 1.15
    p = _kutu(s, 0.2, y2, 1.7, 0.65, "Arcus palmaris profundus", RGBColor(0x8E, 0x24, 0xAA), boyut=11)
    q = _kutu(s, 2.1, y2, 1.7, 0.65, "Arcus palmaris superficialis", RGBColor(0x8E, 0x24, 0xAA), boyut=11)
    for a, b in ((r, p), (u, q)):
        ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(a[0] + a[2] / 2), Inches(a[1] + 0.52), Inches(b[0] + b[2] / 2), Inches(b[1])); ln.line.color.rgb = KIR; ln.line.width = Pt(2.5)
    _sema_metin(s, d["metin"], 7.7, 5.4)
    footer(s, "Şema: bu projede standart anatomi bilgisinden çizilmiştir (gerçek görüntü değildir).", sayfa); fix_runs(s)
    return 1

def gorsel(prs, d, sayfa, bolum=None):
    """Görsel ağırlıklı slayt: solda görsel(ler), sağda lejant + önemli noktalar.
    Metin 13 pt'ye kadar küçültülür; sığmazsa 'önemli noktalar' görsel küçültülerek devam slaytına geçer."""
    TX, TW = 7.35, 5.75
    lej = d.get("lejant") or []; nok = d.get("noktalar") or []
    def ciz(s, figs_box, lej_, nok_, metin_h):
        atif = gorselleri_yerlestir(s, d["figs"], *figs_box, d.get("yatay"))
        y = 1.35
        bloklar = []
        if lej_: bloklar.append(("Şekildeki etiketler", lej_))
        if nok_: bloklar.append((d.get("nbaslik", "Önemli noktalar"), nok_))
        tum = [x for _, b in bloklar for x in b]
        p = sigdir(tum, TW, metin_h - 0.4 * len(bloklar), 16, 13) or 13
        for bt, b in bloklar:
            text(s, TX, y, TW, 0.36, bt, size=14, color=ACCENT, bold=True); y += 0.38
            hb = yukseklik(b, TW, p)
            bullets(s, TX, y, TW, hb, b, size=p); y += hb + 0.05
        return atif
    s = yeni_slayt(prs)
    baslik(s, d["baslik"], d.get("alt")); bolum_seridi(s, bolum); etiket(s, d.get("etiket", "DİSEKSİYON"))
    tum = lej + nok
    if sigdir(tum, TW, 5.5 - 0.8, 16, 13):
        atif = ciz(s, (0.3, 1.35, 6.85, 5.55), lej, nok, 5.5)
        n = 1
    else:
        atif = ciz(s, (0.3, 1.35, 6.85, 5.55), lej, [], 5.5)
        dipnot(s, atif, sayfa); fix_runs(s)
        s = yeni_slayt(prs)
        baslik(s, d["baslik"], d.get("alt"), devam=True); bolum_seridi(s, bolum); etiket(s, d.get("etiket", "DİSEKSİYON"))
        atif = ciz(s, (0.3, 1.35, 6.85, 5.55), [], nok, 5.5)
        n = 2
    if any(r[0] == "pmc" and K.nc_mi(r[1]) for r in d["figs"]):
        text(s, TX, 6.6, TW, 0.32, "Lisans: CC BY-NC – yalnızca ticari olmayan eğitim amaçlı kullanım.", size=10.5, color=ACCENT, italic=True)
    dipnot(s, atif, sayfa + n - 1); fix_runs(s)
    notes(s, "\n".join(K.atif(r[1]) + "\nAltyazı: " + K.sekil(r[1], r[2])["caption"] for r in d["figs"] if r[0] == "pmc"))
    return n

def lit_tablo(prs, baslik_, alt, satirlar, sayfa, bolum=None):
    d = dict(baslik=baslik_, alt=alt, sutunlar=["Varyasyon", "Çalışma", "Örneklem / yöntem", "Sıklık / ana bulgu", "Klinik önem"],
             satirlar=satirlar, genislik=[2.3, 2.1, 2.0, 3.3, 3.0], boyut=13,
             kaynak="Sıklık verileri ilgili makalelerden aynen aktarılmıştır; tam künyeler bölümün çalışma slaytlarında ve kaynakçada.")
    return tablo(prs, d, sayfa, bolum, et="LİTERATÜR TARAMASI")

def kaynakca(prs, pmcler, baslik_, sayfa_bas):
    pmcler = list(dict.fromkeys(pmcler))
    n = 8; sayfa = sayfa_bas
    for i in range(0, len(pmcler), n):
        s = yeni_slayt(prs)
        title_bar(s, baslik_ + (f" ({i // n + 1})" if len(pmcler) > n else ""))
        items = []
        for p in pmcler[i:i + n]:
            e = K.makale(p)
            items.append(f"{e['authors']} {K.baslik_noktali(e)} ~{e['journal']}~ {e['year']}. doi:{e['doi']} – {p} – **{e['license_code']}**")
        pp = sigdir(items, 12.7, 5.9, 13, 10.5) or 10.5
        bullets(s, 0.3, 1.0, 12.7, 5.95, items, size=pp)
        footer(s, "Görseller PMC Open Access AWS deposundan (pmc-oa-opendata); lisans, md5 ve altyazılar sources/*.json içinde.", sayfa); fix_runs(s)
        sayfa += 1
    return sayfa
