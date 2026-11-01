# -*- coding: utf-8 -*-
"""Bölüm kompozisyonu: metin slaytları (icerik_perine) + kadavra görsel slaytları (sources/perine_*.json)."""
from icerik_perine import *

KAPAK = []

def T(d, **kw):
    return dict(d, **kw)

BOLUMLER = [
    ("Pelvis", "Kısa giriş – perinenin kemik-fibröz çerçevesi ve tavanı",
     ["Pelvis major / minor, linea terminalis", "Apertura pelvis superior / inferior", "Ligg. sacrospinale & sacrotuberale",
      "Diaphragma pelvis ve fascia pelvis"], None,
     [PELVIS_TANIM, PELVIS_ACIKLIK, PELVIS_CINSIYET, PELVIS_BAG, PELVIS_TABAN, PELVIS_FASYA]),
    ("Perine – genel", "Tanım, sınırlar, üçgenler, corpus perineale",
     ["Derin ve yüzeyel sınırlar", "Regio urogenitalis / regio analis", "Corpus perineale"], None,
     [PERINE_TANIM, T(PERINE_UCGEN, tip="eskenar"), CORPUS_PERINEALE]),
    ("Regio urogenitalis", "Perine fasyaları, aralıklar, dış genital organ kökleri",
     ["Katmanlar: Colles – Gallaudet – membrana perinei", "Spatium perinei superficiale / profundum", "♂ radix penis, ♀ clitoris ve bulbi vestibuli", "Kaslar, klinik"], None,
     [T(KATMANLAR, tip="katman"), COLLES,
      dict(tip="ekstravazasyon", baslik="Colles fasyasının devamlılığı – idrar ekstravazasyonu", bolum=B3,
           metin=["Bulbar urethra yırtığı + fascia penis profunda (Buck) hasarında idrar/kan Colles fasyası altında yayılır: perine 'kelebek' hematomu, scrotum ve penis şişliği, karın ön duvarı (Scarpa altı).",
                  "Buck fasyası sağlamsa ekstravazasyon penis şaftı ile sınırlı kalır; pars membranacea yırtığında ise membrana perinei üstünde (spatium profundum → retropubik alan)."]),
      GALLAUDET, SPATIA_TABLO, KASLAR_TABLO, KLINIK_UROG]),
    ("Regio analis", "Fossa ischioanalis ve kontinans aparatı",
     ["Fossa ischioanalis sınırları ve recessus'lar", "M. sphincter ani externus", "Corpus anococcygeum"], None,
     [FOSSA_ISCHIOANALIS, SPHINCTER]),
    ("Damar – sinir", "N. pudendus, a. pudenda interna, canalis pudendalis",
     ["Seyir: foramen ischiadicum majus → minus → Alcock kanalı", "Dallar", "Lenfatik drenaj, klinik"], None,
     [T(PUDENDAL_SEMA, tip="pudendal"), PUDENDAL_KLINIK]),
]
