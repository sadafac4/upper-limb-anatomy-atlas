#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perine ve Pelvis – perine odaklı, fasyalar ayrıntılı (Türkçe, Latince terimler).
Görseller: PMC açık erişim (sources/perine.json) + NLM Visible Human erkek ve kadın kesitleri.
Çıktı: perine/Perine_Pelvis.pptx"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from slayt_tipleri import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
PV = ROOT / "perine" / "images" / "vhp"
VHP_K = ("Kaynak: NLM Visible Human Project – {cins} (kriyokesit + aynı NLM numaralı donmuş BT); NCI Imaging Data Commons "
         "(doi:10.5281/zenodo.12690049); NLM Terms and Conditions (2019). Radyolojik yönelim: ön yukarıda, hastanın sağı solda.")

BOLUMLER = [
 dict(ad="TABAN", baslik="Pelvis tabanı", alt="Diaphragma pelvis ve centrum tendineum perinei", konular=["Perinenin sınırları ve üçgenleri", "M. levator ani ve m. coccygeus", "Arcus tendineus ve fasyalar", "Perine kas askıları", "Görüntüleme"]),
 dict(ad="FASYALAR", baslik="Perine fasyaları ve keseler", alt="Camper/Scarpa'dan Denonvilliers'e", konular=["Katman şeması", "Colles, Buck, dartos, Gallaudet", "Membrana perinei ve derin kese", "Pelvis içi fasyalar", "İdrar ekstravazasyonu, Fournier"]),
 dict(ad="ÜROGENİTAL", baslik="Regio urogenitalis", alt="Erkek ve kadın", konular=["Yüzeyel kese içeriği", "Erektil dokular", "Sfinkter urethrae", "Glandula vestibularis major", "MR anatomisi"]),
 dict(ad="ANAL", baslik="Regio analis", alt="Fossa ischioanalis ve sfinkterler", konular=["Canalis analis", "Sfinkter kompleksi", "Fossa ischioanalis", "Canalis pudendalis", "MR ve ultrason"]),
 dict(ad="KESİT + VARYASYON", baslik="Kesitsel anatomi ve varyasyonlar", alt="VHP erkek–kadın; literatür taraması", konular=["Erkek pelvis/perine kesitleri", "Kadın pelvis/perine kesitleri", "N. pudendus ve a. pudenda interna varyasyonları", "Levator avülsiyonu, perine cismi", "Klinik bağlantılar"]),
]

def vk(sex, n, baslik_, alt, et, notlar):
    cins = "Visible Human Male" if sex == "M" else "Visible Human Female"
    return dict(baslik=baslik_, alt=f"{alt} – NLM kesit no. {n} ({'erkek' if sex == 'M' else 'kadın'})",
                cryo=PV / f"{sex}{n}_cryo.jpg", etiketler=et, notlar=notlar,
                paneller=[(PV / f"{sex}{n}_ct.png", "Donmuş BT, aynı kesit no. (yumuşak doku)"), (PV / f"{sex}{n}_ctbone.png", "Aynı BT, kemik penceresi")],
                kaynak=VHP_K.format(cins=cins))

KESITLER = [
 vk("M", 1878, "Erkek pelvis – mesane ve vesiculae seminales", "Caput femoris düzeyi", [
     ("Caput femoris", (75, 330), "L"), ("M. obturatorius internus", (215, 400), "L"), ("Fossa ischioanalis (yağ)", (262, 552), "L"), ("M. gluteus maximus", (130, 595), "L"),
     ("M. rectus abdominis", (330, 125), "R"), ("Vesica urinaria", (335, 300), "R"), ("Vesiculae seminales", (345, 425), "R"), ("Rectum", (355, 505), "R")],
    ["Mesane ile rektum arasında vesiculae seminales ve Denonvilliers fasyası bulunur (rektovezikal septum).", "Fossa ischioanalis yağ dokusu, m. obturatorius internus ile m. levator ani arasında piramit şeklinde uzanır."]),
 vk("M", 1900, "Erkek perine – symphysis pubica ve prostat", "Pelvis çıkımı düzeyi", [
     ("Os ischii", (110, 430), "L"), ("M. obturatorius internus", (240, 390), "L"), ("M. gluteus maximus", (140, 600), "L"),
     ("Symphysis pubica", (343, 215), "R"), ("Prostata", (335, 320), "R"), ("Rectum / canalis analis", (340, 482), "R"), ("Caput femoris", (610, 330), "R")],
    ["Prostat, symphysis pubica'nın arkasında ve rektumun önündedir – parmakla rektal muayenede ön duvardan palpe edilir.", "Prostat ile rektum arasındaki Denonvilliers fasyası, total mezorektal eksizyonda cerrahi düzlemi belirler."]),
 vk("M", 1912, "Erkek perine – urethra ve canalis analis", "Ramus inferior ossis pubis düzeyi", [
     ("Tuber ischiadicum", (140, 460), "L"), ("Fossa ischioanalis", (255, 530), "L"), ("M. gluteus maximus", (180, 585), "L"),
     ("Os pubis (ramus inferior)", (310, 240), "R"), ("Urethra", (345, 322), "R"), ("Canalis analis", (345, 468), "R")],
    ["Bu düzeyde ön tarafta ürogenital üçgen (urethra), arkada anal üçgen (canalis analis) yer alır; ikisini tuber ischiadicum'ları birleştiren hat ayırır.", "Fossa ischioanalis'in lateral duvarında canalis pudendalis (Alcock) içinde n. pudendus ve a./v. pudenda interna seyreder."]),
 vk("M", 1934, "Erkek perine – radix penis", "Yüzeyel perine kesesi düzeyi", [
     ("Fossa ischioanalis", (430, 500), "R"), ("Crus penis ve m. ischiocavernosus", (430, 382), "R"), ("Tuber ischiadicum", (510, 480), "R"),
     ("Radix penis (corpora)", (340, 200), "L"), ("Bulbus penis bölgesi", (340, 390), "L"), ("Canalis analis", (340, 500), "L")],
    ["Radix penis: ortada bulbus penis (m. bulbospongiosus ile örtülü), yanlarda ramus ischiopubicus'a tutunan crura (m. ischiocavernosus ile örtülü).", "Bu yapılar yüzeyel perine kesesindedir; altında membrana perinei, üstünde Colles fasyası bulunur."]),
 vk("F", 1860, "Kadın pelvis – mesane boynu, vajina ve rektum", "Os pubis düzeyi", [
     ("Caput femoris", (45, 330), "L"), ("M. obturatorius internus", (185, 330), "L"), ("Fossa ischioanalis", (215, 482), "L"), ("M. gluteus maximus", (130, 560), "L"),
     ("Os pubis", (440, 230), "R"), ("Collum vesicae / urethra", (330, 240), "R"), ("Vagina", (330, 330), "R"), ("Rectum", (340, 445), "R")],
    ["Kadında önden arkaya üç açıklık sırası: urethra – vagina – rectum; hepsi m. levator ani'nin hiatus'undan geçer.", "Vajina ile rektum arasında rektovajinal septum (kadında Denonvilliers'in karşılığı) bulunur."]),
 vk("F", 1890, "Kadın perine – canalis analis ve anal üçgen", "Tuber ischiadicum düzeyi", [
     ("Tuber ischiadicum", (110, 410), "L"), ("Fossa ischioanalis", (210, 452), "L"), ("M. gluteus maximus", (120, 530), "L"),
     ("Canalis analis", (340, 420), "R"), ("Ürogenital üçgen (vestibulum bölgesi)", (300, 230), "R")],
    ["Canalis analis'i iç ve dış sfinkterler sarar; lateralinde geniş yağlı fossa ischioanalis vardır.", "Fossa ischioanalis'teki apseler bu yağ dokusu içinde kolayca yayılabilir ve arkadan karşı tarafa geçebilir (at nalı apse)."]),
]

GIRIS_DZ = dict(baslik="Perine nedir ve nasıl çalışılır?", alt="Pelvis çıkımının altında kalan elmas şeklindeki bölge",
  paragraflar=[
   "Perine, pelvis çıkımını aşağıdan kapatan, diaphragma pelvis'in altında ve deri ile arasında kalan bölgedir. Litotomi pozisyonunda bakıldığında elmas şeklindedir: önde symphysis pubica, yanlarda ramus ischiopubicus ve tuber ischiadicum, arkada lig. sacrotuberale ve os coccygis bu elmasın köşelerini ve kenarlarını oluşturur.",
   "İki tuber ischiadicum'u birleştiren hayali bir çizgi, perineyi iki üçgene ayırır. Öndeki ürogenital üçgen, dış genital organları ve urethra'yı; arkadaki anal üçgen ise canalis analis'i ve iki yanındaki fossa ischioanalis'i içerir. İki üçgen aynı düzlemde değildir; ürogenital üçgen daha yatay, anal üçgen ise yukarı-arkaya eğimlidir.",
   "Perineyi anlamanın anahtarı fasyalardır. Karın ön duvarının yüzeyel fasyası perineye kesintisiz devam eder, membrana perinei ve pelvis tabanı ise kesin sınırlar çizer. Bu katmanlar, bir idrar kaçağının veya bir enfeksiyonun hangi yöne yayılabileceğini, hangi yöne ise yayılamayacağını belirler. Bu sunumda önce pelvis tabanını, ardından fasyaları ve keseleri, sonra ürogenital ve anal bölgeleri, en son da kesitleri ve varyasyonları ele alacağız."])

TABAN = [
 dict(tip="duzyazi", baslik="Pelvis tabanı: bir huni ve bir askı", alt="Diaphragma pelvis",
   paragraflar=[
    "Pelvis tabanı, pelvis organlarını taşıyan ve karın içi basınca karşı koyan kas–fasya yapısıdır. Ana bileşeni, iki taraflı m. levator ani ve arkadaki m. coccygeus'tur. Bu kaslar üstte ve altta fasyalarla örtülerek diaphragma pelvis'i oluşturur.",
    "M. levator ani bir 'huni' şeklindedir. Önde os pubis'ten, yanlarda m. obturatorius internus fasyası üzerindeki kalınlaşmadan, yani arcus tendineus musculi levatoris ani'den, arkada spina ischiadica'dan başlar. Lifleri aşağı ve mediale inerek orta hatta organların etrafında ve arkada lig. anococcygeum'da birleşir.",
    "Levator ani'nin en medial ve en önemli kısmı m. puborectalis'tir. Rektumun arkasından bir 'U' askı gibi dolanarak anorektal açıyı oluşturur ve kontinansın temel unsurlarından biridir. Bu askının önünde kalan açıklık, levator hiatus'tur; kadında urethra, vagina ve rektum, erkekte urethra ve rektum bu hiatus'tan geçer. Doğum sırasında bu kasın kemiğe yapışma yerinden kopması (avülsiyon) prolapsus ve inkontinansın önemli bir nedenidir."]),
 dict(tip="tablo", baslik="Pelvis tabanı ve perine kasları", alt="Köken – yapışma – sinir – işlev", sutunlar=["Kas", "Köken", "Yapışma", "Sinir", "İşlev"],
   satirlar=[["M. puborectalis", "Os pubis arka yüzü", "Rektum arkasında karşı tarafla 'U' askı", "N. pudendus + S3–S4 dalları", "Anorektal açı, kontinans"],
             ["M. pubococcygeus", "Os pubis", "Lig. anococcygeum, os coccygis", "S3–S4 (n. levator ani)", "Pelvis organlarını destekler"],
             ["M. iliococcygeus", "Arcus tendineus m. levatoris ani, spina ischiadica", "Lig. anococcygeum, coccyx", "S3–S4", "Pelvis tabanını kaldırır"],
             ["M. coccygeus", "Spina ischiadica", "Coccyx ve sacrum alt kenarı", "S4–S5", "Coccyx'i destekler"],
             ["M. transversus perinei superficialis", "Tuber ischiadicum", "Centrum tendineum perinei", "N. perinealis", "Perine cismini sabitler"],
             ["M. bulbospongiosus", "Centrum tendineum, rafe", "Membrana perinei, corpus spongiosum / bulbus vestibuli", "N. perinealis", "Ejakülasyon, ereksiyon; vajina girişini daraltır"],
             ["M. ischiocavernosus", "Ramus ischiopubicus", "Crus penis / clitoridis", "N. perinealis", "Ereksiyonu sürdürür"],
             ["M. sphincter ani externus", "Perine cismi, lig. anococcygeum", "Canalis analis çevresi", "N. rectalis inferior", "İstemli anal kontinans"]],
   genislik=[2.3, 2.6, 2.8, 2.2, 2.8], boyut=12.5),
 dict(tip="gorsel", baslik="Arcus tendineus m. levatoris ani ve fascia obturatoria", alt="Chin ve ark., Sci Rep 2021 – hemipelvis diseksiyonu",
   figs=[("pmc", "PMC8096964", "Fig2"), ("pmc", "PMC8096964", "Fig4")], yatay=True,
   lejant=["**ATLA** arcus tendineus m. levatoris ani; **ATFP** arcus tendineus fasciae pelvis; **PS** symphysis pubica; siyah daireler canalis obturatorius", "Şekil 4: **LAM** m. levator ani; **OIM** m. obturatorius internus; **PRM** m. piriformis; **IAF** fossa ischioanalis; **Ut** uterus; **Rc** rectum"],
   noktalar=["Fascia obturatoria kalınlığı erkekte 0,167 ± 0,031 mm, kadında 0,228 ± 0,036 mm (p < 0,01).", "Tüm kadavralarda levator ani aponevrozu ATLA'nın üstünde fascia obturatoria ile kaynaşmıştır."]),
 dict(tip="gorsel", baslik="Erkek pelvis tabanı – lateral görünüm", alt="Suriyut ve ark., Anat Sci Int 2019 – 15 erkek pelvis",
   figs=[("pmc", "PMC7182620", "Fig1"), ("pmc", "PMC7182620", "Fig2")], yatay=True,
   lejant=["**LA** m. levator ani; **IC** m. ischiocavernosus; **BS** m. bulbospongiosus; **STP** m. transversus perinei superficialis; **EAS** m. sphincter ani externus; **ACL** lig. anococcygeum; pubis, tendinous arch (arcus tendineus), coccyx"],
   noktalar=["Perine kasları lateralde birbiriyle bağlantılıdır.", "Levator ani'den uzanan demetler ve perine kasları dış üretral sfinkteri çevreler.", "Levator ani demetleri lig. anococcygeum ile coccyx'e uzanır."]),
 dict(tip="gorsel", baslik="Kadın perinesi – üç kas askısı", alt="Baramee ve ark., Anat Sci Int 2019 – 16 kadın kadavra",
   figs=[("pmc", "PMC6942605", "Fig2"), ("pmc", "PMC6942605", "Fig6")], yatay=True,
   lejant=["**IC** m. ischiocavernosus; **BS** m. bulbospongiosus; **STP** m. transversus perinei superficialis; **EAS** m. sphincter ani externus (Sub. EAS deri altı bölüm); **LA** m. levator ani; **AB/PB** levator ani ön bölümünün ön/arka demeti; **ACL** lig. anococcygeum"],
   noktalar=["M. bulbospongiosus dış anal sfinkterin lateral yüzüne kaynaşır.", "M. transversus perinei superficialis orta askıyı oluşturur.", "Yazarlar pelvis tabanını destekleyen üç kas askısı önermektedir."]),
 dict(tip="gorsel", baslik="Levator ani ve sfinkter kompleksi – 3B rekonstrüksiyon", alt="Wu ve ark., PLoS ONE 2015 – Chinese Visible Human kesitleri", etiket="KESİT",
   figs=[("pmc", "PMC4549266", "g001"), ("pmc", "PMC4549266", "g002")], yatay=False,
   lejant=["**B** mesane; **V** vagina; **R** rektum; **U** urethra; **OI** m. obturatorius internus; **EAS** m. sphincter ani externus; **PV** m. pubovisceralis; **PR-D/PR-S** m. puborectalis derin/yüzeyel; **RC** m. rectococcygeus; **AL** lig. anococcygeum; **PB** perine cismi; **DP** derin perine kası; **STP**; **BS**"],
   noktalar=["4 kadın ve 2 erkekten ince seri kesitlerle 3B model.", "Puborektal kas halkaları anorektal birleşimi dolanır ve levator hiatus'u tanımlar.", "Lig. anococcygeum dış anal sfinkteri coccyx'e sabitler."]),
 dict(tip="gorsel", baslik="Levator ani alt bölümleri – 3B transperineal ultrason", alt="Manzini ve ark., Insights Imaging 2021", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC8253870", "Fig4"), ("pmc", "PMC8253870", "Fig1")], yatay=False,
   lejant=["Renk kodu: gri os pubis; kahverengi dış sfinkter; kırmızı m. puboperinealis; turuncu m. puboanalis; sarı m. pubovaginalis; yeşil m. puborectalis; mavi m. iliococcygeus"],
   noktalar=["Hiç doğum yapmamış 20 kadında 3B ultrasonla segmentasyon.", "Gözlemciler arası uyum: puborektal 0,83, dış sfinkter 0,81."]),
]

FASYA = [
 dict(tip="duzyazi", baslik="Perine fasyaları: katman katman düşünmek", alt="Karın duvarından perineye kesintisiz bir sistem",
   paragraflar=[
    "Perinenin fasyalarını anlamak için karın ön duvarından başlamak gerekir. Karnın yüzeyel fasyası iki tabakadır: yüzeyde yağlı Camper fasyası, derinde zarsı Scarpa fasyası. Camper fasyası perineye geçerken yağını kaybeder; skrotumda düz kas içeren tunica dartos'a, penis'te ise yüzeyel penis fasyasına dönüşür.",
    "Asıl önemli olan zarsı tabakadır. Scarpa fasyası perineye Colles fasyası (fascia perinei superficialis) adıyla devam eder. Colles fasyası yanlarda ramus ischiopubicus'a, arkada ise membrana perinei'nin arka kenarına sıkıca tutunur. Bu tutunmalar sayesinde Colles fasyası ile membrana perinei arasında, öne ve yukarıya, karın duvarına açık, ama arkaya ve uyluklara kapalı bir boşluk oluşur: yüzeyel perine kesesi.",
    "Yüzeyel kesenin tabanında membrana perinei yer alır. Bu sağlam fibröz tabaka, ürogenital üçgeni iki ramus ischiopubicus arasında germektedir. Membrana perinei'nin üstünde, levator ani'ye kadar uzanan bölge derin perine kesesidir. Klasik kitaplardaki 'diaphragma urogenitale' kavramı günümüzde terk edilmiştir; derin kesede dış üretral sfinkter, m. transversus perinei profundus (kadında büyük ölçüde düz kas ve bağ dokusu) ve damar–sinirler bulunur.",
    "Bu katman düzeni klinikte çok somut sonuçlar doğurur. Bulbus düzeyinde yırtılan bir urethra'dan kaçan idrar yüzeyel kesede birikir; Colles fasyasının tutunmaları nedeniyle uyluklara veya anal bölgeye geçemez, skrotum, penis ve karın ön duvarına doğru yayılır. Fournier gangreni de aynı fasyal planları izler."]),
 dict(tip="katman", baslik="Ürogenital üçgende katmanlar – yüzeyelden derine", alt="Erkek perinesi (kadında karşılıkları parantez içinde)",
   katmanlar=[("Deri", "Skrotum (labia majora) ve perine derisi", "F3E0C7"),
              ("Camper fasyası (yağlı)", "Perinede yağını kaybeder → tunica dartos / yüzeyel penis fasyası", "F7D774"),
              ("Colles fasyası (zarsı)", "Scarpa fasyasının devamı; ramus ischiopubicus ve membrana perinei arka kenarına tutunur", "E0A100"),
              ("Derin perine fasyası (Gallaudet)", "Yüzeyel kese kaslarını örten fasya; penis'te Buck fasyasına devam eder", "C77C02"),
              ("YÜZEYEL PERİNE KESESİ", "Mm. ischiocavernosus, bulbospongiosus, transversus perinei superficialis; crura ve bulbus penis (bulbus vestibuli, Bartholin bezi)", "B71C1C"),
              ("Membrana perinei", "Ramus ischiopubicus'lar arasında gerili sağlam fibröz tabaka; urethra (ve vagina) tarafından delinir", "6D4C41"),
              ("DERİN PERİNE KESESİ", "M. sphincter urethrae externus, m. transversus perinei profundus / düz kas; bulbourethral bezler (erkek); a. ve n. dorsalis penis/clitoridis", "8E24AA"),
              ("Fascia diaphragmatis pelvis inferior", "Levator ani'nin alt yüzü; fossa ischioanalis'in medial duvarının ön uzantısı", "5E35B1"),
              ("M. levator ani", "Pelvis tabanı", "1F5F9E"),
              ("Fascia diaphragmatis pelvis superior / fascia endopelvina", "Pelvis organlarını saran visseral ve parietal fasya", "455A64")],
   dip="Klinik kural: Colles fasyası ile membrana perinei arasındaki kese öne açık, arkaya ve uyluklara kapalıdır."),
 dict(tip="tablo", baslik="Perine fasyaları – süreklilik ve klinik önem", alt="Hangi fasya nereye devam eder?", sutunlar=["Fasya", "Karın / pelvis karşılığı", "Penis / skrotum / vulva karşılığı", "Klinik önem"],
   satirlar=[["Camper (yağlı yüzeyel)", "Karın yüzeyel yağlı tabaka", "Tunica dartos (düz kas), yüzeyel penis fasyası", "Skrotumun ısı düzenlemesi"],
             ["Scarpa → Colles", "Karın zarsı yüzeyel fasya", "Colles fasyası; penis'te dartos ile birlikte", "İdrar ve enfeksiyonun yayılma sınırı"],
             ["Derin perine fasyası (Gallaudet)", "Dış oblik kas fasyası (innominate)", "Buck fasyası (fascia penis profunda)", "Penil hematom Buck içinde kalırsa penise sınırlı"],
             ["Membrana perinei", "—", "Corpus spongiosum ve crura buna tutunur", "Yüzeyel ve derin keseyi ayırır"],
             ["Denonvilliers (rektoprostatik / rektovajinal)", "Peritoneal reflexiondan aşağı uzanır", "—", "Total mezorektal eksizyon ve prostatektomi düzlemi"],
             ["Fascia mesorectalis / presakral / Waldeyer", "Fascia endopelvina'nın parçaları", "—", "Rektum kanseri cerrahisi, presakral venöz kanama"]],
   genislik=[2.8, 3.0, 3.4, 3.5], boyut=13),
 dict(tip="gorsel", baslik="Perine bölgeleri ve membrana perinei – diseksiyon", alt="Kampelmann ve ark., J Anat 2025 – 10 donör", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC13069139", "g001"), ("pmc", "PMC13069139", "g004")], yatay=True,
   lejant=["Sol (a kadın, b erkek): **1** fossa ischioanalis; **2** m. levator ani; **3** membrana perinei / m. transversus perinei profundus (üzerinde a. pudenda interna ve n. pudendus dalları); **4** m. transversus perinei superficialis; **5** m. ischiocavernosus; **6** m. bulbospongiosus",
           "Sağ (erkek): **1** m. levator ani; **2** m. coccygeus; **3** membrana perinei / derin transvers kas; **4** m. ischiocavernosus; **5** m. bulbospongiosus; yeşil daire fossa ischioanalis"],
   noktalar=["Membrana perinei'nin üstünde 4–5 mm kalınlığında, ramus ischiopubicus'lara transvers uzanan bir doku plağı bulunmuştur."]),
 dict(tip="gorsel", baslik="Derin perine kesesinin histolojisi", alt="Kampelmann ve ark., J Anat 2025 – azan boyası ve immünfloresan", etiket="HİSTOLOJİ",
   figs=[("pmc", "PMC13069139", "g006")],
   lejant=["(a) kadın, (b) erkek: mavi transvers kollajen lifler baskın, kırmızı kas lifleri az; yeşil çerçeveler stereolojik sayım alanı. (c–d) siyah oklar düz kas, düz kas aktini ile pozitif (beyaz oklar)"],
   noktalar=["Her iki cinsiyette doku hacminin yaklaşık %80'i bağ dokusudur.", "'M. transversus perinei profundus' olarak bilinen yapı büyük ölçüde bağ dokusu ve düz kastan oluşur – klasik 'kaslı ürogenital diyafram' kavramının terk edilmesinin nedeni."]),
 dict(tip="gorsel", baslik="Erkek perinesi – yüzeyelden derine katmanlar", alt="Muro ve ark., Sci Rep 2025 – 9 kadavra", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC12229694", "Fig1")],
   lejant=["**Ic** m. ischiocavernosus; **Bs** m. bulbospongiosus; **STP** m. transversus perinei superficialis; **EAS** dış anal sfinkter; **BP** bulbus penis; **IPR** ramus ischiopubicus; **PM** membrana perinei; **LA** m. levator ani; **EUS** dış üretral sfinkter; **Ur** urethra; **SM** düz kas; **LM** rektumun longitudinal kası"],
   noktalar=["(A) Perine kasları; (B) STP; (C) daha derinde sert, yoğun bağ dokusu olan membrana perinei; (D) membrana perinei kaldırıldığında rektum duvarıyla devamlı üçgen düz kas plağı."]),
 dict(tip="gorsel", baslik="Kadın perinesi – yüzeyelden derine katmanlar", alt="Muro ve ark., Sci Rep 2025", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC12229694", "Fig2"), ("pmc", "PMC12229694", "Fig7")], yatay=True,
   lejant=["**BV** bulbus vestibuli; **Va** vagina; **Bs**; **Ic**; **STP**; **EAS**; **IPR**; **PM** membrana perinei; **Ur**; **SM** düz kas; **LA**; şemada **Bl** mesane, **R** rektum"],
   noktalar=["Kadında derin perine boşluğundaki düz kas plağı hem vajina hem rektum duvarıyla devamlıdır.", "Her iki cinste perine katmanlı bir yapı gösterir: STP → membrana perinei → düz kas."]),
 dict(tip="gorsel", baslik="Kadında membrana perinei ve rabdosfinkter", alt="Hinata ve ark., Biomed Res Int 2014 – histoloji ve şema", etiket="HİSTOLOJİ",
   figs=[("pmc", "PMC4022307", "011"), ("pmc", "PMC4022307", "007")], yatay=True,
   lejant=["Şema: Uterus, Bladder (mesane), Pubis, **RS** rabdosfinkter, Urethra, **UVS** m. sphincter urethrovaginalis, Vestibular bulb, Bulbospongiosus, Vagina, **CU** m. compressor urethrae, Levator ani, **PM** membrana perinei, External anal sphincter, Anus",
           "Histoloji: **UR** urethra; **CC** crus clitoridis; **VAG** vagina; **LA** levator ani; **REC** rektum"],
   noktalar=["Erkekte membrana perinei ince ama sağlamdır ve rabdosfinkterin alt kenarı boyunca uzanır.", "Kadında rabdosfinkter, membrana perinei ile devamlı elastik lif ağı içine gömülüdür."]),
 dict(tip="duzyazi", baslik="Pelvis içi fasyalar ve cerrahi düzlemler", alt="Denonvilliers, mezorektal fasya ve Waldeyer",
   paragraflar=[
    "Pelvis tabanının üstünde, organları saran fasya sistemi fascia endopelvina olarak adlandırılır. Parietal yaprak pelvis duvarındaki kasları, visseral yaprak ise mesane, prostat, vajina ve rektumu örter. Bu iki yaprak arasında kalan gevşek bağ dokusu, cerrahların 'avasküler düzlem' olarak kullandığı boşlukları oluşturur.",
    "Rektumun ön yüzünde, erkekte prostat ve vesiculae seminales ile rektum arasında Denonvilliers fasyası (septum rectovesicale/rectoprostaticum) bulunur; kadındaki karşılığı rektovajinal septumdur. Peritonun en alt reflexion'undan aşağıya, perine cismine kadar uzanır. Rektum kanseri cerrahisinde tümörün yerine göre diseksiyon bu fasyanın önünden veya arkasından yapılır; fasyanın ön-yanlarında ise ereksiyondan sorumlu kavernöz sinirler seyreder.",
    "Rektumun arkasında ise mezorektumu saran fascia mesorectalis ile sakrumu örten presakral fasya arasında gevşek bir düzlem vardır. Yaklaşık S4 düzeyinde bu iki yaprağı birleştiren rektosakral (Waldeyer) fasya, rektumun tam mobilizasyonu için kesilmesi gereken bir yapıdır. Presakral fasyanın yırtılması, altındaki presakral venlerden ciddi kanamaya yol açabilir."]),
 dict(tip="gorsel", baslik="Denonvilliers fasyası – 'Y' şekli", alt="Li ve ark., BMC Surg 2023 – 20 erkek pelvis (orta sagital kesit)", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC9843937", "Fig2")],
   lejant=["**1** ürogenital fasyanın visseral yaprağı; **2** periton; **3** peritoneal reflexion; **4** Denonvilliers fasyası; **5** vesica urinaria; **6** rectum; **7** vesiculae seminales; **8** prostata"],
   noktalar=["Denonvilliers fasyası tipik olarak tek katlı ve serttir.", "Sagital düzlemde peritoneal reflexion ile birlikte 'Y' şekli oluşturur."]),
 dict(tip="gorsel", baslik="Denonvilliers fasyası – histoloji ve mikro-BT", alt="Muraoka ve ark., BMC Urol 2015; Yang ve ark., Sci Rep 2021", etiket="HİSTOLOJİ",
   figs=[("pmc", "PMC4433060", "Fig4"), ("pmc", "PMC8571354", "Fig2")], yatay=True,
   lejant=["Sol: **DF** Denonvilliers fasyası; **PR** prostat; **UR** urethra; **RS** rabdosfinkter; **LMR/CMR** rektumun longitudinal/sirküler kası; **REC** rektum; **IAS/EAS** iç/dış anal sfinkter; **CG** bulbourethral bez",
           "Sağ: mikro-BT ve Masson trikrom; **U.B** mesane; **SV** vesicula seminalis; **R** rektum; **P** prostat; ok başları DVF"],
   noktalar=["25 erkek kadavrada DF, düzensiz gevşek bağ dokusu ve iç içe 'yapraklar' şeklinde (elastik / düz kas lifleri) bulunmuştur.", "Mikro-BT de DF'nin çok katmanlı yapısını doğrulamaktadır."]),
 dict(tip="gorsel", baslik="Denonvilliers fasyası ve ön mezorektum – cerrahi düzlemler", alt="García-Gausí ve ark., Updates Surg 2022; Yang ve ark. 2021 (şema)", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC8995278", "Fig3"), ("pmc", "PMC8571354", "Fig5")], yatay=False,
   lejant=["Üst: Prostate; **Den (+PC)** Denonvilliers fasyası (prostat kapsülü ile); **SV**; Anterior mesorectum; Rectal wall; sarı ok ön düzlem, kırmızı ok arka düzlem",
           "Alt şema: mezorektal fasya, Denonvilliers fasyası, ön ve arka diseksiyon düzlemleri"],
   noktalar=["31 kadavranın %100'ünde peritoneal reflexiondan başlayıp prostat kapsülüne sıkıca yapışan tek katlı fasya.", "Başarılı mezorektal eksizyon için diseksiyon düzlemi DVF'nin arkasından geçmelidir (Yang ve ark.)."]),
 dict(tip="gorsel", baslik="Presakral, mezorektal ve rektosakral (Waldeyer) fasya", alt="Kim, Yonsei Med J 2005 – hemipelvis diseksiyonu", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC2810586", "001"), ("pmc", "PMC2810586", "002")], yatay=False,
   lejant=["Presacral fascia = fascia presacralis (presakral venleri örter); Rectal proper fascia = fascia mesorectalis; Rectosacral fascia = Waldeyer fasyası; Levator ani muscle"],
   noktalar=["Waldeyer fasyası yaklaşık S4 düzeyinde retrorektal boşlukta bulunur.", "Rektumun tam mobilizasyonu bu fasya kesilmeden mümkün değildir."]),
 dict(tip="klinik", baslik="Fasyalar ve klinik: idrar ekstravazasyonu ve Fournier gangreni", alt="Fasyal planlar yayılımı belirler",
   metin=["**Bulbus düzeyinde urethra rüptürü** (ata biner tarzı düşme): idrar yüzeyel perine kesesinde toplanır → skrotum, penis ve karın ön duvarına (Scarpa altında) yayılır; Colles fasyasının ramus ischiopubicus ve membrana perinei arka kenarına tutunması nedeniyle **uyluk ve anal bölgeye geçmez**.",
          "**Penil rüptürde** kan Buck fasyası sağlamsa penise sınırlı kalır ('patlıcan' görünümü); Buck yırtılmışsa Colles altında 'kelebek' şeklinde perineye yayılır.",
          "**Membranöz urethra yaralanması** (pelvis kırığı): idrar derin kese ve pelvis içine (subperitoneal) yayılır.",
          "**Fournier gangreni:** Colles fasyasından Buck ve dartos'a, oradan Scarpa fasyası boyunca karın duvarına yayılan nekrotizan fasiit; acil debridman gerektirir.",
          "**Perine cismi yaralanması** (doğumda 3.–4. derece yırtık): dış anal sfinkter ve perine kaslarının ortak tutunma noktası bozulur → inkontinans."],
   figs=[("pmc", "PMC11304407", "i03")]),
]

UROG = [
 dict(tip="duzyazi", baslik="Ürogenital üçgen: erkek ve kadın", alt="Aynı plan, farklı organlar",
   paragraflar=[
    "Ürogenital üçgenin temel planı iki cinsiyette aynıdır; farklı olan, bu planın içine yerleşen organlardır. Her iki cinsiyette yüzeyel kesede erektil dokular ve onları örten iskelet kasları bulunur: kemiklere tutunan crura üzerinde m. ischiocavernosus, orta hattaki bulbus üzerinde m. bulbospongiosus.",
    "Erkekte iki crus birleşerek corpora cavernosa penis'i, bulbus ise urethra'yı taşıyan corpus spongiosum'u oluşturur. Kadında ise crura clitoridis klitorisin gövdesini oluşturur; bulbus vestibuli ise ikiye ayrılarak vajina girişinin iki yanında yer alır. Bulbus vestibuli'nin arka ucunda glandula vestibularis major (Bartholin bezi) bulunur.",
    "Derin kesede, membrana perinei'nin üstünde, urethra'yı saran dış üretral sfinkter vardır. Erkekte bu bölgede bulbourethral (Cowper) bezler, kadında ise urethra ile vajinayı birlikte saran m. sphincter urethrovaginalis ve m. compressor urethrae yer alır. Tüm bu kasları n. pudendus'un perineal dalları innerve eder."]),
 dict(tip="anlatim", baslik="Ürogenital üçgenin damar ve sinirleri", alt="A. pudenda interna ve n. pudendus",
   metin=["**N. pudendus** (S2–S4) foramen ischiadicum majus'tan pelvisi terk eder, spina ischiadica/lig. sacrospinale'yi dolanıp foramen ischiadicum minus'tan perineye girer ve **canalis pudendalis (Alcock)** içinde seyreder.",
          "Dalları: **n. rectalis inferior** (dış anal sfinkter, perianal deri), **n. perinealis** (yüzeyel dal: skrotum/labia derisi; derin dal: perine kasları, dış üretral sfinkter) ve **n. dorsalis penis/clitoridis** (derin keseden geçerek glans duyusu).",
          "**A. pudenda interna** sinirle birlikte seyreder; dalları a. rectalis inferior, a. perinealis, a. bulbi penis/vestibuli, a. profunda penis/clitoridis (ereksiyon) ve a. dorsalis penis/clitoridis.",
          "**Pudendal blok:** spina ischiadica referans alınarak transvajinal veya transperineal yapılır; doğumda perine analjezisi sağlar.",
          "**Lenf:** perine derisi ve dış genital organlar **yüzeyel inguinal** lenf düğümlerine; testis ise **lomber/paraaortik** düğümlere drene olur."]),
 dict(tip="gorsel", baslik="Kadın perinesi – diseksiyon ve epizyotomi anatomisi", alt="Garner ve ark., Diagnostics 2021 – 47 kadın kadavra",
   figs=[("pmc", "PMC7913006", "g003"), ("pmc", "PMC7913006", "g004")], yatay=True,
   lejant=["Body / Crus of the clitoris = corpus / crus clitoridis; Bulb of the vestibule = bulbus vestibuli; Greater vestibular gland = Bartholin bezi; Bulbospongiosus m.; Posterior labial nn.; Deep / Superficial perineal n.; **S/D** yüzeyel/derin perineal sinir dalları; ***** m. bulbospongiosus ile örtülü bulbus vestibuli"],
   noktalar=["Orta hat insizyonu kadavraların %100'ünde perine cismi bağ dokusunu kesmiştir.", "Perine cismine ince kas lifleri yalnız %16,6 olguda tutunmuş; %83,4'ünde yalnız bağ dokusu bulunmuştur.", "M. bulbospongiosus dış anal sfinkterin yüzeyel bölümüyle devamlıdır."]),
 dict(tip="gorsel", baslik="Klitoris ve bulbus vestibuli – MR ve illüstrasyon", alt="Golden ve ark., Abdom Radiol 2025", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC13013239", "Fig2"), ("pmc", "PMC13013239", "Fig1")], yatay=False,
   lejant=["İllüstrasyon: Pubic symphysis; Dorsal n. (n. dorsalis clitoridis); Glans; Body; Crus; Bulb; External urethral orifice; Vaginal orifice; Greater vestibular gl. (Bartholin); **Pudendal canal** (Alcock); Pudendal n. (İllüstrasyon © 2025 Elise Butler, makalenin CC BY lisansı ile)",
           "MR: aksiyel T2 ve sagital yağ baskılı T2; siyah oklar T2'de hiperintens bulbus vestibuli"],
   noktalar=["Bulbus vestibuli vajina girişini iki yandan kuşatır.", "Bartholin bezleri vajinanın posterolateralinde yer alır."]),
 dict(tip="gorsel", baslik="Penis'in MR anatomisi ve fasyaları", alt="Regent ve ark., Diagnostics 2025", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC12732017", "g001")],
   lejant=["T2 MR (a sagital, b koronal): yeşil oklar tunica albuginea; sarı oklar corpus spongiosum içindeki urethra; beyaz ok glans penis; kırmızı oklar corpora cavernosa"],
   noktalar=["Tunica albuginea'nın yüzeyinde Buck fasyası (bazen görüntülenebilir), daha yüzeyde ince dartos fasyası ve deri bulunur.", "Yüzeyel ve derin dorsal venler Buck fasyasıyla ilişkili olarak orta hatta seyreder."]),
]

ANAL = [
 dict(tip="duzyazi", baslik="Anal üçgen: canalis analis ve fossa ischioanalis", alt="Kontinans mekanizması ve yağ dolu boşluklar",
   paragraflar=[
    "Anal üçgenin merkezinde yaklaşık 4 cm uzunluğundaki canalis analis yer alır. Kanal, m. puborectalis askısının oluşturduğu anorektal açıda rektumdan başlar ve anüste sonlanır. Kanalın ortasındaki linea pectinata (dentata) önemli bir sınırdır: üstünde iç organ tipi mukoza, otonom innervasyon ve portal drenaj; altında deri tipi epitel, somatik (ağrıya duyarlı) innervasyon ve sistemik drenaj bulunur.",
    "Kanalı iki sfinkter sarar. İç anal sfinkter, rektumun sirküler düz kasının kalınlaşmasıdır ve istemsizdir; istirahat basıncının büyük kısmını sağlar. Dış anal sfinkter ise iskelet kasıdır, n. rectalis inferior ile innerve edilir ve istemli kontrolü sağlar. İkisinin arasında, rektumun longitudinal kasının devamı olan intersfinkterik boşluk vardır; anal fistüllerin sınıflandırması bu katmanlara göre yapılır.",
    "Kanalın iki yanında, levator ani ile m. obturatorius internus arasında yağ dolu fossa ischioanalis bulunur. Bu boşluklar defekasyon sırasında kanalın genişlemesine izin verir. Lateral duvarında, fascia obturatoria'nın yarığı olan canalis pudendalis içinde n. pudendus ve a./v. pudenda interna seyreder. İki taraftaki fossa, kanalın arkasından birbiriyle bağlantılı olduğundan bir taraftaki apse karşı tarafa 'at nalı' şeklinde yayılabilir."]),
 dict(tip="gorsel", baslik="Anal kanal anatomisi – şema ve MR", alt="Alshoabi ve ark., Diagnostics 2026", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC13512459", "g001"), ("pmc", "PMC13512459", "g002")], yatay=True,
   lejant=["Şema: **R** rektum; **AR** anorektal birleşim; **D** linea dentata; **AC** canalis analis; **A** anal kenar; **IAS/EAS** iç/dış anal sfinkter; **PR** m. puborectalis; **LA** m. levator ani; 1–4 fistül tipleri",
           "MR (yüksek çözünürlüklü T2): **AC** canalis analis; **IRF** fossa ischiorectalis (ischioanalis); **R** rektum; **UB** mesane"],
   noktalar=["MR; iç ve dış sfinkteri, puborektal kası, levator ani'yi, intersfinkterik boşluğu ve fossa ischioanalis'i açıkça gösterir.", "Suprasfinkterik fistüller puborektal kasın üstünden geçip levator ani'yi delerek fossa ischioanalis'e iner."]),
 dict(tip="gorsel", baslik="Anal sfinkterler – endoanal ve transperineal ultrason", alt="Carter ve ark., Diagnostics 2023 – 108 hasta", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC9955566", "g001")],
   lejant=["**EAUS** endoanal US (sol); **PUS** transperineal US (sağ); **EAS** dış anal sfinkter (hiperekoik halka); **IAS** iç anal sfinkter (hipoekoik halka)"],
   noktalar=["İç sfinkter düz kas olduğu için hipoekoik, dış sfinkter hiperekoik görülür.", "Fekal inkontinanslı 108 hastada iki yöntem arasında yırtık tanısında uyum %83 (κ = 0,62)."]),
 dict(tip="gorsel", baslik="N. pudendus'un MR'da seyri – canalis pudendalis", alt="Gaeta ve ark., Diagnostics 2026", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC12840153", "g001")],
   lejant=["Dört düzeyde aksiyel T1 MR: (a) m. piriformis önünde lumbosakral (siyah ok) ve pudendal (ok başı) pleksus; (b) spina ischiadica düzeyi; (c) m. obturatorius internus'a komşu pudendal damar–sinir demeti (Alcock kanalı); (d) perine düzeyi"],
   noktalar=["Kronik pudendal nevraljili 81 hastanın 42'sinde DWI anormalliği saptanmıştır.", "Damar–sinir demeti Alcock kanalında m. obturatorius internus'a yakın seyreder – sıkışma noktası."]),
 dict(tip="gorsel", baslik="Perine kasları ve perine cismi – MR", alt="Rotstein ve ark., Acta Obstet Gynecol Scand 2026 – 148 nulligravid kadın", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC13308972", "g001")],
   lejant=["Aksiyel (1) ve koronal (2): **a** puboperineal yapışma; **b** m. transversus perinei profundus; **c** m. transversus perinei superficialis; **d** dış anal sfinkter; **e** iç anal sfinkter"],
   noktalar=["Perine cismi: ortalama uzunluk 17,5 ± 3,0 mm, ön-arka yükseklik 9,7 ± 1,4 mm, alan 120 ± 28 mm².", "Normal değerler, doğum hasarının değerlendirilmesinde referans sağlar."]),
]

VAR_TABLO = [
 ["N. pudendus gövde tipleri", "Ranjan ve ark. 2022", "26 kadavra, 52 hemipelvis", "Tek gövde %51,9; Tip IIa %13,5; IIb %23,1; Tip III %11,5", "Pudendal blok ve dekompresyon"],
 ["N. pudendus kökleri ve gövdeleri (sistematik derleme)", "Yang ve ark. 2026", "509 / 645 örnek", "S2–S4 kökeni %54,62; tek gövde %47,60, çoklu %52,40", "Nöromodülasyon, cerrahi"],
 ["N. pudendus oluşumu (S3–S4) ve gövdeler", "Suganya ve ark. 2025 (CC BY-NC)", "10 kadavra", "Kesit alanı m. piriformis'te 4,04 mm² → Alcock'ta 0,35 mm²", "Sıkışma noktaları"],
 ["A. pudenda interna – a. rectalis media ortak gövdesi", "Badagabettu ve ark. 2025", "80 erkek hemipelvis", "Dal varyasyonu %61; ortak gövde %24; a. glutea inferior varyasyonu %18", "Embolizasyon, pelvis cerrahisi"],
 ["Levator ani (puborektal) avülsiyonu", "Yan ve ark. 2017", "80 doğum sonrası kadın", "Puborektal avülsiyon %13,75", "Prolapsus, inkontinans"],
 ["Perine cismi boyutları", "Rotstein ve ark. 2026", "148 nulligravid kadın (MR)", "Uzunluk 17,5 ± 3,0 mm; alan 120 ± 28 mm²", "Doğum hasarı değerlendirmesi"],
 ["Perineal herni (translevator)", "Coalter ve ark. 2022", "Olgu", "Literatürde ~100 posterior perineal herni olgusu", "Nadir pelvis tabanı defekti"],
]

VAR_CAL = [
 dict(baslik="Varyasyon: N. pudendus'un gövde tipleri", alt="Ranjan ve ark., Cureus 2022 – 26 kadavra", etiket="VARYASYON",
   figs=[("pmc", "PMC9492552", "i01"), ("pmc", "PMC9492552", "i03")], yatay=True,
   lejant=["**PN(I)** tek gövdeli n. pudendus; **PN(IIa)** iki gövdeli; **IPV** a./v. pudenda interna; **SN** n. ischiadicus; **SSL** lig. sacrospinale"],
   noktalar=["Tip I (tek gövde) %51,9; Tip IIa %13,5; Tip IIb %23,1; Tip III (üç gövde) %11,5.", "Şekil altyazısı ile özet arasında delen dalın adı tutarsızdır (n. rectalis inferior / n. gluteus inferior) – dikkatle alıntılanmalıdır."]),
 dict(baslik="Varyasyon: N. pudendus kökleri ve gövdeleri – sistematik derleme", alt="Yang ve ark., Eur Urol Open Sci 2026", etiket="VARYASYON",
   figs=[("pmc", "PMC12908042", "gr3"), ("pmc", "PMC12908042", "gr4")], yatay=True,
   lejant=["Sol: kök kombinasyonları ve yüzdeleri (S2–S4 %54,62; S2–S3 %33,60; S3–S4 %8,84 …)", "Sağ: spina ischiadica yakınında tek/çift/üçlü/dörtlü gövde şemaları; Sacrotuberous / Sacrospinous ligament"],
   noktalar=["509 örnekte S2–S4 kökeni %54,62.", "645 örnekte tek gövde %47,60, çoklu gövde %52,40; çoklu gövdelerin %38,93'ü çift, %12,76'sı üçlü."]),
 dict(baslik="Varyasyon: N. pudendus'un S3–S4'ten oluşumu", alt="Suganya ve ark., Anat Cell Biol 2025 – 10 kadavra", etiket="VARYASYON",
   figs=[("pmc", "PMC12519013", "f2")],
   lejant=["**PN** n. pudendus (yeşil); **LST** truncus lumbosacralis; S1–S4 kökler; 1–4 gövdeler; (A) S3–S4 oluşumu, (B–D) 2, 3 ve 4 gövdeli varyantlar"],
   noktalar=["Kesit alanı m. piriformis düzeyinde 4,04 mm², Alcock kanalında 0,35 mm².", "Cinsiyet ve taraf farkı anlamlı değil."]),
 dict(baslik="Varyasyon: A. pudenda interna ve a. rectalis media ortak gövdesi", alt="Badagabettu ve ark., J Vasc Bras 2025 – 80 erkek hemipelvis", etiket="VARYASYON",
   figs=[("pmc", "PMC11961128", "g06")],
   lejant=["**IIA** a. iliaca interna ön divisiosu; **IIV** v. iliaca interna; **MUL** lig. umbilicale mediale; **EIV** v. iliaca externa; **SVA/IVA** a. vesicalis superior/inferior; **CT** ortak gövde; **MRA** a. rectalis media; **IGA** a. glutea inferior; **IPA** a. pudenda interna; **UB** mesane; **R** rektum"],
   noktalar=["Dallanma varyasyonu hemipelvislerin %61'inde.", "A. pudenda interna + a. rectalis media ortak gövdesi %24; a. glutea inferior varyasyonu %18."]),
 dict(baslik="Varyasyon / hasar: Levator ani avülsiyonu", alt="Yan ve ark., Sci Rep 2017 – 80 doğum sonrası kadın", etiket="VARYASYON",
   figs=[("pmc", "PMC5593956", "Fig1"), ("pmc", "PMC5593956", "Fig3")], yatay=True,
   lejant=["Tomografik US: PUBIS; **PR** m. puborectalis; **LUG** levator–üretra aralığı; 2,5 mm aralıklı kesitler", "**U** urethra; **V** vagina; **R** rektum; **OB** m. obturatorius; **IC** m. iliococcygeus"],
   noktalar=["Vajinal doğumdan 45–60 gün sonra puborektal avülsiyon %13,75.", "İliokoksigeal hasar US ile zor saptanır ve çoğunlukla ağır puborektal hasarla birliktedir."]),
 dict(baslik="Klinik: Translevator perineal herni", alt="Coalter ve ark., BJR Case Rep 2022", etiket="VARYASYON",
   figs=[("pmc", "PMC9668258", "g004"), ("pmc", "PMC9668258", "g003")], yatay=True,
   lejant=["Şema: Bulbospongiosus; Ischiocavernosus; Superficial & deep perinei; Levator ani; External anal sphincter; **A** ön, **P** arka perineal herni", "MR: kırmızı ok sol lateral rektum duvarının Richter tipi hernisi; sarı ok levator ani'de 22 mm defekt"],
   noktalar=["Perineal herniler m. transversus perinei'ye göre ön ve arka olarak sınıflanır.", "Literatürde yaklaşık 100 arka perineal herni olgusu bildirilmiştir."]),
]

KLINIK = dict(tip="klinik", baslik="Perine – klinik bağlantılar", alt="Topografinin klinik karşılıkları",
   metin=["**Epizyotomi:** orta hat insizyonu perine cismini keser ve 3.–4. derece yırtığa uzayabilir; mediolateral insizyon sfinkterden uzaklaşır ama bulbus vestibuli ve perineal sinir dallarına yaklaşır.",
          "**Pudendal blok ve pudendal nevralji:** spina ischiadica / lig. sacrospinale ve Alcock kanalı ana referans ve sıkışma noktalarıdır.",
          "**Anal fistül ve apse:** sınıflama sfinkter katmanlarına göre yapılır; fossa ischioanalis'te at nalı yayılım.",
          "**Pelvis tabanı yetmezliği:** levator avülsiyonu, genişlemiş hiatus → prolapsus ve inkontinans.",
          "**Fasyal yayılım:** idrar ekstravazasyonu ve Fournier gangreni Colles–Scarpa planını izler.",
          "**Rektum kanseri cerrahisi:** mezorektal fasya ve Denonvilliers fasyası doğru düzlemi; kavernöz sinirler ereksiyonun korunmasını belirler."])

def build():
    prs = new_deck(); sayfa = 1; kul = []
    kapak(prs, "Perine ve Pelvis", "Perine odaklı topografik ve kesitsel anatomi – fasyalar ayrıntılı",
          ["Pelvis tabanı → fasyalar ve keseler → ürogenital ve anal bölgeler → kesitler → varyasyonlar",
           "Gerçek kadavra diseksiyonları, histoloji ve MR/US görüntüleri (PMC açık erişim)",
           "NLM Visible Human erkek ve kadın kesitleri (aynı kadavranın BT'si ile)"],
          [("pmc", "PMC12229694", "Fig1"), ("img", "perine/images/vhp/M1900_cryo.jpg", ""), ("pmc", "PMC13069139", "g001"), ("img", "perine/images/vhp/F1860_cryo.jpg", "")])
    sayfa += 1
    icindekiler(prs, BOLUMLER, None, sayfa); sayfa += 1
    sayfa += duzyazi(prs, GIRIS_DZ, sayfa, "GİRİŞ")
    def isle(liste, etk):
        nonlocal sayfa, kul
        for d in liste:
            t = d.get("tip", "gorsel")
            f = {"duzyazi": duzyazi, "anlatim": anlatim, "klinik": anlatim, "tablo": tablo, "gorsel": gorsel, "katman": katman_semasi, "kesit": kesit_paneli}[t]
            sayfa += f(prs, d, sayfa, etk)
            kul += [r[1] for r in d.get("figs", []) if r[0] == "pmc"]
    kap = {0: [("pmc", "PMC7182620", "Fig1")], 1: [("pmc", "PMC12229694", "Fig7")], 2: [("pmc", "PMC7913006", "g003")],
           3: [("pmc", "PMC13512459", "g001")], 4: [("img", "perine/images/vhp/M1934_cryo.jpg", "VHP-M kesit 1934")]}
    for i, (b, liste) in enumerate(zip(BOLUMLER[:4], [TABAN, FASYA, UROG, ANAL])):
        sayfa += bolum_kapak(prs, i + 1, b, kap[i], sayfa)
        isle(liste, f"BÖLÜM {i + 1} · {b['ad']}")
    b = BOLUMLER[4]; etk = f"BÖLÜM 5 · {b['ad']}"
    sayfa += bolum_kapak(prs, 5, b, kap[4], sayfa)
    sayfa += duzyazi(prs, dict(baslik="Pelvis ve perine kesitlerini okumak", alt="Erkek ve kadın Visible Human",
        paragraflar=["Pelvis kesitlerinde yönümüzü kemiklerle buluruz: yukarıda caput femoris ve acetabulum, aşağıda symphysis pubica, ramus ischiopubicus ve tuber ischiadicum. Orta hatta önden arkaya erkekte mesane–prostat–rektum, kadında mesane/urethra–vagina–rektum sıralanır.",
                     "Kaslardan m. obturatorius internus pelvis duvarını, m. levator ani ise organların etrafındaki ince huniyi oluşturur. İkisinin arasında aşağıda genişleyen yağ dokusu fossa ischioanalis'tir. Kesitler aşağı indikçe ürogenital üçgen öne, anal üçgen arkaya ayrılır; en altta yüzeyel kesedeki erektil dokular görülür.",
                     "Aşağıdaki kesitlerde aynı kadavranın aynı düzeydeki BT görüntüsü de verilmiştir: kas, yağ ve kemiğin kriyokesitteki gerçek görünümü ile radyolojik görünümünü doğrudan karşılaştırabilirsiniz."]), sayfa, etk)
    for d in KESITLER:
        sayfa += kesit_paneli(prs, d, sayfa, etk)
    sayfa += duzyazi(prs, dict(baslik="Perinede varyasyonlar neden önemli?", alt="Literatür taramasına giriş",
        paragraflar=["Perinede en önemli varyasyonlar damar ve sinirlerle ilgilidir. N. pudendus'un tek bir gövde yerine iki, üç hatta dört gövde halinde seyredebilmesi, pudendal blokların başarısızlığını veya pudendal nevralji cerrahisinde beklenmedik bulguları açıklayabilir.",
                     "A. iliaca interna'nın dallanma şekli de son derece değişkendir; a. pudenda interna'nın başka arterlerle ortak gövde yapması embolizasyon ve pelvis cerrahisinde önem taşır. Pelvis tabanı ise doğumla birlikte yapısal olarak değişir; levator avülsiyonu ve perine cismi boyutları bu açıdan güncel görüntüleme çalışmalarıyla değerlendirilmektedir."]), sayfa, etk)
    sayfa += lit_tablo(prs, "Perine varyasyonları – literatür taraması", "Kadavra, görüntüleme ve sistematik derleme çalışmaları (PMC açık erişim)", VAR_TABLO, sayfa, etk)
    isle([dict(d, tip="gorsel") for d in VAR_CAL], etk)
    isle([KLINIK], etk)
    s = yeni_slayt(prs); title_bar(s, "Sınırlılıklar")
    bullets(s, 0.45, 1.3, 12.4, 5.5, ["Colles, Scarpa, dartos ve Buck fasyasını doğrudan gösteren açık lisanslı kadavra fotoğrafı veya histoloji bulunamadı; bu fasyalar katman şeması, BT (Fournier) ve MR (penis) üzerinden anlatıldı.",
        "Alcock kanalının açılmış diseksiyon fotoğrafı ve pudendal blok ultrason anatomisi için açık lisanslı görsel bulunamadı.",
        "Bazı görseller CC BY-NC lisanslıdır (slaytlarda işaretli) – yalnızca ticari olmayan eğitim amaçlı.",
        "VHP kesitlerindeki etiketler gözle tanımlanmıştır; kesit eğikliği ve kadavra değişiklikleri nedeniyle bir anatomi öğretim üyesince gözden geçirilmelidir."], size=17)
    footer(s, "", sayfa); fix_runs(s); sayfa += 1
    sayfa = kaynakca(prs, kul, "Kaynakça ve görsel lisansları", sayfa)
    out = ROOT / "perine" / "Perine_Pelvis.pptx"; prs.save(out); print(out, len(prs.slides), "slayt")

if __name__ == "__main__":
    build()
