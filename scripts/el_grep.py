#!/usr/bin/env python3
"""Print body sentences of a PMC JATS XML matching a regex. Usage: python3 -I scripts/el_grep.py file.xml REGEX"""
import re, sys, xml.etree.ElementTree as ET
root = ET.parse(sys.argv[1]).getroot(); body = root.find(".//body")
txt = " ".join("".join((body if body is not None else root).itertext()).split())
for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", txt):
    if re.search(sys.argv[2], s, re.I): print("-", s[:500])
