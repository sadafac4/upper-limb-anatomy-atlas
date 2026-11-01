#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perine – topografik anatomi sunumu (pelvise kısa giriş + ayrıntılı perine).
Akış: Kapak → Ders akışı → 1 Pelvis → 2 Perine genel → 3 Regio urogenitalis (fasyalar, aralıklar, ♂/♀)
→ 4 Regio analis → 5 Damar–sinir → 6 Varyasyonlar (literatür) → Özet → Kaynakça.
Çıktı: perine/Perine_Topografik_Anatomi.pptx   Çalıştır: python3 -I scripts/build_perine.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import perine_slayt as P
import perine_sema as S
import icerik_perine as I
import perine_gorsel as G

ROOT = pathlib.Path(__file__).resolve().parent.parent


def ciz(prs, d, sayfa):
    t = d.get("tip", "anlatim")
    if "not_" in d: d = dict(d, **{"not": d["not_"]})
    f = {"anlatim": P.anlatim, "klinik": P.anlatim, "tablo": P.tablo, "kadavra": P.kadavra, "iki": P.iki_gorsel,
         "calisma": P.calisma, "eskenar": S.perine_eskenar, "katman": S.katman_yigini,
         "ekstravazasyon": S.ekstravazasyon, "pudendal": S.pudendal_agac}[t]
    f(prs, d, sayfa)
    for r in [d.get("fig")] + [x["fig"] for x in d.get("figler", [])]:
        if r: KULLANILAN.append(r[1])


KULLANILAN = []


def build():
    prs = P.new_deck(); n = 1
    P.kapak(prs, "Perineum – Topografik Anatomi", "Pelvise kısa giriş ve perinenin ayrıntılı anatomisi: sınırlar, fasyalar, aralıklar, damar ve sinirler",
            ["Gerçek kadavra diseksiyonları üzerinde Latince etiketli yapılar",
             "Perine fasyaları: Colles, Gallaudet, membrana perinei – güncel kavramlar",
             "Klinik bağlantılar ve varyasyon literatürü (PMC açık erişim)"], G.KAPAK)
    n += 1
    akis = dict(tip="anlatim", baslik="Ders akışı", etiket="ÖZET", metin=[
        "**1. Pelvis** – kısa giriş: pelvis major/minor, apertura pelvis superior/inferior, bağlar, diaphragma pelvis, fascia pelvis",
        "**2. Perine – genel**: tanım, sınırlar, regio urogenitalis ve regio analis, corpus perineale",
        "**3. Regio urogenitalis**: katmanlar ve **perine fasyaları** (Colles, Gallaudet, membrana perinei), spatium perinei superficiale/profundum, ♂ ve ♀ dış genital kökleri, kaslar",
        "**4. Regio analis**: fossa ischioanalis, canalis analis ve sfinkterler, corpus anococcygeum",
        "**5. Damar–sinir**: n. pudendus, a. pudenda interna, canalis pudendalis; lenfatik drenaj; klinik",
        "**6. Varyasyonlar**: seçilmiş kadavra çalışmaları ve özgün görselleri",
    ], boyut=20)
    ciz(prs, akis, n); n += 1
    for no, (ad, alt, konular, kapak_ref, slaytlar) in enumerate(G.BOLUMLER, 1):
        P.bolum_kapak(prs, no, ad, alt, konular, kapak_ref, n); n += 1
        for d in slaytlar:
            ciz(prs, d, n); n += 1
    n = P.kaynakca(prs, KULLANILAN, I.TEMEL_KAYNAK, n)
    out = ROOT / "perine" / "Perine_Topografik_Anatomi.pptx"; out.parent.mkdir(exist_ok=True)
    prs.save(out); print(out, len(prs.slides), "slayt")


if __name__ == "__main__":
    build()
