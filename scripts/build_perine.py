#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perine – topografik anatomi sunumu, tıp öğrencisi düzeyi (pelvise kısa giriş + perine).
Akış: Kapak → Öğrenim hedefleri → 1 Pelvis → 2 Perine genel → 3 Regio urogenitalis → 4 Regio analis
→ 5 Damar–sinir → 6 Klinik–özet (varyasyonlar, özet, sorular) → Kaynakça. Görseller: OpenStax atlas çizimleri (Latince etiketli) + seçilmiş kadavra.
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
         "calisma": P.calisma, "atlas": P.atlas_slayt, "eskenar": S.perine_eskenar, "katman": S.katman_yigini,
         "ekstravazasyon": S.ekstravazasyon, "pudendal": S.pudendal_agac}[t]
    f(prs, d, sayfa)
    for r in [d.get("fig")] + [x["fig"] for x in d.get("figler", [])]:
        if r: KULLANILAN.append(r[1])


KULLANILAN = []


def build():
    prs = P.new_deck(); n = 1
    P.kapak(prs, "Perine Anatomisi", "Pelvise kısa giriş ve perinenin topografik anatomisi – tıp öğrencileri için",
            ["Latince etiketli atlas çizimleri ve seçilmiş kadavra görüntüleri",
             "Perine fasyaları, aralıklar, kaslar, damar ve sinirler",
             "Klinik bağlantılar ve kendini değerlendirme soruları"], G.KAPAK)
    n += 1
    ciz(prs, I.HEDEFLER, n); n += 1
    for no, (ad, alt, konular, kapak_ref, slaytlar) in enumerate(G.BOLUMLER, 1):
        P.bolum_kapak(prs, no, ad, alt, konular, kapak_ref, n); n += 1
        for d in slaytlar:
            ciz(prs, d, n); n += 1
    KULLANILAN.extend(["PMC9492552", "PMC6449584", "PMC3971847"])  # varyasyon tablosunda atıf yapılan çalışmalar
    n = P.kaynakca(prs, KULLANILAN, I.TEMEL_KAYNAK, n)
    out = ROOT / "perine" / "Perine_Topografik_Anatomi.pptx"; out.parent.mkdir(exist_ok=True)
    prs.save(out); print(out, len(prs.slides), "slayt")


if __name__ == "__main__":
    build()
