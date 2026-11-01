# Perineum – Topografik Anatomi (pelvise kısa giriş + ayrıntılı perine)

| Çıktı | Yol |
|---|---|
| Sunum (70 slayt, 16:9) | `perine/Perine_Topografik_Anatomi.pptx` |
| PDF | `perine/Perine_Topografik_Anatomi.pdf` |
| Slayt önizlemeleri (QA) | `perine/qa/png/` |

**Akış:** Kapak → Ders akışı → 1 Pelvis (kısa giriş: pelvis major/minor, apertura sup./inf., kadın–erkek farkı, ligg. sacrospinale/sacrotuberale, diaphragma pelvis, fascia pelvis) → 2 Perine – genel (sınırlar, üçgenler, corpus perineale, episiotomi) → 3 Regio urogenitalis (katmanlar, **perine fasyaları**: Colles–Scarpa–dartos devamlılığı, Gallaudet, membrana perinei; spatium superficiale/profundum, ♂/♀ diseksiyonlar, kaslar, klinik) → 4 Regio analis → 5 Damar–sinir (n. pudendus, a. pudenda interna, canalis pudendalis, lenfatik drenaj, klinik) → 6 Varyasyonlar (2 literatür tablosu + 9 çalışma slaytı) → Özet → Kaynakça.

**Dil ve punto:** Türkçe anlatım, Latince (TA2) terminoloji. Başlık 28 pt, gövde 17–19 pt, tablo 13–15 pt, görsel üzeri etiketler 12–13,5 pt. Konuşmacı notlarında özgün şekil altyazıları ve anlatım notları vardır.

**Görseller:** Yalnızca PubMed Central açık erişim makalelerinin özgün şekilleri (AWS PMC OA deposu; lisans makale bazında doğrulandı). Latince etiketler PowerPoint'in kendi (düzenlenebilir) şekilleridir; görüntünün üzerine çizilmez, kenardaki etiket sütunundan yapıya kılavuz çizgiyle bağlanır. Etiket koordinatları `sources/perine_*.json` → `label_points` (özgün piksel); her nokta yakınlaştırılmış kırpıntıda kontrol edildi ve slaytlar render edilip gözle denetlendi (`scripts/perine_qa_noktalar.py`).
* CC BY-NC-ND görseller (PMC8713160, PMC6785340, PMC7898478) kırpılmadan kullanıldı; CC BY-NC görseller yalnızca kırpıldı. Slaytta lisans notu vardır – ticari olmayan eğitim amaçlıdır.
* Yerel şemalar (perine eşkenar dörtgeni, katman yığını, Colles devamlılığı/ekstravazasyon, pudendal ağaç) "ŞEMA" etiketlidir; gerçek görüntü değildir.

**Bilinen boşluklar (açık erişimde bulunamadı):** Colles/Gallaudet/Buck fasyalarının etiketli kadavra fotoğrafı (CC lisanslı tek aday 267 px, NC-ND – reddedildi; Stanford Bassett koleksiyonu CC BY-SA ama bu ortamdan erişilemiyor), processus falciformis, fossa ischioanalis'in duvarları açık diseksiyonu, gl. vestibularis major kadavra fotoğrafı. Fasyalar bu nedenle şema + membrana perinei kadavra görselleri (PMC12229694, PMC13069139) + Scarpa türevi lig. fundiforme (PMC10594829) ile anlatıldı. Bassett görselleri elle indirilip `perine/images/` altına konursa sunuma eklenebilir.

**Yeniden üretim:**
```
python3 -I scripts/build_perine_pelvis.py; python3 -I scripts/build_perine_urogenital.py; python3 -I scripts/build_perine_anal.py
python3 -I scripts/build_perine.py && bash scripts/render.sh perine/Perine_Topografik_Anatomi.pptx
```
Betikler: `icerik_perine.py` (ders metni, tablolar), `perine_gorsel.py` (bölüm kompozisyonu, kırpma ve etiket seçimi), `perine_slayt.py` (slayt tipleri), `perine_sema.py` (yerel şemalar). Arama günlükleri: `sources/perine_*_arama_gunlugu.md`.

Not: Etiketler belgelenmiş kanıta göre yerleştirilmiştir; derste kullanmadan önce bir anatomi öğretim üyesinin kontrolü önerilir.
