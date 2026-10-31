# -*- coding: utf-8 -*-
"""Birleşik kaynak kayıt defteri: sources/*.json (topografik_kaynaklar + bolge_*) dosyalarını
PMCID → makale bilgisi ve şekil listesi olarak birleştirir. Aynı makale birden fazla dosyada
farklı şekillerle geçebilir; şekil listeleri birleştirilir."""
import json, pathlib, functools

ROOT = pathlib.Path(__file__).resolve().parent.parent

@functools.lru_cache(None)
def kayit():
    reg = {}
    for p in sorted((ROOT / "sources").glob("*.json")):
        if p.name.startswith("kesitsel"): continue
        for e in json.load(open(p)):
            r = reg.setdefault(e["pmcid"], dict(e, figures=[]))
            have = {f["file"] for f in r["figures"]}
            for f in e["figures"]:
                if f["file"] not in have:
                    r["figures"].append(f); have.add(f["file"])
    return reg

def makale(pmcid):
    return kayit()[pmcid]

def sekil(pmcid, anahtar):
    e = makale(pmcid)
    for f in e["figures"]:
        if anahtar in f["file"]:
            return f
    raise KeyError(f"{pmcid}: '{anahtar}' şekli bulunamadı ({[f['file'] for f in e['figures']]})")

def yol(pmcid, anahtar):
    return ROOT / sekil(pmcid, anahtar)["local_path"]

def baslik_noktali(e):
    t = e["title"].rstrip()
    return t if t.endswith((".", "?", "!")) else t + "."

def atif(pmcid, kisa=False):
    e = makale(pmcid)
    if kisa:
        ilk = e["authors"].split(",")[0].strip()
        return f"{ilk} ve ark., {e['year']} ({pmcid}, {e['license_code']})"
    return f"{e['authors']} {baslik_noktali(e)} {e['citation']} PMCID: {pmcid}. Lisans: {e['license_code']}."

def nc_mi(pmcid):
    return "NC" in makale(pmcid)["license_code"]
