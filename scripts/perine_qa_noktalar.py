#!/usr/bin/env python3
"""QA: sources/perine_*.json'daki label_points'leri görüntü üzerine çizer → <out>/<pmc>_<file>.jpg
usage: python3 -I scripts/perine_qa_noktalar.py <out_dir> [pmcid ...]"""
import json, pathlib, sys
from PIL import Image, ImageDraw, ImageFont
ROOT = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True); sec = set(sys.argv[2:])
fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
for p in sorted((ROOT / "sources").glob("perine_*.json")):
    for e in json.load(open(p)):
        if sec and e["pmcid"] not in sec: continue
        for f in e["figures"]:
            im = Image.open(ROOT / f["local_path"]).convert("RGB"); d = ImageDraw.Draw(im)
            for lp in f.get("label_points") or []:
                x, y = lp["xy"]; d.ellipse((x - 6, y - 6, x + 6, y + 6), outline=(0, 255, 0), width=3)
                d.text((x + 8, y - 8), lp["latin"][:28], fill=(0, 255, 0), font=fnt, stroke_width=2, stroke_fill=(0, 0, 0))
            im.save(out / f"{e['pmcid']}_{pathlib.Path(f['file']).stem}.jpg", quality=85)
            print(e["pmcid"], f["file"], f.get("pixels"), len(f.get("label_points") or []), "|", f["specimen"])
