# EL bölgesi (el bileği ve el) – arama günlüğü

Tarih: 2026-10-31. Keşif: WebSearch (sunucu tarafı). Doğrulama ve indirme: yalnızca AWS PMC OA bucket
(`scripts/pmc_oa_fetch.py info/get`). Lisans `license_code` bucket JSON'undan alındı; altyazılar JATS XML'den
birebir (`scripts/build_bolge_el.py`). Her indirilen şekil Read ile tek tek açılıp kontrol edildi.
Toplam EL indirmesi ≈ 11 MB (24 makale klasörü).

Yardımcı betikler: `scripts/el_extract.py` (meta + özet + altyazılar), `scripts/el_grep.py` (gövde metninde
cümle arama), `scripts/build_bolge_el.py` (`sources/bolge_el.json` üretir).

## Yapılan aramalar (WebSearch)
1. site:pmc superficial palmar arch variations cadaveric study classification
2. site:pmc Guyon canal ulnar nerve cadaver dissection anatomy
3. site:pmc Riche-Cannieu anastomosis cadaveric prevalence
4. Insights into Imaging wrist MRI anatomy carpal tunnel Guyon canal review
5. site:pmc anatomical snuffbox cadaveric study radial artery
6. site:pmc bifid median nerve ultrasound prevalence persistent median artery
7. site:pmc flexor tendon pulley system cadaver A1 A2 A4
8. site:pmc extensor compartments wrist ultrasound anatomy review
9. site:pmc extensor digitorum brevis manus prevalence MRI OR cadaver
10. site:pmc Linburg-Comstock FPL FDP interconnection cadaver
11. site:pmc lunotriquetral coalition prevalence radiograph
12. site:pmc carpal tunnel contents cadaveric dissection transverse carpal ligament
13. site:pmc extensor mechanism finger cadaver sagittal bands lateral bands
14. site:pmc palmar cutaneous branch median nerve cadaveric study
15. site:pmc accessory abductor digiti minimi MRI prevalence
16. site:pmc TFCC MRI anatomy review labelled
17. site:pmc deep palmar arch cadaveric study variations
18. site:pmc os styloideum carpal boss imaging / accessory ossicles CT prevalence
19. Insights into Imaging ultrasound wrist hand anatomy median nerve carpal tunnel pictorial
20. site:pmc lumbrical incursion carpal tunnel ultrasound
21. site:pmc extensor retinaculum compartments cadaveric septa EPB
22. site:pmc MRI carpal tunnel axial anatomy labelled hook of hamate
23. site:pmc dorsal branch ulnar nerve cadaveric study wrist
24. site:pmc palmaris profundus / accessory muscles carpal tunnel cadaver prevalence
25. site:pmc anatomical snuffbox dissection scaphoid radial artery cadaver
26. site:pmc lumbrical muscles origin variations cadaveric
27. site:pmc wrist MRI pictorial review extensor tendons carpal ligaments CC BY
28. site:pmc palmar aponeurosis anatomy cadaver dissection
29. site:pmc hypothenar OR thenar muscles cadaveric innervation figure
30. site:pmc accessory muscles wrist hand MRI retrospective prevalence
31. flexor pulleys ultrasound MRI review (Insights/Diagnostics/Cureus)
32. site:pmc carpal coalition prevalence radiographs lunotriquetral Minnaar
33. site:pmc extensor indicis / EDM tendon variations cadaveric prevalence
34. site:pmc Berrettini anastomosis cadaveric prevalence
35. site:pmc Guyon accessory ADM MRI OR ultrasound prevalence
36. site:pmc SPA complete/incomplete percentage hands dissected
37. distal radial artery snuffbox cadaveric (Cureus/JCM/Sci Rep)
38. annular pulleys cadaveric CC BY (Sci Rep/Cureus/BMC)
39. site:pmc interosseous muscles cadaver dissection
40. site:pmc carpal tunnel ultrasound cadaver correlation
41. Rheumatology 2023 ultrasound finger pulleys cadaveric
42. site:pmc extensor apparatus finger dissection central slip
43. site:pmc EDBM MRI OR ultrasound dorsal wrist mass

## Seçilenler
Ayrıntı `sources/bolge_el.json` içinde (29 kayıt, 39 şekil, 24 makale).

## Reddedilen / kullanılmayan adaylar
| PMCID | Konu | Neden |
|---|---|---|
| PMC2938609 | SPA yalnız ulnar (Indian J Plast Surg) | CC BY ama tek, küçük olgu; PMC12823052 + PMC10762056 daha iyi seri |
| PMC10316074 | İnkomplet SPA + Berrettini olgusu | CC BY-NC; daha iyi CC BY seriler bulundu |
| PMC6855928 | Riché-Cannieu derlemesi (Rev Bras Ortop 2019) | CC BY-NC-ND (ND) |
| PMC4898834 | RCA elektrofizyoloji | CC BY-NC, şekiller anatomik değil |
| PMC4579750 | Dorsal el bileği US anatomisi (J Ultrason 2015) | licence_code yok, lisans URL by-nc-nd |
| PMC5516083 | Ventral el bileği US anatomisi (J Ultrason 2017) | licence_code yok, by-nc-nd |
| PMC7016503 | Karpal tünel MRI (Pol J Radiol) | CC BY-NC-ND |
| PMC2917116, PMC4107208, PMC3934360, PMC11078889 | Fleksör tendon MRI; lumbrikal intrüzyonu US; DCBUN dalları; LT koalisyon 4D-CT | Yazar el yazması (TDM), şekil dosyası yok/lisans yok |
| PMC9292555 | A2 makara görüntüleme derlemesi | CC BY-NC-ND |
| PMC10368382 | A2 makara yüzey işareti (PRS GO) | CC BY-NC-ND |
| PMC12049921 | Başparmak makaraları US (RMD Open) | CC BY-NC; parmak makaraları için PMC11534144 (CC BY) seçildi |
| PMC5950968 | İp ile A1 gevşetme (Hand) | CC BY-NC; işlem odaklı |
| PMC9051617 | LT koalisyon artroskopik rezeksiyon | CC BY-NC-ND |
| PMC3018775 | LT koalisyon psödartrozu (GMS) | CC BY-NC-ND |
| PMC8041499 | Bilek bağları derlemesi (J Hand Microsurg) | CC BY-NC-ND |
| PMC2895879 | İntrinsik karpal bağlar MRI/kadavra | CC BY-NC; şekiller küçük çizim; ilk tercih değil (yedek) |
| PMC5381316 | TFCC 3T MRI-kesit anatomi korelasyonu | CC BY-NC-SA; PMC5600038 (CC BY) tercih edildi (yedek aday) |
| PMC4075226 | Median sinir varyasyonları + PMA, 52 el | CC BY-NC-SA; repo zaten PMC10343151 içeriyor; yedek |
| PMC4531452 | Os styloideum/karpal boss MRI | CC BY-NC-SA; PMC5487237 (CC BY) tercih edildi |
| PMC8590423 | Ters Linburg-Comstock (Surg Radiol Anat) | Bucket'ta license_code yok |
| PMC12409753 | Rekürren tenar dal varyasyonları (Cureus 2025) | CC BY ama tek şekil 750x107 px şerit (5 küçük panel) – okunaksız; indirildi, sonra silindi |
| PMC11534144 Fig 2 | A2 makara diseksiyon + histoloji | 769x211 kompozit, paneller çok küçük – silindi (Fig 3 kullanıldı) |
| PMC10762056 Fig 1 | SPA çizimi + döküm | Panel A "modified from Radojević and Bošković" – üçüncü taraf materyal; silindi (Fig 2 kullanıldı) |
| PMC11910384 Fig 1, Fig 7 | Berrettini tip/zon diyagramları | Altyazı: "Image created in BioRender" – kullanılmadı; Fig 1 silindi |
| PMC2893531 Fig 3 | LT koalisyon MRI | Etiketsiz, katkısı az – silindi |
| PMC8748762 | FCRB MRI prevalansı (Sci Rep, CC BY, 849 kişi) | Uygun ama Önkol ajanı aynı anda indirdi (ön kol konusu); çakışmamak için EL'e eklenmedi |
| PMC3552760, PMC5871072, PMC8349448, PMC5258131, PMC8489987, PMC9465795, PMC3509286, PMC4378718, PMC6759961, PMC3026110, PMC7540650, PMC3653005, PMC3377301, PMC4319448, PMC2527151, PMC7441134, PMC5030847, PMC3736087, PMC3074740, PMC11632711, PMC3558235, PMC5016980, PMC3563827, PMC5864491 | çeşitli | OA bucket'ta yok (PMC OA alt kümesi değil) |
| PMC11076429 | Guyon US-kılavuzlu ip gevşetme (Eur Radiol Exp) | CC BY ama işlem odaklı; normal anatomi için PMC11899079/PMC10253229 daha iyi (yedek) |
| PMC7158594 | Transvers karpal kas (Cureus) | CC BY; intraop olgu fotoğrafı, etiket zayıf (yedek) |
| PMC7465746 | Aksesuar FCU (BJR Case Rep) | CC BY; ön kol distali, EL dışı sayıldı (yedek) |
| PMC3556543 | Anomal EIP (Arch Plast Surg) | CC BY-NC; PMC6449591 tercih edildi |
| PMC10244378 | Arc of Buhler meta-analizi | Karın bölgesi – konu dışı |

## Açık kalan boşluklar
- **Tabatière anatomique (snuffbox)**: radial arter + skafoid tabanını etiketli gösteren CC BY kadavra fotoğrafı bulunamadı. PMC3269985 yalnız n. radialis yüzeyel dalı + v. cephalica'yı gösteriyor. Kesit/US için PMC10253229 Fig 21/23 (yüzeyel radial sinir, 1. kompartman) indirilebilir.
- **Tenar/hipotenar kasların tam etiketli normal diseksiyonu**: ayrı bir CC BY kaynak yok; PMC6920165 Fig 1B (ADM, FDMB), PMC2527548 (TE/HE) ve PMC10253229 Fig 13C (US: FDM, Opp DM, AbDM, AdP) kısmen karşılıyor. Repo'daki PMC6834099/PMC3931286 tenar dal için kullanılabilir.
- **Palmar aponevroz**: OA bucket'ta uygun lisanslı figür bulunamadı.
- **Mm. interossei**: CC BY kadavra/kesit figürü bulunamadı.
- **Ekstansör retinakulum 6 kompartmanının tamamı (MRI/US)**: CC BY etiketli kaynak bulunamadı (J Ultrason makaleleri ND). Yalnız 1. kompartman (PMC2586286) ve sagittal bantlar (PMC10716571) var.
- **Karpal tünel aksiyel MRI'ı metin etiketli**: PMC8569728 Fig 1 yalnız renkli ok/yıldız içeriyor; Türkçe lejant eklenmeli.
- **Fleksör tendon kılıfı (sinoviyal) ve C makaraları**: yalnız A1/A2 (PMC13047401 CC BY-NC, PMC11534144 US) var.
- **Kesit varyasyonu – aksesuar ADM / EDBM prevalansı (görüntüleme serisi)**: OA bucket'ta orijinal seri yok; PMC11899079 Fig 4 yalnız örnek görüntü, sayı içermiyor.
- **Lumbrikal intrüzyonu US**: tek aday (PMC4107208) yazar el yazması, şekil dosyası yok.
- **LT koalisyon / os styloideum prevalansı**: yalnız olgu sunumları (literatür alıntısı sayılar); orijinal radyografik/CT seri OA değil (Eur J Anat CT anketi PMC'de yok).
