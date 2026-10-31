# Kesitsel pilot – etiket doğrulama notları

Her etiket noktası kırpılmış kriyokesit pikselinde tanımlıdır (`scripts/build_kesitsel.py`), slayt geometrisinden
EMU'ya çevrilir. Kemik etiketleri renk tabanlı kemik maskesine "snap" edilir; BT etiketleri gerçek BT kemik
bileşenine (>300 HU) yapıştırılır. Sayısal kayıt: `label_qa.json`. Slaytlar PDF→PNG (110–300 dpi) olarak
görsel denetlenmiştir.

## Kanıta dayalı tanımlamalar
* **Radius / ulna ayrımı (1645, 1740, 1785):** donmuş BT'de 1600–1840 arası her 10 mm'de kemik bileşenleri
  izlendi. B kemiği proksimalde daha büyük (1680: 365 px) ve distale doğru küçülüyor (1760: 194 px) → ulna;
  A kemiği distalde genişliyor ve 1780'de karpal kemik sırası onun devamında beliriyor → radius.
  El düzeyinde (1830) hipotenar kasların ulna tarafında (aşağı-sol), başparmak kemiklerinin karşı tarafta olması bu ayrımla tutarlıdır.
* **Clavicula (1320):** donmuş BT koronal MIP'te klavikulalar humerus başlarıyla aynı düzeyde.
* **Eklem aralığı (1615):** kriyokesitte parlak beyaz eklem kıkırdağı hattı; komşu kesit dizisi (1595–1685) ile doğrulandı.

## QA sırasında bulunan ve düzeltilen hatalar
1. 1560 BT "Humerus" etiketi FOV kesilme kenarındaki parlak artefakta yapışmıştı → FOV'un kestiği düzeylerde (1490, 1560, 1615, 1645) BT etiketi kaldırıldı.
2. 1740 "Fleksör kompartman" noktası ön kol dışında, karın duvarı yağ dokusundaydı (gereksiz koordinat ötelemesi) → ön kol fleksör kitlesine taşındı.
3. 1560 "Arka kompartman" noktası yağ çizgisine denk geliyordu → triceps kas kitlesine taşındı.
4. 1830 başparmak etiketi kemik-snap ile kemik kenarına kaymıştı → snap kapatıldı, kemik merkezi kullanıldı.
5. Dipnotta `a_vm` alt çizgileri italik işaretleyici olarak yorumlanıyordu → işaretleyici `~…~` olarak değiştirildi.

## Bilinçli olarak etiketlenmeyenler (anatomist onayı gerekir)
Tek tek karpal kemikler; n. radialis / n. ulnaris'in ayrı ayrı gösterilmesi; yüzeyel venler; 1615'te trochlea/capitulum;
kol düzeylerinde m. biceps brachii ile m. brachialis'in ayrı sınırları (kompartman düzeyinde gruplanmıştır).
1360 (fossa axillaris) düzeyi kırpılmış ama kas tanımlaması kesinleşmediği için pilot slaytlara alınmamıştır.

## Oturum 2 – genişletilmiş sunum (18 düzey)
Yeni düzeyler: 1290, 1340, 1420, 1530, 1596, 1700, 1770, 1800, 1850 (ızgaralı önizleme + BT kemik penceresi ile tanımlandı).

QA sırasında bulunan ve düzeltilen hatalar:
6. **1700 kayıt hatası:** yerel arama 20 BT pikseli kaydırmış, BT kemikleri kriyokesitten ~17 mm sapmıştı → yerel arama ±12 px ile sınırlandı; yeniden üretildi ve BT kemikleri radius/ulna ile çakıştı.
7. **1340:** "Caput breve m. bicipitis + m. coracobrachialis" noktası siyah bir damar lümenine düşüyordu → etiket kaldırıldı; aynı nokta "aksiller damar lümeni" olarak etiketlendi.
8. **1596:** "Damar–sinir yapıları" noktası kas üzerine düşüyordu ve kesin tanımlanamadı → kaldırıldı; cilt altındaki açık yüzeyel ven lümeni etiketlendi.
9. **1530:** triceps noktası yağ çizgisinin ucundaydı → kas kitlesine taşındı.
10. Boylamsal reformat: otomatik kemik izleme yolu gövdeye kaydığı için reddedildi; doğrulanmış etiket noktaları çapa alınarak yeniden üretildi.
