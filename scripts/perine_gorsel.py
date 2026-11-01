# -*- coding: utf-8 -*-
"""Bölüm kompozisyonu: metin slaytları (icerik_perine) + kadavra/illüstrasyon görsel slaytları.
Görsel referansı ("pmc", PMCID, dosya-anahtarı); etiket noktaları sources/perine_*.json label_points'ten gelir
(özgün piksel; kırpma kutusu 'kirp'=(x0,y0,x1,y1) dışındaki noktalar otomatik atılır)."""
from icerik_perine import *

def T(d, **kw):
    return dict(d, **kw)

def F(pmc, key):
    return ("pmc", pmc, key)

KAPAK = [F("PMC7898478", "CA-34-272"), F("PMC12229694", "Fig2_HTML")]

# ---------------- 1. PELVİS ----------------
PELVIS_GORSEL = [
    dict(tip="kadavra", etiket="GÖRÜNTÜLEME", bolum=B1, baslik="Apertura pelvis superior ve inferior – pelvimetri",
         alt="3B-BT rekonstrüksiyonu (canlı bireyler): giriş ve çıkış çapları", fig=F("PMC5768563", "g001"),
         metin=["Sol: apertura superior transvers çapı linea terminalis'in en geniş noktaları arasında; sağ: interspinöz (spinae ischiadicae) ve intertuberöz çaplar, angulus subpubicus.",
                "Interspinöz çap pelvis minor'ün en dar transvers çapıdır (≈10 cm) – fetal başın iniş düzlemi."]),
    dict(tip="kadavra", etiket="GÖRÜNTÜLEME", bolum=B1, baslik="Pelvisin sagittal çapları", alt="Promontorium – symphysis – os coccygis (3B-BT)",
         fig=F("PMC5768563", "g002"), sol_w=3.4, sag_w=2.4,
         metin=["Conjugata (promontorium – symphysis) giriş çapı; çıkışta symphysis alt kenarı – coccyx ucu arası çap coccyx'in geriye hareketiyle doğumda ≈2 cm artar."]),
    dict(tip="kadavra", etiket="KEMİK", bolum=B1, baslik="Kadın ve erkek pelvisi: arcus pubicus",
         alt="Gerçek kemik (os coxae, kurutulmuş): solda erkek, sağda kadın – Colman ve ark. 2019",
         fig=F("PMC6811666", "Fig2_HTML"), kirp=(0, 0, 649, 345), sol_w=3.0, sag_w=3.0,
         etiketler=[("Acetabulum ♂", (250, 165)), ("Foramen obturatum ♂", (160, 200)), ("Angulus subpubicus ♂", (40, 230)),
                    ("Acetabulum ♀", (555, 160)), ("Foramen obturatum ♀", (480, 225)), ("Angulus subpubicus ♀", (356, 238))],
         metin=["Angulus subpubicus kadında geniş ('U'), erkekte dar ('V'); 3B-BT ölçümünde ♂ 68,6° – ♀ 87,4° (Mohd Ali ve ark. 2020).",
                "Phenice/Klales ölçütleri: arcus ventralis, concavitas subpubica, ramus ischiopubicus'un medial yüzü (adli cinsiyet tayini)."]),
    dict(tip="kadavra", bolum=B1, baslik="Ligg. sacrospinale ve sacrotuberale – kadavra", alt="Regio glutealis profunda, arkadan bakış (m. gluteus maximus kaldırılmış)",
         fig=F("PMC8713160", "g01"), sol_w=3.0, sag_w=3.2, eboyut=12.5,
         metin=["Foramen ischiadicum majus (m. piriformis) ve minus'u ayıran lig. sacrospinale; pudendal demet spina ischiadica üzerinden dönerek foramen ischiadicum minus ile fossa ischioanalis'e girer.",
                "Lig. sacrotuberale perinenin posterolateral sınırıdır; fossa ischioanalis medial duvarında m. levator ani görülür."]),
    dict(tip="iki", bolum=B1, baslik="Pelvis yan duvarı: fascia obturatoria ve arcus tendineus'lar",
         alt="Kadavra, pelvis içinden medial bakış",
         figler=[dict(fig=F("PMC8096964", "Fig2_HTML"), kirp=(0, 0, 350, 268)),
                 dict(fig=F("PMC8096964", "Fig4_HTML"), kirp=(0, 0, 668, 436))],
         metin=["Arcus tendineus musculi levatoris ani (ATLA) fascia obturatoria'nın kalınlaşmasıdır; altında arcus tendineus fasciae pelvis (ATFP; os pubis → spina ischiadica).",
                "Chin ve ark. 2021: fascia obturatoria ♂ 0,167 ± 0,031 mm – ♀ 0,228 ± 0,036 mm; levator ani aponevrozu ATLA'nın üstüne, ramus superior ossis pubis'e dek uzanabilir."]),
    dict(tip="iki", bolum=B1, baslik="Diaphragma pelvis ve fascia superior diaphragmatis pelvis",
         alt="Sagittal ikiye bölünmüş erkek pelvisi (kadavra) – medial bakış",
         figler=[dict(fig=F("PMC12452807", "PROS"), kirp=(0, 0, 228, 250)),
                 dict(fig=F("PMC12452807", "PROS"), kirp=(467, 0, 702, 250))],
         metin=["Sol: pelvis organları yerinde; sağ: fasya kaldırılmış – m. levator ani ve arcus tendineus fasciae pelvis.",
                "Fascia superior diaphragmatis pelvis = fascia pelvis parietalis'in taban kısmı; altındaki her şey perinedir."]),
]

# ---------------- 2. PERİNE – GENEL ----------------
PERINE_GORSEL_SINIR = dict(
    tip="kadavra", bolum=B2, baslik="Perinenin sınırları – kadavrada", alt="Erkek perinesi, kaudalden (litotomiye benzer) bakış; tela subcutanea kaldırılmış",
    fig=F("PMC7898478", "CA-34-272"), sol_w=3.0, sag_w=3.1,
    metin=["Kemik-bağ çerçeve: symphysis – rami ischiopubici – tubera ischiadica – (ligg. sacrotuberalia) – os coccygis; tubera arası çizgi m. transversus perinei superficialis hizasından geçer.",
           "Önde regio urogenitalis (m. bulbospongiosus, m. ischiocavernosus), arkada regio analis (m. sphincter ani externus, anus)."])

CORPUS_GORSEL = dict(
    tip="kadavra", bolum=B2, baslik="Corpus perineale ve episiotomi anatomisi", alt="Kadın kadavrası, dıştan görünüm (Garner ve ark. 2021)",
    fig=F("PMC7913006", "g002"), kirp=(60, 540, 772, 1192), sol_w=3.2, sag_w=3.2,
    metin=["Median insizyon 47 kadavranın %100'ünde corpus perineale'yi kesti; %14,3'ünde m. sphincter ani externus'un pars subcutanea'sına ulaştı.",
           "Düşük açılı mediolateral insizyonda %75 m. bulbospongiosus, gl. vestibularis major ve nn. labiales posteriores insizyon düzlemindeydi."])

# ---------------- 3. REGIO UROGENITALIS ----------------
UROG_GORSEL = [
    dict(tip="kadavra", etiket="İLLÜSTRASYON", bolum=B3, baslik="Perine katmanları – yazarların şeması (♂ / ♀)",
         alt="Yüzeyel çizgili kaslar → membrana perinei → derin aralıkta düz kas plağı", fig=F("PMC12229694", "Fig7_HTML"),
         sol_w=3.1, sag_w=3.1, eboyut=12,
         metin=["Muro ve ark. 2025: derin aralıkta rektum (♀ ayrıca vagina) duvarıyla devamlı, transvers lifli üçgen düz kas plağı – yazarlar bunu 'm. transversus perinei profundus' olarak yorumlar."]),
    dict(tip="iki", bolum=B3, baslik="Erkek regio urogenitalis – katman katman diseksiyon (1)",
         alt="Sol: yüzeyel aralık kasları · Sağ: kaslar kaldırılınca membrana perinei",
         figler=[dict(fig=F("PMC12229694", "Fig1_HTML"), kirp=(0, 0, 332, 271)),
                 dict(fig=F("PMC12229694", "Fig1_HTML"), kirp=(0, 277, 332, 549))],
         metin=["Spatium perinei superficiale: bulbus penis'i saran m. bulbospongiosus, crus'u saran m. ischiocavernosus, arkada m. transversus perinei superficialis.",
                "Membrana perinei rami ischiopubici arasında gerilir; bulbus penis bu levhanın alt yüzüne tutunur."]),
    dict(tip="iki", bolum=B3, baslik="Erkek spatium perinei profundum (2)",
         alt="Membrana perinei kaldırılmış: m. sphincter urethrae externus, gl. bulbourethralis",
         figler=[dict(fig=F("PMC12229694", "Fig1_HTML"), kirp=(336, 277, 669, 549)),
                 dict(fig=F("PMC8373982", "Fig2_HTML"), kirp=(0, 460, 668, 914))],
         metin=["Gll. bulbourethrales (Cowper) derin aralıkta, pars membranacea'nın iki yanında; kanalları membrana perinei'yi delip pars spongiosa'ya açılır.",
                "Muro ve ark. 2021: bez lateralde çizgili (STP–levator–EAS'tan rhabdosphincter'e uzanan), posterosuperiorde düz kasla sarılı."]),
    dict(tip="kadavra", bolum=B3, baslik="Erkek yüzeyel perine kasları", alt="M. transversus perinei superficialis'in üst ve alt demetleri (Muro ve ark. 2021)",
         fig=F("PMC8373982", "Fig1_HTML"), sol_w=3.2, sag_w=3.3,
         metin=["M. bulbospongiosus, m. sphincter ani externus ve m. transversus perinei superficialis corpus perineale düzeyinde birbirleriyle lif alışverişi yapar – 'tek merkezli düğüm' yerine kas sürekliliği."]),
    dict(tip="kadavra", bolum=B3, baslik="Perine kaslarının sürekliliği – lateral bakış (♂)", alt="Suriyut ve ark. 2019 – EAS, m. bulbospongiosus ve levator ani bağlantıları",
         fig=F("PMC7182620", "Fig1_HTML"), kirp=(0, 0, 646, 584), sol_w=3.0, sag_w=3.6,
         metin=["M. bulbospongiosus ile m. sphincter ani externus doğrudan birleşir; m. transversus perinei superficialis'in lateral tendonu ve levator ani ile ilişkisi görülmektedir."]),
    dict(tip="iki", bolum=B3, baslik="Kadın regio urogenitalis – katman katman diseksiyon",
         alt="Sol: yüzeyel aralık · Sağ: bulbus vestibuli ve membrana perinei",
         figler=[dict(fig=F("PMC12229694", "Fig2_HTML"), kirp=(0, 0, 332, 271)),
                 dict(fig=F("PMC12229694", "Fig2_HTML"), kirp=(0, 277, 332, 549))],
         metin=["Bulbus vestibuli m. bulbospongiosus'un altında, ostium vaginae'nin iki yanında; membrana perinei'nin alt yüzüne oturur.",
                "Kadında membrana perinei urethra ve vagina tarafından delinir; dorsal kısmı vagina yan duvarı ve corpus perineale'ye tutunur."]),
    dict(tip="kadavra", bolum=B3, baslik="Clitoris ve bulbus vestibuli – kadavra", alt="Spatium perinei superficiale açılmış (Garner ve ark. 2021)",
         fig=F("PMC7913006", "g004"), sol_w=3.0, sag_w=3.6, eboyut=12.5,
         metin=["Clitoris: glans – corpus – iki crus (ramus ischiopubicus'a tutunur, m. ischiocavernosus ile örtülü); lig. suspensorium clitoridis symphysis'e asar.",
                "Fasciculus neurovascularis: n. perinealis'in yüzeyel ve derin dalları m. transversus perinei superficialis'in önünden geçer."]),
    dict(tip="iki", bolum=B3, baslik="Clitoris üç boyutlu bir organ olarak", alt="Sol: çıkarılmış clitoris (kadavra) · Sağ: mikro-BT rekonstrüksiyonu",
         figler=[dict(fig=F("PMC11452485", "Fig1_HTML"), kirp=(49, 22, 710, 437)),
                 dict(fig=F("PMC11452485", "Fig2_HTML"), kirp=(18, 0, 446, 214))],
         metin=["Tunçkol ve ark. 2024: crus'ta ≈2917, hemicorpus'ta ≈3137 akson (%71–76 miyelinli); n. dorsalis clitoridis gevşek demetler hâlinde – innervasyon yoğunluğu penisin ≈6 katı."]),
    dict(tip="kadavra", bolum=B3, baslik="Kadın yüzeyel perine kasları", alt="M. bulbospongiosus EAS'ın lateral yüzüne tutunur; STP orta hattı EAS'ın derininde geçer",
         fig=F("PMC6942605", "Fig3_HTML"), sol_w=3.2, sag_w=3.6, eboyut=12.5,
         metin=["Baramee ve ark. 2019 (16 kadın kadavra, 28 hemipelvis): kasların tümünün corpus perineale'ye sonlandığı klasik modelin aksine, STP orta hattı geçerek 'orta askı' oluşturur."]),
    dict(tip="iki", etiket="İLLÜSTRASYON", bolum=B3, baslik="Derin perine aralığında sfinkter kompleksi (♀ / ♂)",
         alt="Yazar şemaları: rhabdosphincter, m. compressor urethrae, m. sphincter urethrovaginalis",
         figler=[dict(fig=F("PMC4022307", "011"), eboyut=11.5), dict(fig=F("PMC4022307", "010"), eboyut=11.5)],
         metin=["♀: m. sphincter urethrae externus + m. compressor urethrae + m. sphincter urethrovaginalis 'üretral sfinkter kompleksi'ni yapar (Oelrich 1983); ♂: rhabdosphincter prostat apeksine dek dikey uzanır, gl. bulbourethralis ve m. transversus perinei profundus çevresinde."]),
    dict(tip="iki", bolum=B3, baslik="Membrana perinei ve derin aralık – güncel tartışma",
         alt="Kampelmann ve ark. 2025: üst ♀, alt ♂ (kaudalden bakış)",
         figler=[dict(fig=F("PMC13069139", "g001"), kirp=(0, 0, 661, 672)),
                 dict(fig=F("PMC13069139", "g001"), kirp=(0, 686, 661, 1332))],
         metin=["10 bağışçı: membrana perinei'nin üstünde 4–5 mm kalın doku plağı; makroskopik olarak belirgin transvers çizgili kas yok, bağ dokusu hacim yoğunluğu ≈%80, kadında çizgili kas <%1.",
                "Sonuç: derin aralık 'kas diyaframı' değil, fibromusküler bir plaktır (bkz. Muro 2025 – düz kas yorumu)."]),
    dict(tip="kadavra", bolum=B3, baslik="Membrana perinei – çıkarılmış levha (♀ / ♂)", alt="Kampelmann ve ark. 2025: rami ischiopubici arasında üçgen fibröz plak",
         fig=F("PMC13069139", "g005"), kirp=(0, 0, 709, 504), sol_w=2.9, sag_w=2.9,
         metin=["Membrana perinei = eski 'fascia diaphragmatis urogenitalis inferior'; arka serbest kenarı m. transversus perinei superficialis ve Colles fasyasının kaynaştığı çizgidir (spatium superficiale'nin arka sınırı)."]),
    dict(tip="kadavra", bolum=B3, baslik="Penis kökü: lig. fundiforme ve lig. suspensorium", alt="Stratum membranosum (Scarpa) türevi askı yapıları – kadavra (Filipoiu ve ark. 2023)",
         fig=F("PMC10594829", "Fig9_HTML"), sol_w=3.4, sag_w=3.6, eboyut=12.5,
         metin=["Lig. fundiforme penis: Scarpa (stratum membranosum) fasyasının türevi – penisi sararak dartos/Colles'e devam eder; lig. suspensorium: fascia profunda kökenli, derin yaprağı fascia penis profunda (Buck) ile devam eder.",
                "Penis uzatma cerrahisinde lig. suspensorium kesilirken dorsal damar-sinir demeti risk altındadır."]),
]

# ---------------- 4. REGIO ANALIS ----------------
ANAL_GORSEL = [
    dict(tip="kadavra", bolum=B4, baslik="Fossa ischioanalis'in yağ cismi – kadavra", alt="Kadın perinesi, kaudalden bakış (Baramee ve ark. 2019)",
         fig=F("PMC6942605", "Fig2_HTML"), kirp=(0, 280, 709, 1010), sol_w=3.6, sag_w=3.6,
         metin=["Corpus adiposum fossae ischioanalis fibröz septalarla bölmelenmiştir; önde membrana perinei arka kenarı ve m. transversus perinei superficialis hizasında sınırlanır, üstünden recessus anterior uzanır."]),
    dict(tip="kadavra", etiket="İLLÜSTRASYON", bolum=B4, baslik="Anal kas askıları – kaudalden şema", alt="EAS, lig. anococcygeum ve m. puborectalis (yazar şeması, kadavra temelli)",
         fig=F("PMC10256674", "Fig1_HTML"), kirp=(440, 90, 676, 240), sol_w=3.4, sag_w=3.4,
         metin=["M. puborectalis anorektal bileşkenin arkasında askı ('ansa posterior') oluşturur; EAS arkada lig. anococcygeum aracılığıyla os coccygis'e bağlanır."]),
]

# ---------------- 5. DAMAR – SİNİR ----------------
DAMAR_GORSEL = [
    dict(tip="kadavra", bolum=B5, baslik="N. pudendus ve a. pudenda interna – pelvis içinden", alt="Medial bakış; m. levator ani kaldırılmış (kadın kadavrası)",
         fig=F("PMC8713160", "g00"), sol_w=3.0, sag_w=3.4, eboyut=12,
         metin=["N. pudendus lig. sacrospinale / m. coccygeus düzeyinde a. pudenda interna'nın medialinde seyreder; dalları (n. dorsalis clitoridis, n. perinealis, nn. rectales inferiores) canalis pudendalis'te ayrılır."]),
    dict(tip="iki", bolum=B5, baslik="Canalis pudendalis (Alcock) – kadavra", alt="Sol: kanal açılmış (pens ucu) · Sağ: transgluteal yaklaşımda kanaldaki n. pudendus",
         figler=[dict(fig=F("PMC529451", "1471-2482-4-15-3")), dict(fig=F("PMC6785340", "_04"))],
         metin=["Kanal, fascia obturatoria'nın tuber ischiadicum'un ≈2–4 cm üstündeki duplikatürüdür; içinde n. pudendus, a./v. pudenda interna. Processus falciformis ligamenti sacrotuberalis kanalın alt-iç duvarına komşudur."]),
    dict(tip="kadavra", etiket="İLLÜSTRASYON", bolum=B5, baslik="N. pudendus dallarının perinedeki dağılımı (♀)", alt="Litotomi görünümü – 47 kadavra diseksiyonuna dayalı yazar şeması",
         fig=F("PMC7913006", "g003"), kirp=(230, 60, 560, 440), sol_w=3.4, sag_w=3.4, eboyut=13,
         metin=["N. rectalis inferior EAS'ın pars subcutanea'sını ve perianal deriyi; n. perinealis'in derin dalı m. bulbospongiosus, EAS'ın pars superficialis'ini ve gl. vestibularis major çevresini innerve eder."]),
]

# ---------------- 6. VARYASYONLAR ----------------
LIT = dict(tip="tablo", etiket="LİTERATÜR", bolum=B6, baslik="Perine ve pelvis tabanı varyasyonları – literatür taraması",
           alt="Sıklıklar makalelerden aynen aktarılmıştır", sutunlar=["Varyasyon", "Çalışma", "Örneklem", "Sıklık / bulgu", "Klinik önem"],
           genislik=[2.3, 2.0, 2.0, 3.6, 2.8], satir_h=0.9, boyut=12.5,
           satirlar=[
               ["N. pudendus gövde sayısı", "Ranjan ve ark. 2022", "52 hemipelvis", "Tip I tek gövde %51,9; IIa %13,5 (n. rectalis inf. lig. sacrospinale'yi deler); IIb %23,1; III üç gövde %11,5; n. ischiadicus ile bağlantı %26,9", "Eksik pudendal blok, sakrospinöz fiksasyon"],
               ["N. pudendus oluşumu / gövdeleri", "Suganya ve ark. 2025", "10 kadavra", "Tek gövde %60, iki gövde %20, üç ve dört gövde birer olgu; n. ischiadicus bağlantısı 9 kadavrada", "Blokta istenmeyen n. ischiadicus blokajı"],
               ["N. rectalis inferior'un S3'ten çıkışı", "Dupont ve ark. 2019", "Olgu", "N. rectalis inferior doğrudan S3 ramus anterior'dan (nn. splanchnici pelvici sonrası)", "Fekal inkontinans, pudendal blok"],
               ["A. pudenda interna + a. glutea inferior ortak gövde", "Nayak ve ark. 2016", "Olgu (♂)", "İkinci ortak gövde foramen infrapiriforme'den çıkıp yıldız biçimli dallanma", "Transgluteal yaklaşım, embolizasyon"],
               ["A. penis'in pelvis içi kökenli seyri (aksesuar pudendal tip)", "Nayak ve ark. 2014", "Olgu (♂)", "A. penis a. iliaca interna'dan, lig. puboprostaticum altından geçip a. dorsalis/profunda penis'e ayrılır; a. pudenda interna hipoplazik", "Radikal prostatektomide erektil disfonksiyon riski"],
           ],
           kaynak="Tam künyeler kaynakçada; çalışma görselleri sonraki slaytlarda.")
LIT2 = dict(tip="tablo", etiket="LİTERATÜR", bolum=B6, baslik="Kas ve corpus perineale morfolojisi – literatür taraması",
            alt="Klasik ders kitabı modeline meydan okuyan bulgular", sutunlar=["Konu", "Çalışma", "Örneklem", "Bulgu", "Önem"],
            genislik=[2.3, 2.0, 2.0, 3.6, 2.8], satir_h=0.95, boyut=12.5,
            satirlar=[
                ["M. levator ani'nin bölümleri", "Wu ve ark. 2015", "6 genç erişkin, seri kesit 3B", "Puborectal ve pubococcygeal kısımlar arasında perimisyal septum yok; önde ortak tutunma, arkada 'puborectal' ve 'pubovisceral' ayrımı", "Levator avulsiyonu, hiatus ölçümü"],
                ["Levator ani'nin ön askıları", "Baramee ve ark. 2019", "16 ♀ kadavra", "Levator ön kısmı ön ve arka demetlere ayrılır; STP orta askıyı yapar → 'üç kas askısı'", "Obstetrik perine onarımı"],
                ["M. transversus perinei profundus", "Muro ve ark. 2025 / Kampelmann ve ark. 2025", "9 ve 10 kadavra", "Derin aralıkta rektum (♀ vagina) ile devamlı düz kas plağı / makroskopik çizgili DTP yok, ≈%80 bağ dokusu", "'Diaphragma urogenitale' kavramının terki"],
                ["Corpus perineale boyutu", "Asfour ve ark. 2019", "101 kadın (US)", "Kontrol: yükseklik 22,5 ± 3,3 mm, alan 2,8 ± 0,38 cm²; prolapsusta 16,9 mm ve 2,1 cm²", "Alan <2,4 cm² → arka kompartman prolapsusu"],
            ],
            kaynak="Sıklık/ölçüm değerleri makalelerden aynen aktarılmıştır.")

VARY_GORSEL = [
    dict(tip="calisma", bolum=B6, baslik="N. pudendus'un ekstrapelvik varyasyonları (1)", alt="Tip IIa: ikinci gövde (n. rectalis inferior) lig. sacrospinale'yi deler",
         fig=F("PMC9492552", "i03"), kirp=(250, 120, 650, 400),
         calisma=["26 formalinli kadavra (16 ♂, 10 ♀), 52 hemipelvis; gluteal yaklaşım."],
         bulgu=["Tip I (tek gövde) %51,9 · IIa %13,5 · IIb %23,1 · III (üç gövde) %11,5", "N. ischiadicus ile bağlantı %26,9; Mahakkanukrauh 2005: tek gövde %56,2"],
         onem=["Çok gövdeli sinirde transgluteal/transvaginal blok eksik kalabilir; sakrospinöz kolpopeksi sütürü n. rectalis inferior'u yakalayabilir."]),
    dict(tip="iki", etiket="VARYASYON", bolum=B6, baslik="N. pudendus'un ekstrapelvik varyasyonları (2)", alt="Sol: tip IIb (iki gövde) · Sağ: tip III (üç gövde) – Ranjan ve ark. 2022",
         figler=[dict(fig=F("PMC9492552", "i04"), eboyut=11.5), dict(fig=F("PMC9492552", "i06"), eboyut=11.5)],
         metin=["Gövdeler genellikle lig. sacrospinale düzeyinde vasa pudenda interna'nın medialinde seyreder; n. musculi obturatorii interni ve n. ischiadicus lateralde komşudur."]),
    dict(tip="calisma", bolum=B6, baslik="N. pudendus'un oluşumu ve gövde sayısı", alt="Suganya ve ark. 2025 – Doğu Hindistan popülasyonu",
         fig=F("PMC12519013", "f2"), etiketli=False,
         calisma=["10 kadavra (5 ♂, 5 ♀), bilateral diseksiyon ve morfometri."],
         bulgu=["Tek gövde %60, iki gövde %20, üç gövde %10, dört gövde bir olguda (bilateral)", "N. ischiadicus ile bağlantı 9 kadavrada; en geniş kesit alanı m. piriformis altında (4,04 mm²)"],
         onem=["Bağlantı varlığında pudendal blok n. ischiadicus'u da etkileyebilir; literatürde çok gövde %38–40,5 (Maldonado, Gruber)."]),
    dict(tip="calisma", bolum=B6, baslik="N. rectalis inferior'un S3'ten bağımsız çıkışı", alt="Dupont ve ark. 2019 – olgu sunumu",
         fig=F("PMC6449584", "g001"), kirp=(150, 60, 520, 340),
         calisma=["Kadavra diseksiyonu, pelvis içinden bakış."],
         bulgu=["S3 ramus anterior önce nn. splanchnici pelvici verip n. rectalis inferior olarak devam ediyor", "Bilinen varyantlar: S4'ten bağımsız çıkış, lig. sacrospinale'yi delme"],
         onem=["Pudendal blok, pudendal anastomoz ve sakrospinöz kolpopeksi sırasında yaralanma → fekal inkontinans."]),
    dict(tip="calisma", bolum=B6, baslik="A. pudenda interna ve a. glutea inferior ortak gövdesi", alt="Nayak ve ark. 2016 – olgu sunumu (♂)",
         fig=F("PMC5829714", "g02"), kirp=(150, 120, 640, 470),
         calisma=["Erkek kadavra, regio glutealis diseksiyonu."],
         bulgu=["A. glutea inferior ve a. pudenda interna a. iliaca interna'nın ikinci ortak gövdesinden çıkıyor", "Gövde foramen infrapiriforme'den geçip m. gluteus maximus derininde yıldız biçimli dallanıyor"],
         onem=["Transgluteal pudendal dekompresyon ve pelvik embolizasyonda dikkat; Adachi/Yamaki sınıflamaları."]),
    dict(tip="calisma", bolum=B6, baslik="A. penis'in pelvis içi kökenli seyri", alt="Nayak ve ark. 2014 – 'aksesuar pudendal' tipte seyir",
         fig=F("PMC3971847", "002"), kirp=(120, 150, 520, 440),
         calisma=["Erkek kadavra, pelvis yan duvarı ve perine diseksiyonu."],
         bulgu=["A. penis a. iliaca interna'nın ortak gövdesinden; mesane–pelvis yan duvarı arasında öne, lig. puboprostaticum altından geçiyor", "Symphysis alt kenarının arkasında a. dorsalis ve a. profunda penis'e ayrılıyor; a. pudenda interna küçük"],
         onem=["Radikal prostatektomide yaralanma → arteriyojenik erektil disfonksiyon; penil revaskülarizasyon planlaması."]),
    dict(tip="calisma", bolum=B6, baslik="M. levator ani'nin 3B topografisi", alt="Wu ve ark. 2015 – seri anatomik kesitlerden rekonstrüksiyon",
         fig=F("PMC4549266", "g001"), kirp=(480, 555, 750, 800),
         calisma=["6 genç erişkin (4 ♀, 2 ♂), deforme olmamış seri kesitlerden 3B rekonstrüksiyon."],
         bulgu=["Puborectal ve pubococcygeal kısımlar arasında ayırıcı septum yok", "Post-mortem levator hiatus canlıdakinden ≈61 mm uzun, ≈23 mm dar"],
         onem=["Ders kitabındaki üç parçalı levator modelini sorgular; levator avulsiyonu ve kontinans değerlendirmesi."]),
    dict(tip="calisma", bolum=B6, baslik="Levator ani'nin ön demetleri – üç kas askısı", alt="Baramee ve ark. 2019 – kadın kadavrası, medial bakış",
         fig=F("PMC6942605", "Fig5_HTML"), kirp=(0, 0, 345, 284),
         calisma=["16 kadın kadavrası (ort. yaş 79,75), 28 hemipelvis."],
         bulgu=["Levator ani'nin ön kısmı ön ve arka demetlere ayrılarak ön ve arka askıları oluşturur", "M. bulbospongiosus EAS'ın lateral yüzüne kaynaşır"],
         onem=["Anal kanal önündeki destek askı modeli; obstetrik perine yırtığı onarımında anatomik hedefler."]),
    dict(tip="calisma", etiket="GÖRÜNTÜLEME", bolum=B6, baslik="Corpus perineale boyutu – transperineal US", alt="Asfour ve ark. 2019",
         fig=F("PMC7270988", "Fig1"), kirp=(0, 0, 354, 248),
         calisma=["101 kadın: 22 nullipar sağlıklı gönüllü, 79 prolapsus hastası."],
         bulgu=["Kontrol: yükseklik 22,5 ± 3,3 mm, uzunluk 17,4 ± 2,7 mm, alan 2,8 ± 0,38 cm²", "Prolapsus: yükseklik 16,9 ± 1,7 mm, alan 2,1 ± 0,5 cm²"],
         onem=["Küçük corpus perineale arka kompartman prolapsusu ile güçlü ilişkili (p < 0,0001); alan <2,4 cm² eşik."]),
]

OZET = dict(tip="anlatim", etiket="ÖZET", baslik="Özet – akılda kalacak noktalar", boyut=17, metin=[
    "Perine = diaphragma pelvis'in altı; sınırları apertura pelvis inferior; tubera ischiadica arası çizgi → regio urogenitalis / regio analis.",
    "**Fasyalar**: panniculus adiposus → **Colles** (stratum membranosum; Scarpa ve dartos ile devamlı) → **Gallaudet** (fascia perinei) → **membrana perinei**.",
    "**Spatium superficiale** önde karın duvarına açık (ekstravazasyon yolu); **spatium profundum** üstte fasyasız, fibromusküler plak – 'diaphragma urogenitale' terk edildi.",
    "Gl. bulbourethralis derin, gl. vestibularis major yüzeyel aralıkta.",
    "**Corpus perineale** kas sürekliliklerinin düğümü; episiotomi ve obstetrik yırtıkların anatomik temeli.",
    "**Fossa ischioanalis** at nalı biçiminde iletişimli; lateral duvarında canalis pudendalis.",
    "**N. pudendus** S2–S4; foramen ischiadicum majus → spina ischiadica/lig. sacrospinale → foramen minus → Alcock; gövde sayısı ≈%40–50 olguda birden fazla.",
])

BOLUMLER = [
    ("Pelvis", "Kısa giriş – perinenin kemik-fibröz çerçevesi ve tavanı",
     ["Pelvis major / minor, linea terminalis", "Apertura pelvis superior / inferior", "Ligg. sacrospinale & sacrotuberale",
      "Diaphragma pelvis ve fascia pelvis"], F("PMC8096964", "Fig4_HTML"),
     [PELVIS_TANIM, PELVIS_ACIKLIK, PELVIS_GORSEL[0], PELVIS_GORSEL[1], PELVIS_CINSIYET, PELVIS_GORSEL[2], PELVIS_BAG, PELVIS_GORSEL[3],
      PELVIS_TABAN, PELVIS_GORSEL[4], PELVIS_FASYA, PELVIS_GORSEL[5]]),
    ("Perine – genel", "Tanım, sınırlar, üçgenler, corpus perineale",
     ["Derin ve yüzeyel sınırlar", "Regio urogenitalis / regio analis", "Corpus perineale"], F("PMC7898478", "CA-34-272"),
     [PERINE_TANIM, T(PERINE_UCGEN, tip="eskenar"), PERINE_GORSEL_SINIR, CORPUS_PERINEALE, CORPUS_GORSEL]),
    ("Regio urogenitalis", "Perine fasyaları, aralıklar, dış genital organ kökleri",
     ["Katmanlar: Colles – Gallaudet – membrana perinei", "Spatium perinei superficiale / profundum", "♂ radix penis, ♀ clitoris ve bulbi vestibuli", "Kaslar, klinik"], F("PMC12229694", "Fig1_HTML"),
     [T(KATMANLAR, tip="katman"), UROG_GORSEL[0], COLLES,
      dict(tip="ekstravazasyon", baslik="Colles fasyasının devamlılığı – idrar ekstravazasyonu", bolum=B3,
           metin=["Bulbar urethra yırtığı + fascia penis profunda (Buck) hasarında idrar/kan Colles fasyası altında yayılır: perine 'kelebek' hematomu, scrotum ve penis şişliği, karın ön duvarı (Scarpa altı).",
                  "Buck fasyası sağlamsa ekstravazasyon penis şaftı ile sınırlı kalır; pars membranacea yırtığında ise membrana perinei üstünde (spatium profundum → retropubik alan)."]),
      UROG_GORSEL[12], GALLAUDET, UROG_GORSEL[11], UROG_GORSEL[10], SPATIA_TABLO, KASLAR_TABLO,
      UROG_GORSEL[1], UROG_GORSEL[2], UROG_GORSEL[3], UROG_GORSEL[4],
      UROG_GORSEL[5], UROG_GORSEL[6], UROG_GORSEL[7], UROG_GORSEL[8], UROG_GORSEL[9], KLINIK_UROG]),
    ("Regio analis", "Fossa ischioanalis ve kontinans aparatı",
     ["Fossa ischioanalis sınırları ve recessus'lar", "M. sphincter ani externus", "Corpus anococcygeum"], F("PMC6942605", "Fig2_HTML"),
     [FOSSA_ISCHIOANALIS, ANAL_GORSEL[0], SPHINCTER, ANAL_GORSEL[1]]),
    ("Damar – sinir", "N. pudendus, a. pudenda interna, canalis pudendalis",
     ["Seyir: foramen ischiadicum majus → minus → Alcock kanalı", "Dallar", "Lenfatik drenaj, klinik"], F("PMC8713160", "g01"),
     [T(PUDENDAL_SEMA, tip="pudendal"), DAMAR_GORSEL[0], DAMAR_GORSEL[1], DAMAR_GORSEL[2], PUDENDAL_KLINIK]),
    ("Varyasyonlar", "Literatür taraması ve seçilmiş kadavra çalışmaları",
     ["N. pudendus dallanma tipleri", "A. pudenda interna / a. penis varyasyonları", "Levator ani ve perine kasları – yeni modeller", "Corpus perineale morfometrisi"], F("PMC9492552", "i06"),
     [LIT, LIT2] + VARY_GORSEL + [OZET]),
]
