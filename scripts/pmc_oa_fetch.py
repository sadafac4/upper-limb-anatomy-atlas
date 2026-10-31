#!/usr/bin/env python3
"""Fetch article metadata, JATS XML and selected figures from the AWS PMC Open Access bucket.

Usage:
  python3 -I scripts/pmc_oa_fetch.py info PMC1234567 [PMC...]      # download .json/.xml to a scratch dir, print licence + figures
  python3 -I scripts/pmc_oa_fetch.py get PMC1234567 fig1.jpg [fig2.jpg ...]   # save json/xml + named figure files into
                                                                       # topografik/images/raw/PMC<id>/
Options: --out DIR (raw root, default topografik/images/raw), --cache DIR (for 'info').
Reads only from https://pmc-oa-opendata.s3.amazonaws.com/ ; articles not in the bucket are not in the PMC OA subset.
"""
import json, pathlib, re, sys, urllib.request, xml.etree.ElementTree as ET

BUCKET = "https://pmc-oa-opendata.s3.amazonaws.com"
ROOT = pathlib.Path(__file__).resolve().parent.parent
XL = "{http://www.w3.org/1999/xlink}href"


def _get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def versions(pmcid):
    xml = _get(f"{BUCKET}/?list-type=2&prefix={pmcid}.").decode()
    keys = re.findall(r"<Key>([^<]+)</Key>", xml)
    vers = sorted({k.split("/")[0] for k in keys}, key=lambda v: int(v.rsplit(".", 1)[1]))
    return vers, keys


def text(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


def parse(xml_bytes):
    root = ET.fromstring(xml_bytes)
    meta = root.find(".//article-meta")
    title = text(meta.find(".//article-title"))
    authors = []
    for c in meta.findall(".//contrib[@contrib-type='author']"):
        n = c.find("name")
        if n is not None:
            authors.append(f"{text(n.find('surname'))} {text(n.find('given-names'))}".strip())
    lic = meta.find(".//license")
    lic_url = lic.get(XL) if lic is not None else None
    if lic is not None and not lic_url:
        u = lic.find(".//ext-link")
        lic_url = u.get(XL) if u is not None else None
        if not lic_url:
            for ali in lic.iter():
                if ali.tag.endswith("license_ref"):
                    lic_url = text(ali)
    figs = []
    for f in root.iter("fig"):
        figs.append({
            "id": f.get("id"),
            "label": text(f.find("label")),
            "caption": text(f.find("caption")),
            "graphics": [g.get(XL) for g in f.iter("graphic")],
        })
    return {"title": title, "authors": authors, "license_url": lic_url,
            "license_text": text(lic), "journal": text(root.find(".//journal-title")), "figs": figs}


def info(pmcid, cache):
    vers, keys = versions(pmcid)
    if not vers:
        print(f"{pmcid}: NOT IN OA BUCKET"); return None
    v = vers[-1]
    d = cache / v; d.mkdir(parents=True, exist_ok=True)
    for ext in ("json", "xml"):
        p = d / f"{v}.{ext}"
        if not p.exists():
            p.write_bytes(_get(f"{BUCKET}/{v}/{v}.{ext}"))
    j = json.loads((d / f"{v}.json").read_text())
    x = parse((d / f"{v}.xml").read_bytes())
    print(f"== {v}  licence={j.get('license_code')}  {x['license_url']}")
    print(f"   {j.get('citation')}\n   {x['title']}")
    media = {k.split('/')[-1] for k in keys if k.startswith(v + '/')}
    for f in x["figs"]:
        files = [m for m in media if any(m.startswith(g + ".") or m == g for g in f["graphics"] if g)]
        print(f"   [{f['label']}] {files} :: {f['caption'][:300]}")
    return v


def get(pmcid, files, out):
    vers, keys = versions(pmcid)
    v = vers[-1]
    d = out / pmcid; d.mkdir(parents=True, exist_ok=True)
    for name in [f"{v}.json", f"{v}.xml", *files]:
        p = d / name
        if not p.exists():
            p.write_bytes(_get(f"{BUCKET}/{v}/{name}"))
        print(p, p.stat().st_size)


if __name__ == "__main__":
    a = sys.argv[1:]
    out = ROOT / "topografik/images/raw"
    cache = pathlib.Path("/tmp/pmc_oa_cache")
    if "--out" in a:
        i = a.index("--out"); out = pathlib.Path(a[i + 1]); del a[i:i + 2]
    if "--cache" in a:
        i = a.index("--cache"); cache = pathlib.Path(a[i + 1]); del a[i:i + 2]
    if a[0] == "info":
        for p in a[1:]:
            try:
                info(p, cache)
            except Exception as e:
                print(p, "ERROR", e)
    elif a[0] == "get":
        get(a[1], a[2:], out)
