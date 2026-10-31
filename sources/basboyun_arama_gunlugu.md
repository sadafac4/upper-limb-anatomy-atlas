# Baş–Boyun Kesitsel Anatomi – kaynak arama günlüğü

Tarih: 2026-10-31. Keşif: WebSearch (sunucu tarafı; wikimedia/ncbi/europepmc/doi.org vb. proxy tarafından engelli).
Doğrulama ve indirme: yalnızca AWS PMC OA kovası (`https://pmc-oa-opendata.s3.amazonaws.com/`), `scripts/pmc_oa_fetch.py get
… --out basboyun/images/raw` ile. Kovada olmayan makale = OA alt kümesinde değil ⇒ atlandı.
Lisans `license_code` kova JSON'undan; atıf (`citation`), DOI, başlık, yazarlar, dergi, altyazılar (birebir) ve piksel
boyutları `scripts/build_basboyun_sources.py` tarafından indirilen JSON/XML/görüntü dosyalarından okunur → `sources/basboyun.json`.
`key_findings`/`clinical_relevance`/`notes` içindeki tırnaklı tüm alıntılar makale XML metninde birebir aranarak doğrulandı (0 eksik).
İndirilen her şekil Read aracıyla tek tek açılıp içerik, okunabilirlik ve görüntü üzerindeki etiketler kontrol edildi;
küçük/uygunsuz olanlar silindi (aşağıda). XML ayrıştırma `python3 -I` ile yapıldı. Toplam `basboyun/` ≈ 16 MB (45 şekil + 26 JSON/XML çifti).

## Sonuç özeti
27 kayıt / 26 makale / 45 şekil (PMC6420596 iki bölümde: beyin Fig. 1, kafa tabanı Fig. 2).
- Lisans: CC BY 20 makale; CC BY-NC 4 (PMC3026334, PMC3955795, PMC4347276, PMC5217945); CC BY-NC-SA 1 (PMC6251248). ND/lisanssız yok.
- beyin: kesit_lecture 3, topo_lecture 1, kesit_variation 3
- kafa_tabani: kesit_lecture 4, kesit_variation 2
- yuz_farinks: kesit_lecture 3, kesit_variation 3
- boyun: kesit_lecture 3, topo_lecture 1, kesit_variation 4

## Çalıştırılan aramalar (WebSearch)
1. Insights into Imaging pictorial review parapharyngeal space anatomy MRI labelled
2. Insights into Imaging deep neck spaces fascia anatomy CT pictorial review PMC
3. Insights into Imaging paranasal sinus CT anatomy variants pictorial review PMC
4. Insights into Imaging skull base foramina CT anatomy pictorial review
5. "Imaging of cranial nerves: a pictorial overview" Insights into Imaging PMC
6. "MRI of acute neck infections: evidence summary and pictorial review" PMC
7. circle of Willis variations MR angiography prevalence fetal PCA hypoplastic A1 open access PMC
8. Keros classification olfactory fossa CT prevalence Onodi Haller study PMC open access
9. Insights into Imaging larynx anatomy CT MRI pictorial review normal anatomy laryngeal spaces
10. Insights into Imaging orbit anatomy MRI pictorial review extraocular muscles labelled
11. Insights into Imaging temporal bone CT anatomy pictorial review middle ear inner ear
12. Insights into Imaging basal ganglia thalamus MRI anatomy pictorial review
13–16. (allowed_domains insightsimaging.springeropen.com) neck spaces / temporal bone / orbit / larynx-hypopharynx reviews
17. "A radiologic review of hoarse voice…" PMC; "Post traumatic deafness: a pictorial review…" PMC; Gomes temporal bone Radiol Bras
18. cavum septum pellucidum / cavum vergae prevalence MRI open access
19. elongated styloid process prevalence CT (Cureus/BMC/Diagnostics)
20. aberrant right subclavian artery prevalence CT angiography PMC open access
21. pyramidal lobe thyroid prevalence US/CT PMC; KJR 2015 multicentre title search
22. paranasal sinus variations concha bullosa Onodi Haller agger nasi Cureus
23. circle of Willis variants CTA prevalence (Sci Rep/Diagnostics/BMC)
24. high riding jugular bulb dehiscence prevalence temporal bone CT open access (2 kez) + temporal bone variations HRCT Cureus
25. retropharyngeal ICA / kissing carotids prevalence CT MRI open access
26. cervical lymph node levels CT labelled pictorial review (Insights/Cancer Imaging)
27. salivary gland ultrasound normal anatomy pictorial review open access
28. brainstem MRI anatomy labelled 7T atlas open access
29. thyroid ultrasound normal anatomy labelled PMC
30. Journal of Clinical Imaging Science labelled head-neck anatomy; larynx CT labelled CC BY; ostiomeatal complex CT labelled PMC; orbit MRI labelled PMC
31. cerebellum MRI labelled lobules pictorial review; basal ganglia labelled MRI CC BY; ventricular system MRI labelled
32. enlarged perivascular spaces / mega cisterna magna prevalence MRI
33. brain MRI labelled cortex sulci (insightsimaging domain); white matter/basal ganglia/hippocampus pictorial review; Lehman cerebellum atlas title
34. 7T basal ganglia STN GP labelled CC BY; hippocampus MRI pictorial review; Neuroradiology J / JBSR normal brain MRI
35. persistent trigeminal artery prevalence MRA (3 kez, Saltzman, Surg Radiol Anat 2023)
36. non-recurrent laryngeal nerve prevalence CT; carotid bifurcation level CTA PMC; optic canal / ICA dehiscence sphenoid CT
37. frontiers fnana.2025.1566762 (CSP) → PMC12131514
38. laryngeal cancer CT/MRI normal anatomy (Insights/Cancer Imaging); parapharyngeal prestyloid/poststyloid review CC BY; Radiol Bras paranasal sinus pictorial essay; infrahyoid neck spaces review
39. Pameijer JBSR "Imaging of the infrahyoid neck" (PMCID bulunamadı); JBSR neck reviews
40. (domain filtered) larynx normal axial CT; parapharyngeal/masticator space MRI pictorial review
41. "Pictorial Review of MRI Findings in Acute Neck Infections in Children" PMC
42. accessory parotid gland prevalence CT/MRI/US; Eagle syndrome styloid CT 3D
43. sphenoid sinus pneumatization optic/ICA protrusion CT prevalence PMC
44. cadaveric dissection deep cervical fascia carotid sheath open access

## Kovada kontrol edilip REDDEDİLEN / kullanılmayan adaylar
| PMCID | Konu | Neden |
|---|---|---|
| PMC3259331 | Insights Imaging 2010, kronik rinosinüzit/OMC anatomisi | `license_code` yok, XML'de lisans metni yok (eski Springer "open access") → lisanssız, ret |
| PMC4841358 | Pol J Radiol 2016, uncinate/OMC etiketli BT | CC kodu yok ("Unrestricted non-commercial use") → ret |
| PMC1434593 | Cancer Imaging 2004, boyun lenf nodu seviyeleri BT | lisans yok → ret |
| PMC1931513 | Cancer Imaging 2007, larinks normal BT anatomisi (etiketli) | lisans yok → ret (en iyi larinks BT adayıydı) |
| PMC5108369 | Med Sci Monit 2016, temporal kemik varyasyonları (yüksek bulbus juguli) | CC BY-NC-ND → ret |
| PMC9948571 | paraglottik boşluk endoskopik diseksiyon | CC BY-NC-ND → ret |
| PMC5552018 | retrofaringeal ICA vaka | CC BY-NC-ND → ret |
| PMC4721920 | retrofaringeal ICA pozisyon değişkenliği (Laryngoscope) | yazar el yazması (TDM), CC yok → ret |
| PMC2991531 | süpernümerer ekstraoküler kas MRG | yazar el yazması, CC yok → ret |
| PMC4220687 | 7T bazal ganglion etiketli (Front Hum Neurosci, CC BY) | Fig.1-3 "Adopted/Adapted with permission", Fig.4 "(Courtesy D. Ivanov)" → tüm şekiller ret |
| PMC6252390 | Front Neuroanat gyrus/sulcus terminolojisi (CC BY) | Fig.2 "Adapted from Tzourio-Mazoyer", Fig.3-6 izinli/uyarlanmış → ret |
| PMC3624744 | IJRI larinks kanseri görüntüleme | CC BY-NC-SA, normal anatomi şekillerinin altyazıları boş, patoloji ağırlıklı → kullanılmadı |
| PMC3475875 | kalıcı trigeminal arter (Surg Neurol Int) | CC BY-NC-SA, prevalans verisi yok (anatomik derleme/olgu) → kullanılmadı |
| PMC6861408 | ses kısıklığı radyolojik derleme (larinks/RLN şemaları) | normal anatomi yalnızca çizim; görüntüler patoloji → kullanılmadı (yedek: Fig.1 larinks, Fig.3 RLN seyri şemaları, CC BY) |
| PMC6386756 | talamus lezyonları (Insights) | normal anatomi yalnızca şema, geri kalanı patoloji → kullanılmadı |
| PMC10747582 | temporal kemik inflamatuvar patolojiler (Tomography) | normal anatomi şekli yok → kullanılmadı |
| PMC8755868 | orbita travması BT (Insights) | normal anatomi yok → kullanılmadı |
| PMC11598162 | orbita MR normatif ölçüm (Tomography, CC BY) | PMC9617817 tercih edildi (yedek) |
| PMC6472855 | Radiol Bras temporal kemik editoryali | şekil yok |
| PMC9640455 dışındaki US adayları PMC3542035, PMC4421527 | tiroid US | konu dışı (Hashimoto doku analizi / nefroloji vakası) |
| PMC11172921 | sağ arkus aorta meta-analiz (J Clin Med) | ARSA değil RAA; PMC7936046 tercih edildi |
| PMC12908009 | ARSA + sağ vertebral (Radiol Case Rep, CC BY) | vaka + veri tabanı; yedek |
| PMC6411572 | ARSA prevalansı BTA (J Korean Neurosurg Soc) | CC BY-NC; CC BY'li PMC7936046 tercih edildi (yedek) |
| PMC5363258 | non-rekürren laringeal sinir meta-analizi (PeerJ, CC BY) | şekiller şema/forest plot; PMC5217945 görüntü verdiği için tercih edildi (yedek: havuzlanmış prevalans) |
| PMC9768386, PMC10833526 | karotis bifurkasyon seviyesi (Cureus / PLoS ONE, CC BY) | PMC11246274 daha iyi etiketli; yedek |
| PMC12529820 | Eagle/stiloid HRCT 3D (Front Med, CC BY) | olgu-kontrol; prevalans yok; yedek |
| PMC3810670 | 7T beyin sapı (Front Hum Neurosci, CC BY) | PMC10651583 daha iyi etiketli; yedek |
| PMC8579044 | 7T pallidotalamik yollar (Front Neuroanat, CC BY) | traktografi odaklı; yedek |
| PMC9868889 Fig.3, PMC6377693 diğer şekiller, PMC9826778 Fig.9/10/18/19, PMC10296820 Fig.18/24, PMC5359145 Fig.5/12 | — | "modified from"/"with permission" ifadeleri veya patoloji → indirilmedi |
| PMC9497082 | genç erişkinlerde ePVS (Brain Sci) | şekil yalnızca akış şeması; PMC9512514 tercih edildi |
| PMC7051272, PMC4261488, PMC3976721, PMC4671896, PMC7055440 (Lehman serebellum atlası), PMC7144651, PMC5480796, PMC3552675, PMC2689563, PMC7965591 (servikal kosta, AJNR), PMC8562754, PMC5449872, PMC3699211, PMC10447682, PMC10112183 | — | AWS OA kovasında YOK → OA alt kümesinde değil, atlandı |

## İndirildikten sonra görsel kontrolde ELENEN dosyalar
- PMC4877355 Fig.1 (307x410) ve Fig.3 (kadavra, 307x275): çok küçük → silindi; yalnızca Fig.2 (520x517) kaldı.
- PMC6601480 Fig.3: kırpılmış, düşük kalite, tarayıcı cetveli/"tion" yazısı → silindi.
- PMC12721976 Fig.8: serebellar inme olguları (patoloji) → silindi.

## Görsel kontrol notları (önemli)
- PMC12085865 Fig.3 panel C'de tarayıcı katmanında "MOHAN" ve tarih benzeri metin var (hasta kimliği olabilir) → slaytta kırpılmalı.
- PMC6377693 Fig.1 karotis boşluğu şemasında University of Rochester "UR MEDICINE" logosu ve sanatçı imzası var → logo maskelenmeli.
- PMC5359145 (hipokampus) şekilleri küçük (394x358, 520x193); etiketler okunuyor ama yarım slayt boyutu önerilir.
- PMC6251248 tükürük bezi şekillerindeki etiket yazıları 605 px genişlikte küçük; Türkçe yeniden etiketleme önerilir.
- PMC9617817 orbita şekillerinde yalnızca ölçüm çizgileri/mm değerleri var; kas adları slayta eklenmeli.
- PMC6601480 CoW BTA şekilleri etiketsiz; ok/etiket eklenmeli.
- PMC12721976 Fig.3B şemasında yazım hatası "Whire matter".

## Boşluklar (bulunamayan / uygun lisanslı olmayan)
- Etiketli normal LARİNKS BT/MR anatomisi (CC BY): bulunamadı (PMC1931513 lisanssız, PMC3624744 BY-NC-SA ve altyazısız). Yerine laringeal US (PMC9640455 Fig.2) + VHP kesitleri önerilir.
- Etiketli normal ORBİTA MR atlası, etiketli normal OMK (ostiomeatal kompleks) BT, etiketli bazal ganglion/ventrikül MR (CC BY, izinsiz üçüncü taraf malzemesi olmayan): bulunamadı. Ventrikül/bazal ganglion için PMC9512514 Fig.2 ve PMC12131514 Fig.2 kısmen kullanılabilir; asıl etiketli kesit VHP'den.
- Parafaringeal boşluk için ayrı etiketli normal MR derlemesi bulunamadı (PMC9826778 Fig.2'de parafaringeal yağ işaretli).
- Varyasyon: yüksek/dehisan bulbus juguli (OA adaylar ND veya kovada yok), kalıcı trigeminal arter prevalansı (yalnızca CC BY-NC-SA olgu derlemesi), cavum vergae prevalansı (PMC12131514 vergae'li olguları dışladı), mega sisterna magna, servikal kosta (AJNR çalışması kovada yok), a. thyroidea ima, Onodi/optik kanal dehisansı için ayrı prevalans çalışması (yalnızca PMC12085865'te Onodi %13 ve PMC6472854'te görüntü), karotis kanalı dehisansı.
- Topo_lecture: boyun fasyası için gerçek kadavra diseksiyon fotoğrafı bulunamadı; E12 plastinat sagittal kesit (PMC9868889) kullanıldı. Beyin için serebellum sagittal diseksiyonu (PMC12721976).
