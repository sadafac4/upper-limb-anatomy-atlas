# -*- coding: utf-8 -*-
"""Düzyazı (paragraf) tarzı konu anlatımları – üst ekstremite sunumları için.
Her bölümün başında bölgeyi 'ders anlatır gibi' tanıtır; varyasyon bölümünden önce de bir köprü paragrafı verir."""

TOPO = {
 "giris": [dict(baslik="Üst ekstremiteyi nasıl düşünmeliyiz?", alt="Bir bütün olarak kol: hareket için tasarlanmış bir sistem",
   paragraflar=[
    "Üst ekstremite, alt ekstremitenin aksine yük taşımak için değil, eli uzayda istenen noktaya götürmek ve orada ince işler yaptırmak için tasarlanmıştır. Bu nedenle omuz kuşağı gövdeye yalnızca küçük bir eklemle, art. sternoclavicularis ile bağlanır; geri kalan bağlantıyı kaslar sağlar. Bu düzen bize büyük bir hareket serbestliği kazandırır, ama aynı zamanda omzu çıkıklara ve kas–tendon yaralanmalarına açık hale getirir.",
    "Topografik anatomiyi öğrenirken her bölgede aynı soruları sormak işimizi kolaylaştırır: Bu bölgenin iskeletini hangi kemik çıkıntıları oluşturur? Kaslar hangi fasyalarla kompartmanlara ayrılmıştır ve her kompartmanı hangi sinir yönetir? Ana arter ve sinirler bölgeye nereden girip nereden çıkar, yol boyunca hangi dar geçitlerden geçer? Son olarak, bu yapıların yeri hangi kırık, çıkık veya sıkışma tablosunu açıklar?",
    "Bu sunumda omuzdan başlayıp parmak uçlarına doğru ilerleyeceğiz. Her bölümün sonunda o bölgede sık karşılaşılan anatomik varyasyonları güncel literatürle birlikte ele alacağız; çünkü ameliyathanede ve görüntülemede karşımıza çıkan anatomi, çoğu zaman ders kitabındaki 'tipik' anatomiden biraz farklıdır."])],
 "omuz": [dict(baslik="Omuz bölgesine genel bakış", alt="Kemik çerçeve, kas manşeti ve aksilla",
   paragraflar=[
    "Omuz bölgesini anlamanın en kolay yolu onu üç katman halinde düşünmektir. En derinde clavicula, scapula ve humerus başından oluşan kemik çerçeve vardır. Bunun üzerinde caput humeri'yi sığ glenoid çukurunda tutan rotator manşet kasları yer alır. En dışta ise omzun yuvarlak konturunu veren m. deltoideus ve göğüs–sırt duvarından gelip kolu hareket ettiren büyük kaslar bulunur.",
    "Glenohumeral eklem, vücudun en hareketli eklemidir; ancak bu hareketlilik kemik uyumundan değil, yumuşak dokuların dengesinden gelir. Caput humeri'nin ancak üçte biri kadar bir alanla temas eden cavitas glenoidalis, labrum ile derinleştirilir ve kapsül–bağ kompleksiyle desteklenir. Rotator manşet ise kas tonusuyla başı sürekli olarak glenoide doğru bastırır. Bu dengenin bozulması, örneğin bir supraspinatus yırtığı veya ön kapsül hasarı, omuz ağrısı ve instabilitenin temel nedenidir.",
    "Kolun damar ve sinirleri boyundan kola geçerken aksilla adı verilen piramit şeklindeki boşluktan geçer. A. axillaris'i m. pectoralis minor'ün önünden geçişine göre üç bölüme ayırmak, dallarını ve plexus brachialis'in fasiküllerini yerleştirmek için pratik bir çerçevedir. Aksillanın arka duvarındaki küçük aralıklar – özellikle n. axillaris'in geçtiği dörtgen boşluk – omuz çıkığı ve humerus boyun kırıklarında hangi sinirin risk altında olduğunu anlamamızı sağlar."])],
 "omuz_var": [dict(baslik="Omuz bölgesinde varyasyonlar neden önemli?", alt="Literatür taramasına giriş",
   paragraflar=[
    "Aksilla, üst ekstremitenin damar–sinir 'kavşağıdır' ve bu kavşakta varyasyon oldukça sıktır. Plexus brachialis'in fasiküllerinin oluşumu, n. medianus köklerinin sayısı ve a. axillaris'in dallarının ortak gövdeler halinde çıkması, kadavra serilerinde dikkate değer oranlarda bildirilmektedir.",
    "Bu farklılıklar yalnızca akademik bir merak konusu değildir. Aksiller lenf nodu diseksiyonu, plexus blokları, omuz artroskopisi ve flep cerrahisi sırasında beklenmeyen bir arter veya sinir dalı ciddi komplikasyonlara yol açabilir. Aşağıdaki tablolar ve çalışma slaytları, her varyasyonun hangi sıklıkta görüldüğünü ve klinik olarak neden akılda tutulması gerektiğini, makalelerin kendi görselleriyle birlikte özetlemektedir."])],
 "kol": [dict(baslik="Kol bölgesine genel bakış", alt="İki kompartman, bir kemik ve üç büyük sinir",
   paragraflar=[
    "Kol, anatomik olarak üst ekstremitenin en 'düzenli' bölgesidir: ortada humerus, önde fleksörler, arkada ekstensörler ve bunları ayıran iki intermüsküler septum. Ön kompartmandaki m. biceps brachii, m. brachialis ve m. coracobrachialis'i n. musculocutaneus; arka kompartmandaki m. triceps brachii'yi ise n. radialis innerve eder.",
    "Kolu anlamanın anahtarı, büyük sinirlerin humerus etrafındaki seyrini takip etmektir. N. medianus a. brachialis ile birlikte kolun iç yüzünde iner ve kolda dal vermez. N. ulnaris kolun ortasında arka kompartmana geçerek epicondylus medialis'in arkasına yönelir. N. radialis ise humerus'un arkasını spiral bir olukta dolanır; bu yüzden humerus gövde kırıklarında yaralanan sinir genellikle n. radialis'tir ve hasta 'düşük el' tablosuyla gelir.",
    "Kolun distal ucunda humerus genişleyerek epikondilleri oluşturur ve dirsek bölgesine geçeriz. Burada a. brachialis ve n. medianus, aponeurosis bicipitalis'in altında fossa cubiti'ye girer. Çocuklarda sık görülen suprakondiler kırıklar, tam bu yapıları tehdit ettiği için acil bir durumdur."])],
 "kol_var": [dict(baslik="Kol bölgesinde varyasyonlar neden önemli?", alt="Literatür taramasına giriş",
   paragraflar=[
    "Kolda en sık karşılaşılan varyasyonlar kas başlarının sayısı (m. biceps brachii'nin aksesuar başı, m. coracobrachialis'in çok başlı oluşu), n. musculocutaneus ile n. medianus arasındaki bağlantılar ve a. brachialis'in normalden yüksek düzeyde bölünmesidir.",
    "Yüzeyel seyreden bir a. brachialis superficialis veya yüksek çıkışlı bir a. radialis, damar yolu açılırken yanlışlıkla arter içine enjeksiyon riskini artırır; sinir bağlantıları ise sinir yaralanmalarının klinik tablosunu 'atipik' hale getirebilir. Aşağıdaki çalışmalar bu varyasyonların ne kadar sık olduğunu kadavra ve görüntüleme verileriyle göstermektedir."])],
 "onkol": [dict(baslik="Dirsek ve önkola genel bakış", alt="Döner bir önkol ve katmanlı kas grupları",
   paragraflar=[
    "Dirsek eklemi aslında tek bir kapsül içinde üç eklemden oluşur: humerus–ulna arasındaki menteşe eklem fleksiyon–ekstansiyonu, radius başının yer aldığı eklemler ise önkolun dönme hareketini sağlar. Pronasyon sırasında radius, ulnanın önünden çaprazlanarak yer değiştirir; bu nedenle kesitlerde iki kemiğin konumu kolun pozisyonuna göre değişir.",
    "Önkolun ön yüzündeki fleksör kaslar, epicondylus medialis'ten başlayan yüzeyel bir tabaka, ortada m. flexor digitorum superficialis ve derinde parmak ile başparmak fleksörlerinden oluşan katmanlar halinde dizilir. Bu katmanlar arasında n. medianus ve n. ulnaris seyreder. Arka yüzde ise epicondylus lateralis'ten başlayan ekstensörler ve onları innerve eden n. radialis'in derin dalı bulunur.",
    "Klinik açıdan önkol, sinirlerin dar geçitlerden geçtiği bir bölgedir: n. medianus m. pronator teres'in başları arasından, n. ulnaris kubital tünelden ve FCU başları arasından, n. radialis'in derin dalı ise m. supinator'un Frohse arkadı altından geçer. Bu noktaların her biri, kendine özgü bir sıkışma sendromunun adresidir."])],
 "onkol_var": [dict(baslik="Önkolda varyasyonlar neden önemli?", alt="Literatür taramasına giriş",
   paragraflar=[
    "Önkol, embriyolojik gelişimin izlerini en çok taşıyan bölgelerden biridir. Gelişim sırasında geçici olan a. mediana'nın erişkinde kalıcı olması, n. medianus ile n. ulnaris arasındaki Martin-Gruber bağlantısı veya m. flexor pollicis longus'un aksesuar başı (Gantzer kası) gibi varyasyonlar sanılandan çok daha sık görülür.",
    "Bu varyasyonlar sinir iletim çalışmalarının yorumunu değiştirebilir, karpal tünel sendromuna zemin hazırlayabilir veya önkol flepleri ve radial arter girişimleri sırasında beklenmeyen kanamalara yol açabilir."])],
 "el": [dict(baslik="El bileği ve ele genel bakış", alt="Dar kanallar, ince kaslar ve hassas bir denge",
   paragraflar=[
    "El bileğinde önkoldan ele geçen tüm tendon, damar ve sinirler dar osteofibröz kanallardan geçmek zorundadır. Ön yüzde karpal tünel n. medianus ile dokuz fleksör tendonu, Guyon kanalı ise n. ulnaris ile a. ulnaris'i taşır. Arka yüzde ekstensör tendonlar retinaculum extensorum'un altında altı ayrı kompartmanda düzenlenir.",
    "Elin kendi küçük kasları – tenar, hipotenar, lumbrikal ve interosseöz kaslar – parmakların ince ayarını yapar. Bu kasların büyük çoğunluğunu n. ulnaris, başparmağın opozisyonunu sağlayan tenar kasları ise n. medianus'un motor dalı innerve eder. Bu yüzden n. ulnaris hasarı 'pençe el', n. medianus hasarı ise başparmak opozisyonunun kaybıyla kendini gösterir.",
    "Elin beslenmesi, a. radialis ve a. ulnaris'in oluşturduğu iki arkla güvence altına alınır. Bu çift kaynaklı sistem, bir arterin kateterizasyon veya flep için kullanılabilmesini sağlar; ancak arkların tam olup olmadığı kişiden kişiye değişir ve Allen testiyle değerlendirilmelidir."])],
 "el_var": [dict(baslik="El bileği ve elde varyasyonlar neden önemli?", alt="Literatür taramasına giriş",
   paragraflar=[
    "Elde varyasyonlar özellikle cerrahi açıdan önemlidir. N. medianus'un motor dalının retinakulum ile ilişkisi, karpal tünel gevşetmesi sırasında kesinin nereye yapılacağını belirler. N. ulnaris'in Guyon kanalındaki dallanma şekli ve n. medianus ile n. ulnaris arasındaki palmar bağlantılar (Riché-Cannieu, Berrettini) sinir yaralanmalarında beklenmedik bulguları açıklar.",
    "Ekstensör kompartmanlardaki ara bölmeler veya aksesuar kaslar da de Quervain tenosinovitinde tedavi başarısızlığı ya da el sırtında 'kitle' görünümü gibi klinik tablolarla karşımıza çıkabilir."])],
}

KESIT = {
 "giris": [dict(baslik="Kesitsel anatomi neden zor, nasıl kolaylaşır?", alt="Üç boyutlu düşünmeyi öğrenmek",
   paragraflar=[
    "Kesitsel anatomide zorluk, bildiğimiz yapıları alışık olmadığımız bir açıdan görmemizdir. Diseksiyon salonunda kası baştan sona izleriz; kesitte ise yalnızca o kasın bir 'dilimini' görürüz. Bu nedenle kesit okumanın ilk kuralı, her kesitte önce kemiği tanımak ve bulunduğumuz düzeyi belirlemektir: humerus başı mı, gövdesi mi, yoksa epikondiller mi?",
    "İkinci adım, fasyaların çizdiği sınırları takip etmektir. Kol ve önkolda kaslar kompartmanlar halinde düzenlenmiştir ve her kompartmanın kendine ait bir siniri vardır. Damar–sinir demetleri ise genellikle kompartmanların birleştiği yerlerde, yağ dokusu içinde seyreder. Kriyokesitlerde bu demetler, kadavrada boşalmış damarların siyah lümenleri sayesinde kolayca seçilir.",
    "Bu sunumda aynı kadavranın aynı düzeydeki renkli kesit fotoğrafını ve BT görüntüsünü yan yana göreceğiz. Böylece kas, yağ ve kemiğin gerçek görünümü ile radyolojik görünümü arasındaki ilişkiyi doğrudan kurabileceğiz. Literatürden alınan MR ve ultrason görüntüleri de klinikte bu bilginin nasıl kullanıldığını gösterecek."])],
 "omuz": [dict(baslik="Omuz kesitlerini okumak", alt="Caput humeri'den aksillaya",
   paragraflar=[
    "Omuz kesitlerinde yönümüzü bulmak için caput humeri ve scapula'yı kullanırız. Caput humeri'nin hemen medialinde sığ glenoid yüzey, onun önünde m. subscapularis, arkasında ise m. infraspinatus ve m. teres minor yer alır. Daha üst kesitlerde spina scapulae'nin önünde m. supraspinatus görülür. Bu düzen, MR'da rotator manşet yırtıklarını değerlendirirken temel referansımızdır.",
    "Biraz daha aşağı indiğimizde humerus'un boyun bölgesine ve aksillaya ulaşırız. Aksillanın ön duvarını pektoral kaslar, arka duvarını m. subscapularis oluşturur; aradaki yağ dokusunda a./v. axillaris ve plexus brachialis'in fasikülleri bulunur. Kriyokesitlerde damarlar boş lümenleri sayesinde siyah olarak seçilir."])],
 "kol": [dict(baslik="Kol kesitlerini okumak", alt="Merkezde humerus, etrafında iki kompartman",
   paragraflar=[
    "Kol kesitleri en kolay okunan kesitlerdir: merkezde yuvarlak humerus, önde fleksör kas kitlesi, arkada m. triceps brachii. Ön ve arka kompartmanları ayıran septumlar ince yağ çizgileri olarak görülür. Kolun iç yüzünde, iki kompartmanın birleştiği yerde a. brachialis, eşlik eden venler ve n. medianus'tan oluşan damar–sinir demeti bulunur.",
    "Distale indikçe humerus'un şekli yuvarlaktan üçgene döner ve m. brachialis kemiğin ön yüzünü örter. Bu düzeylerde n. radialis'in humerus'un arkasındaki seyri ve kol distalinde laterale geçişi, ultrason ile kolayca izlenebilir; literatürden eklenen ultrason görüntüleri bunu göstermektedir."])],
 "onkol": [dict(baslik="Dirsek ve önkol kesitlerini okumak", alt="İki kemik, beş bölme",
   paragraflar=[
    "Dirsek düzeyinde humerus'un genişlemiş distal ucu ve eklem yüzleri görülür; eklem kıkırdağı kriyokesitlerde parlak beyaz bir çizgi olarak seçilir. Hemen altında radius başı ve ulna ayrı kemikler olarak belirir. Önkol kesitlerinde radius ve ulnayı ayırt etmek için kemiklerin şekline ve proksimalden distale boyutlarının nasıl değiştiğine bakarız: ulna proksimalde, radius ise distalde daha geniştir.",
    "Kadavramızda önkol pronasyonda olduğu için iki kemik çaprazlanmış görünür ve kompartmanlar eğik olarak kesilmiştir. Ön yüzde hacimli fleksör kitlesi, arka-dış yüzde ise ekstensör ve mobil kas grubu bulunur. Literatürden eklenen kompartman şemaları ve Doppler ultrason görüntüleri, sinir ve arterlerin bu bölmelerdeki yerini ayrıntılı olarak göstermektedir."])],
 "el": [dict(baslik="El bileği ve el kesitlerini okumak", alt="Kanallar ve tendon dizilimi",
   paragraflar=[
    "El bileği kesitlerinde iki standart düzey kullanılır: proksimalde os pisiforme ve os scaphoideum, distalde hamulus ossis hamati ve os trapezium düzeyi. Bu iki düzeyde karpal tünelin çatısını oluşturan retinakulum, tünelin içindeki n. medianus ve fleksör tendonları ile medialde Guyon kanalı açıkça izlenir.",
    "Kadavramızda el uyluğa yaslı olduğu için kesitler eğiktir; buna rağmen karpal kemiklerin, tenar ve hipotenar kasların ve metakarpların düzeni tanınabilir. Ulnar taraftaki hipotenar kasların ve radial taraftaki başparmağın yeri, kesitin yönünü doğrulamamızı sağlar."])],
}
