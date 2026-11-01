# Perine Anatomisi – tıp öğrencisi düzeyi (pelvise kısa giriş + topografik perine)

| Çıktı | Yol |
|---|---|
| Sunum (41 slayt, 16:9) | `perine/Perine_Topografik_Anatomi.pptx` |
| PDF | `perine/Perine_Topografik_Anatomi.pdf` |
| Slayt önizlemeleri (QA) | `perine/qa/png/` |

**Sürüm 2 (revizyon):** Uzmanlık/PhD düzeyindeki ilk sürüm (70 slayt; git geçmişinde, PR #3) tıp öğrencilerine göre sadeleştirildi:
* Metinler kısa ve sınav odaklı; öğrenim hedefleri, özet ve "kendini değerlendir" soruları eklendi (cevaplar konuşmacı notunda).
* **Atlas çizimleri ağırlıkta** (8 çizim, 9 slayt): OpenStax *Anatomy & Physiology* (1. baskı, **CC BY**) – pelvis, kadın/erkek pelvisi, pelvis bağları, diaphragma pelvis, perine kasları (♂/♀), erkek genital/urethra, kadın sagittal, vulva. İngilizce etiketler silinip **Latince (TA)** karşılıklarıyla değiştirildi (`scripts/atlas_latince.py`; yazı yerleri RapidOCR ile bulundu, eşlemeler betikte elle yazılı; çizim ve kılavuz çizgileri değiştirilmedi).
* **Kadavra görselleri azaltıldı** (6 slayt): perinenin sınırları, erkek regio urogenitalis (yüzeyel aralık / membrana perinei), clitoris ve bulbus vestibuli, fossa ischioanalis, pelvis içinden n. pudendus; ayrıca 1 yazar çizimi (n. pudendus dalları).
* Araştırma ağırlıklı içerik (derin aralık tartışması, morfometri, 9 varyasyon çalışması) çıkarıldı; yerine kısa bir "sık varyasyonlar" tablosu kondu.
* Not: Netter vb. ticari atlas görselleri telif nedeniyle kullanılmadı; açık lisanslı OpenStax çizimleri tercih edildi.

**Akış:** Kapak → Öğrenim hedefleri → 1 Pelvis → 2 Perine – genel → 3 Regio urogenitalis (perine fasyaları, aralıklar, kaslar, ♂/♀) → 4 Regio analis → 5 Damar–sinir → 6 Klinik–özet (varyasyonlar, özet, sorular) → Kaynakça.

**Punto:** başlık 28, metin 15–20, tablolar 15–16; atlas etiketleri görüntüye işlenmiştir.

**Lisanslar:** OpenStax CC BY (uyarlama: etiket çevirisi, slaytta belirtilmiştir). PMC görselleri makale bazında doğrulandı; CC BY-NC-ND olanlar (PMC7898478, PMC8713160) kırpılmadan kullanıldı ve slaytta işaretlidir.

**Yeniden üretim:**
```
python3 -I scripts/atlas_latince.py            # perine/images/atlas_raw → perine/images/atlas (+ sources/perine_atlas.json)
python3 -I scripts/build_perine.py && bash scripts/render.sh perine/Perine_Topografik_Anatomi.pptx
```
Atlas kaynağı: github.com/philschatz/anatomy-book (OpenStax A&P, CC BY), commit eadaa6b; özgün dosyalar `perine/images/atlas_raw/`.
Betikler: `icerik_perine.py` (ders metni), `perine_gorsel.py` (kompozisyon), `perine_slayt.py` (slayt tipleri), `perine_sema.py` (şemalar).

Etiketler belgelenmiş kaynaklara göre yerleştirilmiştir; derste kullanmadan önce bir anatomi öğretim üyesinin kontrolü önerilir.
