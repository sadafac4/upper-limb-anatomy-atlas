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
