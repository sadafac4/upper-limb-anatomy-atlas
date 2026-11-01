# -*- coding: utf-8 -*-
"""Bölüm kompozisyonu (tıp öğrencisi düzeyi): atlas çizimleri ağırlıklı (OpenStax, Latince etiketli),
seçilmiş az sayıda kadavra görseli (PMC açık erişim) ve yerel şemalar."""
from icerik_perine import *

def T(d, **kw):
    return dict(d, **kw)

def F(pmc, key):
    return ("pmc", pmc, key)

def A(ad):
    return ("atlas", "atlas:" + ad)

KAPAK = [A("perine_kaslari"), F("PMC7898478", "CA-34-272")]

# ---------------- 1. PELVİS ----------------
PELVIS = [
    T(PELVIS_KEMIK, tip="atlas", fig=A("pelvis")),
    PELVIS_ACIKLIK,
    T(PELVIS_CINSIYET, tip="atlas", fig=A("pelvis_cinsiyet")),
    T(PELVIS_BAG, tip="atlas", fig=A("pelvis_bag")),
    T(PELVIS_TABAN, tip="atlas", fig=A("diaphragma_pelvis"), gw=8.0),
]

# ---------------- 2. PERİNE – GENEL ----------------
GENEL = [
    PERINE_TANIM,
    T(PERINE_UCGEN, tip="eskenar"),
    dict(tip="kadavra", bolum=B2, baslik="Perinenin sınırları – kadavrada", alt="Erkek perinesi, aşağıdan bakış (deri altı yağ kaldırılmış)",
         fig=F("PMC7898478", "CA-34-272"), sol_w=3.0, sag_w=3.1, boyut=16,
         metin=["Tuber ischiadicum, ramus ischiopubicus ve os coccygis perinenin kemik çerçevesini oluşturur.",
                "Önde ürogenital kaslar (m. bulbospongiosus, m. ischiocavernosus), arkada m. sphincter ani externus ve anüs."]),
    CORPUS,
]

# ---------------- 3. REGIO UROGENITALIS ----------------
UROG = [
    T(KATMANLAR, tip="katman"),
    FASYALAR,
    dict(tip="ekstravazasyon", baslik="Colles fasyasının devamlılığı – idrar ekstravazasyonu", bolum=B3, boyut=16,
         metin=["Bulbar urethra yırtılırsa idrar Colles fasyası altında yayılır: perine, scrotum, penis ve karın ön duvarı şişer.",
                "Uyluğa ve anal bölgeye geçmez, çünkü Colles fasyası fascia lata'ya ve membrana perinei'nin arka kenarına yapışıktır."]),
    SPATIA,
    dict(tip="atlas", bolum=B3, baslik="Perine kasları – erkek ve kadın", alt="Aşağıdan (litotomi) bakış", fig=A("perine_kaslari"),
         not_="Önce ortak kasları gösterin (m. ischiocavernosus, m. bulbospongiosus, m. transversus perinei superficialis), sonra regio analis'teki m. sphincter ani externus ve m. levator ani."),
    KASLAR,
    dict(tip="atlas", fig=A("erkek_genital"), baslik="Erkek: urethra ve perine ilişkisi", bolum=B3, boyut=15, metin_alt=[
        "Urethra: **pars prostatica** → **pars membranacea** (derin aralık; m. sphincter urethrae externus; kateterde en dar ve en kolay yaralanan kısım) → **pars spongiosa** (bulbus ve corpus spongiosum içinde).",
        "**Gl. bulbourethralis (Cowper)** derin aralıkta pars membranacea'nın yanında; penis kökü (bulbus ve crura) yüzeyel aralıkta."]),
    T(dict(baslik="Kadın: pelvis organları ve perine", alt="Sagittal kesit çizimi", bolum=B3, boyut=16, metin=[
        "Önden arkaya: **vesica urinaria / urethra** → **vagina** → **rectum / canalis analis**.",
        "Kadın urethrası kısadır (≈4 cm) → idrar yolu enfeksiyonu daha sık.",
        "Vagina ile anüs arasında **corpus perineale**."]), tip="atlas", fig=A("sagittal_kadin")),
    T(dict(baslik="Vulva ve yüzeyel aralık", bolum=B3, boyut=15, metin=[
        "**Glans, corpus ve crura clitoridis**; crura m. ischiocavernosus ile örtülüdür.",
        "**Bulbus vestibuli** ostium vaginae'nin iki yanında, m. bulbospongiosus altında.",
        "**Gl. vestibularis major (Bartholin)** bulbusun arka ucunda; kanalı ostium vaginae'nin arka-yanına açılır."]), tip="atlas", fig=A("vulva")),
    dict(tip="iki", bolum=B3, baslik="Kadavrada erkek regio urogenitalis", alt="Sol: yüzeyel aralık kasları · Sağ: kaslar kaldırılınca membrana perinei",
         figler=[dict(fig=F("PMC12229694", "Fig1_HTML"), kirp=(0, 0, 332, 271)),
                 dict(fig=F("PMC12229694", "Fig1_HTML"), kirp=(0, 277, 332, 549))],
         boyut=16, metin=["Atlas çiziminde gördüğünüz kaslar kadavrada: m. bulbospongiosus, m. ischiocavernosus, m. transversus perinei superficialis.",
                          "Bu kaslar kaldırılınca membrana perinei görülür; bulbus penis bu levhanın alt yüzüne oturur."]),
    dict(tip="kadavra", bolum=B3, baslik="Kadavrada clitoris ve bulbus vestibuli", alt="Kadın perinesi, yüzeyel aralık açılmış",
         fig=F("PMC7913006", "g004"), sol_w=3.0, sag_w=3.6, eboyut=13, boyut=16,
         haric=["Nervus perinealis"],
         metin=["Clitoris'in glans, corpus ve crura'sı; bulbus vestibuli m. bulbospongiosus'un altında.",
                "Arkada m. transversus perinei superficialis."]),
    UROG_KLINIK,
]

# ---------------- 4. REGIO ANALIS ----------------
ANALIS = [
    FOSSA,
    dict(tip="kadavra", bolum=B4, baslik="Kadavrada fossa ischioanalis", alt="Kadın perinesi, aşağıdan bakış",
         fig=F("PMC6942605", "Fig2_HTML"), kirp=(0, 280, 709, 1010), sol_w=3.6, sag_w=3.6, boyut=16,
         metin=["Anüsün yanındaki sarı yağ dokusu fossa ischioanalis'i doldurur; önünde ürogenital kaslar görülür."]),
    ANAL,
]

# ---------------- 5. DAMAR – SİNİR ----------------
DAMAR = [
    T(PUDENDAL, tip="pudendal"),
    dict(tip="kadavra", etiket="İLLÜSTRASYON", bolum=B5, baslik="N. pudendus dallarının perinedeki dağılımı", alt="Kadın perinesi, litotomi görünümü (yazar çizimi)",
         fig=F("PMC7913006", "g003"), kirp=(230, 60, 560, 440), sol_w=3.4, sag_w=3.4, eboyut=13.5, boyut=16,
         metin=["**N. rectalis inferior** → m. sphincter ani externus ve anüs çevresi derisi.",
                "**N. perinealis** → perine kasları ve labia/scrotum derisi; **n. dorsalis clitoridis/penis** → clitoris/penis duyusu."]),
    dict(tip="kadavra", bolum=B5, baslik="Kadavrada n. pudendus ve a. pudenda interna", alt="Pelvis içinden medial bakış",
         fig=F("PMC8713160", "g00"), sol_w=3.0, sag_w=3.4, eboyut=13, boyut=16,
         metin=["N. pudendus lig. sacrospinale hizasında a. pudenda interna'nın medialinde seyreder (pudendal blokta bu ilişki kullanılır)."]),
    DAMAR_KLINIK,
]

BOLUMLER = [
    ("Pelvis", "Kısa giriş – perinenin kemik çerçevesi ve tabanı",
     ["Pelvis kemikleri", "Pelvis major / minor", "Kadın – erkek pelvisi", "Bağlar, diaphragma pelvis"], A("pelvis"), PELVIS),
    ("Perine – genel", "Tanım, sınırlar, üçgenler",
     ["Sınırlar", "Regio urogenitalis / regio analis", "Corpus perineale"], A("perine_kaslari"), GENEL),
    ("Regio urogenitalis", "Fasyalar, aralıklar, kaslar, dış genital organlar",
     ["Perine fasyaları", "Yüzeyel ve derin aralık", "Erkek ve kadın", "Klinik"], A("vulva"), UROG),
    ("Regio analis", "Fossa ischioanalis ve anal sfinkterler",
     ["Fossa ischioanalis", "Canalis analis", "M. sphincter ani externus"], F("PMC6942605", "Fig2_HTML"), ANALIS),
    ("Damar – sinir", "N. pudendus, a. pudenda interna, lenfatik drenaj",
     ["Seyir ve dallar", "Pudendal blok", "Lenfatik drenaj"], A("pelvis_bag"), DAMAR),
    ("Klinik – özet", "Varyasyonlar, özet, kendini değerlendir",
     ["Sık varyasyonlar", "Özet", "Sorular"], A("sagittal_kadin"), [VARYASYON, OZET, SORULAR]),
]
