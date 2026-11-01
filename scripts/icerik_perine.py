# -*- coding: utf-8 -*-
"""Perine sunumu – ders metinleri, TIP ÖĞRENCİSİ düzeyi (dönem I–II).
Türkçe anlatım, Latince terminoloji (TA2). Metinler kısa ve sınav odaklıdır; ayrıntı konuşmacı notlarındadır."""

B1, B2, B3, B4, B5, B6 = ("PELVİS", "PERİNE – GENEL", "REGIO UROGENITALIS", "REGIO ANALIS", "DAMAR – SİNİR", "KLİNİK – ÖZET")

HEDEFLER = dict(tip="anlatim", etiket="ÖZET", baslik="Öğrenim hedefleri", boyut=20, metin=[
    "Pelvisi oluşturan kemikleri ve **apertura pelvis superior / inferior** sınırlarını sayabilmek",
    "**Diaphragma pelvis**'i (m. levator ani, m. coccygeus) tanımlayabilmek",
    "Perinenin sınırlarını ve **regio urogenitalis – regio analis** ayrımını açıklayabilmek",
    "**Perine fasyalarını** (Colles fasyası, fascia perinei, membrana perinei) ve aralıkları (spatium perinei superficiale / profundum) sıralayabilmek",
    "Perine kaslarını, **corpus perineale**'yi ve **fossa ischioanalis**'i tanımlayabilmek",
    "**N. pudendus** ve **a. pudenda interna**'nın seyrini ve dallarını bilmek; temel klinik bağlantıları kurabilmek",
])

# ---------------- 1. PELVİS ----------------
PELVIS_KEMIK = dict(baslik="Pelvis: kemikler ve eklemler", alt="Pelvis = iki os coxae + os sacrum + os coccygis", bolum=B1,
    metin=["**Os coxae** üç kemiğin kaynaşmasıdır: os ilium, os ischii, os pubis (acetabulum'da birleşirler).",
           "Eklemler: **art. sacroiliaca**, **symphysis pubica**, art. sacrococcygea.",
           "**Linea terminalis** (promontorium → linea arcuata → pecten ossis pubis → symphysis): pelvis major / minor sınırı.",
           "Perine açısından önemli noktalar: **tuber ischiadicum**, **ramus ischiopubicus**, **os coccygis**, symphysis pubica."])

PELVIS_ACIKLIK = dict(tip="tablo", baslik="Pelvis major – pelvis minor ve pelvis açıklıkları", bolum=B1,
    sutunlar=["", "Sınırlar", "Önemi"], genislik=[2.6, 5.6, 4.0], satir_h=1.05, boyut=16,
    satirlar=[
        ["Pelvis major", "Linea terminalis'in **üstü**; iki ala ossis ilii arası", "Karın boşluğunun alt kısmı (barsaklar)"],
        ["Pelvis minor", "Linea terminalis'in **altı**", "Mesane, rektum, iç genital organlar; doğum kanalı"],
        ["Apertura pelvis superior", "Promontorium – linea arcuata – pecten ossis pubis – symphysis üst kenarı", "Pelvis girişi"],
        ["Apertura pelvis inferior", "Symphysis alt kenarı – **rami ischiopubici** – **tubera ischiadica** – **ligg. sacrotuberalia** – **os coccygis**", "Pelvis çıkışı = **perinenin sınırları**"],
    ])

PELVIS_CINSIYET = dict(baslik="Kadın ve erkek pelvisi", alt="Kadın pelvisi doğuma uyumludur", bolum=B1,
    metin=["Kadında **angulus subpubicus** geniş (≈80–90°), erkekte dar (≈50–60°).",
           "Kadında apertura pelvis superior **oval/yuvarlak**, erkekte **kalp biçimli**.",
           "Kadın pelvisi daha geniş ve sığ; erkek pelvisi dar ve derin.",
           "Erkek kemikleri daha kalın, kas izleri belirgin."])

PELVIS_BAG = dict(baslik="Pelvis bağları ve foramina ischiadica", bolum=B1, alt="Lig. sacrospinale ve lig. sacrotuberale",
    metin=["**Lig. sacrospinale**: os sacrum → spina ischiadica.",
           "**Lig. sacrotuberale**: os sacrum → tuber ischiadicum.",
           "Bu iki bağ incisura ischiadica'ları foramene çevirir: **foramen ischiadicum majus** ve **minus**.",
           "**N. pudendus** ve **a. pudenda interna**: majus'tan pelvisi terk eder, spina'nın arkasından dolanıp **minus**'tan perineye girer."])

PELVIS_TABAN = dict(baslik="Diaphragma pelvis (pelvis tabanı)", bolum=B1, alt="Perinenin tavanı",
    metin=["**M. levator ani**: m. pubococcygeus (+ m. puborectalis) ve m. iliococcygeus.",
           "Arkada **m. coccygeus** tabanı tamamlar.",
           "Görevi: pelvis organlarını taşımak, karın içi basınca karşı koymak, kontinansa yardım.",
           "Ortada açıklık (**hiatus urogenitalis**): urethra (kadında + vagina) geçer.",
           "İnnervasyon: S3–S4 dalları (n. levatoris ani) ve n. pudendus.",
           "Diaphragma pelvis'in **altında** kalan bölge = **perine**."])

# ---------------- 2. PERİNE – GENEL ----------------
PERINE_TANIM = dict(baslik="Perine: tanım ve sınırlar", bolum=B2, boyut=20,
    metin=["**Perineum**: diaphragma pelvis'in altında, uyluklar arasındaki **eşkenar dörtgen** biçimli bölge.",
           "Önde: **symphysis pubica**",
           "Önde-yanda: **rami ischiopubici**",
           "Yanda: **tubera ischiadica**",
           "Arkada-yanda: **ligg. sacrotuberalia**;  arkada: **os coccygis**",
           "İki tuber ischiadicum'u birleştiren çizgi perineyi ikiye ayırır: önde **regio urogenitalis**, arkada **regio analis**."])

PERINE_UCGEN = dict(baslik="Perinenin iki üçgeni", bolum=B2, alt="Litotomi pozisyonu – aşağıdan bakış", boyut=16,
    metin=["**Regio urogenitalis** (ön üçgen): dış genital organlar, urethra (kadında + vagina).",
           "**Regio analis** (arka üçgen): canalis analis, m. sphincter ani externus, iki yanda fossa ischioanalis.",
           "Ortada **corpus perineale**: perine kaslarının birleştiği fibromusküler merkez."])

CORPUS = dict(baslik="Corpus perineale (centrum tendineum perinei)", bolum=B2, boyut=19,
    metin=["Erkekte bulbus penis ile anüs, kadında vagina ile anüs arasında yer alan fibromusküler düğüm.",
           "Buraya tutunan kaslar: **m. bulbospongiosus**, **m. transversus perinei superficialis** ve **profundus**, **m. sphincter ani externus**, m. levator ani lifleri.",
           "Kadında pelvis tabanının önemli destek noktasıdır.",
           "**Klinik**: doğumda **perine yırtıkları** (1.–4. derece) ve **epizyotomi**. Mediolateral epizyotomi anal sfinkteri korumak için tercih edilir."])

# ---------------- 3. REGIO UROGENITALIS ----------------
KATMANLAR = dict(baslik="Regio urogenitalis – yüzeyden derine katmanlar", bolum=B3, boyut=15,
    metin=["**1.** Deri ve **panniculus adiposus** (yağlı tabaka)",
           "**2.** **Colles fasyası** (stratum membranosum) – karındaki Scarpa fasyasının devamı",
           "**3.** **Spatium perinei superficiale** – penis/clitoris kökü, yüzeyel kaslar",
           "**4.** **Membrana perinei**",
           "**5.** **Spatium perinei profundum** – m. sphincter urethrae externus",
           "**6.** Diaphragma pelvis (m. levator ani) – perinenin tavanı"])

FASYALAR = dict(tip="tablo", baslik="Perine fasyaları", bolum=B3, alt="Sınavda en çok sorulan yapılar",
    sutunlar=["Fasya", "Nerede / neye devam eder?", "Önemi"], genislik=[3.0, 5.4, 4.3], satir_h=1.25, boyut=15,
    satirlar=[
        ["Colles fasyası (fascia perinei superficialis, stratum membranosum)", "Karında **Scarpa**, scrotum'da **tunica dartos** ile devamlı; yanda rami ischiopubici'ye, arkada membrana perinei'nin arka kenarına yapışır", "Spatium perinei superficiale'nin alt sınırı; idrar ekstravazasyon yolu"],
        ["Fascia perinei (Gallaudet fasyası)", "Yüzeyel perine kaslarını (m. ischiocavernosus, m. bulbospongiosus, m. transversus perinei superf.) saran fasya; penisde **Buck fasyası** ile devam eder", "Kasları sarar"],
        ["Membrana perinei", "Arcus pubicus'u kapatan üçgen fibröz levha; urethra (kadında + vagina) deler", "Yüzeyel ve derin aralığı ayırır; penis/clitoris kökü buraya oturur"],
    ],
    dip="Eski kitaplardaki 'diaphragma urogenitale' terimi artık kullanılmıyor: yerine membrana perinei ve spatium perinei profundum denir.")

SPATIA = dict(tip="tablo", baslik="Spatium perinei superficiale ve profundum", bolum=B3,
    sutunlar=["", "Spatium perinei superficiale", "Spatium perinei profundum"], genislik=[2.3, 5.2, 5.2], satir_h=1.4, boyut=15,
    satirlar=[
        ["Sınırlar", "Colles fasyası ile membrana perinei arası", "Membrana perinei'nin üstü (diaphragma pelvis'e kadar)"],
        ["Erkek", "Crura penis, **bulbus penis**; m. ischiocavernosus, m. bulbospongiosus, m. transversus perinei superf.", "Pars membranacea urethrae; **m. sphincter urethrae externus**; m. transversus perinei prof.; **gl. bulbourethralis (Cowper)**"],
        ["Kadın", "Crura clitoridis, **bulbi vestibuli**, **gl. vestibularis major (Bartholin)**; aynı üç kas", "Urethra, vaginanın alt kısmı; m. sphincter urethrae externus, m. compressor urethrae, m. sphincter urethrovaginalis"],
    ],
    dip="Akılda tut: Cowper bezi DERİN aralıkta, Bartholin bezi YÜZEYEL aralıktadır.")

KASLAR = dict(tip="tablo", baslik="Perine kasları", bolum=B3, alt="Hepsini n. pudendus (n. perinealis) innerve eder",
    sutunlar=["Kas", "Yeri", "Görevi"], genislik=[3.6, 4.6, 4.5], satir_h=0.85, boyut=15,
    satirlar=[
        ["M. ischiocavernosus", "Crus penis / clitoridis üzerinde", "Ereksiyonun sürdürülmesi"],
        ["M. bulbospongiosus", "Bulbus penis / bulbus vestibuli üzerinde", "Erkekte ejakülasyon ve idrar boşaltma; kadında vestibulumu daraltır"],
        ["M. transversus perinei superficialis", "Tuber ischiadicum → corpus perineale", "Corpus perineale'yi sabitler"],
        ["M. transversus perinei profundus", "Derin aralıkta", "Corpus perineale'yi sabitler"],
        ["M. sphincter urethrae externus", "Urethra çevresinde (derin aralık)", "İstemli idrar tutma"],
        ["M. sphincter ani externus", "Anüs çevresinde (regio analis)", "İstemli gaita tutma"],
    ])

UROG_KLINIK = dict(tip="klinik", etiket="KLİNİK BAĞLANTI", baslik="Klinik bağlantılar – regio urogenitalis", bolum=B3, boyut=18,
    metin=["**Urethra rüptürü (bulbar)**: idrar Colles fasyası altında yayılır → perine, scrotum, penis ve karın ön duvarı şişer; **uyluğa geçmez**.",
           "**Bartholin kisti / apsesi**: gl. vestibularis major kanalının tıkanması; ostium vaginae'nin arka-yanında şişlik.",
           "**Fournier gangreni**: perine fasyaları boyunca hızla yayılan nekrotizan enfeksiyon.",
           "**Epizyotomi**: doğumda perinenin kontrollü kesisi; mediolateral kesi anal sfinkteri korur."])

# ---------------- 4. REGIO ANALIS ----------------
FOSSA = dict(tip="tablo", baslik="Fossa ischioanalis", bolum=B4, alt="Anüsün iki yanında, yağ dolu kama biçimli boşluk",
    sutunlar=["", "Yapı"], genislik=[2.6, 10.1], satir_h=0.8, boyut=16,
    satirlar=[
        ["Lateral duvar", "M. obturatorius internus ve fasyası (**canalis pudendalis** burada)"],
        ["Medial duvar", "M. levator ani ve m. sphincter ani externus"],
        ["Arka", "Lig. sacrotuberale ve m. gluteus maximus"],
        ["Ön", "Membrana perinei'nin arka kenarı (üstünden **recessus anterior** öne uzanır)"],
        ["İçerik", "Yağ dokusu; n. / a. / v. rectalis inferior; canalis pudendalis içinde n. pudendus ve vasa pudenda interna"],
        ["Klinik", "İki taraf anüsün arkasından birbiriyle bağlantılı → **at nalı apse**; iskioanal apse"],
    ])

ANAL = dict(baslik="Canalis analis ve m. sphincter ani externus", bolum=B4, boyut=18,
    metin=["**M. sphincter ani externus**: çizgili kas, istemli; pars subcutanea, superficialis, profunda. İnnervasyon: **n. rectalis inferior** (n. pudendus).",
           "**M. sphincter ani internus**: düz kas, istemsiz (otonom).",
           "**M. puborectalis** anorektal bileşkeyi öne çeker → **angulus anorectalis** (kontinans).",
           "**Lig. anococcygeum**: anüs ile os coccygis arasında.",
           "**Linea pectinata**: üstü visseral (ağrısız; iç hemoroid), altı somatik (ağrılı; dış hemoroid)."])

# ---------------- 5. DAMAR – SİNİR ----------------
PUDENDAL = dict(baslik="N. pudendus ve a. pudenda interna", bolum=B5, boyut=14.5,
    metin=["Yol: pelvis → foramen ischiadicum majus → spina ischiadica / lig. sacrospinale arkası → foramen ischiadicum minus → **canalis pudendalis (Alcock)** → perine.",
           "Venler arterlere eşlik eder; v. dorsalis penis profunda ise pelvis içindeki venöz pleksusa açılır."])

DAMAR_KLINIK = dict(tip="klinik", etiket="KLİNİK BAĞLANTI", baslik="Klinik: pudendal blok ve lenfatik drenaj", bolum=B5, boyut=18,
    metin=["**Pudendal blok**: doğumda perine anestezisi; vajinal yoldan **spina ischiadica** palpe edilip hemen medial-arkasına enjeksiyon.",
           "**Pudendal nöralji**: uzun süre oturma, bisiklet; canalis pudendalis'te sıkışma → oturunca artan perine ağrısı.",
           "**Lenfatik drenaj**: perine derisi, scrotum / labia, anüsün alt kısmı → **nodi inguinales superficiales**.",
           "Derin yapılar (urethra, prostat, vagina üst kısmı) → **nodi iliaci interni**; testis → paraaortik (lomber) nodlar."])

VARYASYON = dict(tip="tablo", etiket="VARYASYON", baslik="Sık görülen varyasyonlar (kısa)", bolum=B6,
    sutunlar=["Varyasyon", "Sıklık / bulgu", "Neden önemli?"], genislik=[4.0, 4.6, 4.1], satir_h=1.15, boyut=15,
    satirlar=[
        ["N. pudendus'un birden fazla gövdeyle seyretmesi", "52 hemipelviste tek gövde %51,9; iki veya üç gövde geri kalanında (Ranjan ve ark. 2022)", "Pudendal blok eksik kalabilir"],
        ["N. rectalis inferior'un doğrudan plexus sacralis'ten çıkması", "Olgu sunumları (ör. S3'ten; Dupont ve ark. 2019)", "Blokta anal bölge uyuşmayabilir"],
        ["A. pudenda accessoria (pelvis içinden penise giden arter)", "Olgu sunumları (Nayak ve ark. 2014)", "Prostat cerrahisinde yaralanırsa erektil disfonksiyon"],
    ],
    kaynak="Kaynaklar kaynakçada (PMC açık erişim).")

OZET = dict(tip="anlatim", etiket="ÖZET", baslik="Özet", boyut=18, bolum=B6, metin=[
    "Perine = diaphragma pelvis'in altı; sınırı = apertura pelvis inferior.",
    "Tuber ischiadicum'lar arası çizgi → **regio urogenitalis** (önde) + **regio analis** (arkada).",
    "Fasyalar: **Colles** (Scarpa ve dartos ile devamlı) → **fascia perinei** → **membrana perinei**.",
    "Yüzeyel aralık: penis/clitoris kökü, bulbus, **Bartholin**; derin aralık: m. sphincter urethrae externus, **Cowper**.",
    "Bulbar urethra rüptüründe idrar Colles altında karın duvarına yayılır, uyluğa geçmez.",
    "**N. pudendus** (S2–S4): foramen ischiadicum majus → minus → Alcock kanalı; dalları: n. rectalis inferior, n. perinealis, n. dorsalis penis/clitoridis.",
])

SORULAR = dict(tip="anlatim", etiket="SORU", baslik="Kendini değerlendir", boyut=18, bolum=B6, metin=[
    "1. Perineyi ön ve arka üçgene ayıran çizgi hangi iki noktayı birleştirir?",
    "2. Gl. bulbourethralis ve gl. vestibularis major hangi aralıklarda bulunur?",
    "3. Bulbar urethra rüptüründe idrar neden uyluğa yayılmaz?",
    "4. N. pudendus perineye hangi açıklıktan girer ve hangi kanalda seyreder?",
    "5. Fossa ischioanalis'in medial ve lateral duvarlarını sayınız.",
    "6. Corpus perineale'ye tutunan kaslardan üçünü sayınız.",
], not_=("Cevaplar: 1) İki tuber ischiadicum. 2) Cowper (bulbourethralis) derin, Bartholin (vestibularis major) yüzeyel aralıkta. "
         "3) Colles fasyası uylukta fascia lata'ya, arkada membrana perinei'ye yapışır. 4) Foramen ischiadicum minus; canalis pudendalis (Alcock). "
         "5) Medial: m. levator ani + m. sphincter ani externus; lateral: m. obturatorius internus + fasyası. "
         "6) M. bulbospongiosus, m. transversus perinei superf./prof., m. sphincter ani externus, m. levator ani lifleri."))

TEMEL_KAYNAK = [
    "Moore KL, Dalley AF, Agur AMR. ~Clinically Oriented Anatomy~, 9. baskı. Wolters Kluwer 2023 – Pelvis ve Perine.",
    "Standring S (ed.). ~Gray's Anatomy~, 42. baskı. Elsevier 2021 – Perineum.",
    "Federative International Programme for Anatomical Terminology (FIPAT). ~Terminologia Anatomica~, 2. baskı, 2019.",
    "Mirilas P, Skandalakis JE. Urogenital diaphragm: an erroneous concept. ~J Am Coll Surg~ 2004;198:279–290.",
]
