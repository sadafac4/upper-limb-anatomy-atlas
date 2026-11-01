# -*- coding: utf-8 -*-
"""Perine sunumu – ders metinleri (Türkçe anlatım, Latince terminoloji; TA2/FIPAT 2019).
Görsel slaytları (kadavra) build_perine.py içinde kaynak JSON'larına bağlanır.
Her slaytın 'not' alanı konuşmacı notudur (derste anlatım akışı)."""

B1, B2, B3, B4, B5, B6 = ("PELVİS", "PERİNE – GENEL", "REGIO UROGENITALIS", "REGIO ANALIS", "DAMAR – SİNİR", "VARYASYONLAR")

# ---------------- BÖLÜM 1: PELVİSE KISA GİRİŞ ----------------
PELVIS_TANIM = dict(
    baslik="Pelvis: tanım ve bölümleri", alt="Pelvis major – pelvis minor – apertura pelvis superior / inferior", bolum=B1,
    metin=[
        "**Pelvis** = cingulum pelvicum (iki os coxae) + os sacrum + os coccygis; eklemleri: art. sacroiliaca, symphysis pubica, art. sacrococcygea.",
        "**Linea terminalis** (promontorium → ala ossis sacri kenarı → linea arcuata → pecten ossis pubis → crista pubica → symphysis'in üst kenarı) pelvisi ikiye ayırır:",
        "  - **Pelvis major** (pelvis falsa): linea terminalis'in üstü; cavitas abdominis'in parçası, iliak fossalar.",
        "  - **Pelvis minor** (pelvis vera): linea terminalis'in altı; cavitas pelvis – obstetrik doğum kanalı.",
        "**Apertura pelvis superior** (inlet) = linea terminalis'in çevrelediği açıklık; **apertura pelvis inferior** (outlet) = perinenin osteofibröz çerçevesi.",
        "Pelvis eğimi (inclinatio pelvis): ayakta apertura superior horizontale ≈50–60°; spina iliaca anterior superior ve tuberculum pubicum aynı koronal düzlemde.",
    ],
    not_="Derse pelvisle başlıyoruz çünkü perine, pelvis minor'ün çıkışını kapatan yumuşak doku bölgesidir. Linea terminalis'i kemik üzerinde baştan sona gösterin.")

PELVIS_ACIKLIK = dict(
    tip="tablo", baslik="Apertura pelvis superior ve inferior – sınırlar", bolum=B1,
    alt="Perinenin sınırlarını apertura pelvis inferior belirler",
    sutunlar=["", "Apertura pelvis superior (inlet)", "Apertura pelvis inferior (outlet)"],
    genislik=[1.6, 5.2, 5.2], satir_h=0.95, boyut=15,
    satirlar=[
        ["Ön", "Symphysis pubica'nın üst kenarı, crista pubica", "Symphysis pubica'nın alt kenarı (**lig. pubicum inferius**), arcus pubicus"],
        ["Yan", "Pecten ossis pubis, linea arcuata (os ilium)", "**Rami ischiopubici**, **tubera ischiadica**, **ligg. sacrotuberalia**"],
        ["Arka", "Promontorium ve ala ossis sacri'nin ön kenarı", "**Os coccygis**'in ucu (apex)"],
        ["Klinik çap", "Diameter vera (conjugata anatomica ≈11 cm); conjugata obstetrica (en kısa ön-arka çap ≈ 10,5–11 cm); diameter transversa ≈13 cm",
         "Diameter transversa (bituberal / intertuberal) ≈11 cm; ön-arka çap (alt symphysis – coccyx ucu) ≈9,5 cm, coccyx geriye esneyince ≈11,5 cm"],
    ],
    dip="Apertura inferior elmas (eşkenar dörtgen) biçimlidir; tubera ischiadica arası çizgi onu ön (regio urogenitalis) ve arka (regio analis) üçgenlere ayırır.",
    kaynak="Standart anatomi bilgisi; çaplar yaklaşık ortalama değerlerdir (kadın pelvisi).")

PELVIS_CINSIYET = dict(
    tip="tablo", baslik="Kadın ve erkek pelvisi – karşılaştırma", bolum=B1, alt="Seksüel dimorfizm (adli antropoloji ve obstetri açısından)",
    sutunlar=["Özellik", "Kadın (pelvis gynecoides tipik)", "Erkek (pelvis androides tipik)"],
    genislik=[2.6, 4.7, 4.7], satir_h=0.62, boyut=14.5,
    satirlar=[
        ["Genel yapı", "İnce, hafif; kas izleri silik", "Kalın, ağır; kas izleri belirgin"],
        ["Apertura superior", "Oval / yuvarlak, transvers çap geniş", "Kalp biçimli (promontorium çıkıntılı)"],
        ["Arcus pubicus (angulus subpubicus)", "Geniş, ≈80–85° (U-biçimli)", "Dar, ≈50–60° (V-biçimli)"],
        ["Pelvis minor", "Geniş ve sığ; duvarlar paralele yakın", "Dar ve derin; huni biçimli"],
        ["Incisura ischiadica major", "Geniş (≈90°)", "Dar (≈70°)"],
        ["Tubera ischiadica / spinae", "Dışa açılı; spinae ischiadicae daha az içe çıkıntılı", "İçe dönük; spinae ischiadicae belirgin"],
        ["Foramen obturatum", "Oval / üçgenimsi", "Yuvarlak / oval"],
        ["Acetabulum", "Küçük, ön-yan yönelimli", "Büyük, lateral yönelimli"],
    ],
    dip="Caldwell–Moloy sınıflaması: gynecoides, androides, anthropoides, platypelloides tipleri (obstetrik prognozda kullanılır).",
    kaynak="Standart anatomi bilgisi; açılar yaklaşık değerlerdir.")

PELVIS_BAG = dict(
    tip="tablo", baslik="Ligg. sacrospinale & sacrotuberale – foramina ischiadica", bolum=B1,
    alt="Perineye giden damar-sinir demeti gluteal bölgeden foramen ischiadicum minus ile geçer",
    sutunlar=["Yapı", "Sınırlar", "Geçen yapılar"],
    genislik=[2.6, 4.4, 5.6], satir_h=1.2, boyut=14,
    satirlar=[
        ["Foramen ischiadicum majus", "Incisura ischiadica major + lig. sacrospinale + lig. sacrotuberale",
         "M. piriformis; **suprapiriforme**: a./v./n. gluteus superior; **infrapiriforme**: n. ischiadicus, n. cutaneus femoris post., a./v./n. gluteus inferior, **a./v. pudenda interna, n. pudendus**, n. musculi obturatorii interni, n. musculi quadrati femoris"],
        ["Foramen ischiadicum minus", "Incisura ischiadica minor + lig. sacrospinale + lig. sacrotuberale",
         "Tendo m. obturatorii interni; **a./v. pudenda interna ve n. pudendus** (perineye giriş), n. musculi obturatorii interni"],
        ["Lig. sacrotuberale", "Spina iliaca post., os sacrum–coccyx kenarı → tuber ischiadicum; **processus falciformis** ile ramus ossis ischii'ye uzanır",
         "Fossa ischioanalis'in posterolateral sınırı; processus falciformis canalis pudendalis'e komşu (pudendal sıkışma)"],
        ["Lig. sacrospinale", "Os sacrum–coccyx yan kenarı → spina ischiadica; m. coccygeus'un dorsal (fibröz) parçası",
         "N. pudendus spina'nın / bağın arkasından (a. pudenda interna'nın medialinden) geçer – pudendal blok için kılavuz"],
    ],
    kaynak="Standart anatomi bilgisi (Terminologia Anatomica).")

PELVIS_TABAN = dict(
    baslik="Diaphragma pelvis (pelvis tabanı)", alt="M. levator ani + m. coccygeus; perinenin 'tavanı'", bolum=B1,
    metin=[
        "**M. levator ani** – üç parça (TA): **m. pubococcygeus** (+ m. puboperinealis, m. pubovaginalis/puboprostaticus, m. puboanalis), **m. puborectalis**, **m. iliococcygeus**.",
        "Orijin: os pubis'in arka yüzü – **arcus tendineus musculi levatoris ani** (fascia obturatoria kalınlaşması) – spina ischiadica.",
        "Sonlanma: corpus perineale, corpus anococcygeum (lig. anococcygeum), os coccygis; m. puborectalis anorektal bileşkede U-askı → **angulus anorectalis** (≈90°).",
        "**M. coccygeus** (m. ischiococcygeus): spina ischiadica → os sacrum/coccyx yan kenarı; lig. sacrospinale ile kaynaşık.",
        "İnnervasyon: pelvik yüzden doğrudan **S3–S4** (n. levatoris ani); perineal yüzden n. pudendus dalları (n. rectalis inferior) – katkı tartışmalıdır.",
        "**Hiatus urogenitalis**: puborectalis kolları arasında; urethra (♀ vagina) geçer. Doğum travması → levator avulsiyonu, prolapsus.",
    ],
    not_="Diaphragma pelvis'in altındaki her şey perinedir. Fossa ischioanalis'in medial duvarı levator ani'nin perineal yüzüdür; bunu bir sonraki bölümde göreceğiz.")

PELVIS_FASYA = dict(
    baslik="Fascia pelvis ve perineye geçiş", alt="Parietal – visseral fasya; arcus tendineus", bolum=B1,
    metin=[
        "**Fascia pelvis parietalis** (endopelvik olmayan, kasları örten): fascia obturatoria, fascia musculi piriformis, **fascia superior diaphragmatis pelvis**.",
        "**Fascia pelvis visceralis** (endopelvik fasya): organ kapsülleri ve aralarındaki gevşek bağ dokusu; yoğunlaşmalar: lig. puboprostaticum/pubovesicale, lig. cardinale (lig. transversum cervicis), lig. uterosacrale.",
        "**Arcus tendineus fasciae pelvis** (beyaz çizgi): os pubis → spina ischiadica; vaginanın lateral askısı (DeLancey seviye II).",
        "**Fascia inferior diaphragmatis pelvis**: levator ani'nin perineal yüzü = fossa ischioanalis'in medial-üst duvarı.",
        "Fascia obturatoria'nın alt kısmı ikiye ayrılarak **canalis pudendalis**'i (Alcock) oluşturur → pelvis–perine sınırında damar-sinir yolu.",
        "Sonuç: **perine**, diaphragma pelvis'in altında, apertura pelvis inferior ile deri arasında kalan bölgedir.",
    ])

# ---------------- BÖLÜM 2: PERİNE – GENEL ----------------
PERINE_TANIM = dict(
    baslik="Perineum: tanım ve sınırlar", bolum=B2, alt="Anatomik (derin) ve yüzeyel (topografik) perine",
    metin=[
        "**Perineum (regio perinealis)**: pelvis minor çıkışında, diaphragma pelvis ile deri arasında kalan bölge; litotomi pozisyonunda uylukların arasında eşkenar dörtgen alan.",
        "**Derin sınırlar** = apertura pelvis inferior: önde symphysis pubica (lig. pubicum inferius), anterolateralde rami ischiopubici, lateralde tubera ischiadica, posterolateralde ligg. sacrotuberalia, arkada os coccygis.",
        "**Yüzeyel sınırlar**: önde mons pubis, lateralde uyluk iç yüzü (sulcus genitofemoralis), arkada nates arası yarık (crena analis) üst ucu.",
        "**Tavan**: diaphragma pelvis (m. levator ani + m. coccygeus).  **Taban**: deri ve fascia perinei superficialis.",
        "Tubera ischiadica'nın ön uçlarını birleştiren çizgi (corpus perineale'den geçer) → **regio urogenitalis** (önde) ve **regio analis** (arkada).",
        "Klinik 'perine' (obstetride): vagina ile anüs arasındaki yumuşak doku = corpus perineale bölgesi.",
    ])

PERINE_UCGEN = dict(
    baslik="Perinenin topografik bölümlenmesi", bolum=B2, alt="Litotomi pozisyonu – kaudalden bakış",
    metin=[
        "İki üçgen aynı düzlemde değildir: **regio urogenitalis** ≈horizontal, **regio analis** öne-aşağı eğik; aralarındaki açı ≈ 'çatı' biçimi.",
        "**Regio urogenitalis**: membrana perinei ile örtülü; urethra (♀ + vagina) delip geçer; dış genital organların kökü.",
        "**Regio analis**: canalis analis + m. sphincter ani externus ve iki yanda **fossa ischioanalis**.",
        "Merkezde **corpus perineale** (centrum tendineum perinei): iki üçgenin ve kas sistemlerinin birleşme noktası.",
        "Yüzey işaretleri: raphe perinei (♂ raphe scroti ve raphe penis ile devam eder), frenulum labiorum pudendi / commissura labiorum posterior (♀).",
    ])

CORPUS_PERINEALE = dict(
    baslik="Corpus perineale (centrum tendineum perinei)", bolum=B2,
    alt="Fibromusküler düğüm noktası – obstetrik ve kolorektal cerrahinin merkezi",
    metin=[
        "Konum: ♂ bulbus penis ile canalis analis arasında; ♀ vestibulum vaginae arka kenarı (fourchette) ile anüs arasında, ≈2–4 cm piramidal kitle.",
        "Bağlanan yapılar: **m. bulbospongiosus**, **mm. transversi perinei superficialis et profundus**, **m. sphincter ani externus** (yüzeyel parça), m. puboperinealis (levator ani), m. sphincter urethrovaginalis, **membrana perinei** arka kenarı ve Colles fasyası; düz kas lifleri (m. rectourethralis ♂).",
        "Kadında üç katlı bir yapı olarak tanımlanır (yüzeyel kaslar – membrana perinei – derin levator bağlantıları) ve vaginanın distal desteğidir (**DeLancey seviye III**).",
        "Erkekte m. rectourethralis ve corpus perineale, radikal perineal prostatektomi ve abdominoperineal rezeksiyonda kritik disseksiyon düzlemidir.",
        "**Klinik**: obstetrik perine yırtıkları (1.–4. derece; 3a/3b/3c sphincter ani externus/internus tutulumuna göre), **episiotomi** (mediolateral – sphincter yaralanmasını azaltır; median – corpus perineale'yi keser), perineal hipermobilite → rektosel.",
    ],
    kaynak="Woodman PJ, Graney DO. Clin Anat 2002;15:321–334 • RCOG Green-top Guideline No.29 (2015) – yırtık sınıflaması.")

# ---------------- BÖLÜM 3: REGIO UROGENITALIS ----------------
KATMANLAR = dict(
    baslik="Regio urogenitalis – yüzeyden derine katmanlar", bolum=B3, alt="Fasyalar ve aralıklar (spatia)",
    metin=[
        "**Tela subcutanea perinei** iki katlı: yağlı **panniculus adiposus** (karın ön duvarında Camper) + **stratum membranosum** (**Colles fasyası**; karında Scarpa).",
        "**Spatium perinei superficiale**: Colles fasyası ile membrana perinei arası (kapalı arka sınır, önde karın duvarına açık).",
        "**Fascia perinei** (Gallaudet; 'investing fascia'): yüzeyel perine kaslarını sarar; terminoloji tartışmalı.",
        "**Membrana perinei**: arcus pubicus'u kapatan üçgen fibröz tabaka; ♂ urethra, ♀ urethra + vagina tarafından delinir.",
        "**Spatium perinei profundum**: membrana perinei'nin üstü; üstte kesin fasyal sınır yoktur → recessus anterior fossae ischioanalis ile komşu.",
    ],
    not_="Klasik 'diaphragma urogenitale' (iki fasya arasında sandviç kas) modeli artık kabul görmüyor; bir sonraki slaytlarda nedenini tartışacağız.")

COLLES = dict(
    baslik="Fascia perinei superficialis – stratum membranosum (Colles)", bolum=B3,
    alt="Tutunma yerleri ve devamlılık – klinik önemi büyük",
    metin=[
        "**Lateral**: rami ischiopubici (periost) ve fascia lata'ya; **arka**: m. transversus perinei superficialis hizasında membrana perinei'nin arka kenarına kaynaşır.",
        "**Önde**: penis/clitoris ve scrotum/labia majora boyunca devam eder → ♂ **tunica dartos** (düz kas içerir) ve **fascia penis superficialis**; ardından karın ön duvarında **Scarpa fasyası** (stratum membranosum abdominis).",
        "Scarpa fasyası uylukta lig. inguinale'nin ≈1 parmak altında fascia lata'ya tutunur → uyluğa geçiş kapalıdır.",
        "♀: aynı katman labia majora'ya uzanır; daha ince ve yağdan zengindir, dartos benzeri düz kas (tunica dartos labialis) zayıftır.",
        "Sonuç: spatium perinei superficiale **arkada ve yanlarda kapalı, önde karın ön duvarına açık** bir torbadır.",
    ])

GALLAUDET = dict(
    baslik="Fascia perinei (Gallaudet) ve membrana perinei", bolum=B3, alt="'Diaphragma urogenitale' neden terk edildi?",
    metin=[
        "**Fascia perinei (Gallaudet)**: m. ischiocavernosus, m. bulbospongiosus ve m. transversus perinei superficialis'i saran derin yatırım fasyası; önde fascia penis profunda (**Buck**) ve lig. suspensorium penis ile devam eder.",
        "**Membrana perinei**: TA2'de diaphragma urogenitale terimi kaldırılmış; tek, kalın fibröz levha olarak tanımlanır (eski 'fascia diaphragmatis urogenitalis inferior').",
        "Oelrich (1980 ♂, 1983 ♀) fetal/yenidoğan seri kesitlerinde **m. sphincter urethrae'nin** horizontal bir 'diaphragma' değil, urethra çevresinde dikey uzanan çizgili sfinkter kompleksi olduğunu gösterdi.",
        "Mirilas & Skandalakis (2004): 'diaphragma urogenitale' hatalı bir kavram; derin perine aralığının üst fasyası yoktur, alanı yukarıda levator ani ve recessus anterior ile sınırlıdır.",
        "♀'de membrana perinei iki bölgeli: **dorsal** (rami ischiopubici → vagina yan duvarı ve corpus perineale arası transvers levha) ve **ventral** (compressor urethrae + sphincter urethrovaginalis ile birleşik, urethrayı destekleyen kısım) (Stein & DeLancey 2008).",
    ],
    kaynak="Oelrich TM. Am J Anat 1980;158:229–246; Anat Rec 1983;205:223–232 • Mirilas P, Skandalakis JE. J Am Coll Surg 2004;198:279–290 • Stein TA, DeLancey JOL. Obstet Gynecol 2008;111:686–693 • FIPAT. Terminologia Anatomica, 2. baskı, 2019.")

SPATIA_TABLO = dict(
    tip="tablo", baslik="Spatium perinei superficiale ve profundum – içerik", bolum=B3, alt="Erkek ve kadında karşılaştırmalı",
    sutunlar=["Aralık", "Erkek (♂)", "Kadın (♀)"], genislik=[2.6, 5.0, 5.0], satir_h=1.55, boyut=14,
    satirlar=[
        ["Spatium perinei superficiale",
         "Radix penis: **crura penis** + **bulbus penis**; m. ischiocavernosus, m. bulbospongiosus, m. transversus perinei superficialis; pars spongiosa urethrae'nin proksimali; a./n. perinealis dalları, nn./aa. scrotales posteriores",
         "**Crura clitoridis**, **bulbi vestibuli**, **gll. vestibulares majores (Bartholin)**; m. ischiocavernosus, m. bulbospongiosus, m. transversus perinei superficialis; nn./aa. labiales posteriores"],
        ["Spatium perinei profundum",
         "Pars membranacea urethrae; **m. sphincter urethrae externus**; m. transversus perinei profundus; **gll. bulbourethrales (Cowper)** – kanalları membrana perinei'yi delip bulbus'a açılır; a./n. dorsalis penis, a. bulbi penis",
         "Urethra'nın proksimali ve vaginanın alt kısmı; **m. sphincter urethrae externus**, **m. compressor urethrae**, **m. sphincter urethrovaginalis**; (m. transversus perinei profundus kadında çoğunlukla düz kas/bağ dokusu); a./n. dorsalis clitoridis"],
    ],
    dip="Gl. bulbourethralis derin aralıkta, gl. vestibularis major yüzeyel aralıktadır – sık sorulan bir ayrım.")

KASLAR_TABLO = dict(
    tip="tablo", baslik="Regio urogenitalis kasları", bolum=B3, alt="Tümünün innervasyonu: n. pudendus – n. perinealis (r. profundus)",
    sutunlar=["Kas", "Orijin", "İnsersiyo", "Fonksiyon"], genislik=[2.8, 3.1, 3.4, 3.4], satir_h=0.95, boyut=13,
    satirlar=[
        ["M. ischiocavernosus", "Ramus ossis ischii iç yüzü, tuber ischiadicum", "Crus penis/clitoridis (tunica albuginea)", "Crus'tan venöz dönüşü azaltır, ereksiyonu sürdürür"],
        ["M. bulbospongiosus", "♂ corpus perineale, raphe (bulbus altında); ♀ corpus perineale", "♂ membrana perinei, corpus spongiosum, fascia penis profunda; ♀ arcus pubicus, clitoris (bulbi vestibuli üstü)", "♂ ejakülasyon, işeme sonrası boşaltma; ♀ vestibulum daraltma (sphincter vaginae)"],
        ["M. transversus perinei superficialis", "Tuber ischiadicum ön-iç yüzü", "Corpus perineale", "Corpus perineale'yi sabitler"],
        ["M. transversus perinei profundus", "Ramus ossis ischii iç yüzü", "Corpus perineale, raphe", "Corpus perineale'yi sabitler (♀ zayıf)"],
        ["M. sphincter urethrae externus", "Urethra çevresinde halka (♂ prostat apeksine dek dikey uzanır)", "Urethra çevresi", "İstemli kontinans"],
        ["M. compressor urethrae (♀)", "Rami ischiopubici", "Urethra önünde karşı taraf ile birleşir", "Urethrayı sıkıştırır"],
        ["M. sphincter urethrovaginalis (♀)", "Corpus perineale", "Urethra ve vagina'yı çevreler", "Urethra ve vagina'yı daraltır"],
    ],
    kaynak="Standart anatomi bilgisi; ♀ üretral sfinkter kompleksi: Oelrich 1983 Anat Rec 205:223–232.")

KLINIK_UROG = dict(
    tip="klinik", baslik="Klinik bağlantılar – regio urogenitalis", bolum=B3, etiket="KLİNİK BAĞLANTI",
    metin=[
        "**Fournier gangreni**: nekrotizan fasiit Colles–dartos–Scarpa düzleminde yayılır; uyluğa ve anal üçgene geçişi fasyal tutunmalar sınırlar, testisler (ayrı kan akımı) çoğunlukla korunur.",
        "**Bartholin kisti/apsesi**: gl. vestibularis major kanalı labium minus iç yüzünde, hymen dışında, vestibulum'da saat ≈4 ve ≈8 hizasında açılır; marsupializasyon.",
        "**Pars membranacea urethrae rüptürü** (pelvis kırığı): membrana perinei üstünde → ekstravazasyon spatium profundum ve retropubik/extraperitoneal alana; perineal hematom 'kelebek' biçimi görülmez.",
        "**Pudendal blok**: transvaginal yolla spina ischiadica'nın hemen medial-posterioruna (lig. sacrospinale); a. pudenda interna laterale yakındır → aspirasyon zorunlu.",
        "**Erektil fonksiyon**: n. cavernosus (plexus hypogastricus inferior, otonom) prostatın posterolateralinden geçer; somatik duyu n. dorsalis penis.",
    ])

# ---------------- BÖLÜM 4: REGIO ANALIS ----------------
FOSSA_ISCHIOANALIS = dict(
    tip="tablo", baslik="Fossa ischioanalis – sınırlar ve içerik", bolum=B4, alt="Kama biçimli, yağla dolu, iki tarafta at nalı biçiminde birbirine bağlı aralık",
    sutunlar=["Sınır / öğe", "Yapı"], genislik=[2.7, 10.0], satir_h=0.66, boyut=14.5,
    satirlar=[
        ["Lateral duvar", "M. obturatorius internus + **fascia obturatoria** (üzerinde canalis pudendalis); tuber ischiadicum"],
        ["Medial duvar", "M. levator ani + fascia inferior diaphragmatis pelvis; aşağıda m. sphincter ani externus"],
        ["Tavan (apex)", "Levator ani'nin fascia obturatoria'dan çıktığı çizgi (arcus tendineus m. levatoris ani)"],
        ["Ön sınır", "Membrana perinei arka kenarı ve corpus perineale; üstünden **recessus anterior** pubis'e dek uzanır"],
        ["Arka sınır", "Lig. sacrotuberale ve m. gluteus maximus alt kenarı; **recessus posterior** gluteus maximus altına"],
        ["Taban", "Perianal deri ve tela subcutanea"],
        ["İçerik", "Corpus adiposum fossae ischioanalis (fibröz septalı yağ); n./a./v. rectalis inferior; canalis pudendalis içinde n. pudendus, a./v. pudenda interna; n. cutaneus perforans (S2–3), r. perinealis n. cutanei femoris post."],
        ["İletişim", "İki taraf **spatium postanale profundum** (Courtney aralığı; corpus anococcygeum üstü) ile birleşir → at nalı (horseshoe) apse"],
    ])

SPHINCTER = dict(
    baslik="Canalis analis ve m. sphincter ani externus", bolum=B4, alt="Kontinans aparatı",
    metin=[
        "**M. sphincter ani externus** (çizgili, n. rectalis inferior S2–S4): klasik olarak **pars subcutanea**, **pars superficialis** (corpus anococcygeum ve corpus perineale'ye tutunan eliptik) ve **pars profunda** (yukarıda m. puborectalis ile kaynaşır).",
        "Güncel görüntüleme/diseksiyon çalışmaları parçaların sınırlarının net olmadığını, kadında önde kısa olduğunu gösterir (obstetrik yaralanmada önemli).",
        "**M. sphincter ani internus**: m. circulare'nin kalınlaşması (otonom); arada **m. longitudinalis conjunctus** (conjoint longitudinal muscle).",
        "**Corpus anococcygeum** (lig. anococcygeum): anüs ile coccyx arasında fibromusküler raphe; levator ani ve sphincter ani externus'un arka tutunma yeri.",
        "**Linea pectinata**: üstü visseral (a. rectalis superior, v. portae drenajı, otonom innervasyon, nodi iliaci interni), altı somatik (a. rectalis inferior, sistemik ven, n. rectalis inferior, nodi inguinales superficiales).",
        "**Klinik**: perianal/iskioanal apse, fistula ani (Parks sınıflaması), hemoroidal hastalık, obstetrik sfinkter hasarı (OASIS).",
    ])

# ---------------- BÖLÜM 5: DAMAR-SİNİR ----------------
PUDENDAL_SEMA = dict(
    baslik="N. pudendus ve a. pudenda interna – seyir ve dallar", bolum=B5, alt="Pelvis → regio glutealis → perine",
    metin=[
        "N. pudendus'un dallanması değişkendir: n. rectalis inferior canalis pudendalis'e girmeden önce, hatta doğrudan plexus sacralis'ten çıkabilir; n. dorsalis penis/clitoridis kanalda ayrılabilir (oranlar için varyasyon bölümüne bakınız).",
        "Venler arterlere eşlik eder; v. dorsalis penis profunda ise lig. arcuatum pubis altından plexus venosus prostaticus/vesicalis'e drene olur.",
    ])

PUDENDAL_KLINIK = dict(
    tip="klinik", baslik="Pudendal nöropati ve sıkışma noktaları", bolum=B5, etiket="KLİNİK BAĞLANTI",
    metin=[
        "**Sıkışma noktaları**: (1) lig. sacrospinale–lig. sacrotuberale arasındaki 'kıskaç' (spina ischiadica hizası), (2) canalis pudendalis (fascia obturatoria, processus falciformis), (3) membrana perinei hizası (n. dorsalis).",
        "**Nantes kriterleri** (Labat 2008): n. pudendus alanında ağrı, oturmakla artma, gece uyandırmama, nesnel duyu kaybı olmaması, tanısal pudendal blokla geçme.",
        "**Pudendal blok**: transvaginal (spina ischiadica palpasyonu) veya transperineal (tuber ischiadicum medialinden); BT/US eşliğinde gluteal yaklaşım.",
        "**Siklist/uzun süreli oturma, doğum travması** (gerilme nöropatisi) ve pelvik cerrahi (sacrospinous fixation) n. pudendus hasarı nedenleridir.",
        "**Lenfatik drenaj**: perine derisi, alt anal kanal, scrotum/labia → **nodi inguinales superficiales**; corpus cavernosum, urethra proksimali, derin yapılar → **nodi iliaci interni**; glans → nodi inguinales profundi.",
    ],
    kaynak="Labat JJ ve ark. Neurourol Urodyn 2008;27:306–310 (Nantes kriterleri).")

TEMEL_KAYNAK = [
    "Federative International Programme for Anatomical Terminology (FIPAT). ~Terminologia Anatomica~, 2nd ed. 2019.",
    "Oelrich TM. The urethral sphincter muscle in the male. ~Am J Anat~ 1980;158:229–246.",
    "Oelrich TM. The striated urogenital sphincter muscle in the female. ~Anat Rec~ 1983;205:223–232.",
    "Mirilas P, Skandalakis JE. Urogenital diaphragm: an erroneous concept casting its shadow over the sphincter urethrae and deep perineal space. ~J Am Coll Surg~ 2004;198:279–290.",
    "Stein TA, DeLancey JOL. Structure of the perineal membrane in females: gross and microscopic anatomy. ~Obstet Gynecol~ 2008;111:686–693.",
    "Woodman PJ, Graney DO. Anatomy and physiology of the female perineal body with relevance to obstetrical injury and repair. ~Clin Anat~ 2002;15:321–334.",
    "Labat JJ, Riant T, Robert R ve ark. Diagnostic criteria for pudendal neuralgia by pudendal nerve entrapment (Nantes criteria). ~Neurourol Urodyn~ 2008;27:306–310.",
    "Standring S (ed.). ~Gray's Anatomy: The Anatomical Basis of Clinical Practice~, 42nd ed. Elsevier 2021 – Perineum bölümü.",
]
