#!/usr/bin/env python3
"""Helpers to fetch selected VHP-M DICOM instances from the IDC public bucket by NLM slice number."""
import io, pathlib, functools, requests, pydicom, numpy as np, pandas as pd

BUCKET = "https://idc-open-data.s3.amazonaws.com"
ROOT = pathlib.Path(__file__).resolve().parent.parent
IDX = ROOT / "kesitsel" / "vhp_index"
CACHE = pathlib.Path("/tmp/vhp_cache"); CACHE.mkdir(exist_ok=True)

SERIES = {  # IDC series UUID -> role (see kesitsel/KAYNAKLAR.md)
    "cryo":     ["4aaf9181-fb6a-4a4c-bf49-d1eb9ed4a385"],                      # a_vm####.raw full colour 2048x1216, 0.33 mm px, 1 mm
    "frozenCT": ["f3a311eb-3abb-4b22-a28d-36ede7ddf127", "aa81356d-32f2-4b71-ad81-c1defa3175ca",
                 "3455adc0-1341-4058-88a2-c511e38e72ef"],                     # c_vm####.fro 1 mm
    "normalCT": ["477cf391-d387-4ec0-8daa-85207c808a77", "29c772e1-1ea7-4c7e-8de0-dedafb72e347"],  # c_vm####.fre (fresh)
    "cryoF":    ["56f8119f-5940-48c1-96ee-8d445dc0b5fd"],                      # VHP-F a_vf, 0.33 mm aralık
    "frozenCT_F": ["2397283b-eb7d-41f7-b310-cc2bc0181865", "e82cd88f-9865-49c8-a14f-7b67c40dac90"],
    "MR_T1ax":  ["a83c457a-d8c9-4290-b657-d1570d99fbef"], "MR_T2ax": ["342d9e2a-7c85-4de3-bb7b-baf6246ba537"],
}

@functools.lru_cache(None)
def index(role):
    d = pd.concat([pd.read_csv(IDX / f"{s}.csv") for s in SERIES[role]])
    d["slice"] = pd.to_numeric(d["sliceloc"], errors="coerce")
    return d.sort_values("slice")

def get(key):
    p = CACHE / key.replace("/", "_")
    if not p.exists():
        r = requests.get(f"{BUCKET}/{key}", timeout=300); r.raise_for_status(); p.write_bytes(r.content)
    return pydicom.dcmread(p)

def nearest(role, slice_no):
    d = index(role); i = (d["slice"] - slice_no).abs().idxmin() if d.index.is_unique else None
    row = d.iloc[(d["slice"] - slice_no).abs().values.argmin()]
    return row

def load(role, slice_no):
    row = nearest(role, slice_no); ds = get(row.key)
    arr = ds.pixel_array
    if ds.Modality == "CT":
        arr = arr * float(ds.RescaleSlope) + float(ds.RescaleIntercept)
    return arr, ds, row

def window(hu, c=40, w=400):
    lo, hi = c - w / 2, c + w / 2
    return (np.clip((hu - lo) / (hi - lo), 0, 1) * 255).astype(np.uint8)
