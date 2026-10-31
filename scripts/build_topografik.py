#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Topografik anatomi sunumu (uzun, bölümlü): Giriş → Omuz → Kol → Önkol → El.
Her bölüm: kapak → konu anlatımı (metin/tablo) → diseksiyon görselleri → klinik bağlantılar →
varyasyon literatür taraması (tablo) → seçilmiş çalışmalar (görsel + özet).
Çıktı: topografik/Topografik_Anatomi.pptx"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from slayt_tipleri import *
import icerik_topografik as IT
import icerik_topo_ek as EK
import icerik_anlatim as AN

ROOT = pathlib.Path(__file__).resolve().parent.parent
EKLER = {"omuz": (EK.OMUZ_DIS, EK.OMUZ_LIT, EK.OMUZ_CAL), "kol": (EK.KOL_DIS, EK.KOL_LIT, EK.KOL_CAL),
         "onkol": (EK.ONKOL_DIS, EK.ONKOL_LIT, EK.ONKOL_CAL), "el": (EK.EL_DIS, EK.EL_LIT, EK.EL_CAL)}
KAPAK_GORSEL = {"omuz": [("vhp_crop", 1320, "VHP-M kesit 1320"), ("pmc", "PMC5992113", "Fig1")],
                "kol": [("vhp_crop", 1490, "VHP-M kesit 1490"), ("pmc", "PMC10514118", "Fig3")],
                "onkol": [("vhp_crop", 1740, "VHP-M kesit 1740"), ("pmc", "PMC6850211", "g001")],
                "el": [("vhp_crop", 1830, "VHP-M kesit 1830"), ("pmc", "PMC12823052", "i02")]}

def tip_ciz(prs, d, sayfa, bolum):
    t = d.get("tip", "duzyazi")
    if t == "duzyazi": return duzyazi(prs, d, sayfa, bolum)
    if t in ("anlatim", "klinik"): return anlatim(prs, d, sayfa, bolum)
    if t == "tablo": return tablo(prs, d, sayfa, bolum)
    if t == "sema_plexus": return sema_plexus(prs, d, sayfa, bolum)
    if t == "sema_arter": return sema_arter(prs, d, sayfa, bolum)
    if t == "gorsel": return gorsel(prs, d, sayfa, bolum)
    raise ValueError(t)

def pmc_topla(liste):
    out = []
    for d in liste:
        for r in d.get("figs") or []:
            if r[0] == "pmc": out.append(r[1])
    return out

def build():
    prs = new_deck(); sayfa = 1; kullanilan = []
    kapak(prs, "Membrum Superius – Topografik Anatomi",
          "Konu anlatımı, gerçek kadavra diseksiyonları ve bölgesel varyasyon literatür taraması",
          ["Bölümler: Omuz → Kol → Önkol → El",
           "Her bölümün sonunda o bölgeye ait anatomik varyasyonların literatür taraması ve çalışmaların özgün görselleri",
           "Görseller: PubMed Central açık erişim (lisans makale bazında doğrulandı) ve NLM Visible Human Project",
           "Sıklık verileri makalelerden aynen aktarılmıştır."],
          [("pmc", "PMC8958867", "i04"), ("pmc", "PMC12206543", "i01"), ("pmc", "PMC12500735", "Fig4"), ("pmc", "PMC12823052", "i02")])
    sayfa += 1
    icindekiler(prs, IT.BOLUMLER, "Giriş: bölgeler, plexus brachialis şeması, arteriyel ağaç, venöz ve lenfatik drenaj", sayfa); sayfa += 1
    for d in AN.TOPO["giris"] + IT.GIRIS:
        sayfa += tip_ciz(prs, d, sayfa, "GİRİŞ")
    kullanilan += pmc_topla(IT.GIRIS)
    for no, b in enumerate(IT.BOLUMLER, 1):
        dis, lit, cal = EKLER[b["kod"]]
        sayfa += bolum_kapak(prs, no, b, KAPAK_GORSEL[b["kod"]], sayfa)
        etk = f"BÖLÜM {no} · {b['ad']}"
        anl = [d for d in b["slaytlar"] if d["tip"] != "klinik"]
        kli = [d for d in b["slaytlar"] if d["tip"] == "klinik"]
        for d in AN.TOPO[b["kod"]] + anl:
            sayfa += tip_ciz(prs, d, sayfa, etk)
        for d in dis:
            sayfa += gorsel(prs, dict(d, etiket=d.get("etiket", "DİSEKSİYON")), sayfa, etk)
        for d in kli + AN.TOPO[b["kod"] + "_var"]:
            sayfa += tip_ciz(prs, d, sayfa, etk)
        # literatür taraması tablosu (en çok 5 satır/slayt)
        sayfa += lit_tablo(prs, f"{b['ad'].capitalize() if b['kod'] != 'onkol' else 'Önkol'} bölgesi varyasyonları – literatür taraması",
                           "Kadavra çalışmaları, seriler ve olgu sunumları (PMC açık erişim)", lit, sayfa, etk)
        for d in cal:
            sayfa += gorsel(prs, d, sayfa, etk)
        kullanilan += pmc_topla(b["slaytlar"]) + pmc_topla(dis) + pmc_topla(cal)
    sayfa = kaynakca(prs, kullanilan, "Kaynakça ve görsel lisansları", sayfa)
    out = ROOT / "topografik" / "Topografik_Anatomi.pptx"; prs.save(out)
    print(out, len(prs.slides), "slayt")

if __name__ == "__main__":
    build()
