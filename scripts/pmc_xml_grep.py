#!/usr/bin/env python3
"""Inspect a downloaded PMC JATS XML: list figures (full captions) or grep body/abstract sentences.
Usage: python3 -I scripts/pmc_xml_grep.py figs <file.xml>
       python3 -I scripts/pmc_xml_grep.py grep <file.xml> <regex> [maxhits]
       python3 -I scripts/pmc_xml_grep.py meta <file.xml>
"""
import re, sys, xml.etree.ElementTree as ET
XL = "{http://www.w3.org/1999/xlink}href"
def t(e): return " ".join("".join(e.itertext()).split()) if e is not None else ""
mode, path = sys.argv[1], sys.argv[2]
root = ET.parse(path).getroot()
if mode == "figs":
    for f in root.iter("fig"):
        print(f"[{t(f.find('label'))}] {[g.get(XL) for g in f.iter('graphic')]}\n  {t(f.find('caption'))}\n")
elif mode == "meta":
    m = root.find(".//article-meta")
    au = []
    for c in m.findall(".//contrib[@contrib-type='author']"):
        n = c.find("name")
        if n is not None: au.append(f"{t(n.find('surname'))} {t(n.find('given-names'))}")
    print("TITLE:", t(m.find(".//article-title"))); print("AUTHORS:", "; ".join(au))
    print("JOURNAL:", t(root.find(".//journal-title"))); print("ABSTRACT:", t(m.find(".//abstract")))
elif mode == "grep":
    rx = re.compile(sys.argv[3], re.I); mx = int(sys.argv[4]) if len(sys.argv) > 4 else 30
    txt = t(root.find(".//abstract")) + " " + t(root.find(".//body"))
    n = 0
    for s in re.split(r"(?<=[.;])\s+(?=[A-Z(])", txt):
        if rx.search(s):
            print("-", s[:600]); n += 1
            if n >= mx: break
