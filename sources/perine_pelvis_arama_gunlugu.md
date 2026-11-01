# PERİNE destesi – kısa PELVİS girişi – arama günlüğü

Tarih: 2026-11-01. Keşif: WebSearch (sunucu tarafı). Doğrulama ve indirme: yalnızca AWS PMC OA bucket
(`scripts/pmc_oa_fetch.py info/get --out perine/images/raw`). Lisans `license_code` bucket JSON'undan alındı; altyazılar
JATS XML'den birebir (`scripts/build_perine_pelvis.py` → `sources/perine_pelvis.json`). İndirilen her şekil Read ile açılıp
kontrol edildi; `label_points` koordinatları PIL ile işaretlenmiş/büyütülmüş kırpıntılar üzerinde doğrulandı (orijinal piksel
koordinatı). Pelvis kısmı toplam indirme ≈ 3 MB (11 makale klasörü).

Kapsam dışı (diğer ajanlar): ürogenital üçgen/fasyalar, anal üçgen/pudendal kanal. PMC6942605 ve PMC4549266 klasörleri
ürogenital/anal ajanlarla ortak olabilir (PMC6942605'te Fig 2-4 diğer ajana aittir; burada yalnız Fig 5 kullanıldı).

## Yapılan aramalar (WebSearch)
1. site:pmc levator ani cadaver dissection superior view pubococcygeus iliococcygeus
2. site:pmc sacrospinous sacrotuberous ligament cadaveric study greater sciatic foramen figure
3. site:pmc arcus tendineus fasciae pelvis cadaver dissection ischial spine
4. site:pmc sexual dimorphism pelvis pelvic inlet outlet morphometry CT open access
5. levator ani cadaveric dissection CC BY Int Urogynecol J / Scientific Reports puborectalis
6. site:pmc Cureus levator ani cadaver dissection pelvic diaphragm
7. site:pmc coccygeus ischiococcygeus muscle cadaveric study morphology
8. site:pmc sacrotuberous ligament anatomy cadaver morphometric study photograph
9. site:pmc dry bone pelvis male female photograph subpubic angle sex estimation
10. site:pmc endopelvic fascia cadaver dissection parietal visceral pelvic fascia figure
11. site:pmc puborectalis muscle anatomy cadaver study levator ani subdivisions
12. site:pmc sacrospinous ligament pudendal nerve ischial spine cadaver dissection figure
13. site:pmc pelvic floor muscles cadaver inferior view levator ani ischioanal fossa removed
14. site:pmc sacrospinous ligament morphometry cadaver length width coccygeus
15. site:pmc levator ani 3D reconstruction pubovisceral puborectal iliococcygeal CC BY
16. site:pmc linea terminalis pelvic brim promontory arcuate line figure
17. sacrotuberous/sacrospinous cadaver posterior view (Cureus / Sci Rep / Anat Sci Int)
18. levator hiatus urogenital hiatus cadaver study open access
19. site:pmc pudendal nerve entrapment sacrotuberous sacrospinous interligamentous cadaver
20. site:pmc iliococcygeus fixation cadaver photograph ischial spine
21. site:pmc ossified sacrospinous ligament dry pelvis photograph
22. site:pmc gluteal region dissection sacrotuberous ligament piriformis CC BY
23. site:pmc long posterior sacroiliac ligament sacrotuberous dissection
24. site:pmc coccygeus sacrospinous ligament complex photograph
25. site:pmc levator ani coccygeus superior view obturator internus
26. site:pmc levator ani MRI 3D model subdivisions (Sci Rep / Frontiers)
27. site:pmc male pelvic floor levator ani cadaver prostate puboprostatic
28. Cureus sacrotuberous ligament gluteal dissection greater sciatic foramen
29. site:pmc sacrotuberous + sacrospinous + lesser sciatic foramen cadaver photograph

## Kabul edilenler (sources/perine_pelvis.json)
| PMCID | Şekil | Lisans | Ne gösteriyor |
|---|---|---|---|
| PMC9303760 | Fig 1 (panel a) | CC BY-NC | Çizim: linea terminalis = "arcuate line" + "ala margin", crista iliaca düzeyi |
| PMC5768563 | Fig 1, Fig 2 | CC BY-NC | 3D-BT pelvimetri: giriş/orta/çıkış çapları, subpubik açı; K/E sayıları (Tablo 1) |
| PMC7118257 | Fig 2 | CC BY-NC | 3D-BT erkek vs kadın pelvis, subpubik açı (68.6° vs 87.4°) |
| PMC6811666 | Fig 2 | CC BY | Kuru kemik (maserasyon) erkek vs kadın os coxae, pubik açı |
| PMC10924905 | Fig 1 (panel A) | CC BY-NC | 3D-BT üzerine şema: lig. sacrotuberale, m. piriformis, n. ischiadicus, n. pudendus |
| PMC10410660 | Fig 1 | CC BY | Laparoskopi (canlı hasta): OIM, arcus tendineus m. levatoris ani, lig. sacrospinale, spina ischiadica |
| PMC8096964 | Fig 2, Fig 4 | CC BY | Kadavra hemipelvis: fascia obturatoria, ATLA, ATFP, canalis obturatorius; PRM, OIM; frontal kesitte levator hunisi |
| PMC12452807 | Fig 1 | CC BY-NC | Erkek kadavra, medial görünüm: SFPD (fascia diaphragmatis pelvis superior), TAPF, LA |
| PMC4549266 | Fig 1 (G/H) | CC BY | Seri kesitten 3D: Co, PV (pubo+iliococcygeus), PR, OI – levator alt bölümleri tartışması |
| PMC6942605 | Fig 5 | CC BY | Kadın kadavra: levator ani ön kısmının ön/arka demetleri (sling'ler) |
| PMC12287122 | Fig 1 | CC BY | MRI 3D PICS: levator alt bölüm vektörleri, kontrol vs prolapsus morfometrisi |

## Reddedilen / kullanılamayan
| Kaynak | Konu | Neden |
|---|---|---|
| PMC4104205 | Pelvik taban kasları en bloc üst/alt görünüm (Int Urogynecol J) | Yazar el yazması, license_code TDM, bucket'ta şekil dosyası yok |
| PMC5003683 | In situ pelvik taban üstten (C/IC/PV, ATFP, IS) | Yazar el yazması, TDM, şekil yok – en iyi "üstten diaphragma pelvis" adayıydı |
| PMC4336854 | Pubovisseral kas orijini (Neurourol Urodyn) | Yazar el yazması, TDM, şekil yok |
| PMC3508430, PMC4140951 | Puborektal kas MRI / lif yönleri | Yazar el yazması, TDM, şekil yok |
| PMC2775042, PMC3739221, PMC8801847, PMC7879354, PMC2989401 | Levator/fasya/pelvik çizgiler | OA bucket'ta yok |
| PMC7617076 | Pelvis cinsiyet farkı evrimi (Nat Ecol Evol) | Yazar el yazması, license TDM |
| PMC2687900 | Pelvis dimorfizmi derlemesi | CC BY-NC-ND, şekil yok |
| PMC8053576 | Pelvik halka asimetrisi 3D model | CC BY-NC-ND |
| PMC11328984 | Giriş/çıkış açıları (JBJS OA) | CC BY-NC-ND |
| PMC9837515 | Sakrokoksigeal MRI morfometri | CC BY-NC-ND |
| PMC5114254 | Sakrokoksigeal BT morfometri (Kore) | CC BY-NC; koksiks konusu kapsam kenarında (yedek: Fig 4 erkek/kadın sakrum-koksiks) |
| PMC10014651 | 3D-BT ile cinsiyet tayini (Fig 1) | CC BY ama 749x219, küçük; PMC7118257/PMC6811666 daha iyi – indirildi, silindi |
| PMC8096964 Fig 3 | ATLA üstündeki lifler + histoloji | Fig 2/4 ile tekrar, histoloji kapsam dışı – silindi |
| PMC6942605 Fig 2 | Ürogenital üçgen alt görünüm (BS, IC, STP) | Kapsam dışı (ürogenital ajan); benim kopyam silindi, dosya diğer ajan tarafından tekrar indirilmiş – dokunulmadı |
| PMC7806572 | Pelvik retroperiton fasyal modeli (Anat Sci Int, CC BY) | Cerrahi/retroperitoneal kompartmanlar; fascia pelvis parietalis/visceralis için PMC12452807 daha doğrudan (yedek) |
| PMC7498749 | Radikal histerektomi anatomisi | CC BY-NC-ND |
| PMC3846937 | Ektopik hava ile kompartmanlar (BT) | CC BY-NC, kesitsel – kapsam dışı |
| PMC4718483 | Laparoskopik intrapelvik sinir sıkışmaları (CC BY) | Fig 3/10 SSL+IS gösteriyor ama pudendal odaklı (anal/pudendal ajan); PMC10410660 seçildi (yedek) |
| PMC5012987 | Pudendal ganglion kisti | CC BY-NC, olgu/MRI |
| PMC11144494 | Kemikleşmiş lig. sacrotuberale (Orthop Surg, CC BY) | Yalnız röntgen/BT/MRI olgu görüntüleri; varyasyon slaytı için yedek |
| PMC10366308 | N. cutaneus femoris posterior (Anat Sci Int, CC BY) | Gluteal; lig. sacrotuberale diseksiyonda çıkarılmış |
| PMC9705086 | Lig. iliolumbale kadavra (CC BY) | Konu dışı |
| PMC11083419 | Levator alt bölümleri MRI 3D (Diagnostics, CC BY) | PMC12287122 ile aynı grup/yöntem; yedek (Fig 2) |
| PMC7182620 | Erkek pelvik taban kas bağlantıları (CC BY) | Anal/ürogenital ajan kapsamı; yedek (Fig 2: LA → ACL → koksiks) |
| PMC7898478 | Erkek pelvik tabanda düz kas (Clin Anat) | CC BY-NC-ND |
| Stanford Bassett koleksiyonu (CC BY-SA) | Bağlı pelvis, foramen ischiadicum majus/minus fotoğrafları | PMC değil; lane.stanford.edu bu ortamda erişilebilir değil |

## Açık kalan boşluklar
- **Ligamentli kuru pelvis / kadavrada lig. sacrospinale + lig. sacrotuberale + foramen ischiadicum majus/minus**: OA bucket'ta
  etiketli gerçek-örnek fotoğrafı bulunamadı. Yalnız PMC10924905 (CC BY-NC şema, STL+piriformis) ve PMC10410660 (laparoskopi,
  SSL+IS) var. Öneri: Stanford Bassett (CC BY-SA 4.0) ağ izni verilirse en iyi kaynak.
- **Diaphragma pelvis'in üstten (superior) ve alttan tam kadavra görünümü (m. coccygeus dahil)**: en iyi adaylar (PMC5003683,
  PMC4104205) yalnız TDM yazar el yazması. Burada yerine PMC4549266 H paneli (3D rekonstrüksiyon) + PMC8096964 (hemipelvis) kullanılabilir.
- **Hiatus urogenitalis**: etiketli kadavra şekli yok; PMC4549266 metninde levator hiatus ölçüleri (post-mortem ~61 mm uzun, ~23 mm dar) var.
- **Fascia pelvis visceralis**: ayrı etiketli şekil yok (PMC12452807 yalnız parietal yaprak SFPD + TAPF).
- **Linea terminalis'in gerçek kemik fotoğrafında etiketli hali (promontorium, pecten ossis pubis, crista pubica)**: yok; yalnız
  PMC9303760 çizimi ve PMC5768563 3D-BT ölçü çizgileri.
- **Pelvis major/minor ayrımı**: doğrudan etiketli şekil yok; linea terminalis şekilleri üzerinden anlatılmalı.
