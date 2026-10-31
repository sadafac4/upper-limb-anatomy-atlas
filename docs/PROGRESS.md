# Progress report – upper-limb anatomy atlas (session 1, 2026-10-31)

## Deliverables in this session
| Item | Path | Status |
|---|---|---|
| Cross-sectional pilot deck (11 slides: cover, method, 8 levels, sources) | `kesitsel/Kesitsel_Anatomi_Pilot.pptx` + `.pdf` | done, visually QA'd |
| Topographic pilot deck (13 slides: cover, 6 normal topography, 5 variations, sources) | `topografik/Topografik_Anatomi_Pilot.pptx` + `.pdf` | done, visually QA'd |
| Slide PNG previews | `kesitsel/qa/png/`, `topografik/qa/png/` | done |
| Cross-sectional provenance + reproduction | `kesitsel/KAYNAKLAR.md`, `sources/kesitsel_kaynaklar.json`, `kesitsel/vhp_index/*.csv` | done |
| Label QA log (incl. errors found & fixed) | `kesitsel/qa/QA_NOTLARI.md`, `kesitsel/qa/label_qa.json` | done |
| Topographic sources (17 PMC OA articles, licence/md5/captions) | `sources/topografik_kaynaklar.json`, `sources/topografik_arama_gunlugu.md`, `topografik/images/raw/` | done |
| Pipeline scripts | `scripts/` (see below) | done |

## Important: missing Turkish master specification
`README.md` ends with the placeholder `[PASTE THE FULL TURKISH MASTER PROMPT HERE]`; the detailed Turkish
specification was **not** in the repository. This pilot follows the English execution requirements in the README
and a standard upper-limb curriculum (regions: shoulder/axilla, arm, cubital fossa, forearm, wrist/hand; common
variations). Once the Turkish spec is added, slide lists, depth and style should be re-aligned to it.

## Environment findings (network policy)
The cloud environment's egress proxy **denied** these hosts (HTTP 403 on CONNECT): commons/upload.wikimedia.org,
data.lhncbc.nlm.nih.gov, www.nlm.nih.gov, www.ncbi.nlm.nih.gov, eutils.ncbi.nlm.nih.gov, europepmc.org, doi.org,
api.openverse.org, radiopaedia.org, huggingface.co, zenodo.org, figshare.com, archive.org, openneuro.org,
api.crossref.org, api.openalex.org, api.semanticscholar.org, google.com, jsdelivr/unpkg.
Reachable and used instead:
* **NCI Imaging Data Commons** public bucket (`idc-open-data.s3.amazonaws.com`) – contains the full NLM Visible Human dataset as DICOM.
* **PMC Open Access AWS bucket** (`pmc-oa-opendata.s3.amazonaws.com`) – article XML, figures and per-article licence code.
* Server-side WebSearch for literature discovery; PyPI for libraries.
To allow Wikimedia/NLM/PMC web hosts directly, add them under the environment's *Network access → Allowed domains*.

## Method highlights
* **Cross-sectional:** VHP-Male cryosection and frozen CT with the *same NLM slice number* (documented 1 mm coincidence;
  original filenames preserved in DICOM tag 0009,1001) – no fabricated level matching. In-plane registration by
  mask cross-correlation (+ local limb refinement), verified by overlaying CT bone contours on cryosections.
* **Topographic:** only real human-cadaver photographs / author schematics from peer-reviewed OA articles; licence read
  from the PMC bucket JSON (17 articles: 15 × CC BY, 1 × CC BY-NC-SA, 1 × CC BY-NC; the two non-commercial sources are flagged and not used in this pilot); figures used
  unmodified with Turkish legends translated from the authors' labels as actually printed in the image.
* **QA:** decks rendered with LibreOffice → PDF → PNG and inspected; 5 cross-sectional labelling/rendering errors and
  1 legend/figure mismatch (cubital fossa caption letters not present in the image) were found and fixed (see QA notes).

## Known limitations
* Frozen-CT field of view (480 mm) truncates the arm from mid-arm to elbow (levels 1490–1645): CT shown but not labelled there.
* VHP-Male axial MRI covers only the head; no MRI correlation is possible for limb levels from this dataset.
  Candidate next step: IDC clinical extremity MR (e.g. QIN-Sarcoma shoulder/elbow) – would need careful selection of tumour-free regions and is *not* the same subject.
* PMC OA figures are web-resolution (390–800 px); fine for half-slide use, not full-screen.
* Labels were placed by the pipeline author using documented evidence; **an anatomy faculty member should review** before teaching use.
* Not yet covered on slides (sources already downloaded): third head of biceps (CC BY-NC-SA), reversed palmaris longus,
  Gantzer muscle, ligament of Struthers (CC BY-NC), axillary-artery branching, Martin-Gruber pattern diagram (BioRender – excluded).

## Next steps
1. Add the Turkish master specification and re-plan the full slide lists.
2. Cross-sectional: add axilla (≈1360), more forearm/hand levels, VHP-Female (0.33 mm) levels, sagittal/coronal cryosection reformats through the limb (download every n-th cryosection), per-nerve labels with neighbour-slice tracking.
3. Topographic: remaining variation slides; additional normal-topography regions (scapular anastomosis, anatomical snuffbox, Guyon canal); seek higher-resolution CC BY figures.
4. Optional: Turkish overlay labels (native shapes) on topographic figures after anatomist review.

## Pipeline
```
scripts/vhp_index_headers.py   IDC header index (HTTP Range, no pixel download)
scripts/vhp_fetch.py           fetch/cached load by NLM slice number
scripts/vhp_register.py        cryo→CT in-plane registration (+ local refinement)
scripts/vhp_crops.py           level definitions, crops, gridded identification previews
scripts/vhp_assets.py          locator thumbnails, coronal CT MIP with level lines
scripts/pmc_oa_fetch.py        PMC OA bucket fetcher (licence/figures)
scripts/build_topografik_sources.py  rebuild + md5-check topographic source JSON
scripts/deck_common.py         python-pptx helpers (native, editable leader-line labels)
scripts/build_kesitsel.py      cross-sectional deck
scripts/build_topografik.py    topographic deck
scripts/render.sh              PPTX → PDF → PNG for visual QA
```
