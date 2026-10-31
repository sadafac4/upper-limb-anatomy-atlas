#!/usr/bin/env python3
"""Print metadata, abstract and verbatim captions of downloaded figures for one PMC raw folder.
Usage: python3 -I scripts/el_extract.py topografik/images/raw/PMC123 [--abstract]"""
import json, pathlib, sys, xml.etree.ElementTree as ET
XL = "{http://www.w3.org/1999/xlink}href"
def t(e): return " ".join("".join(e.itertext()).split()) if e is not None else ""
d = pathlib.Path(sys.argv[1]); x = next(d.glob("*.xml")); j = json.loads(next(d.glob("*.json")).read_text())
root = ET.parse(x).getroot(); meta = root.find(".//article-meta")
au = [f"{t(c.find('name/surname'))} {t(c.find('name/given-names'))}" for c in meta.findall(".//contrib[@contrib-type='author']") if c.find('name') is not None]
print("PMCID", d.name, "| ver", x.stem.split('.')[-1], "| lic", j.get("license_code"), "| doi", j.get("doi"))
print("CIT", j.get("citation")); print("TITLE", t(meta.find(".//article-title"))); print("AUTH", au[:3], len(au))
print("JOUR", t(root.find(".//journal-title")))
files = {p.name for p in d.glob("*.jpg")}
for f in root.iter("fig"):
    gs = [g.get(XL) for g in f.iter("graphic")]
    if any(any(fn.startswith(g + ".") or fn == g for fn in files) for g in gs if g):
        print(f"\n[{t(f.find('label'))}] {gs}\n{t(f.find('caption'))}")
if "--abstract" in sys.argv:
    print("\nABSTRACT:", t(meta.find(".//abstract")))
