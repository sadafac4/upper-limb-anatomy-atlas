#!/usr/bin/env python3
"""Print title, journal, year, authors, abstract and keyword-matching sentences from a PMC JATS XML.
Usage: python3 -I scripts/kol_abstract.py <xml> [regex]"""
import re, sys, xml.etree.ElementTree as ET
t = lambda e: " ".join("".join(e.itertext()).split()) if e is not None else ""
r = ET.parse(sys.argv[1]).getroot(); m = r.find(".//article-meta")
au = [f"{t(c.find('name/surname'))} {t(c.find('name/given-names'))}" for c in m.findall(".//contrib[@contrib-type='author']") if c.find('name') is not None]
print("TITLE:", t(m.find(".//article-title"))); print("JOURNAL:", t(r.find(".//journal-title")), "| YEAR:", t(m.find(".//pub-date/year")))
print("AUTHORS:", "; ".join(au)); print("ABSTRACT:", t(m.find(".//abstract")))
if len(sys.argv) > 2:
    body = t(r.find(".//body"))
    for s in re.split(r"(?<=[.!?])\s+", body):
        if re.search(sys.argv[2], s, re.I): print(" *", s)
