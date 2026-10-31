# Kesitsel anatomi – veri kaynakları ve yeniden üretim

## Veri
**NLM Visible Human Project – Visible Human Male (VHP-M)**, NCI Imaging Data Commons (IDC) koleksiyonu
`nlm_visible_human_project` (doi:10.5281/zenodo.12690049) üzerinden, herkese açık `s3://idc-open-data`
deposundan (HTTPS: `https://idc-open-data.s3.amazonaws.com/`) alınmıştır.

Lisans: *National Library of Medicine Terms and Conditions; May 21, 2019* (IDC indeksindeki `license_short_name`).

Kullanılan seriler (tam liste ve UID'ler: `sources/kesitsel_kaynaklar.json`):

| Rol | IDC seri UUID | Not |
|---|---|---|
| Kriyokesit `a_vm####` (2048×1216 RGB, 0,33 mm/piksel, 1 mm aralık, 1001–2878) | 4aaf9181-fb6a-4a4c-bf49-d1eb9ed4a385 | ~7,5 MB/kesit |
| Donmuş BT `c_vm####.fro` (512², 0,9375 mm, 1 mm, FOV 480 mm) | f3a311eb…, aa81356d…, 3455adc0… | 3 seri = 1877 kesit (1006–2882) |
| Taze BT `c_vm####.fre` (3 mm / 5 mm) | 477cf391…, 29c772e1… | kullanılmadı (FOV 460 mm) |
| MR T1/T2 aksiyel | a83c457a…, 342d9e2a… | yalnız baş bölgesi – ekstremite için uygun değil |

## Düzey eşleştirme (uydurma eşleştirme yok)
* Her DICOM örneğinde özel etiket **(0009,1001)** özgün NLM dosya adını taşır (ör. `Visible-Human/Male-Images/radiological/frozenCT/c_vm1749.fro`)
  ve **SliceLocation** aynı numarayı verir. Kriyokesitte `ImagePositionPatient z = −(kesit no.)`.
* NLM belgeleri (Ackerman 1995, D-Lib Magazine; Spitzer ve ark. 1996, JAMIA) erkek veri setinde anatomik kesitlerin 1 mm aralıklı olduğunu ve
  BT aksiyel görüntüleriyle çakıştığını belirtir. Bu projede **aynı kesit numarası = aynı düzey** kabul edilmiş, ek bir düzey tahmini yapılmamıştır.
* Düzlem içi hizalama: ölçek sabit (0,33/0,9375); öteleme gövde maskeleri çapraz korelasyonu (Dice 0,84–0,93), ardından uzuv bölgesinde yerel
  arama (doku Dice 0,94–0,97; kayma 4–7 BT pikseli ≈ 4–7 mm – kesitleme öncesi blok ayırma sırasında uzuv hareketi ile uyumlu).
* Kriyokesit DICOM yönelimi `[1,0,0, 0,−1,0]`: görüntü dikey çevrilerek BT ile aynı radyolojik yönelime getirildi
  (doğrulama: kalp/karaciğer tarafı, penis ve ellerin ön konumu; BT kemik konturlarının çakışması).

## Yeniden üretim
```bash
pip install -r requirements.txt
python3 scripts/vhp_index_headers.py <seri-uuid> ...   # yalnız başlıklar (HTTP Range), kesitsel/vhp_index/*.csv
python3 scripts/vhp_crops.py                           # 9 düzeyin kriyo + BT kırpımları (kesitsel/images/vhp)
python3 scripts/vhp_assets.py                          # konum küçük resimleri + koronal BT MIP
python3 scripts/build_kesitsel.py                      # PPTX
scripts/render.sh kesitsel/Kesitsel_Anatomi_Pilot.pptx # PDF + PNG önizleme
```
Ham DICOM'lar depoya eklenmez; yalnızca seçilmiş kırpımlar (JPEG/PNG) ve indeks CSV'leri saklanır.
İndirilen DICOM önbelleği: `/tmp/vhp_cache` (oturum sonunda silinir).

## Kaynakça
1. Spitzer V, Ackerman MJ, Scherzinger AL, Whitlock D. The Visible Human Male: a technical report. *J Am Med Inform Assoc.* 1996;3(2):118–130.
2. Ackerman MJ. Accessing the Visible Human Project. *D-Lib Magazine*, October 1995.
3. Fedorov A, et al. National Cancer Institute Imaging Data Commons: toward transparency, reproducibility, and scalability in imaging AI. *RadioGraphics.* 2023;43(12):e230180.
