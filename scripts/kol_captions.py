#!/usr/bin/env python3
"""Print full figure captions (and graphic hrefs) from a cached/downloaded PMC JATS XML.
Usage: python3 -I scripts/kol_captions.py <path/to/PMCxxx.N.xml> [label-substring ...]"""
import sys, xml.etree.ElementTree as ET
XL = "{http://www.w3.org/1999/xlink}href"
t = lambda e: " ".join("".join(e.itertext()).split()) if e is not None else ""
root = ET.parse(sys.argv[1]).getroot()
want = sys.argv[2:]
for f in root.iter("fig"):
    lab = t(f.find("label"))
    if want and not any(w == lab or w in lab for w in want):
        continue
    print(f"[{lab}] {[g.get(XL) for g in f.iter('graphic')]}\n  {t(f.find('caption'))}\n")
