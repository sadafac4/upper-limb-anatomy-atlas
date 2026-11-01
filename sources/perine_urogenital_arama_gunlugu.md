# PERİNE – Ürogenital üçgen + perine fasyaları – arama günlüğü

Tarih: 2026-11-01. Keşif: WebSearch (sunucu tarafı). Doğrulama ve indirme: yalnızca AWS PMC OA bucket
(`scripts/pmc_oa_fetch.py info/get --out perine/images/raw`). Lisans `license_code` bucket JSON'undan; altyazılar
JATS XML'den birebir (`scripts/build_perine_urogenital.py` → `sources/perine_urogenital.json`).
Her indirilen şekil Read ile açıldı; `label_points` koordinatları özgün piksel sisteminde, ızgaralı (grid) büyütülmüş
kırpıntılar üzerinde okunup kırmızı daire bindirmesiyle kontrol edildi.
Kabul edilen dosyaların toplam boyutu ≈ 4.7 MB (12 makale klasörü, 23 şekil, 213 etiket noktası).

Kapsam: ürogenital üçgen (yüzeyel/derin perine aralığı), membrana perinei, fasyalar, corpus perineale, dış genital
organların kökü. Pelvis tabanı ve anal üçgen/pudendal damar-sinir diğer ajanlarda; çakışan PMCID klasörlerine
dokunulmadı (ör. PMC12452807 diğer ajanın klasörü).

## Yapılan aramalar (WebSearch)
1. site:pmc perineal membrane cadaver dissection anatomy
2. site:pmc Colles fascia superficial perineal fascia cadaveric study
3. site:pmc perineal body anatomy cadaver dissection female
4. site:pmc clitoris anatomy cadaveric dissection bulb vestibule crura
5. site:pmc superficial perineal pouch dissection bulbospongiosus ischiocavernosus cadaver
6. site:pmc external urethral sphincter compressor urethrae sphincter urethrovaginalis cadaver
7. site:pmc Bartholin gland anatomy cadaver dissection
8. site:pmc Buck's fascia dartos penis anatomy cadaver dissection layers
9. clitoris dissection cadaver open access (Cureus / Clin Anat / Sci Rep)
10. perineal body morphometry cadaver length thickness female
11. dorsal nerve of clitoris cadaveric dissection pmc
12. deep transverse perineal muscle existence cadaver dissection male
13. pmc "perineal membrane" dissection photograph ischiocavernosus 2020-2025 (extended)
14. site:pmc vestibular bulb clitoris cadaver anatomy
15. site:pmc bulbourethral (Cowper) gland cadaver anatomy
16. site:pmc ischiocavernosus bulbospongiosus penis cadaveric
17. "perineal complex triad" urogenital hiatus
18. Muro/Akita perineal body female cadaver Sci Rep / J Anat
19. Scarpa–Colles continuity cadaver dissection open access (extended)
20. clitoris cadaver dissection Cureus / JCM / Sexual Medicine (extended)
21. site:pmc perineal body cadaver Thiel/embalmed
22. site:pmc clitoris suspensory ligament / prepuce / glans
23. site:pmc superficial transverse perineal muscle variation cadaver
24. site:pmc penile crura root of penis ligament cadaver
25. site:pmc Fournier gangrene fascial planes Colles Buck dartos Scarpa
26. site:pmc labia majora cadaver fat pad dartos
27. site:pmc superficial fascia perineum histology membranous layer Colles
28. site:pmc female perineum dissection vestibular bulb greater vestibular gland
29. perineal body cadaver dimensions mm 2019-2025 (extended)
30. site:pmc female urethral sphincter complex dissection compressor urethrae
31. site:pmc clitoris MRI/dissection review vestibular bulbs
32. site:pmc bulbospongiosus female cadaver variations
33. site:pmc Buck's fascia cadaver photograph tunica albuginea
34. site:pmc Colles fascia urethral injury extravasation
35. site:pmc clitoral dissection gender-affirming / vulvar surgery dorsal nerve crura
36. site:pmc rhabdosphincter male cadaver membranous urethra
37. clitoris cadaver 2022-2024 Sexual Medicine / J Sex Med (extended)
38. site:pmc ischiocavernosus cadaver erection crus penis
39. site:pmc perineal body central tendon obstetric cadaver
40. "Innervation pattern and fiber counts of the human dorsal nerve of clitoris" PMC
41. "Anatomy of muscle connections in the male urethra and anorectal canal" (Muro, BJU)
42. site:pmc female perineal muscles bulbospongiosus lateral anal sphincter Muro
43. Insights into Imaging perineum fascia Colles Fournier review
44. site:pmc Scarpa fascia dissection membranous layer continuity
45. site:pmc "deep perineal fascia" OR Gallaudet
46. site:pmc anterior urethral injury butterfly hematoma Colles/Buck
47. site:pmc penile fascial layers dartos Buck histology
48. site:pmc scrotum layers dartos cadaver
49. site:pmc perineal muscle variation case report (accessory IC/BS/STP)
50. site:pmc female external genitalia morphometry clitoris labia
51. site:pmc perineal membrane US/MRI 3D model levator ani
52. "membranous layer" superficial fascia perineum scrotum cadaver photograph Colles (2020-2025)

## Seçilenler (ayrıntı `sources/perine_urogenital.json`)
| PMCID | Lisans | Şekil(ler) | İçerik |
|---|---|---|---|
| PMC12229694 | CC BY | Fig 1, 2, 7 | Erkek/kadın ürogenital üçgen katman katman diseksiyon (Bs, Ic, STP → PM → SM/DTP, EUS); Fig 7 yazar şeması |
| PMC13069139 | CC BY | Fig 1, 2, 4 | Membrana perinei / "DTP" tartışması; embalmlı erkek-kadın diseksiyon; çıkarılmış PM plakası |
| PMC8373982 | CC BY | Fig 1, 2 | Erkek: STPs/STPi, PM, Cowper (bulbourethral) bezi, DTP in situ |
| PMC6942605 | CC BY | Fig 3, 4 | Kadın: BS'nin EAS lateral yüzüne tutunması; STP orta hattı geçer |
| PMC7182620 | CC BY | Fig 1 | Erkek perine kasları sürekliliği (lateral görünüm) |
| PMC7913006 | CC BY | Fig 2, 3, 4 | Kadın: klitoris gövde/krus/glans, bulbus vestibuli, Bartholin bezi (şema), corpus perineale, epizyotomi riski |
| PMC11452485 | CC BY | Fig 1, 2 | Klitoris (eksize) – krus, lig. suspensorium, prepusyum; microCT 3D (CC, CS, VB, glans) |
| PMC10594829 | CC BY | Fig 5, 9 | Penis kökü: lig. fundiforme (Scarpa türevi) + lig. suspensorium (3 demet) |
| PMC4022307 | CC BY | Fig 10, 11 | Yazar diyagramları: kadın CU/UVS/RS + kalın PM; erkek RS, Cowper, DTP |
| PMC12003430 | CC BY | Fig 3 | Kadın EUS'nin at nalı biçimi (seri kesitlerden 3D) |
| PMC7270988 | CC BY | Fig 1 | VARYASYON – perine cismi US morfometrisi (normal vs prolapsus) |
| PMC7538817 | CC BY | Fig 1 | VARYASYON – 208 Türk kadında dış genital morfometri (şema) |

## Reddedilen / kullanılmayan adaylar
| PMCID | Konu | Neden |
|---|---|---|
| PMC2775042 | Stein & DeLancey, perineal membrane (Obstet Gynecol 2008) | OA bucket'ta yok |
| PMC2696929, PMC3353407, PMC9344198 | DeLancey grubu PM/perine cismi MRI | Yazar el yazması (TDM), şekil dosyası yok |
| PMC9544139 | Vajinal introitus cerrahi anatomisi (yüzeyel perine fasyası, PM etiketli diseksiyon) | CC BY-NC-ND + şekiller 267x182 px (okunaksız); indirildi, silindi |
| PMC13069139 Fig 3 | PM iç (posterior) görünüm | Kalabalık numaralama, didaktik değeri düşük; silindi |
| PMC6942605 Fig 2 | Kadın perine alttan | Karanlık, Fig 3/4'e katkısı az; bu listede kullanılmadı (dosya anal üçgen ajanı için klasörde duruyor) |
| PMC10594829 Fig 1, Fig 12 | Fundiform lig. üçgen; dorsal nörovasküler demet | Fig 1 numaraları altyazıda açıklanmamış; Fig 12 pudendal bölge (diğer ajan); silindi |
| PMC5964499 | Penis en bloc eksplant (trans erkek transplantasyonu) | CC BY ama eksplant fotoğrafları – topografi gösterimi zayıf; 3 şekil indirildi, silindi |
| PMC10340559 | Üretral sfinkter derlemesi (Cancers) | CC BY ama şekiller şematik/mekanik; PMC4022307 tercih edildi (yedek) |
| PMC3469827 | Üretral sfinkter klinik anatomi | CC BY-NC, şekil yok |
| PMC12452807 | Prostatektomi – SFPD/EUS | CC BY-NC; diğer ajanın klasöründe mevcut, pelvis kapsamı |
| PMC10521954 | Dartos histolojisi (buried penis) | CC BY-NC-SA; yalnız histoloji (yedek: kadavra derin dartos elastik lifleri) |
| PMC11184429 | Glans clitoridis korona/frenulum (Anat Cell Biol 2024) | CC BY-NC; ayrıntılı glans makrofotoları – yedek aday |
| PMC6131961 | Genç erişkin erkek/kadın ürogenital üçgen 3D (J Anat 2018) | CC BY-NC; kesitsel/3D, topografik değil – yedek |
| PMC4927426 | Fetal perineal rafe/BS | CC BY-NC, fetal histoloji |
| PMC6376168 | Köpek perinesi | İnsan değil |
| PMC12471538 | Penil fibro-ligamanlar (Life 2025) | CC BY ama şema hipotez-yüklü (Colles/fundiform tarifi standart dışı) |
| PMC9831181 | Penil süspansuar sistem (PRS GO) | CC BY-NC-ND |
| PMC5448629 | Penil ligamanlar VHP | CC BY-NC-ND, kesitsel |
| PMC3560785, PMC5503924, PMC5503951 | Penis anatomisi/skrotum/penil fraktür US (Transl Androl Urol, Med Sci Monit) | license_code yok |
| PMC7047600 | Fournier gangreni – fasya planları | TDM, şekil dosyası yok |
| PMC4005052 | Metoidioplasti klitoris anatomisi | CC BY ama intraoperatif klinik fotoğraflar (hasta) – kapsam dışı |
| PMC4878251 | Klitoromegali cerrahisi (Buck fasyası görünümü) | CC BY-NC-SA, hasta fotoğrafı |
| PMC3175415 | Klitoris terminolojisi (ISRN) | Şekiller "Modified from" – üçüncü taraf |
| PMC12464070 | Ürogenital hiatus kapanması (IUJ 2025) | CC BY ama MRI/pelvik taban – pelvis ajanının kapsamı |
| PMC10410282, PMC13308972 | Perine cismi US/3D endoanal US | CC BY; PMC7270988 seçildi (yedek) |
| PMC2775042/F*, PMC1283096, PMC6284436, PMC5827285 | çeşitli | OA bucket'ta yok |

## Açık kalan boşluklar
- **Colles fasyası (fascia perinei superficialis, stratum membranosum), Scarpa sürekliliği, tunica dartos, Buck fasyası
  (fascia penis profunda), Gallaudet (fascia perinei)**: OA bucket'ta bu fasyaları kadavrada gösteren CC BY figür
  BULUNAMADI. Tek etiketli adaylar ND/küçük (PMC9544139 – "superficial perineal fascia" etiketli, 267 px, CC BY-NC-ND).
  Kısmi ikame: PMC12229694 Fig 7 (PM katmanı şeması), PMC13069139 Fig 4 (çıkarılmış PM plakası), PMC10594829
  (Scarpa türevi lig. fundiforme). Öneri: Stanford Bassett koleksiyonu (CC BY-SA 4.0; "membranous layer of superficial
  fascia in urogenital triangle") – ancak lane.stanford.edu ağ politikasında erişilemedi; manuel indirme gerekir.
  Aksi halde fasya slaytı için kendi şemamızı çizmek gerekecek.
- **M. compressor urethrae / m. sphincter urethrovaginalis kadavra fotoğrafı**: yok; PMC4022307 Fig 11 (yazar diyagramı)
  ve PMC12003430 (3D) kullanılabilir.
- **Bartholin bezi (gl. vestibularis major) kadavra fotoğrafı**: yok; yalnız PMC7913006 Fig 3 şeması.
- **Corpus perineale kadavra morfometrisi**: OA'da yok; US morfometrisi (PMC7270988) ve PMC7913006 yüzdeleri
  (perine cisminde kas lifi %16.6) kullanıldı. PMC7538817'de perine cismi uzunluğu ölçülmüş ama değer yalnız
  görsel tabloda.
- **Bulbus penis/crura penis klasik "kök" diseksiyonu (erkek)**: PMC12229694 Fig 1C (BP) ve PMC8373982 Fig 2 (CSP)
  dışında krusları iskiyopubik dala tutunurken gösteren CC BY fotoğraf yok.
- **M. transversus perinei superficialis varyasyon sıklığı**: sayısal OA kaynak yok (yalnız STPs/STPi ikiye ayrılması –
  PMC8373982; DTP'nin varlığı tartışması – PMC12229694 vs PMC13069139).
- **O'Connell klitoris diseksiyonları** (J Urol 1998/2005): PMC OA'da değil; PMC11452485 (microCT 3D) ikame.
