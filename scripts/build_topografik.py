#!/usr/bin/env python3
"""Build the topographic (topografik) pilot deck from license-verified PMC Open Access figures.

Figures are used unmodified (only scaled) with the authors' own labels; Turkish legends translate
the authors' keys 1:1 from the verbatim captions in sources/topografik_kaynaklar.json.
Output: topografik/Topografik_Anatomi_Pilot.pptx
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from deck_common import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = {e["pmcid"] + "|" + e["topic"]: e for e in json.load(open(ROOT / "sources" / "topografik_kaynaklar.json"))}
def src(pmcid):
    return next(e for k, e in SRC.items() if k.startswith(pmcid + "|"))
def fig(pmcid, key):
    e = src(pmcid); f = next(f for f in e["figures"] if key in f["file"])
    return ROOT / f["local_path"], f["label"]
LIC = {"CC BY": "CC BY", "CC BY-NC": "CC BY-NC", "CC BY-NC-SA": "CC BY-NC-SA"}
def cite(pmcid, figs):
    e = src(pmcid)
    t = e['title'].rstrip(); t = t if t.endswith(('.', '?', '!')) else t + "."
    return (f"{e['authors']} {t} {e['citation']} PMCID: {e['pmcid']}. "
            f"Lisans: {e['license_code']} – {', '.join(figs)} değiştirilmeden (yalnızca ölçeklendirilerek) kullanılmıştır; Türkçe açıklama bu projeye aittir.")

SLIDES = [
 dict(kind="normal", title="Plexus brachialis – infraklavikular bölüm", sub="Normal düzen (şema) ve kadavra diseksiyonunda n. medianus kök varyasyonları",
      pmc="PMC12578619", figs=["g012", "g011"],
      legend=["**Şekil 1 (şema):** ST/MT/IT = truncus superior/medius/inferior; AD/PD = divisio anterior/posterior; LC/MC/PC = fasciculus lateralis/medialis/posterior; MCN = n. musculocutaneus; LR/MR = radix lateralis/medialis n. mediani; MN = n. medianus; UN = n. ulnaris; RN = n. radialis; AN = n. axillaris; TDN = n. thoracodorsalis; USSN/LSSN = n. subscapularis superior/inferior.",
              "**Şekil 2A:** 1 fasciculus lateralis; 2 radix lateralis; 3 aksesuar radix lateralis; 4 radix medialis; 5 a. axillaris (ana); 6 n. musculocutaneus; 7 aberran a. axillaris; 8 n. ulnaris; 9 n. medianus.",
              "**Şekil 2B:** 1 n. medianus; 2 radix medialis; 3 fasciculus medialis ile radix lateralis arasında iletişim dalı; 4 radix lateralis."],
      points=["18 kadavranın 36 üst ekstremitesinde plexus brachialis'in **%44,4**'ünde (16/36) varyasyon saptanmış; toplam 32 varyasyon, çoğu bilateral (%77,8).",
              "N. medianus, fasciculus lateralis ve medialis'ten gelen iki kökün a. axillaris önünde birleşmesiyle oluşur; köklerin sayı ve birleşme düzeyi değişkendir."]),
 dict(kind="normal", title="Spatium axillare laterale (dörtgen boşluk)", sub="Ön (deltopektoral) ve arka yaklaşımla kadavra diseksiyonu",
      pmc="PMC8958867", figs=["i04", "i03"],
      legend=["**AXN** = n. axillaris; **PHCA** = a. circumflexa humeri posterior.",
              "**Şekil 4 (arka):** Deltoid m. deltoideus; Teres Minor/Major m. teres minor/major; Long Head of Triceps caput longum m. tricipitis brachii; Surgical neck… collum chirurgicum humeri (caput mediale m. tricipitis ile örtülü).",
              "**Şekil 3 (ön, deltopektoral):** Cephalic vein v. cephalica; Pectoralis Major m. pectoralis major; Conjoint tendon m. coracobrachialis ile caput breve m. bicipitis'in ortak tendonu."],
      points=["Sınırlar: yukarıda **m. teres minor**, aşağıda **m. teres major**, medialde **caput longum m. tricipitis brachii**, lateralde **collum chirurgicum humeri**.",
              "İçerik: n. axillaris ve a./v. circumflexa humeri posterior – collum chirurgicum kırıkları ve omuz çıkıklarında n. axillaris hasarı (m. deltoideus güçsüzlüğü, omuz lateralinde duyu kaybı).",
              "Çalışmada (8 ekstremite) arka yaklaşım daha kolay ve hızlı bulunmuş, ön yaklaşım ise daha az morbidite ile ilişkilendirilmiştir."]),
 dict(kind="normal", title="Incisura scapulae ve n. suprascapularis", sub="Lig. transversum scapulae superius ile damar–sinir ilişkisi",
      pmc="PMC4555201", figs=["Fig2"],
      legend=["**1** a. suprascapularis; **2** v. suprascapularis; **3** n. suprascapularis; **4** lig. transversum scapulae superius. La = lateral, Me = medial.",
              "A: kadavra görüntüsü (ölçek 1 mm); B: şematik düzen (Tip I)."],
      points=["106 kadavra omzunda: **Tip I %61,3** (arter bağın üstünde, ven ve sinir altında); Tip II %17; Tip III %12,3 (hepsi bağın altında); Tip IV %9,4.",
              "N. suprascapularis m. supraspinatus ve m. infraspinatus'u innerve eder; incisura'da sıkışma (suprascapular nöropati) bu kaslarda güçsüzlük ve atrofi yapar.",
              "Lig. coracoscapulare anterius 106 omzun 55'inde bulunmuştur."]),
 dict(kind="normal", title="Fossa cubiti – kadavra diseksiyonu", sub="Dikkat: bu olguda yüksek a. brachialis bölünmesi vardır (varyasyon); normal içerik notlarda verilmiştir",
      pmc="PMC10823296", figs=["i05", "i06"],
      legend=["Görüntülerdeki İngilizce etiketler: **Brachial A** a. brachialis; **Radial A** a. radialis; **Ulnar A** a. ulnaris; **Median N** n. medianus; **Ulnar N** n. ulnaris; **Biceps brachii mm** m. biceps brachii; **Bicipital aponeurosis** aponeurosis m. bicipitis brachii; **Pronator teres mm** m. pronator teres; **Brachioradialis mm** m. brachioradialis; **Triceps mm** m. triceps brachii.",
              "Şekil 5: sağ (Right UL); Şekil 6: sol üst ekstremite (Left UL). (Yayımlanan altyazıdaki a–h harfleri görüntüde yer almaz; etiketler görüntüden çevrilmiştir.)"],
      points=["**Normal düzen:** fossa cubiti'de lateralden mediale tendo m. bicipitis brachii, a. brachialis ve n. medianus bulunur; çatısını aponeurosis m. bicipitis brachii oluşturur.",
              "**Bu olguda (bilateral):** a. brachialis kolun orta üçte birinde a. radialis ve a. ulnaris'e ayrılmış; m. pronator teres humerus'un distal üçte birinden başlamış ve n. medianus fossa cubiti dışında, bu kasın altında seyretmiştir.",
              "Literatürde yüksek a. brachialis bölünmesi kadavraların %5–14'ünde bildirilmiştir (makalede aktarılan)."]),
 dict(kind="normal", title="N. radialis'in bölünmesi ve Frohse arkadı", sub="R. superficialis, n. interosseus posterior ve m. supinator",
      pmc="PMC12500735", figs=["Fig4", "Fig6"],
      legend=["**Şekil 4:** pembe iğne art. humeroradialis düzeyinde; ★ r. superficialis n. radialis; ■ n. interosseus posterior (PIN); ● m. extensor carpi radialis brevis dalı.",
              "**Şekil 6:** ■ PIN, m. supinator'un (Supinator) yüzeyel ve derin başları arasında korunarak seyreder; Biceps tendon tendo m. bicipitis brachii; Radial tuberosity tuberositas radii.",
              "Yön okları: Lateral / Distal."],
      points=["29 taze kadavra üst ekstremitesinde n. radialis art. humeroradialis'in **5 ± 3 mm** proksimalinde ikiye ayrılmış; PIN, Frohse arkadına (m. supinator) bu eklemin **22 ± 1 mm** distalinde girmiştir.",
              "PIN, tuberositas radii'nin radial kenarından pronasyonda ortalama 13 ± 2 mm, supinasyonda 19 ± 2 mm uzaklıktadır – proksimal radius cerrahisinde güvenli bölge planlaması için önemlidir.",
              "Frohse arkadı, PIN sıkışma sendromunun (supinator sendromu) en sık yeridir."]),
 dict(kind="normal", title="Canalis carpi – n. medianus'un r. recurrens'i", sub="Lig. carpi transversum (retinaculum musculorum flexorum) ile ilişki",
      pmc="PMC3931286", figs=["-1", "-2"],
      legend=["**Şekil 1:** bağ içinden (intraligamentöz) çıkan r. recurrens (işaretçi).",
              "**Şekil 2:** bağ dışından (ekstraligamentöz) çıkan çok sayıda r. recurrens (işaretçi)."],
      points=["13 kadavranın 26 elinde r. recurrens çoğunlukla **tek gövde (%76,9)** ve **ekstraligamentöz (%84,6)** bulunmuştur.",
              "Bağın distal kenarından r. recurrens'e ortalama uzaklık 7,75 mm; arcus palmaris superficialis'e 11,48 mm.",
              "Karpal tünel gevşetmesinde intraligamentöz dal yaralanma riski taşır; kesi bağın ulnar tarafında yapılmalıdır."]),
 dict(kind="var", title="Varyasyon: M. arcus axillaris (Langer kası)", sub="M. latissimus dorsi'den köken alan aksiller kemer – bilateral olgu",
      pmc="PMC12206543", figs=["i01"],
      legend=["Görüntüdeki etiketler: **Axillary arch** m. arcus axillaris; **Latissimus Dorsi** m. latissimus dorsi; **Short head of biceps** caput breve m. bicipitis brachii; **Coracobrachialis** m. coracobrachialis; **Deltoid** m. deltoideus.",
              "Sağ aksiller diseksiyon: kemer kası m. latissimus dorsi'nin ön kenarından başlar, a. axillaris ve plexus brachialis dallarının **önünden** geçer, caput breve m. bicipitis brachii'ye tutunur ve 'T' şeklinde iki aksesuar demete ayrılarak m. coracobrachialis ve m. deltoideus liflerine katılır."],
      points=["Olgu: bilateral aksiller kemer; solda tek ince demet halinde m. coracobrachialis ile m. deltoideus arasındaki fasyaya tutunuyor.",
              "Klinik önem: aksiller damar–sinir yapılarına bası (torasik çıkış benzeri belirtiler), aksiller lenf nodu diseksiyonu ve meme cerrahisinde yanıltıcı yapı.",
              "Makale kendi sıklık verisini sunmaz; sıklığın toplumlara göre değiştiğini belirtir."]),
 dict(kind="var", title="Varyasyon: A. brachialis superficialis ve trifurkasyon", sub="A. brachialis'in m. latissimus dorsi tendonu altında üçe ayrılması",
      pmc="PMC10599095", figs=["i01"],
      legend=["**AA** a. axillaris; **BA** a. brachialis; **SBA** a. brachialis superficialis; **CT** ortak gövde: (1) aberran a. circumflexa humeri posterior, (2) a. nutricia humeri, (3) a. profunda brachii (n. radialis – **RN** – eşliğinde); **LD** m. latissimus dorsi tendonu.",
              "**MN** n. medianus (iki radix lateralis – sarı yıldız – ve bir radix medialis – beyaz yıldız); **UN** n. ulnaris; **AN** n. axillaris; **SSA** a. subscapularis (yüksek köken); **ACHA1/2** çift a. circumflexa humeri anterior; **MCN** n. musculocutaneus. Panel A–C aynı diseksiyonun farklı görünümleridir; damarlar ve sinirler yazarlarca dijital olarak renklendirilmiştir.",
              "Not: görüntüdeki kırmızı/mavi yıldızlar ve 'CV' kısaltması yayımlanan altyazıda tanımlanmamıştır; bu nedenle çevrilmemiştir."],
      points=["SBA'nın sıklığı **%1,07–%19,7** arasında bildirilmiştir; De Garis ve Swartley'e göre Afrika kökenli Amerikalılarda (%13,4) beyazlara (%4,6) göre daha sıktır (makalede aktarılan).",
              "Klinik önem: yüzeyel seyreden arter venipunktur sırasında yanlışlıkla arteriyel enjeksiyona, travmada kolay yaralanmaya ve flep/greft planlamasında hataya yol açabilir."]),
 dict(kind="var", title="Varyasyon: N. musculocutaneus yokluğu", sub="Fasciculus lateralis doğrudan radix lateralis n. mediani olarak devam ediyor",
      pmc="PMC11026042", figs=["gf1", "gf2"],
      legend=["**Şekil 1 (aksilla, lateral):** 1 m. pectoralis minor; 2 fasciculus lateralis; 3 radix lateralis n. mediani; 4 a. axillaris; 5 n. medianus; 6 radix medialis; 7 n. ulnaris; 8 n. cutaneus antebrachii medialis.",
              "**Şekil 2 (kol, ön):** 1 m. coracobrachialis; 2 n. medianus'tan m. biceps brachii dalı; 3 n. medianus'tan m. brachialis dalı; 4 m. biceps brachii; 5 m. brachialis; 6 n. medianus; 7 a. brachialis; 8 n. cutaneus antebrachii medialis; 9 n. ulnaris."],
      points=["Olgu: sağ kolda n. musculocutaneus yok; m. coracobrachialis, m. biceps brachii ve m. brachialis'i **n. medianus** innerve ediyor; m. brachialis dalı n. cutaneus antebrachii lateralis olarak devam ediyor.",
              "Aktarılan sıklık: Beheiry 60 kolun 1'inde (%1,7); Prasada Rao ve Chaudhary 24 kolun %8'inde.",
              "Klinik önem: n. medianus hasarında beklenmedik dirsek fleksiyon zaafı; aksiller blok ve aksilla cerrahisinde dikkat."]),
 dict(kind="var", title="Varyasyon: Martin-Gruber anastomozu", sub="Ön kolda n. medianus → n. ulnaris iletişim dalı (Tip I)",
      pmc="PMC11867591", figs=["i01"],
      legend=["**MGA** Martin-Gruber anastomozu; **MN** n. medianus (görünürlük için laterale çekilmiş); **UN** n. ulnaris; **FDP** m. flexor digitorum profundus; **ME** epicondylus medialis (yön referansı: distal görüntünün üst tarafında)."],
      points=["101 kadavra ön kolunda sıklık **%37,6** (38/101): Tip I %58, Tip III %32, Tip II %11; anastomozların çoğu FDP içinde seyretmiştir.",
              "Klinik önem: dirsekte n. ulnaris lezyonunda intrinsik el kaslarının beklenmedik şekilde korunması; sinir iletim çalışmalarının yanlış yorumlanması."]),
 dict(kind="var", title="Varyasyon: A. mediana persistens ve bifid n. medianus", sub="Aynı olguda m. palmaris longus reversus",
      pmc="PMC10343151", figs=["i01"],
      legend=["**1** a. mediana persistens (PMA); **2** PMA'yı arcus palmaris profundus'a bağlayan dal; **3** a. ulnaris; **4** arcus palmaris superficialis; **5** arcus palmaris profundus; **6** a. radialis; **7** ilk a. metacarpalis palmaris communis.",
              "**MN** n. medianus; **RBMN/MBMN** n. medianus'un radial/medial dalı (bifid sinir); **BR** m. brachioradialis; **FCR** m. flexor carpi radialis; **FDS** m. flexor digitorum superficialis; **R-PL** m. palmaris longus reversus; **CT** FDS'ye ait kesilmiş tendon."],
      points=["Olguda PMA a. radialis'ten çıkmış ve a. ulnaris ile anastomoz yaparak arcus palmaris superficialis'i oluşturmuştur.",
              "Aktarılan sıklık: 125 ekstremitenin 5'inde (%4); bir Avustralya örnekleminde %33,3.",
              "Klinik önem: PMA ve bifid n. medianus karpal tünel sendromuna katkıda bulunabilir; endoskopik/açık gevşetmede yaralanma riski."]),
]

def content_slide(prs, d, page):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title_bar(s, d["title"], d["sub"])
    tag = "NORMAL TOPOGRAFİ" if d["kind"] == "normal" else "ANATOMİK VARYASYON"
    text(s, 10.6, 0.92, 2.5, 0.3, tag, size=10, color=WHITE, bold=True, align=PP_ALIGN.CENTER,
         fill=RGBColor(0x2E, 0x7D, 0x32) if d["kind"] == "normal" else ACCENT)
    paths = [fig(d["pmc"], k) for k in d["figs"]]
    # image area: x 0.3–7.9, y 1.0–6.0
    X, Y, W, H = 0.3, 1.0, 7.6, 4.95
    from PIL import Image
    sizes = [Image.open(p).size for p, _ in paths]
    if len(paths) == 1:
        boxes = [(X, Y, W, H)]
    else:
        ar = [w / h for w, h in sizes]
        if all(a < 1.05 for a in ar) or sum(ar) * H < W * 1.1:   # side by side
            ws = [W * a / sum(ar) for a in ar]; ws = [w - 0.1 for w in ws]
            boxes = [(X + sum(ws[:i]) + 0.2 * i, Y, ws[i], H) for i in range(len(paths))]
        else:                                                    # stacked
            hs = [H * (1 / a) / sum(1 / a for a in ar) - 0.25 for a in ar]
            boxes = [(X, Y + sum(hs[:i]) + 0.3 * i, W, hs[i]) for i in range(len(paths))]
    for (p, lab), b in zip(paths, boxes):
        g = picture_fit(s, p, *b)
        text(s, g["x"], g["y"] + g["h"] - 0.02, g["w"], 0.25, f"{lab} ({d['pmc']})", size=8.5, color=GREY, italic=True, align=PP_ALIGN.CENTER)
    text(s, 8.15, 1.3, 4.95, 0.3, "Şekil açıklaması (yazarların etiketleri)", size=12, color=ACCENT, bold=True)
    bullets(s, 8.15, 1.6, 4.95, 2.6, d["legend"], size=10.5)
    text(s, 8.15, 4.05, 4.95, 0.3, "Önemli noktalar", size=12, color=ACCENT, bold=True)
    bullets(s, 8.15, 4.35, 4.95, 2.6, d["points"], size=10.5)
    footer(s, cite(d["pmc"], [lab for _, lab in paths]), page)
    fix_runs(s)
    e = src(d["pmc"])
    notes(s, f"Kaynak: {e['citation']}\nDOI: {e['doi']}\nLisans (PMC OA S3 JSON): {e['license_code']}\nAnahtar bulgular (makaleden): {e['key_findings']}")

def build():
    prs = new_deck()
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height); bg.fill.solid(); bg.fill.fore_color.rgb = NAVY; bg.line.fill.background()
    text(s, 0.7, 1.3, 7.6, 1.0, "Membrum Superius – Topografik Anatomi", size=36, color=WHITE, bold=True)
    text(s, 0.7, 2.45, 7.6, 1.0, "Gerçek insan kadavra diseksiyonları ve hakemli yayınlardan anatomik varyasyonlar", size=18, color=RGBColor(0xC8, 0xD1, 0xE6))
    text(s, 0.7, 3.9, 7.6, 1.8, ["PİLOT SÜRÜM – 6 normal topografi + 5 varyasyon slaytı",
                                 "Görseller: PubMed Central Open Access alt kümesi (lisans makale bazında doğrulandı)",
                                 "Her varyasyon gerçek bir yayına dayanır; sıklık verileri makalelerden aynen aktarılmıştır."], size=14, color=WHITE)
    picture_fit(s, fig("PMC8958867", "i04")[0], 8.7, 0.5, 2.1, 3.1); picture_fit(s, fig("PMC12206543", "i01")[0], 10.9, 0.5, 2.1, 3.1)
    picture_fit(s, fig("PMC12500735", "Fig4")[0], 8.7, 3.8, 2.1, 3.1); picture_fit(s, fig("PMC4555201", "Fig2")[0], 10.9, 3.8, 2.1, 3.1)
    text(s, 0.7, 6.75, 7.6, 0.4, "Sunum dili Türkçe; anatomik terimler Terminologia Anatomica (Latince).", size=11, color=RGBColor(0xC8, 0xD1, 0xE6), italic=True)
    for i, d in enumerate(SLIDES):
        content_slide(prs, d, i + 2)
    s = prs.slides.add_slide(prs.slide_layouts[6])
    title_bar(s, "Kaynaklar ve görsel lisansları")
    items = []
    for d in SLIDES:
        e = src(d["pmc"])
        t = e['title'].rstrip(); t = t if t.endswith(('.', '?', '!')) else t + "."
        items.append(f"{e['authors']} {t} ~{e['journal']}~ {e['year']}. doi:{e['doi']} – {e['pmcid']} – **{e['license_code']}**")
    bullets(s, 0.3, 1.0, 12.7, 5.9, items, size=10)
    footer(s, "Görseller PMC OA AWS deposundan (pmc-oa-opendata) indirilmiş; lisans kodu, md5 ve altyazılar sources/topografik_kaynaklar.json içinde kayıtlıdır.", len(SLIDES) + 2)
    fix_runs(s)
    out = ROOT / "topografik" / "Topografik_Anatomi_Pilot.pptx"; prs.save(out); print(out)

if __name__ == "__main__":
    build()
