#!/usr/bin/env python3
"""Index NLM Visible Human Male (VHP-M) DICOM series hosted by NCI Imaging Data Commons
(public bucket s3://idc-open-data, HTTPS) WITHOUT downloading pixel data.

For every instance we fetch only the first 16 KiB (HTTP Range) and parse the DICOM header
(stop_before_pixels) to obtain InstanceNumber, ImagePositionPatient, SliceLocation, etc.
Output: kesitsel/vhp_index/<series_uuid>.csv  — used to find level-matched cryosection/CT/MR.

Source collection: IDC 'nlm_visible_human_project', DOI 10.5281/zenodo.12690049
License: National Library of Medicine Terms and Conditions (May 21, 2019).
"""
import csv, io, re, sys, concurrent.futures as cf, pathlib, requests, pydicom

BUCKET = "https://idc-open-data.s3.amazonaws.com"
OUT = pathlib.Path(__file__).resolve().parent.parent / "kesitsel" / "vhp_index"

def list_keys(prefix):
    keys, token = [], None
    while True:
        params = {"list-type": "2", "prefix": prefix + "/"}
        if token: params["continuation-token"] = token
        r = requests.get(BUCKET + "/", params=params, timeout=60); r.raise_for_status()
        keys += [k for k in re.findall(r"<Key>([^<]+)</Key>", r.text) if k.endswith(".dcm")]
        m = re.search(r"<NextContinuationToken>([^<]+)<", r.text)
        if not m: return keys
        token = m.group(1)

def head(key, nbytes=16384):
    for n in (nbytes, nbytes * 8):
        r = requests.get(f"{BUCKET}/{key}", headers={"Range": f"bytes=0-{n-1}"}, timeout=60)
        try:
            ds = pydicom.dcmread(io.BytesIO(r.content), stop_before_pixels=True, force=True)
            ipp = ds.get("ImagePositionPatient")
            return dict(key=key, inst=ds.get("InstanceNumber"),
                        z=float(ipp[2]) if ipp else None,
                        x=float(ipp[0]) if ipp else None, y=float(ipp[1]) if ipp else None,
                        sliceloc=ds.get("SliceLocation"), rows=ds.get("Rows"), cols=ds.get("Columns"),
                        spacing="/".join(map(str, ds.get("PixelSpacing", []) or [])),
                        thick=ds.get("SliceThickness"), comments=str(ds.get("ImageComments", ""))[:80],
                        desc=ds.get("SeriesDescription", ""), for_uid=ds.get("FrameOfReferenceUID", ""))
        except Exception as e:
            err = e
    return dict(key=key, comments=f"ERR {err}")

def main(series_uuids):
    OUT.mkdir(parents=True, exist_ok=True)
    for s in series_uuids:
        keys = list_keys(s)
        with cf.ThreadPoolExecutor(32) as ex:
            rows = list(ex.map(head, keys))
        rows.sort(key=lambda r: (r.get("z") is None, r.get("z") or 0))
        with open(OUT / f"{s}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=sorted({k for r in rows for k in r})); w.writeheader(); w.writerows(rows)
        print(s, len(rows), "instances indexed", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1:])
