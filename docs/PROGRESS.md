# İlerleme Raporu

## 2026-10-31 — Oturum 1

### Yapılan
- Klasör yapısı: `topografik/`, `kesitsel/` (her birinde `slides/` spec, `images/` + `PROVENANCE.csv`, `sources/`), `pipeline/`, `docs/`.
- `pipeline/build_deck.py`: YAML slayt tanımından .pptx üretir, LibreOffice ile PDF'e, `pdftoppm` ile PNG önizlemeye çevirir.
  Görsel, `PROVENANCE.csv`'de lisanslı satırı yoksa build durur (kaynaksız görsel girmez).
- Ortam: python-pptx 1.0.2, Pillow, LibreOffice, pdftoppm, ImageMagick mevcut. Görselsiz test slaytı başarıyla render edildi.

### Engeller (pilot slaytlar üretilemedi)
1. **Ağ politikası:** bulut ortamı yalnızca paket yöneticilerine + GitHub'a izin veriyor. Şu hostlar reddedildi:
   `commons.wikimedia.org`, `upload.wikimedia.org`, `data.lhncbc.nlm.nih.gov` (Visible Human), `www.ncbi.nlm.nih.gov` (PMC),
   `openi.nlm.nih.gov`, `radiopaedia.org`. Gerçek kadavra/BT/MR görseli indirilemedi. README gereği sahte/üretilmiş görsel konmadı.
2. **Ana Türkçe şartname eksik:** README sonunda `[PASTE THE FULL TURKISH MASTER PROMPT HERE]` yer tutucusu duruyor.

### Sonraki Adım
- Ortam ayarlarında (Network access) yukarıdaki domainleri Allowed domains'e ekle; ek olarak önerilen:
  `europepmc.org`, `*.ncbi.nlm.nih.gov`, `ftp.ncbi.nlm.nih.gov`, `api.openverse.org`.
- Türkçe ana şartnameyi README'ye yapıştır.
- Ardından: görsel envanteri (PROVENANCE) → 10 topografik + 10 kesitsel pilot slayt → render + görsel kontrol.
