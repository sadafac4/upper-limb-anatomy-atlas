#!/usr/bin/env python3
"""Build the cross-sectional (kesitsel) pilot deck from VHP-M cryosection + frozen-CT crops.

Run after: vhp_index_headers.py (index), vhp_crops.py (crops), vhp_assets.py (locators, scout).
Outputs kesitsel/Kesitsel_Anatomi_Pilot.pptx and kesitsel/qa/label_qa.json.
"""
import json, pathlib, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from deck_common import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = ROOT / "kesitsel" / "images" / "vhp"
QA = ROOT / "kesitsel" / "qa"; QA.mkdir(exist_ok=True)

SRC_VHP = ("Kaynak: NLM Visible Human Project – Visible Human Male (kriyokesit a_vm{n}, donmuş BT c_vm{n}.fro); "
           "NCI Imaging Data Commons 'nlm_visible_human_project' (doi:10.5281/zenodo.12690049). "
           "Lisans: NLM Terms and Conditions (21.05.2019). Kırpma/yön/etiketler: bu proje.")
ORIENT = ("Yönelim: radyolojik (ön yukarıda, hastanın sağı izleyicinin solunda). Sağ üst ekstremite. "
          "Kadavrada kol gövde yanında, ön kol pronasyonda olduğundan kompartmanlar eğik izlenir.")

# label: (text, (x, y) in crop px, side 'L'/'R', snap) ; snap='bone' → move to nearest bone-coloured pixel
LEVELS = [
 dict(n=1320, title="Düzey 1 – Articulatio humeri (caput humeri düzeyi)",
      sub="Kriyokesit ve aynı kesit numaralı donmuş BT – NLM kesit no. 1320",
      labels=[("M. deltoideus", (91, 309), "L", None), ("Caput humeri", (251, 259), "L", "bone"),
              ("M. infraspinatus", (331, 509), "L", None),
              ("M. pectoralis major", (451, 99), "R", None), ("Clavicula", (646, 129), "R", "bone"),
              ("M. subscapularis", (431, 339), "R", None), ("Scapula", (421, 452), "R", "bone"),
              ("Pulmo dexter (apex)", (641, 309), "R", None)],
      ct=["Caput humeri", "Scapula", "Clavicula"],
      notes=["Caput humeri ile cavitas glenoidalis arasındaki küçük temas yüzeyi, art. humeri'nin geniş hareket açıklığını ve **instabiliteye yatkınlığını** açıklar.",
             "Rotator manşetin kesitteki ilişkisi: **M. subscapularis** scapula'nın önünde, **M. infraspinatus** arkasında.",
             "M. deltoideus eklemi lateral, ön ve arkadan sarar; altında n. axillaris seyreder (bu kesitte ayrı etiketlenmemiştir)."]),
 dict(n=1490, title="Düzey 2 – Brachium, orta üçte bir",
      sub="Kol kompartmanları ve medial damar–sinir demeti – NLM kesit no. 1490",
      labels=[("Humerus (corpus)", (161, 229), "L", "bone"),
              ("Arka kompartman: M. triceps brachii", (156, 349), "L", None),
              ("Ön kompartman: M. biceps brachii, M. brachialis", (216, 110), "R", None),
              ("Damar–sinir demeti: A. brachialis, Vv. brachiales, N. medianus", (262, 259), "R", None)],
      ct=[], ct_note="BT görüş alanı (FOV 480 mm) kolu kısmen dışarıda bırakır; kenarda kesilme artefaktı vardır. Güvenilir kemik etiketi konamadığından BT etiketlenmemiştir.",
      notes=["Kol, septum intermusculare brachii mediale et laterale ile **ön (fleksör)** ve **arka (ekstensör)** kompartmana ayrılır.",
             "Medial damar–sinir demeti kolun iç yüzünde, ön ve arka kompartman sınırında seyreder; nabız ve kompresyon noktasıdır.",
             "N. radialis bu düzeyde humerus arkasında sulcus nervi radialis içindedir; cisim kırıklarında risk altındadır (bu kesitte ayrı etiketlenmemiştir)."]),
 dict(n=1560, title="Düzey 3 – Brachium, distal (suprakondiler) bölge",
      sub="Humerus'un üçgenimsi distal kesiti – NLM kesit no. 1560",
      labels=[("Humerus (suprakondiler bölge)", (130, 250), "L", "bone"),
              ("Arka kompartman: M. triceps brachii", (200, 320), "L", None),
              ("Ön kompartman: M. brachialis, M. biceps brachii", (240, 180), "R", None),
              ("Damar–sinir demeti (A. brachialis, N. medianus)", (280, 255), "R", None)],
      ct=[], ct_note="BT görüş alanı kolu kısmen dışarıda bırakır; BT etiketlenmemiştir (kenar artefaktı kemikle karışabilir).",
      notes=["Distal humerus mediolateral olarak genişleyerek epikondillere uzanır; kesit üçgenimsi hale gelir.",
             "Suprakondiler humerus kırıklarında (özellikle çocuklarda) öndeki **a. brachialis** ve **n. medianus** yaralanma riski taşır."]),
 dict(n=1615, title="Düzey 4 – Articulatio cubiti",
      sub="Dirsek eklem aralığı ve fossa cubiti içeriği – NLM kesit no. 1615",
      labels=[("Eklem aralığı ve eklem kıkırdağı (art. cubiti)", (125, 300), "L", None),
              ("Lateral kas grubu: M. brachioradialis, Mm. extensores carpi radiales", (190, 150), "R", None),
              ("Fossa cubiti: A. brachialis ve N. medianus bölgesi", (255, 232), "R", None),
              ("Ön kas grubu (M. brachialis, fleksör–pronator kaslar)", (300, 330), "R", None)],
      ct=[], ct_note="Bu düzeyde kol BT görüş alanının dışında kalmaktadır; yalnızca kriyokesit yorumlanmıştır.",
      notes=["Fossa cubiti içeriği lateralden mediale: **tendo m. bicipitis brachii – a. brachialis – n. medianus**.",
             "Eklem kıkırdağı kriyokesitte parlak beyaz hat olarak seçilir; BT'de kıkırdak doğrudan görünmez.",
             "Kemik yüzeylerin tek tek adlandırılması (trochlea/capitulum) kesitin eğikliği nedeniyle pilotta yapılmamıştır."]),
 dict(n=1645, title="Düzey 5 – Antebrachium, proksimal bölüm",
      sub="Radius ve ulna, mobil kas grubu ve fleksör–pronator kitle – NLM kesit no. 1645",
      labels=[("Radius", (145, 255), "L", "bone"), ("Ulna", (110, 330), "L", "bone"),
              ("Arka (ekstensör) kas grubu", (80, 365), "L", None),
              ("Mobil kas grubu: M. brachioradialis, Mm. extensores carpi radiales", (190, 130), "R", None),
              ("Damar–sinir yapıları (a. brachialis dalları, n. medianus)", (255, 200), "R", None),
              ("Fleksör–pronator kas grubu", (265, 300), "R", None)],
      ct=[], ct_note="Kol BT görüş alanının kenarında; radius halkası kısmen izlenir, ancak kenar artefaktı nedeniyle etiketlenmemiştir.",
      notes=["Radius–ulna ayrımı, 1 mm donmuş BT'de kemiklerin proksimalden distale kesintisiz izlenmesiyle doğrulanmıştır (bkz. QA).",
             "N. radialis'in derin dalı (n. interosseus posterior) bu bölgede m. supinator içinden geçer – topografik sunumdaki Frohse arkadı slaytı ile karşılaştırınız."]),
 dict(n=1740, title="Düzey 6 – Antebrachium, distal üçte bir",
      sub="Pronasyondaki ön kolda radius ve ulna – NLM kesit no. 1740",
      labels=[("Radius", (167, 157), "L", "bone"), ("Ulna", (62, 287), "L", "bone"),
              ("Ekstensör (arka) kompartman", (67, 197), "L", None),
              ("Fleksör (ön) kompartman", (200, 260), "R", None)],
      ct=["Radius", "Ulna"],
      notes=["Ön kol **pronasyonda**: radius, ulnanın önünden çaprazlanarak mediale yer değiştirmiştir.",
             "Distalde kas karınları tendonlara dönüşür; fleksör kompartman ekstensörden belirgin şekilde kalındır.",
             "Ulnanın subkutan arka kenarı deriye yakındır (kırıkların sık açık olmasının anatomik temeli)."]),
 dict(n=1785, title="Düzey 7 – Articulatio radiocarpalis / ossa carpi",
      sub="El bileği düzeyi (kesit eğik) – NLM kesit no. 1785",
      labels=[("Caput ulnae (distal uç)", (120, 235), "L", "bone"),
              ("Ossa carpi", (215, 185), "R", "bone")],
      ct=["Caput ulnae", "Ossa carpi"],
      notes=["Karpal kemikler 1785 civarında ortaya çıkar (radiokarpal düzey ≈ 1775–1780).",
             "Canalis carpi, ossa carpi ile retinaculum musculorum flexorum arasında kalır; içinden **n. medianus** ve 9 fleksör tendon geçer.",
             "El gövdeye eğik yaslandığından tek tek karpal kemik adlandırması pilotta yapılmamıştır; tam sürümde 3B izleme ile eklenecektir."]),
 dict(n=1830, title="Düzey 8 – Metacarpus (avuç içi)",
      sub="Metakarpal kemikler, interosseöz, tenar ve hipotenar kaslar – NLM kesit no. 1830",
      labels=[("Hipotenar kaslar", (90, 270), "L", None), ("Ossa metacarpi", (132, 188), "L", "bone"),
              ("Mm. interossei", (155, 160), "L", None),
              ("Başparmak (pollex) kemikleri", (265, 82), "R", None),
              ("Tenar kaslar", (220, 120), "R", None), ("Fleksör tendonlar", (215, 180), "R", None)],
      ct=["Ossa metacarpi", "Başparmak (pollex) kemikleri"],
      notes=["Ulnar taraf (hipotenar) aşağı-solda, radial taraf (başparmak) yukarı-sağdadır – el bileği düzeyindeki ulna konumu ile tutarlıdır.",
             "Mm. interossei metakarpallar arasında; palmar tarafta fleksör tendonlar izlenir."]),
]

def bone_like(rgb):
    r, g, b = [rgb[..., i].astype(int) for i in range(3)]
    return (r > 170) & (g > 135) & (b > 115) & ((r - b) < 72)

def snap_bone(img, pt, radius=30):
    a = np.asarray(img); m = bone_like(a)
    m = ndi.binary_opening(m, iterations=1)
    x, y = pt; H, W = m.shape
    y0, y1, x0, x1 = max(0, y - radius), min(H, y + radius), max(0, x - radius), min(W, x + radius)
    ys, xs = np.nonzero(m[y0:y1, x0:x1])
    if len(xs) == 0: return pt, None
    d = (xs + x0 - x) ** 2 + (ys + y0 - y) ** 2; i = d.argmin()
    nx, ny = int(xs[i] + x0), int(ys[i] + y0)
    lab, _ = ndi.label(m); comp = lab == lab[ny, nx]
    if 30 < comp.sum() < 40000:                       # move to the interior of that bone
        dist = ndi.distance_transform_edt(comp)
        yy, xx = np.nonzero(comp)
        near = (xx - nx) ** 2 + (yy - ny) ** 2 < 25 ** 2
        j = np.argmax(np.where(near, dist[yy, xx], -1)); nx, ny = int(xx[j]), int(yy[j])
    return (nx, ny), float(np.hypot(nx - x, ny - y))

def ct_bone_points(ct_path, cryo_points):
    """For each requested CT label, snap the corresponding cryo point to the nearest CT bone component."""
    a = np.asarray(Image.open(ct_path).convert("L")).astype(int)   # window 500/2000 → >~102 is >300 HU
    m = a > 110; lab, n = ndi.label(m)
    out = []
    for name, p in cryo_points:
        if n == 0: out.append((name, None)); continue
        best = None
        for i in range(1, n + 1):
            yy, xx = np.nonzero(lab == i)
            if len(xx) < 25: continue
            d = np.min((xx - p[0]) ** 2 + (yy - p[1]) ** 2) ** 0.5
            if best is None or d < best[0]:
                k = np.argmin((xx - p[0]) ** 2 + (yy - p[1]) ** 2); best = (d, (int(xx[k]), int(yy[k])))
        out.append((name, best[1] if best and best[0] < 70 else None))
    return out

def level_slide(prs, L, page, qa):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title_bar(s, L["title"], L["sub"])
    n = L["n"]
    cryo = Image.open(IMG / f"cryo_{n}_R.jpg")
    meta = json.loads((IMG / f"meta_{n}.json").read_text())
    pts, rec = [], []
    for t, p, side, snap in L["labels"]:
        q, shift = (snap_bone(cryo, p) if snap == "bone" else (p, None))
        pts.append((t, q, side)); rec.append(dict(label=t, given=p, used=q, snap_shift_px=shift))
    g = picture_fit(s, IMG / f"cryo_{n}_R.jpg", 2.05, 1.0, 4.4, 4.85)
    text(s, g["x"], g["y"] + g["h"] + 0.02, g["w"], 0.28, "Kriyokesit (renkli fotoğraf, 0,33 mm/piksel)", size=10, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    labels(s, g, [(t, q) for t, q, sd in pts if sd == "L"], 0.15, 1.82, "L", 1.0, 5.75, size=11)
    labels(s, g, [(t, q) for t, q, sd in pts if sd == "R"], 6.55, 2.05, "R", 1.0, 5.75, size=11)
    # CT panel
    gc = picture_fit(s, IMG / f"ct_{n}_R.png", 8.7, 1.0, 2.75, 4.75)
    text(s, gc["x"] - 0.1, gc["y"] + gc["h"] + 0.02, gc["w"] + 0.2, 0.28, "Donmuş BT, aynı kesit no. (P 40/400)", size=10, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    want = [(name, next(q for t, q, sd in pts if t.startswith(name.split(" (")[0]) or name.startswith(t.split(" (")[0]))) for name in L["ct"]]
    ctp = ct_bone_points(IMG / f"ctbone_{n}_R.png", want)
    ok = [(t, q) for t, q in ctp if q is not None]
    labels(s, gc, ok, 11.55, 1.6, "R", 2.55, 5.75, size=11)
    rec.append(dict(ct_labels=[dict(label=t, point=q) for t, q in ctp]))
    if L.get("ct_note"):
        text(s, gc["x"] - 0.15, gc["y"] + gc["h"] + 0.32, gc["w"] + 0.3, 0.7, L["ct_note"], size=9, color=ACCENT, italic=True)
    # locator
    picture_fit(s, IMG / f"loc_{n}.jpg", 11.5, 1.0, 1.7, 1.0)
    text(s, 11.5, 2.0, 1.7, 0.45, "Konum: tüm kesit (kırmızı = büyütülen alan)", size=8, color=GREY, italic=True)
    bullets(s, 0.3, 6.05, 12.8, 0.95, L["notes"], size=11.5)
    footer(s, SRC_VHP.format(n=n) + "  " + ORIENT, page)
    fix_runs(s)
    notes(s, f"Kriyokesit dosyası: {meta['cryo_file']}\nBT dosyası: {meta['ct_file']} (kesit no. {meta['ct_slice']})\n"
             f"Kırpma kutusu (kriyo piksel, dikey çevrilmiş): {meta['box_cryo_px']}\nKayıt: {meta['reg']}\n"
             "Etiket noktaları kaynak görüntü pikselinde tanımlıdır; kemik etiketleri renk tabanlı kemik maskesine 'snap' edilmiştir.")
    qa[str(n)] = dict(meta=meta, labels=rec)

def build():
    prs = new_deck(); qa = {}
    # 1 – cover
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height); bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
    text(s, 0.7, 1.4, 7.4, 1.2, "Membrum Superius – Kesitsel Anatomi", size=38, color=WHITE, bold=True)
    text(s, 0.7, 2.95, 7.4, 1.0, "Gerçek kadavra kriyokesitleri ile aynı kadavranın aynı düzeydeki BT görüntülerinin karşılaştırmalı atlası", size=18, color=RGBColor(0xC8, 0xD1, 0xE6))
    text(s, 0.7, 4.2, 7.4, 1.4, ["PİLOT SÜRÜM – 8 düzey (omuzdan avuç içine)", "Veri: NLM Visible Human Project – Visible Human Male",
                                 "Tüm görüntüler gerçek kadavra/radyoloji verisidir; üretilmiş (sentetik) görüntü kullanılmamıştır."], size=14, color=WHITE)
    picture_fit(s, IMG / "cryo_1490_R.jpg", 8.6, 0.6, 4.3, 3.1)
    picture_fit(s, IMG / "ct_1740_R.png", 8.6, 3.9, 2.1, 3.0); picture_fit(s, IMG / "cryo_1740_R.jpg", 10.8, 3.9, 2.1, 3.0)
    text(s, 0.7, 6.7, 12, 0.4, "Sunum dili Türkçe; anatomik terimler Terminologia Anatomica (Latince).", size=11, color=RGBColor(0xC8, 0xD1, 0xE6), italic=True)
    # 2 – method
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title_bar(s, "Veri kaynağı ve düzey eşleştirme yöntemi", "Neden bu kesitler gerçekten 'aynı düzey'dir?")
    bullets(s, 0.3, 1.05, 8.3, 5.6, [
        "**Visible Human Male** (erkek; DICOM başlığında yaş 39): aynı kadavradan taze BT, MR, donmuş BT ve 1 mm aralıklı renkli kriyomakrotom kesitleri (2048×1216 piksel, 0,33 mm/piksel) elde edilmiştir.",
        "NLM'nin belgelerine göre erkek veri setinde anatomik kesitler 1 mm aralıklıdır ve **BT aksiyel görüntüleri ile çakışır**; kriyokesit a_vm#### ile donmuş BT c_vm####.fro aynı kesit numarasını paylaşır (Ackerman 1995).",
        "Veriler NCI Imaging Data Commons'ta DICOM olarak yayımlanmıştır. Her görüntünün özgün NLM dosya adı DICOM etiketi (0009,1001)'de korunur; eşleştirme bu numaraya dayanır, **tahmin edilmemiştir**.",
        "Yalnızca düzlem içi kayma, gövde ve uzuv maskelerinin çapraz korelasyonu ile hesaplanmıştır (ölçek sabit: 0,33/0,9375 mm). Kontrol: BT kemik konturları kriyokesitteki kemiklerle çakıştırılmıştır (Dice 0,84–0,93; uzuvda yerel doku Dice 0,94–0,97).",
        "Kriyokesit DICOM yönelimi (1,0,0 / 0,−1,0) nedeniyle görüntüler dikey çevrilerek BT ile aynı **radyolojik yönelime** getirilmiştir.",
        "**Sınırlılık:** donmuş BT'nin görüş alanı 480 mm'dir; kol ortası–dirsek düzeylerinde kol kısmen alan dışında kalır. Aksiyel MR yalnızca baş bölgesini kapsar, bu nedenle ekstremite düzeylerinde MR karşılığı yoktur.",
    ], size=13)
    g = picture_fit(s, IMG / "scout_coronal_mip.png", 8.9, 1.0, 4.2, 5.7)
    text(s, 8.7, 6.65, 4.6, 0.35, "Donmuş BT koronal MIP; sarı çizgiler = sunumdaki kesit numaraları", size=9.5, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    footer(s, "Spitzer V, Ackerman MJ, Scherzinger AL, Whitlock D. The Visible Human Male: a technical report. J Am Med Inform Assoc. 1996;3(2):118–30. • "
              "Ackerman MJ. Accessing the Visible Human Project. D-Lib Magazine, Oct 1995. • Fedorov A, et al. NCI Imaging Data Commons. RadioGraphics. 2023;43(12):e230180.", 2)
    fix_runs(s)
    for i, L in enumerate(LEVELS):
        level_slide(prs, L, i + 3, qa)
    # last – sources & limitations
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title_bar(s, "Kaynaklar, lisans ve kalite kontrol notları")
    bullets(s, 0.3, 1.05, 12.7, 5.8, [
        "Spitzer V, Ackerman MJ, Scherzinger AL, Whitlock D. The Visible Human Male: a technical report. ~J Am Med Inform Assoc.~ 1996;3(2):118–130.",
        "Ackerman MJ. Accessing the Visible Human Project. ~D-Lib Magazine~, October 1995 (BT ve anatomik kesitlerin 1 mm aralıkla çakıştığı belirtilir).",
        "Fedorov A, et al. National Cancer Institute Imaging Data Commons: toward transparency, reproducibility, and scalability in imaging AI. ~RadioGraphics.~ 2023;43(12):e230180.",
        "IDC koleksiyonu: nlm_visible_human_project, doi:10.5281/zenodo.12690049. Seri UID'leri ve indirme betikleri: kesitsel/KAYNAKLAR.md, scripts/.",
        "Lisans: National Library of Medicine Terms and Conditions (21 Mayıs 2019) – kaynak gösterilerek eğitim amaçlı kullanım.",
        "**Etiket doğrulama:** her etiket noktası kaynak piksel koordinatında tanımlıdır; slaytlar PDF/PNG'ye dönüştürülüp görsel olarak denetlenmiştir (kesitsel/qa/).",
        "**Pilotta bilinçli olarak etiketlenmeyenler:** tek tek karpal kemikler, sinirlerin ayrı ayrı adlandırılması (n. radialis, n. ulnaris) ve yüzeyel venler – kesin tanımlama için daha yüksek çözünürlüklü komşu kesit izlemesi gerekir. Etiketler bir anatomi öğretim üyesince onaylanmalıdır.",
    ], size=13)
    footer(s, "Tüm görüntüler gerçek kadavra (kriyokesit) ve radyoloji (BT) verisidir.", len(LEVELS) + 3)
    fix_runs(s)
    out = ROOT / "kesitsel" / "Kesitsel_Anatomi_Pilot.pptx"
    prs.save(out)
    (QA / "label_qa.json").write_text(json.dumps(qa, indent=1, ensure_ascii=False, default=str))
    print(out)

if __name__ == "__main__":
    build()
