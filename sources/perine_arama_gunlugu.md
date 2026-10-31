# Perine ve Pelvis – kaynak arama günlüğü

Tarih: 2026-10-31. Keşif: WebSearch (çoğu `allowed_domains: pmc.ncbi.nlm.nih.gov`). Doğrulama ve indirme yalnızca AWS PMC OA bucket'ından (`scripts/pmc_oa_fetch.py info/get --out perine/images/raw`). Bucket'ta olmayan makaleler OA alt kümesinde değildir, atlandı. Lisans = bucket JSON'daki `license_code`.
Çıktı: `sources/perine.json` (`python3 -I scripts/build_perine_sources.py` ile üretilir; atıf/DOI/lisans/başlık/yazar/altyazı/piksel değerleri indirilen dosyalardan okunur; betik, JSON'da kullanılmayan "yetim" görsel kalmadığını da denetler). İndirilen her görsel Read ile açılıp incelendi; görselin üzerindeki etiketler `labels_visible_in_image` alanına elle yazıldı.

Sonuç: 28 makale, 47 görsel, toplam ~9,7 MB. Lisans: 25 CC BY, 3 CC BY-NC (işaretli: PMC3381476, PMC2810586, PMC12519013).

## Yapılan aramalar (özet)
1. cadaveric dissection perineal membrane Colles fascia superficial perineal pouch (genel + PMC)
2. Denonvilliers fascia histology cadaver
3. pudendal nerve branching variations cadaver / ischioanal fossa / pudendal canal
4. perineal body anatomy dissection female cadaver levator ani
5. Insights into Imaging MRI anatomy perineum pelvic floor pictorial review
6. Fournier gangrene fascial planes imaging (genel, PMC, Cureus)
7. Murakami/Jin perineal histology (Anat Cell Biol)
8. ischioanal fossa / Alcock canal cadaver; pudendal canal histology fetuses
9. accessory pudendal artery prevalence; internal pudendal artery branching (cadaver/CTA)
10. levator ani avulsion prevalence TPUS; levator ani subdivisions
11. endoanal ultrasound anal sphincter normal anatomy; OASI ultrasound perineal body
12. vestibular bulb / clitoris / Bartholin dissection
13. MRI female perineum / vulva; anal sphincter MRI perianal fistula
14. Waldeyer / rectosacral / mesorectal fascia
15. US-guided pudendal block sonoanatomy (genel + PMC)
16. perineal hernia imaging/anatomy
17. Buck's fascia / dartos / tunica albuginea; scrotal layers Colles–Scarpa continuity
18. urethral injury urine extravasation imaging
19. male rhabdosphincter / membranous urethra
20. anococcygeal ligament/body histology
21. EAS morphology variation MRI; inferior rectal nerve origin variation
22. sacrospinous ligament–pudendal nerve distances

## Seçilen makaleler (bölüme göre)
| Bölüm | Kullanım | PMCID | Lisans | Kısa |
|---|---|---|---|---|
| taban | topo | PMC8096964 | CC BY | ATLA/obturator fasya, LAM fasyası (kadavra + frontal kesit) |
| taban | topo | PMC6942605 | CC BY | Kadın perine kasları, üç kas askısı (kadavra + şema) |
| taban | topo | PMC7182620 | CC BY | Erkek pelvis tabanı, LA–EAS–ACL bağlantıları |
| taban | topo | PMC4549266 | CC BY | Chinese Visible Human kesitleri: LA, EAS, perineal body 3D |
| taban | kesit | PMC8253870 | CC BY | 3D TPUS'ta LA alt bölümleri |
| taban | variation | PMC5593956 | CC BY | Doğum sonrası LA avülsiyonu %13,75 (TUI + MRI) |
| taban | topo | PMC3381476 | CC BY-NC | Anococcygeal ligament vs raphe (histoloji + şema) |
| fasya | topo | PMC13069139 | CC BY | Perineal membran / derin poş: diseksiyon + stereoloji |
| fasya | topo | PMC12229694 | CC BY | Katmanlı perine (STP → PM → düz kas), erkek/kadın + şema |
| fasya | topo | PMC4022307 | CC BY | Rabdosfinkter–LA–perineal membran histolojisi + kadın şeması |
| fasya | topo | PMC4433060 | CC BY | Denonvilliers çok yapraklı histoloji |
| fasya | topo | PMC9843937 | CC BY | Denonvilliers tek katlı "Y" (kadavra) |
| fasya | topo | PMC8571354 | CC BY | Denonvilliers mikro-BT + Masson; TME planları şeması |
| fasya | topo | PMC8995278 | CC BY | Denonvilliers ve anterior mezorektal planlar (kadavra) |
| fasya | topo | PMC2810586 | CC BY-NC | Presakral, rektal proper (mezorektal), rektosakral (Waldeyer) fasya |
| urogenital | kesit | PMC13013239 | CC BY | Klitoris/bulbus vestibuli MRI + ürogenital üçgen çizimi |
| urogenital | kesit | PMC12732017 | CC BY | Normal penis MRI (tunika, Buck/dartos metni) |
| anal | kesit | PMC13512459 | CC BY | Anal kanal şeması + etiketli normal MRI (IRF) |
| anal | kesit | PMC9955566 | CC BY | EAUS vs TPUS mid-anal kanal |
| anal | variation | PMC13308972 | CC BY | Perineal body boyutu (n=148, 3D EAUS) |
| damar_sinir | variation | PMC9492552 | CC BY | Pudendal sinir gövde tipleri (52 hemipelvis) |
| damar_sinir | variation | PMC12519013 | CC BY-NC | Pudendal sinir oluşumu/gövde varyantları |
| damar_sinir | variation | PMC12908042 | CC BY | Sistematik derleme: kök ve gövde prevalansı |
| damar_sinir | variation | PMC11961128 | CC BY | A. pudenda interna + a. rectalis media ortak gövde %24 |
| damar_sinir | kesit | PMC12840153 | CC BY | Pudendal sinir seyri 4 düzeyde T1 MRI (Alcock) |
| klinik | topo | PMC7913006 | CC BY | Epizyotomi riski: 47 kadavra + şema |
| klinik | kesit | PMC11304407 | CC BY | Fournier gangreni BT |
| klinik | kesit | PMC9668258 | CC BY | Translevator perineal herni MRI + şema |

## Reddedilen / atlanan adaylar
| PMCID | Konu | Neden |
|---|---|---|
| PMC2775042 | Perineal membrane in females (DeLancey) | Bucket'ta yok (OA değil) |
| PMC7163926 | Denonvilliers, Cancer Commun | CC BY-NC-ND |
| PMC7047600 | Fournier gangrene CT/US/MRI (CARJ) | Author manuscript, lisans TDM |
| PMC9544139 | Surgical anatomy of the vaginal introitus | CC BY-NC-ND |
| PMC9344198 | 3D MRI perineal membrane | TDM (author manuscript) |
| PMC12997456 | Bulboclitoris anatomy (radiotherapy) | TDM |
| PMC8376743 | Photogrammetry pelvic floor fascicles | TDM |
| PMC6003834, PMC4140951, PMC10513003, PMC3277789 | Anal sfinkter MRI normları, LA lif yönü, vb. | TDM (author manuscript) |
| PMC1472875, PMC3474057, PMC3746407, PMC3312188, PMC5827285, PMC1571491, PMC1232908, PMC3949029, PMC4956015, PMC5642855, PMC4734920, PMC10996428, PMC6565404, PMC11496422, PMC7542186, PMC4209220, PMC4483306 | Çeşitli (pelvis tabanı, endoanal US derlemesi, penis MRI, Colles/Scarpa tarihçe, dorsal penil sinir, Fournier US...) | Bucket'ta yok |
| PMC11375228 | TME derlemesi (Ann Coloproctol) | CC BY-NC ve şekillerin çoğu "Adapted/Reprinted from Kim..." – orijinal kaynak PMC2810586 tercih edildi |
| PMC8624255 | Vulvar cancer MRI (illustration) | Fig 5 "modified from Protzel et al."; Fig 2 basit yüzey çizimi – gerekmedi |
| PMC4752977 | Urethral bulb & continence | Fig 2 Wikipedia'dan uyarlanmış, Fig 5–7 "©Peter Rehder" |
| PMC6444342, PMC11791247, PMC12271287, PMC5772902, PMC13231030, PMC8784283 | IIA CTA, pudendal blok (çocuk/hemoroid), anterior perineal herni, pelvik nörovasküler, Fournier US/BT | CC BY-NC-ND |
| PMC3731464 | Urethral/peri-urethral lesions MRI (Insights Imaging 2013) | CC BY-NC; normal perineal anatomi figürü yok |
| PMC2844751 | MRI in perianal fistulae – normal sfinkter MRI | İndirildi, sonra çıkarıldı: 616x449, etiketler çok küçük; PMC13512459 daha iyi |
| PMC5639160 | Anal kanal kanseri MRI (Fig 1–2 numaralı anatomi) | CC BY-NC; PMC13512459 yeterli olduğundan indirilmedi (yedek) |
| PMC12999470 | Subgluteal internal pudendal ven (kadavra) | İndirildi, sonra çıkarıldı: Fig 6 yalnız a/b harfli, didaktik değeri düşük |
| PMC8467746 | Female pelvic floor fascia systematic review | CC BY ama tek figür PRISMA; metin kaynağı olarak kullanılabilir |
| PMC13477793 | Alcock kanalında PNE sistematik derleme | CC BY ama tek figür PRISMA |
| PMC9600881 | Fournier imaging (Diagnostics) | CC BY; figürler perianal fistül/abse MRI, fasyal yayılım net değil – yedek |
| PMC4279881 | IIA dallanma (Adachi) | CC BY; PMC11961128 daha iyi pudendal örnek verdiği için indirilmedi (yedek) |
| PMC13291358, PMC7687169 | Anterior perineal herni olgu | CC BY; PMC9668258 (MRI + şema) tercih edildi – yedek |
| PMC13401730 | RUG/VCUG resimli derleme (Cureus) | CC BY; ekstravazasyon/fasyal yayılım figürü kontrol edilmedi – yedek (bkz. boşluklar) |
| PMC12519013 Fig 4 | Kaliperle ölçüm fotoğrafları | Didaktik değeri düşük, silindi |
| PMC4433060 Fig 5, PMC8995278 Fig 1 | İntraop foto + kaba şema / etiketsiz sagital kesit | Silindi |

## Lisans / provenance uyarıları
- PMC13013239 Fig 2: altyazı "Illustration © 2025 Elise Butler" ile bitiyor, görselde ressam imzası var; makale CC BY 4.0. Ressama atıfla CC BY kabul edilebilir, ancak katı politikada çıkarılmalı.
- PMC8571354 Fig 5: kurum içi medikal illüstratöre teşekkür (izin/telif notu yok) – CC BY.
- PMC9492552: özet "inferior gluteal nerve piercing the sacrospinous ligament" derken Fig 3 altyazısı "inferior rectal nerve" diyor; alıntıda dikkat.
- PMC4549266 kesitleri Chinese Visible Human veri tabanından (yazarların kendi rekonstrüksiyonu) – telif notu yok.

## Boşluklar (bulunamayanlar)
- **Colles fasyası / Scarpa–dartos sürekliliği / Buck fasyası** için açık lisanslı kadavra fotoğrafı veya histoloji bulunamadı (PMC3312188, PMC5827285 OA değil). Öneri: VHP kesitleri + kendi şemamız; metin için PMC11304407 ve PMC12732017 alıntıları.
- **Yüzeyel perineal poşun (Colles fasyası açılarak) erkek diseksiyonu** – özel bir figür yok; PMC12229694 Fig 1 ve PMC13069139 Fig 1–2 en yakın.
- **Alcock kanalının açılmış kadavra fotoğrafı / histolojisi** – OA bulunamadı; PMC13013239 Fig 2 (çizim), PMC12840153 Fig 1 (MRI) ve PMC4549266 kesitleri ile karşılanabilir.
- **İdrar ekstravazasyonu** (RUG/BT) için CC BY, fasyal sınırları gösteren görüntü doğrulanamadı (PMC10996428 OA değil; PMC13401730 incelenmedi).
- **US eşliğinde pudendal blok sonoanatomisi**: tüm adaylar ND veya OA dışı.
- **Aksesuar pudendal arter** prevalans çalışmaları OA değil; dorsal penil/klitoral sinir seyri (PMC7542186) OA değil.
- **Perineal membranın MRI'ı** (PMC9344198) TDM.
- **Bartholin bezi diseksiyonu**: yalnız şemalarda (PMC7913006 Fig 3, PMC13013239 Fig 2).
- Endopelvik fasya için ayrı bir kadın kadavra figürü yok (PMC8096964 ATFP ile kısmen).
