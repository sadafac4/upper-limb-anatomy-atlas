#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baş–Boyun Kesitsel Anatomi (Türkçe, Latince terimler).
VHP-M kriyokesit + aynı NLM numaralı donmuş BT + (≤1165) aynı numaralı MR; literatürden MR/BT/US ve varyasyonlar.
Önce: scripts/vhp_basboyun.py. Çıktı: basboyun/Bas_Boyun_Kesitsel.pptx"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from slayt_tipleri import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
BV = ROOT / "basboyun" / "images" / "vhp"
VK = ("Kaynak: NLM Visible Human Male – kriyokesit a_vm{n}, donmuş BT c_vm{n}.fro{mr}; NCI Imaging Data Commons (doi:10.5281/zenodo.12690049); "
      "NLM Terms and Conditions (2019). Radyolojik yönelim (ön yukarıda, hastanın sağı solda).")

def vk(n, b, alt, et, notlar):
    mr = (BV / f"t2_{n}.png").exists()
    pan = [(BV / f"ct_{n}.png", "Donmuş BT, aynı kesit no.")]
    pan.append((BV / f"t2_{n}.png", "MR (T2), aynı NLM kesit no.") if mr else (BV / f"ctbone_{n}.png", "Aynı BT, kemik penceresi"))
    return dict(tip="kesit", baslik=b, alt=f"{alt} – NLM kesit no. {n}", cryo=BV / f"cryo_{n}.jpg", etiketler=et, paneller=pan, notlar=notlar,
                kaynak=VK.format(n=n, mr=f", MR m_vm{n}" if mr else ""))

BOLUMLER = [
 dict(ad="BEYİN", baslik="Beyin ve kafatası", alt="Hemisferler, ventriküller, beyin sapı, serebellum", konular=["Okuma rehberi", "VHP düzeyleri 1060–1125", "Beyin sapı ve hipokampus MR'ı", "Kranial sinirler", "Varyasyonlar: Willis, CSP, perivasküler boşluklar"]),
 dict(ad="KAFA TABANI", baslik="Kafa tabanı, orbita, sinüsler", alt="Foramenler, orbita, paranazal sinüsler, temporal kemik", konular=["Okuma rehberi", "VHP düzeyleri 1125–1140", "Foramenler, kemikçikler, orbita, sinüs BT", "Varyasyonlar: Keros, konka bülloza, Onodi/Haller"]),
 dict(ad="YÜZ–FARİNKS", baslik="Yüz, ağız ve farinks", alt="Derin yüz boşlukları ve tükürük bezleri", konular=["Okuma rehberi", "VHP düzeyleri 1165–1200", "Orofarinks, ağız tabanı, parotis MR'ı", "Varyasyonlar: stiloid, aksesuar parotis, 'kissing' karotis"]),
 dict(ad="BOYUN", baslik="Boyun", alt="Larinks, tiroid, fasyalar ve karotis kılıfı", konular=["Okuma rehberi", "VHP düzeyleri 1230–1260", "Boyun US'si, fasyalar", "Varyasyonlar: arkus aorta, karotis bifurkasyonu, piramidal lob"]),
]

GIRIS = dict(baslik="Baş ve boyunda kesitsel anatomi", alt="Küçük bir alanda yoğun anatomi",
  paragraflar=[
   "Baş ve boyun, vücudun en yoğun anatomik bölgesidir: birkaç santimetrelik bir kesitte beyin, kafa tabanı foramenleri, orbita, sinüsler, çiğneme kasları, farinks, büyük damarlar ve kranial sinirler bir arada bulunabilir. Bu nedenle kesit okurken düzeyi doğru belirlemek her şeyden önce gelir.",
   "Kafa içinde düzeyi ventriküller ve bazal çekirdekler belirler: lateral ventriküllerin gövdesi, foramen interventriculare ve üçüncü ventrikül, beyin sapının mezensefalon, pons ve medulla oblongata düzeyleri. Kafa tabanında orbita, sfenoid sinüs ve temporal kemik; yüzde maksiller sinüs, sert damak ve mandibula; boyunda ise hyoid kemik, kıkırdak larinks ve vertebralar yol göstericidir.",
   "Bu sunumda Visible Human erkek kadavrasının baş–boyun kesitlerini, aynı kadavranın aynı numaralı BT'si ve baş bölgesinde aynı numaralı MR görüntüsüyle birlikte göreceğiz. MR ile kriyokesit arasındaki uyum o kadar iyidir ki, girus ve sulkusların deseni iki görüntüde birebir izlenebilir. Literatürden eklenen MR, BT ve ultrason görüntüleri klinik görüntülemeyi; bölüm sonlarındaki varyasyon çalışmaları ise bu bölgedeki bireysel farklılıkları gösterecektir."])

BEYIN = [
 dict(tip="duzyazi", baslik="Beyin kesitlerini okumak", alt="Gri cevher, beyaz cevher ve BOS boşlukları",
   paragraflar=["Aksiyel beyin kesitinde ilk dikkati çeken, korteksin gri cevheri ile altındaki beyaz cevher arasındaki sınırdır. Kriyokesitte gri cevher kahverengimsi, beyaz cevher krem rengindedir; T1 MR'da beyaz cevher daha parlak, T2'de ise daha koyudur. BT'de bu ayrım çok daha silik olup beyin omurilik sıvısı (BOS) koyu görülür.",
                "Yukarıdan aşağıya inerken önce iki hemisferi ayıran fissura longitudinalis ve centrum semiovale görülür. Daha aşağıda lateral ventriküllerin ön boynuzları, aralarında septum pellucidum ve corpus callosum, yanlarda nucleus caudatus ve lentiform çekirdek belirir. Ardından talamuslar, üçüncü ventrikül, mezensefalon ve en altta pons ile serebellum gelir.",
                "Kafatasının hemen içinde dura mater ve venöz sinüsler yer alır; arka orta hatta sinus sagittalis superior kesitte üçgen bir boşluk olarak görülür. Kafatasının dışında ise yanlarda m. temporalis kası bulunur."]),
 vk(1060, "Beyin – centrum semiovale düzeyi", "Lateral ventriküllerin üstü", [
     ("Sinus frontalis", (210, 85), "L"), ("Substantia alba (centrum semiovale)", (160, 250), "L"), ("Sinus sagittalis superior", (258, 565), "L"),
     ("Fissura longitudinalis cerebri", (255, 300), "R"), ("Cortex cerebri (gyri ve sulci)", (390, 300), "R")],
    ["MR ile kriyokesitteki girus deseninin birebir örtüşmesi, kesitlerin gerçekten aynı düzeyde olduğunu gösterir.", "T2 MR'da sulkuslardaki BOS parlak, kriyokesitte ince kırmızı damarlarla izlenir."]),
 vk(1080, "Beyin – lateral ventriküller ve corpus callosum", "Foramen interventriculare'nin üstü", [
     ("Sinus frontalis", (250, 95), "L"), ("Genu corporis callosi", (285, 238), "L"), ("M. temporalis", (70, 320), "L"), ("Sinus sagittalis superior", (265, 595), "L"),
     ("Cornu frontale ventriculi lateralis", (262, 290), "R"), ("Septum pellucidum", (290, 300), "R"), ("Cornu occipitale ventriculi lateralis", (330, 425), "R")],
    ["Kadavrada ventriküller kısmen kollabe olduğundan ince yarıklar şeklindedir; MR'da BOS ile dolu olarak görülür.", "Corpus callosum iki hemisferi bağlayan en büyük komissürdür (genu önde, splenium arkada)."]),
 vk(1095, "Beyin – talamus ve orbita tavanı düzeyi", "Diensefalon düzeyi", [
     ("Bulbus oculi", (180, 150), "L"), ("M. temporalis", (95, 300), "L"), ("Lobus temporalis", (110, 430), "L"),
     ("Cellulae ethmoidales", (265, 110), "R"), ("Thalamus", (315, 355), "R"), ("Splenium corporis callosi", (270, 428), "R"), ("Cornu occipitale / atrium", (340, 462), "R")],
    ["Talamuslar üçüncü ventrikülün iki yanındadır; arkalarında corpus callosum'un splenium'u bulunur.", "Bu düzeyde ön tarafta orbitalar ve etmoid hücreler, kafatası dışında m. temporalis izlenir."]),
 dict(tip="duzyazi", baslik="Beyin sapı ve serebellum", alt="Arka çukurun içeriği",
   paragraflar=["Fossa cranii posterior'da beyin sapı ve serebellum yer alır. Beyin sapı yukarıdan aşağıya mezensefalon, pons ve medulla oblongata olarak üç bölümdür. Mezensefalonda substantia nigra ve nucleus ruber, ponsta kalın transvers lifler, medullada ise olivalar ve piramitler kesitlerde ayırt edilir.",
                "Ponsun ve medullanın arkasında dördüncü ventrikül, onun da arkasında serebellum bulunur. Serebellum ince ve paralel foliaları ile kriyokesitte kolayca tanınır; ortada vermis, yanlarda hemisferler vardır. Kranial sinirlerin III–XII çiftleri beyin sapından çıkar ve sisternalarda seyrederek kafa tabanı foramenlerine yönelir."]),
 vk(1125, "Arka çukur – pons ve serebellum", "Sfenoid sinüs düzeyi", [
     ("Sinus maxillaris", (225, 200), "L"), ("M. temporalis", (130, 250), "L"), ("Cerebellum (hemisphaerium)", (215, 520), "L"), ("Auricula", (60, 450), "L"),
     ("Cavitas nasi", (300, 160), "R"), ("Sinus sphenoidalis", (305, 310), "R"), ("Pons", (305, 405), "R")],
    ["Ponsun arkasında serebellum foliaları kriyokesitte belirgindir.", "Kesit hafif eğik olduğundan sağda serebellum, solda temporal/oksipital lob dokusu görülmektedir."]),
 dict(tip="gorsel", baslik="Beyin sapı – 7T MR ve histoloji karşılaştırması", alt="Donatelli ve ark., Eur Radiol Exp 2023", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC10651583", "Fig1"), ("pmc", "PMC10651583", "Fig3")], yatay=False,
   lejant=["Üst: nucleus ruber düzeyi (rostral mezensefalon); alt: pedunculus cerebellaris superior düzeyi (rostral pons). a–b ex vivo PD ve T2* MR, c Perls (demir) / Weigert-Pal (miyelin) boyası, d–f in vivo 7T T2*, duyarlılık ve frekans haritaları. Numaralar çekirdek ve yolları gösterir (anahtar makalede)."],
   noktalar=["46 yaşındaki gönüllüde 7T MR (0,3 × 0,3 × 1,2 mm³) ile aynı düzeyde boyanmış kadavra beyin sapı karşılaştırılmıştır.", "Demir içeren çekirdekler (nucleus ruber, substantia nigra) T2* ve duyarlılık haritalarında belirgindir."]),
 dict(tip="gorsel", baslik="Hipokampus – 3T MR anatomisi", alt="Dekeyzer ve ark., Insights Imaging 2017", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC5359145", "Fig1"), ("pmc", "PMC5359145", "Fig2")], yatay=True,
   lejant=["**1** caput hippocampi; **2** corpus; **3** cauda; **CA1–CA4** cornu ammonis sektörleri; **DG** gyrus dentatus; **Sub** subiculum; **PHG** gyrus parahippocampalis; **HS** hipokampal kist; **ChF** fissura choroidea; **T** cornu temporale"],
   noktalar=["Hipokampus, cornu ammonis (CA1–CA4) ve gyrus dentatus'tan oluşur.", "Temporal lob epilepsisi ve demanslarda koronal T2 MR temel değerlendirme düzlemidir."]),
 dict(tip="gorsel", baslik="Kranial sinirlerin sisternal segmentleri", alt="Romano ve ark., Insights Imaging 2019", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC6420596", "Fig1")],
   lejant=["Aksiyel SSFP MR: (a) I – n. olfactorius (daireler); (b) II – n. opticus; (c) III – n. oculomotorius; (d) IV – n. trochlearis; (e) V – n. trigeminus; (f) VI – n. abducens; (g) VII ve VIII – n. facialis ve n. vestibulocochlearis; (h) IX–X; (i) XI; (j) XII"],
   noktalar=["SSFP sekansı BOS içindeki ince sinirleri yüksek kontrastla gösterir.", "MR kranial sinirlerin değerlendirilmesinde altın standarttır."]),
 dict(tip="gorsel", baslik="Serebellum – sagital diseksiyon", alt="Tamanini ve ark., Arq Neuropsiquiatr 2025", etiket="DİSEKSİYON",
   figs=[("pmc", "PMC12721976", "-3")],
   lejant=["Midbrain = mesencephalon; Pons; IV ventricle = ventriculus quartus; Medulla oblongata; Superior / Inferior vermis; Primary fissure = fissura prima; Cortex; White matter = substantia alba (arbor vitae)"],
   noktalar=["Her hemisfer iki transvers fissürle üç loba ayrılır: fissura prima ön ve arka lobu, fissura posterolateralis arka lob ile flokülonodüler lobu ayırır.", "Lobuller Schmahmann nomenklatürüne göre I–X olarak numaralandırılır."]),
]

BEYIN_VAR_T = [
 ["Willis poligonu varyasyonları (BTA)", "Machasio ve ark. 2019", "94 hasta", "Tam poligon %37,2; fetal PCA %25,5 (ajan raporu)", "Kollateral dolaşım, inme riski"],
 ["Genişlemiş perivasküler boşluklar", "Lara ve ark. 2022", "3710 kişi (Framingham)", "Derece I–IV; <60 yaşta yüksek yük %10'un altında", "Küçük damar hastalığı ile ilişki"],
 ["Cavum septi pellucidi", "Rios ve ark. 2025", "410 genç erişkin MR", "%95,6 (manuel); otomatik yöntemle %57,1", "Normal varyant; büyükse nöropsikiyatrik ilişki"],
]
BEYIN_VAR = [
 dict(baslik="Varyasyon: Willis poligonu – BT anjiyografi", alt="Machasio ve ark., Radiol Res Pract 2019 – 94 hasta", etiket="VARYASYON",
   figs=[("pmc", "PMC6601480", "002"), ("pmc", "PMC6601480", "004")], yatay=True,
   lejant=["Sol: tam Willis poligonu (aksiyel MIP); sağ: bilateral fetal tip a. cerebri posterior ve sağ P1 aplazisi (şekillerde etiket yoktur)"],
   noktalar=["Tam poligon olguların %37,2'sinde (erkek %37,7, kadın %36,6).", "Fetal PCA'da arka serebral arter, baziler sistem yerine a. carotis interna'dan beslenir – inme dağılımını etkiler."]),
 dict(baslik="Varyasyon: Genişlemiş perivasküler (Virchow–Robin) boşluklar", alt="Lara ve ark., Aging 2022 – Framingham, 3710 kişi", etiket="VARYASYON",
   figs=[("pmc", "PMC9512514", "g002")],
   lejant=["Koronal T2 MR: üst sıra bazal ganglionlar, alt sıra centrum semiovale; (A) derece I (0–10), (B) II (10–20), (C) III (20–40), (D) IV (40+); beyaz oklar tek tek perivasküler boşluklar"],
   noktalar=["Yüksek yük (derece III–IV) 60 yaş altında bazal ganglionlarda %10'un altındadır.", "Genişlemiş boşluklar yaşla artar; normal varyant ile küçük damar hastalığı arasında yorum gerektirir."]),
 dict(baslik="Varyasyon: Cavum septi pellucidi", alt="Rios ve ark., Front Neuroanat 2025 – 410 genç erişkin", etiket="VARYASYON",
   figs=[("pmc", "PMC12131514", "g001"), ("pmc", "PMC12131514", "g002")], yatay=False,
   lejant=["Üst: küçük (A) ve büyük (B) cavum septi pellucidi 3B segmentasyonu (yeşil) orta sagital T1 üzerinde; alt: manuel (yeşil) ve otomatik (kırmızı) sınırlama"],
   noktalar=["CSP olguların **%95,6**'sında saptanmış; otomatik segmentasyonla yalnız %57,1.", "Erkeklerde hacim daha büyüktür; ortalama hacim 18,0 mm³."]),
]

KAFA = [
 dict(tip="duzyazi", baslik="Kafa tabanı, orbita ve sinüsleri okumak", alt="Kemik pencerede ince yapılar",
   paragraflar=["Kafa tabanı üç çukurdan oluşur: ön çukurda lamina cribrosa ve orbita tavanı, orta çukurda sella turcica ve sfenoid kemiğin büyük kanatları, arka çukurda ise klivus ve foramen magnum. Kafa tabanındaki foramenler kranial sinirlerin ve damarların geçiş yollarıdır; BT'de kemik pencerede bu kanallar doğrudan izlenir.",
                "Orbita konik bir boşluktur; içinde göz küresi, dört rektus ve iki oblik kas, n. opticus ve yağ dokusu bulunur. Orbitanın medial duvarı ince lamina papyracea ile etmoid hücrelerden ayrılır; bu ince duvar sinüs enfeksiyonlarının orbitaya yayılmasına izin verir.",
                "Paranazal sinüsler – maksiller, etmoid, frontal ve sfenoid – kriyokesitlerde mavi jelle dolu boşluklar olarak görülür. Maksiller sinüs ostiyomeatal kompleks aracılığıyla orta meatusa açılır. Sinüs cerrahisinden önce koronal BT'de olfaktör fossanın derinliği (Keros) ve Onodi, Haller hücreleri gibi varyasyonlar mutlaka değerlendirilir."]),
 vk(1140, "Kafa tabanı – maksiller sinüs ve temporal kemik", "Dördüncü ventrikül düzeyi", [
     ("Sinus maxillaris", (224, 235), "L"), ("Mm. masticatorii (m. pterygoideus, m. temporalis)", (195, 300), "L"), ("Cellulae mastoideae", (144, 470), "L"), ("Meatus acusticus externus", (94, 410), "L"),
     ("Septum nasi", (314, 180), "R"), ("Medulla oblongata / pons", (299, 465), "R"), ("Ventriculus quartus", (299, 487), "R"), ("Cerebellum", (390, 560), "R")],
    ["Maksiller sinüslerin arkasında çiğneme kasları, yanlarda kulak kepçesi ve meatus acusticus externus görülür.", "Temporal kemiğin mastoid hücreleri kriyokesitte mavi jelle dolmuştur."]),
 dict(tip="gorsel", baslik="Kafa tabanı foramenleri – BT", alt="Romano ve ark., Insights Imaging 2019", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC6420596", "Fig2")],
   lejant=["(a) lamina cribrosa (yıldız); (b) canalis opticus (yıldız) ve fissura orbitalis superior (ok); (c) foramen rotundum; (d) foramen ovale; (e) canalis facialis; (f) meatus acusticus internus; (g) foramen jugulare; (h) canalis hypoglossi"],
   noktalar=["BT, sinirlerin kemik içi segmentlerini ve geçtikleri foramenleri gösterir.", "Foramen ovale'den n. mandibularis (V3), foramen rotundum'dan n. maxillaris (V2), foramen jugulare'den IX–XI geçer."]),
 dict(tip="gorsel", baslik="Orta kulak kemikçikleri – 2B ve 3B BT", alt="Maillot ve ark., Insights Imaging 2016", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC4877355", "Fig2")],
   lejant=["**1** malleus; **2** incus'un uzun kolu; **3** stapes – aksiyel ve oblik düzlemde kemikçik 'V'si; b ve d 3B BT"],
   noktalar=["Kemikçik zinciri malleus–incus–stapes olarak ses titreşimini oval pencereye iletir.", "En sık orta kulak travmaları inkudomalleolar ve inkudostapedial eklem çıkıklarıdır."]),
 dict(tip="gorsel", baslik="Orbita – 3T MR ölçümleri", alt="Rana ve ark., Int Ophthalmol 2022 – 141 orbita", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC9617817", "Fig1"), ("pmc", "PMC9617817", "Fig2")], yatay=False,
   lejant=["Üst: aksiyel ve koronal T1 – m. rectus medialis/lateralis, üst kas grubu, m. rectus inferior ve v. ophthalmica superior çap ölçümleri (turuncu çizgiler); alt: n. opticus kılıf çapı (8,1 mm)"],
   noktalar=["Normal değerler: m. rectus medialis 4,1 ± 0,5 mm; lateralis 3,9 ± 0,7 mm; üst grup 4,5 ± 0,7 mm; inferior 4,6 ± 0,7 mm; v. ophthalmica superior 1,8 ± 0,7 mm.", "Tiroid oftalmopatisinde kas kalınlıkları bu referanslarla karşılaştırılır."]),
 dict(tip="gorsel", baslik="Paranazal sinüs BT anatomisi", alt="Ribeiro ve ark., Radiol Bras 2019", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC6472854", "g06"), ("pmc", "PMC6472854", "g13"), ("pmc", "PMC6472854", "g16")], yatay=True,
   lejant=["Sol: olfaktör fossalar (oklar) ~7,5 mm derinlikte – Keros tip 3; orta: sfenoetmoidal (Onodi) hücre (ok), n. opticus'a komşu (ok başı); sağ: orta konkanın lamellar ve bülböz kısmının havalanması (konka bülloza)"],
   noktalar=["Bu varyasyonların tanınması endoskopik sinüs cerrahisinde tedavi başarısızlığını ve iyatrojenik komplikasyonları önler.", "Onodi hücresi n. opticus ve a. carotis interna'ya yakın olabilir."]),
]
KAFA_VAR_T = [
 ["Keros sınıflaması", "Almushayti ve ark. 2022", "296 olfaktör fossa (BT)", "Tip I %28,4; Tip II %63,5; Tip III %8,1", "Tip III'te kafa tabanı yaralanma riski"],
 ["Sinüs anatomik varyasyonları", "Subbiah ve ark. 2025", "75 hasta (BT)", "Septum deviasyonu %66,6; büyük etmoid bulla %46,6; konka bülloza %40; agger nasi %26,6; Haller %20; Onodi %13", "Endoskopik sinüs cerrahisi planlaması"],
]
KAFA_VAR = [
 dict(baslik="Varyasyon: Keros sınıflaması", alt="Almushayti ve ark., Cureus 2022 – 296 olfaktör fossa", etiket="VARYASYON",
   figs=[("pmc", "PMC8935634", "i01")],
   lejant=["Fovea ethmoidalis; lateral lamella (lamina lateralis laminae cribrosae); lamina cribrosa; Type I / II / III"],
   noktalar=["Tip I %28,4, Tip II %63,5, Tip III %8,1; ortalama derinlik sağ 5,1 mm, sol 5,28 mm.", "Derin olfaktör fossa (Tip III) ince lateral lamel nedeniyle BOS kaçağı riski taşır."]),
 dict(baslik="Varyasyon: Orta konka havalanması", alt="Subbiah ve ark., Cureus 2025 – 75 hasta", etiket="VARYASYON",
   figs=[("pmc", "PMC12085865", "i02")],
   lejant=["Koronal BT: A lamellar tip; B bülböz tip; C yaygın tip (konka bülloza) – sarı oklar"],
   noktalar=["Konka bülloza %40; septum deviasyonu %66,6 ile en sık varyasyon.", "Agger nasi %26,6, Haller hücresi %20, Onodi hücresi %13."]),
]

YUZ = [
 dict(tip="duzyazi", baslik="Yüz ve farinksin derin boşlukları", alt="Fasyalarla sınırlı alanlar",
   paragraflar=["Yüzün derinliğindeki yapılar, boyun fasyalarının sınırladığı 'boşluklar' halinde düşünülür. Farinksin hemen lateralindeki parafaringeal boşluk, çevresindeki boşlukları (çiğneme, parotis, karotis) ayıran yağlı bir merkezdir; bir kitlenin bu yağı hangi yöne ittiği, kitlenin kökenini gösterir.",
                "Çiğneme (mastikatör) boşluğu ramus mandibulae ile m. masseter, m. pterygoideus medialis ve lateralis'i içerir. Parotis boşluğunda glandula parotidea, n. facialis'in bez içi dalları ve v. retromandibularis bulunur; n. facialis bezi yüzeyel ve derin loba ayırır.",
                "Ağız tabanında m. mylohyoideus, sublingual boşluğu (yukarıda) submandibular boşluktan (aşağıda) ayırır. Farinksin arkasında retrofaringeal boşluk ve onun da arkasında 'tehlike boşluğu' yer alır; buradaki enfeksiyonlar mediastene kadar yayılabilir."]),
 vk(1165, "Yüz – atlas ve dens axis düzeyi", "Sert damak / nazofarinks altı", [
     ("M. masseter", (465, 250), "R"), ("Auricula", (530, 450), "R"),
     ("Dens axis", (290, 375), "L"), ("Medulla spinalis", (290, 425), "L"), ("Ense kasları (mm. nuchae)", (250, 560), "L")],
    ["Dens axis atlasın ön kemeri ile eklem yapar; arkasında omurilik bulunur.", "Bu düzeyde VHP MR kesiti de mevcuttur: kas ve yağ dokusu ayrımı T2'de belirgindir."]),
 vk(1200, "Yüz – dil ve orofarinks", "Mandibula gövdesi düzeyi", [
     ("V. jugularis interna", (144, 365), "L"), ("Corpus vertebrae (C2–C3)", (269, 372), "L"), ("Ense kasları (m. splenius, m. semispinalis)", (164, 520), "L"),
     ("Arcus dentalis / mandibula", (274, 105), "R"), ("Lingua", (274, 220), "R"), ("Oropharynx", (269, 320), "R"), ("M. masseter", (424, 270), "R"), ("M. sternocleidomastoideus", (464, 400), "R")],
    ["Orofarinksin hava yolu dilin arkasında dar bir yarık şeklindedir.", "Karotis kılıfı içeriği (v. jugularis interna, a. carotis) m. sternocleidomastoideus'un derininde yer alır."]),
 dict(tip="gorsel", baslik="Orofarinks ve ağız boşluğunun MR anatomisi", alt="Hirvonen ve ark., Insights Imaging 2023", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC9826778", "Fig2"), ("pmc", "PMC9826778", "Fig3")], yatay=False,
   lejant=["Üst (aksiyel T2): beyaz yıldız tonsilla palatina; ok m. constrictor pharyngis superior; kesikli ok m. palatoglossus; noktalı ok m. palatopharyngeus",
           "Alt (koronal T2): ok m. mylohyoideus; siyah yıldız glandula sublingualis; sublingual (üstte) ve submandibular (altta) boşluklar"],
   noktalar=["Retrofaringeal boşluk önde m. constrictor superior ve bukkofaringeal fasya, arkada prevertebral fasya ile sınırlıdır.", "Retrofaringeal boşluk üst torakal düzeyde sonlanır; tehlike boşluğu ise mediastene açılır."]),
 dict(tip="gorsel", baslik="Çocukta orofarinks ve Rouvière lenf düğümleri", alt="Nurminen ve ark., Children 2023", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC10296820", "g001"), ("pmc", "PMC10296820", "g003")], yatay=True,
   lejant=["Sol: 12 yaş – tonsilla palatina (yıldız), m. constrictor superior (ok), m. palatopharyngeus (noktalı ok başı); sağ: 2 yaş – lateral retrofaringeal (Rouvière) lenf düğümleri (oklar)"],
   noktalar=["Çocuklarda boyun enfeksiyonlarının tipi ve anatomisi erişkinden farklıdır.", "Rouvière düğümleri retrofaringeal apsenin çıkış noktasıdır."]),
 dict(tip="gorsel", baslik="Parotis ve submandibular boşluk", alt="Kessler ve ark., J Clin Imaging Sci 2018", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC6251248", "g002"), ("pmc", "PMC6251248", "g004")], yatay=False,
   lejant=["Üst: Deep / Superficial parotid gland = parotis derin / yüzeyel lobu; Intraparotid facial nerve; Retromandibular vein; External carotid artery (çizim, BT, T2 MR)",
           "Alt: Sublingual space; Submandibular space; Mylohyoid cleft; Genioglossus; Sublingual gland; Lingual artery"],
   noktalar=["Parotis boşluğu mastikatör boşluğun posterolateralinde, parafaringeal boşluğun lateralindedir.", "N. facialis gerçek bir fasyal düzlem olmamakla birlikte bezi yüzeyel ve derin bölüme ayırır.", "Lisans: CC BY-NC-SA."]),
]
YUZ_VAR_T = [
 ["Uzun processus styloideus (KIBT)", "Yang ve ark. 2024", "498 kişi", "Sol uzun stiloid kadınlarda %24,13, erkeklerde %41,91 (≥30 mm)", "Eagle sendromu"],
 ["Aksesuar parotis bezi / fasiyal uzantı", "Ahn ve ark. 2017", "1600 BT", "Aksesuar bez %10,2; fasiyal uzantı %28,3", "Yanak kitlesi ayırıcı tanısı"],
 ["'Kissing' karotisler (retrofaringeal ICA)", "Muñoz ve ark. 2010 (CC BY-NC)", "5500 BT", "%0,2 (14 hasta); bilateral %43", "Farinks cerrahisinde ölümcül kanama riski"],
]
YUZ_VAR = [
 dict(baslik="Varyasyon: Uzun processus styloideus", alt="Yang ve ark., BMC Med Imaging 2024 – 498 kişi (KIBT)", etiket="VARYASYON",
   figs=[("pmc", "PMC11622470", "Fig1"), ("pmc", "PMC11622470", "Fig8")], yatay=True,
   lejant=["Sol: stiloid uzunluğu ölçümü (18,52 mm ve 16,08 mm); sağ: cinsiyete göre dağılım, 30 mm eşik (kırmızı kesikli çizgi)"],
   noktalar=["Sol tarafta uzun stiloid: kadınlarda %24,13, erkeklerde %41,91; sağda %29,18 ve %37,34.", "Erkeklerde stiloid her iki tarafta anlamlı olarak daha uzun.", "Klinik: Eagle sendromu (boğaz ağrısı, yutma güçlüğü, karotis basısı)."]),
 dict(baslik="Varyasyon: Aksesuar parotis bezi ve fasiyal uzantı", alt="Ahn ve ark., PLoS ONE 2017 – 1600 BT", etiket="VARYASYON",
   figs=[("pmc", "PMC5600370", "g001"), ("pmc", "PMC5600370", "g002")], yatay=True,
   lejant=["Sol: ana bezden ayrı, m. masseter üzerinde aksesuar parotis (ok); sağ: ramus mandibulae ön kenarını aşan, ana bezle devamlı fasiyal uzantı (ok)"],
   noktalar=["Aksesuar bez %10,2, fasiyal uzantı %28,3; aksesuar bezin ortalama boyutu 15,8 × 5,0 mm.", "Yaşla aksesuar bez sıklığı azalır, fasiyal uzantı artar."]),
 dict(baslik="Varyasyon: Retrofaringeal seyirli a. carotis interna ('kissing carotids')", alt="Muñoz ve ark., Open Neuroimaging J 2010 – 5500 BT", etiket="VARYASYON",
   figs=[("pmc", "PMC3026334", "F3")],
   lejant=["Kontrastlı BT: her iki a. carotis interna retrofaringeal orta hatta yaklaşmış (oklar); vv. jugulares internae de medialize"],
   noktalar=["5500 hastada %0,2 (14 olgu); sağ %43, sol %14, bilateral %43.", "Olguların %28'i semptomatik; tonsillektomi ve farinks cerrahisi öncesi bilinmesi hayati önem taşır."]),
]

BOYUN = [
 dict(tip="duzyazi", baslik="Boyun: fasyalar ve boşluklar", alt="Üç yapraklı derin servikal fasya",
   paragraflar=["Boyun anatomisinin iskeleti, derin servikal fasyanın üç yaprağıdır. Yüzeyel (örtücü) yaprak boynu bir manşon gibi sarar ve m. sternocleidomastoideus ile m. trapezius'u kılıflar. Orta (pretrakeal) yaprak tiroid bezi, trakea, özofagus ve infrahyoid kasları çevreler. Derin (prevertebral) yaprak ise vertebralar ve onlara tutunan kasları örter.",
                "Bu üç yaprağın katkısıyla oluşan karotis kılıfı, a. carotis communis/interna, v. jugularis interna ve n. vagus'u içerir ve kafa tabanından aort kavsine kadar uzanır. Prevertebral yaprak ile retrofaringeal boşluk arasında alar fasya bulunur; alar fasyanın arkasındaki 'tehlike boşluğu' enfeksiyonların mediastene inmesine aracılık eder.",
                "Boyun kesitlerinde larinksin kıkırdakları (tiroid, krikoid, aritenoid), hyoid kemik ve tiroid bezi düzeyi belirlemede yol göstericidir. Ultrason, tiroid bezi ve boyun lenf düğümlerinin değerlendirilmesinde ilk basamak yöntemdir."]),
 vk(1230, "Boyun – os hyoideum ve laryngopharynx", "Hyoid düzeyi", [
     ("Glandula submandibularis", (185, 225), "L"), ("V. jugularis interna", (180, 320), "L"), ("Medulla spinalis", (305, 400), "L"),
     ("Os hyoideum", (300, 115), "R"), ("Laryngopharynx (hava yolu)", (300, 300), "R"), ("Corpus vertebrae", (305, 350), "R")],
    ["Hyoid kemik yaklaşık C3 düzeyindedir; dil kökü ve epiglotun önünde yer alır.", "Glandula submandibularis'in yüzeyel bölümü m. mylohyoideus'un altında, boynun üst kısmındadır."]),
 vk(1260, "Boyun kökü – larinks", "Tiroid kıkırdağı düzeyi (boyun bölgesine kırpılmış)", [
     ("Ense kasları (m. trapezius ve derin kaslar)", (80, 400), "L"), ("V. jugularis interna (lümen)", (132, 180), "L"),
     ("Cartilago thyroidea / larynx", (297, 130), "R"), ("A. carotis communis", (194, 168), "R"), ("Corpus vertebrae", (297, 270), "R")],
    ["Larinks tiroid kıkırdağının içinde, önde; arkasında hipofarinks ve vertebra yer alır.", "Karotis kılıfı larinksin posterolateralindedir."]),
 dict(tip="gorsel", baslik="Boyun ve larinks – ultrason", alt="Furukawa, J Med Ultrason 2022", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC9640455", "Fig1"), ("pmc", "PMC9640455", "Fig2")], yatay=True,
   lejant=["**SG** glandula submandibularis; **PG** glandula parotidea; **BIF** karotis bifurkasyonu; **TH** tiroid; **TR** trakea; **ES** özofagus; **LX** larinks; **HB** os hyoideum; **HP** hipofarinks; **CCA** a. carotis communis; **JV** v. jugularis interna; **VC** plica vocalis; **TC** cartilago thyroidea; **AR** cartilago arytenoidea; **EP** epiglottis"],
   noktalar=["Sistematik boyun US'si submandibular bölgeden tiroide kadar tüm yapıları sırayla tarar.", "Larinks US'si ses tellerinin hareketini ve hava yolunu değerlendirmede kullanılır."]),
 dict(tip="gorsel", baslik="Tiroid bezi – normal transvers ultrason", alt="Choi ve ark., Korean J Radiol 2014", etiket="GÖRÜNTÜLEME",
   figs=[("pmc", "PMC3955795", "g001")],
   lejant=["**SCM** m. sternocleidomastoideus; **CCA** a. carotis communis; **IJV** v. jugularis interna; Ant. strap m. = infrahyoid kaslar; Isthmus; Thyroid; Trachea; Longus colli m.; Esophagus"],
   noktalar=["Tiroid parankimi infrahyoid kaslardan daha ekojeniktir.", "Lateral loblar ~4–5 cm uzunluğunda, ~2 cm genişliğindedir; bireylerin ~%40'ında piramidal lob vardır (aktarılan)."]),
 dict(tip="gorsel", baslik="Alar fasya – çizim ve plastinasyon", alt="Phan ve ark., Cureus 2022 – 32 E12 plastinasyon kesiti", etiket="KESİT",
   figs=[("pmc", "PMC9868889", "i01"), ("pmc", "PMC9868889", "i02")], yatay=True,
   lejant=["Çizim (C6): ***** alar fasya; **RF** retrofaringeal fasya; **RS** retrofaringeal boşluk; **DS** tehlike boşluğu; **PVF** prevertebral fasya; **CS** karotis kılıfı; **SLDCF** derin servikal fasyanın yüzeyel yaprağı",
           "Plastinat (sagital, 4 mm): C1–C3; **AAL** lig. atlantoaxiale anterius; ***** alar fasya"],
   noktalar=["Alar fasya retrofaringeal boşluk ile tehlike boşluğu arasında gerçek bir fasyal tabakadır.", "Enfeksiyonun mediastene yayılmasına karşı fiziksel bir bariyer olabilir."]),
]
BOYUN_VAR_T = [
 ["Arkus aorta varyasyonları (BT)", "Pandalai ve ark. 2021", "4000 BT", "Varyasyon prevalansı %0,675; aberran sağ a. subclavia 7 olgu (%25,9 varyasyonlar içinde)", "Disfaji lusoria, cerrahi"],
 ["Karotis bifurkasyon düzeyi (BTA)", "Manta ve ark. 2024", "294 bifurkasyon", "C3 %27,21; C3/C4 %26,19; C4 %25,51; bilateral simetri %51,7", "Endarterektomi, boyun diseksiyonu"],
 ["Piramidal tiroid lobu", "Kim ve ark. 2015 (CC BY-NC)", "582 hasta (US + BT)", "US'de %39,5; BT'de %47,6", "Tiroidektomide rezidü doku"],
 ["Aberran sağ a. subclavia → non-rekürren larinks siniri", "Niu ve ark. 2016 (CC BY-NC)", "2697 hasta", "26 hasta (%0,96); hepsinde NRLN", "Tiroid cerrahisinde sinir yaralanması"],
]
BOYUN_VAR = [
 dict(baslik="Varyasyon: Arkus aorta dallanma varyasyonları", alt="Pandalai ve ark., Cureus 2021 – 4000 BT", etiket="VARYASYON",
   figs=[("pmc", "PMC7936046", "i01"), ("pmc", "PMC7936046", "i03")], yatay=False,
   lejant=["Üst: **ARSA** aberran sağ a. subclavia; **AA** arcus aortae; **RCCA/LCCA** sağ/sol a. carotis communis; **LSA** sol a. subclavia", "Alt: Tip 1 'bovine' arkus; **BCT** truncus brachiocephalicus; **RVA/LVA** sağ/sol a. vertebralis"],
   noktalar=["4000 BT'de varyasyon prevalansı %0,675 (27 olgu); bunların 7'si aberran sağ a. subclavia.", "ARSA özofagusun arkasından geçer (disfaji lusoria) ve non-rekürren larinks siniriyle ilişkilidir."]),
 dict(baslik="Varyasyon: Karotis bifurkasyonunun düzeyi", alt="Manta ve ark., Surg Radiol Anat 2024 – BT anjiyografi", etiket="VARYASYON",
   figs=[("pmc", "PMC11246274", "Fig1"), ("pmc", "PMC11246274", "Fig6")], yatay=True,
   lejant=["Sol: (a) yüksek bifurkasyon (C2 ve C2/C3), (b) düşük bifurkasyon (C5) – 1 sağ bifurkasyon, 2 C3, 3 hyoid gövdesi, 4 atlas ön arkı, 5 axis, 6 sol bifurkasyon", "Sağ: düşük bilateral bifurkasyon (oklar) ve normal düzey; 1 proc. styloideus, 2 a. carotis interna, 3 a. carotis externa, 4 a. facialis"],
   noktalar=["En sık düzeyler: C3 %27,21, C3/C4 %26,19, C4 %25,51; bilateral simetri %51,7.", "Bifurkasyonun yüksekliği karotis endarterektomisi ve stent planlamasını etkiler."]),
 dict(baslik="Varyasyon: Piramidal tiroid lobu", alt="Kim ve ark., Korean J Radiol 2015 – US ve BT", etiket="VARYASYON",
   figs=[("pmc", "PMC4347276", "g001")],
   lejant=["Transvers (A) ve longitudinal (B) US ile kontrastsız (C) ve kontrastlı (D) BT'de sol piramidal lob (oklar); ana tiroid bezi (ok başları)"],
   noktalar=["Piramidal lob US'de %39,5, BT'de %47,6 oranında saptanmış; merkezler arasında %22–59.", "Total tiroidektomide gözden kaçarsa rezidü doku/nüks kaynağı olur."]),
 dict(baslik="Varyasyon: Aberran sağ a. subclavia ve non-rekürren larinks siniri", alt="Niu ve ark., Thorac Cancer 2016 – 2697 hasta", etiket="VARYASYON",
   figs=[("pmc", "PMC5217945", "g001")],
   lejant=["(a) arkus aortadan son dal olarak çıkan, (b) orta hattı geçen, (c) özofagus arkasından (kısa ok) seyreden (d) sağ aksillaya ulaşan aberran sağ a. subclavia (uzun ok)"],
   noktalar=["2697 hastanın 26'sında (%0,96) ARSA; hepsinde ameliyatta non-rekürren larinks siniri doğrulanmıştır.", "Ameliyat öncesi BT'de ARSA görülmesi sinir yaralanmasını önlemek için güçlü bir uyarıdır."]),
]

BOL = [(BEYIN, BEYIN_VAR_T, BEYIN_VAR, "Beyin"), (KAFA, KAFA_VAR_T, KAFA_VAR, "Kafa tabanı ve sinüs"), (YUZ, YUZ_VAR_T, YUZ_VAR, "Yüz–farinks"), (BOYUN, BOYUN_VAR_T, BOYUN_VAR, "Boyun")]
KAP = [("img", "basboyun/images/vhp/cryo_1080.jpg", "VHP-M 1080"), ("img", "basboyun/images/vhp/cryo_1140.jpg", "VHP-M 1140"),
       ("img", "basboyun/images/vhp/cryo_1200.jpg", "VHP-M 1200"), ("img", "basboyun/images/vhp/cryo_1260.jpg", "VHP-M 1260")]

def build():
    prs = new_deck(); sayfa = 1; kul = []
    kapak(prs, "Baş–Boyun Kesitsel Anatomi", "Gerçek kadavra kriyokesitleri, aynı kadavranın BT ve MR görüntüleri ve literatürden klinik görüntüleme",
          ["Bölümler: Beyin → Kafa tabanı → Yüz–farinks → Boyun", "Her bölüm sonunda görüntüleme tabanlı varyasyon literatür taraması", "Tüm görüntüler gerçek kadavra/radyoloji verisidir."],
          [("img", "basboyun/images/vhp/cryo_1095.jpg", ""), ("img", "basboyun/images/vhp/t2_1095.png", ""), ("img", "basboyun/images/vhp/cryo_1140.jpg", ""), ("img", "basboyun/images/vhp/cryo_1230.jpg", "")])
    sayfa += 1
    icindekiler(prs, BOLUMLER, None, sayfa); sayfa += 1
    sayfa += duzyazi(prs, GIRIS, sayfa, "GİRİŞ")
    for i, (b, (lst, vt, vc, ad)) in enumerate(zip(BOLUMLER, BOL)):
        etk = f"BÖLÜM {i + 1} · {b['ad']}"
        sayfa += bolum_kapak(prs, i + 1, b, [KAP[i]], sayfa)
        for d in lst:
            t = d.get("tip", "gorsel")
            sayfa += {"duzyazi": duzyazi, "kesit": kesit_paneli, "gorsel": gorsel}[t](prs, d, sayfa, etk)
            kul += [r[1] for r in d.get("figs", []) if r[0] == "pmc"]
        sayfa += lit_tablo(prs, f"{ad} – görüntüleme tabanlı varyasyonlar: literatür taraması", "MR, BT, BT anjiyografi ve ultrason çalışmaları (PMC açık erişim)", vt, sayfa, etk)
        for d in vc:
            sayfa += gorsel(prs, d, sayfa, etk); kul += [r[1] for r in d["figs"] if r[0] == "pmc"]
    s = yeni_slayt(prs); title_bar(s, "Sınırlılıklar ve kalite kontrol")
    bullets(s, 0.45, 1.3, 12.4, 5.5, [
        "Kriyokesit, BT ve MR aynı NLM kesit numarasını taşır; MR (m_vm####) 5 mm aralıkla yalnız baş bölgesini (≤1165) kapsar. Hizalama yalnız öteleme ile yapılmıştır (Dice BT 0,95–0,99; MR 0,85–0,99).",
        "Baş bölgesinde donmuş BT piksel boyutu 0,527 mm, boyun kökünde 0,781 mm'dir; hizalamada gerçek piksel boyutu kullanılmıştır.",
        "Kadavra başı hafif eğik kesildiğinden bazı düzeylerde sağ ve sol taraf farklı yapıları gösterir.",
        "Etiketler gözle tanımlanmıştır; ventrikül ve çekirdek sınırları kadavrada değişmiş olabilir. Bir anatomi/radyoloji öğretim üyesince gözden geçirilmesi önerilir.",
        "Açık lisanslı etiketli normal larinks BT/MR, ostiyomeatal kompleks ve boyun fasyası kadavra fotoğrafı bulunamadı; bazı görseller CC BY-NC(-SA) lisanslıdır (slaytlarda belirtilmiştir)."], size=16)
    footer(s, "", sayfa); fix_runs(s); sayfa += 1
    sayfa = kaynakca(prs, kul, "Kaynakça ve görsel lisansları", sayfa)
    out = ROOT / "basboyun" / "Bas_Boyun_Kesitsel.pptx"; prs.save(out); print(out, len(prs.slides), "slayt")

if __name__ == "__main__":
    build()
