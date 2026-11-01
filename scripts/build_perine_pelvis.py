#!/usr/bin/env python3
"""Build sources/perine_pelvis.json (PERINE deck - short PELVIS introduction) from downloaded PMC OA files.

Scope: bony pelvis / apertura pelvis superior et inferior / pelvis major-minor / male-female differences,
ligg. sacrotuberale & sacrospinale, diaphragma pelvis (m. levator ani, m. coccygeus, arcus tendinei), fascia pelvis,
and levator-ani subdivision / morphometry studies. Urogenital & anal triangles are covered by other agents.

Citation, DOI, licence, title, authors, journal, year, verbatim captions and pixel sizes are read from the files in
perine/images/raw/PMC<id>/ ; only the descriptive fields below are hand-written (after viewing every figure).
label_points: xy = pixel coordinate in the ORIGINAL image (checked on PIL crops with marker overlays).
Run: python3 -I scripts/build_perine_pelvis.py
"""
import json, pathlib, re, xml.etree.ElementTree as ET
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "perine/images/raw"
XL = "{http://www.w3.org/1999/xlink}href"


def t(e):
    return " ".join("".join(e.itertext()).split()) if e is not None else ""


def P(latin, author_label, x, y):
    return {"latin": latin, "author_label": author_label, "xy": [x, y]}


# (use, topic, pmcid, {file: (specimen, what_it_shows, labels_visible, [label_points])}, key_findings, clinical_relevance, notes)
E = [
 # ---------------- pelvis_lecture: bony pelvis ----------------
 ("pelvis_lecture", "Linea terminalis (arcuate line + ala margin) and pelvic inlet - author drawing", "PMC9303760",
  {"AJPA-177-690-g006.jpg": ("author drawing (from CT-based 3D model outlines)",
    "Panel (a): anterior-view line drawing of lower spine and pelvis; blue dashed line traces the linea terminalis on each side "
    "(iliac 'arcuate line' continuing onto the sacral 'ala margin' of S1), and a horizontal dashed line marks the iliac-crest level "
    "(L4/L5). Panels (b, c) are schematics of segmentation-anomaly levels (not needed for the lecture - crop to panel a).",
    "(a) T12, L4, L5, S1, 'Iliac crest', 'ala margin', 'arcuate line'; (b) 1, 2, 3, 4; (c) 1, 2, 3",
    [P("Crista iliaca", "Iliac crest", 75, 241),
     P("Linea arcuata (ossis ilii)", "arcuate line", 135, 352),
     P("Linea terminalis, pars sacralis (margo alae sacri)", "ala margin", 150, 318),
     P("Vertebra sacralis I (basis ossis sacri)", "S1", 205, 300),
     P("Vertebra lumbalis V", "L5", 205, 262)])},
  "145 clinical CT scans. 'the trajectory of the margin of the pelvic brim onto the sacral alae (the iliac portion of linea terminalis) could either be (1) upwards, (2) straight, or (3) downwards with respect to the arcuate line'. 'Such a second promontory was found in 13 specimens with lumbosacral transitional vertebra (60%).'",
  "Lumbosacral transitional vertebrae (sacralisation/lumbarisation) change the shape of the pelvic inlet and the position of the promontory - relevant to obstetric pelvimetry and spinal level counting.",
  "CC BY-NC (non-commercial) - flag. Drawing, not a photograph; promontorium, pecten ossis pubis and crista pubica are not labelled in the image - add Turkish labels manually only if an anatomist confirms. Crop to panel (a)."),
 ("pelvis_lecture", "Pelvic inlet / mid-cavity / outlet diameters on 3D-CT (pelvimetry, female vs male)", "PMC5768563",
  {"acb-50-265-g001.jpg": ("3D CT reconstruction (living patients)",
    "Two 3D-CT volume renderings of the pelvis (anterior view left, posterior-inferior view right) with numbered white lines: "
    "1 transverse diameter of inlet, 2 biacetabular, 3 bispinous (between ischial spines), 4 bituberous (outlet), 5 subpubic angle.",
    "numbers 1, 2, 3, 4, 5; white measurement lines; dotted black lines",
    [P("Diameter transversa aperturae pelvis superioris", "1", 180, 137),
     P("Linea terminalis (end-point of transverse inlet diameter)", "", 107, 137),
     P("Spina ischiadica", "3", 498, 183),
     P("Spina ischiadica", "", 608, 183),
     P("Tuber ischiadicum", "4", 482, 220),
     P("Tuber ischiadicum", "", 625, 220),
     P("Angulus subpubicus", "5", 553, 241)]),
   "acb-50-265-g002.jpg": ("3D CT reconstruction (living patients)",
    "Lateral (hemipelvis + sacrum) 3D-CT renderings with sagittal diameters drawn from the pubic symphysis: 6 inlet (to promontory), "
    "7 midplane 1, 8 midplane 2, 9 outlet (to coccyx tip); right panel: 10 sacral slope, 11 pelvic inclination.",
    "numbers 6, 7, 8, 9, 10, 11; white measurement lines",
    [P("Promontorium", "", 148, 113),
     P("Symphysis pubica", "", 86, 300),
     P("Diameter sagittalis aperturae superioris (conjugata)", "6", 118, 158),
     P("Diameter sagittalis aperturae inferioris", "9", 208, 308),
     P("Os coccygis (apex)", "", 275, 273)])},
  "211 females, 181 males (CT). Table 1 (female vs male, mm): transverse inlet 135.0±8.5 vs 126.8±7.0; bispinous 112.2±9.2 vs 93.6±8.4; outlet (bituberous) 123.9±10.4 vs 103.5±9.3; sagittal inlet 124.6±10.3 vs 119.2±10.2; sagittal outlet 99.9±9.8 vs 96.0±7.4; 'Subpubic angle' 132±12 vs 94±12 degrees. 'The results demonstrated that more pronounced age-related changes occurred in the inlet and the outlet of the lesser pelvis. The mid-cavity was less changing.'",
  "'The pelvic floor dysfunction and the pelvic organ prolapse are observed more often in females with a wider ... and more horizontally oriented pelvic inlet ..., a wider distance between ischial spines ..., and a longer sagittal diameter of the outlet'.",
  "CC BY-NC - flag. Gives real male/female numbers for the 'pelvis feminina vs masculina' slide. Subpubic angle here measured on CT differently from PMC7118257 (values not interchangeable)."),
 ("pelvis_lecture", "Male vs female pelvis: subpubic angle on 3D-CT", "PMC7118257",
  {"acb-53-27-g002.jpg": ("3D CT reconstruction (living patients)",
    "Anterior-inferior 3D-CT views of a male (A) and female (B) pelvis with landmarks L1-L4 (inferior ischiopubic ramus points and "
    "anteroinferior symphysis points) and the subpubic angle arc - narrow male vs wide female pubic arch.",
    "A, B, L1, L2, L3, L4 (orange dots), white arc",
    [P("Ramus ossis ischii / ramus ischiopubicus (male)", "L1", 128, 247),
     P("Symphysis pubica (male)", "L2", 182, 188),
     P("Symphysis pubica (male)", "L3", 190, 188),
     P("Ramus ischiopubicus (male)", "L4", 241, 243),
     P("Ramus ischiopubicus (female)", "L1", 487, 247),
     P("Symphysis pubica (female)", "L2", 540, 206),
     P("Symphysis pubica (female)", "L3", 566, 206),
     P("Ramus ischiopubicus (female)", "L4", 618, 246),
     P("Angulus subpubicus / arcus pubicus (female)", "", 553, 240)])},
  "50 male + 50 female MDCT. 'Results showed that the subpubic angle in males was 68.6°±7.6° and in females 87.4°±6.5°.' 'The overall accuracy of sex estimation using the subpubic angle was 94% (P<0.001). The subpubic angle, with a demarcating point of 78.6°, showed a sensitivity and specificity of 94% in the classification of female individuals.'",
  "Subpubic angle is the classic male/female discriminator (angulus subpubicus vs arcus pubicus); population-specific cut-offs.",
  "CC BY-NC - flag. Best whole-pelvis male/female comparison found."),
 ("pelvis_lecture", "Male vs female os coxae on dried bone: pubic (subpubic) angle", "PMC6811666",
  {"414_2019_2002_Fig2_HTML.jpg": ("dried bone (macerated os coxae) + virtual 3D models",
    "Row a: photographs of macerated male and female hip bones (same orientation) with black lines drawing the pubic angle - wider in "
    "the female; rows b, c: the same bones as CT surface models (two software packages). Obturator foramen and acetabulum visible.",
    "'Male', 'Female', a, b, c; black angle lines on row a",
    [P("Angulus subpubicus (pubic angle, male) - vertex of drawn lines", "", 40, 230),
     P("Angulus subpubicus (pubic angle, female) - vertex of drawn lines", "", 356, 238),
     P("Foramen obturatum (male)", "", 160, 200),
     P("Foramen obturatum (female)", "", 480, 225),
     P("Acetabulum (male)", "", 250, 165),
     P("Acetabulum (female)", "", 555, 160)])},
  "27 cadavers (13 male, 14 female) CT-scanned then macerated. Klales traits on dry bone: intra-observer K = 0.78-0.89, inter-observer K = 0.61-0.77; virtual model vs dry bone (in-house software) K = 0.74 (ventral arc), 0.84 (subpubic concavity), 0.82 (medial aspect ischiopubic ramus). 'one cannot readily assume that morphological sex estimation methods that are traditionally applied to dry skeletal remains perform equally when applied to virtual 3D skeletal elements.'",
  "Sex estimation from the pubic region (Phenice/Klales traits) - forensic and anatomical teaching of pelvic dimorphism.",
  "CC BY. Only real dried-bone photo of male vs female in this set; crop to row a. Lines only, no text labels on the bones."),
 # ---------------- pelvis_lecture: ligaments, walls, fascia, diaphragm ----------------
 ("pelvis_lecture", "Lig. sacrotuberale, m. piriformis in the greater sciatic notch, sciatic & pudendal nerves (posterior view)", "PMC10924905",
  {"jkns-2023-0166f1.jpg": ("author schematic over 3D-CT bone rendering",
    "Posterior view of the hip region: semi-transparent grey sacrotuberous ligament (STL) from sacrum towards the ischial tuberosity, "
    "piriformis (Pfm, red) passing through the greater sciatic notch/foramen, sciatic nerve (SN) emerging below it and pudendal nerve "
    "(PN) curving medially deep to the STL. Dotted circles = surgical decompression extent (A conventional, B extended).",
    "A, B, STL, Pfm, SN, PN; grey and red dotted circles",
    [P("Lig. sacrotuberale", "STL", 235, 140),
     P("M. piriformis", "Pfm", 180, 180),
     P("N. ischiadicus", "SN", 92, 262),
     P("N. pudendus", "PN", 318, 268)])},
  "81 patients analysed (transgluteal sciatic decompression). 'sciatic nerve decompression was successful in 50 of 81 patients (61.7%)'. 'Among the factors that affect the surgical outcome, only additional division of the sacrotuberous ligament during piriformis muscle resection played a significant role. The success rate was higher in the scarotuberous ligementectomy group (79.4%) than in the non-resection group (42.6%)' [sic].",
  "Shows that the STL roofs the sciatic/pudendal pathway at the greater/lesser sciatic foramina; surgical division of the STL in piriformis syndrome.",
  "CC BY-NC - flag. Schematic overlay on a CT model, not a dissection. Lig. sacrospinale and the foramina are not labelled. Crop to panel A. No CC BY real-specimen photo of the ligamentous pelvis was found (see search log)."),
 ("pelvis_lecture", "Pelvic side wall from above (laparoscopy): m. obturator internus, arcus tendineus m. levatoris ani, lig. sacrospinale, spina ischiadica", "PMC10410660",
  {"FVVinObGyn-15-181-g001.jpg": ("intra-operative laparoscopic photograph (living patient)",
    "Upper panel: retroperitoneal laparoscopic view of the lateral pelvic wall with the obturator internus muscle and the white levator ani "
    "arcus tendineus (LAAT) running across it; lower panel: deeper view showing the sacrospinous ligament (SSL) and ischial spine (IS).",
    "OIM, LAAT, SSL, IS",
    [P("M. obturatorius internus", "OIM", 545, 215),
     P("Arcus tendineus musculi levatoris ani", "LAAT", 412, 342),
     P("Lig. sacrospinale", "SSL", 480, 695),
     P("Spina ischiadica", "IS", 628, 818)])},
  "Two case reports of laparoscopic pudendal decompression. 'The arcus tendinous of the endopelvic fascia is identified and followed until the ischial spine (Figure 1).' 'The coccygeus muscle fibres and the sacrospinous ligament are coagulated and transected whilst protecting the underneath structures.'",
  "Surgical landmarks of the pelvic side wall (ATLA -> ischial spine -> SSL/coccygeus) used in sacrospinous fixation and pudendal nerve surgery.",
  "CC BY. Living-patient laparoscopy, not a cadaver. Caption calls it 'Levator ani arcus tendinous'; text calls the same landmark 'arcus tendinous of the endopelvic fascia' - author inconsistency, keep TA term 'arcus tendineus musculi levatoris ani' per the image label."),
 ("pelvis_lecture", "Fascia obturatoria, arcus tendineus m. levatoris ani (ATLA) and arcus tendineus fasciae pelvis (ATFP) - cadaver hemipelvis", "PMC8096964",
  {"41598_2021_89041_Fig2_HTML.jpg": ("human cadaver (embalmed)",
    "Inner (medial) view of four hemipelves (A-C female/right-left, D male) with intact obturator fascia: ATLA crossing the fascia from "
    "the ischial spine towards the superior pubic ramus, ATFP lower down towards the pubic symphysis (PS); obturator canal circled. "
    "Panel E = bar chart of obturator fascia thickness (male vs female).",
    "A-E, PS, ATLA, ATFP, black circles; bar chart axis 'Thickness of obturator fascia (mm)', male, female, *",
    [P("Symphysis pubica", "PS", 25, 110),
     P("Arcus tendineus musculi levatoris ani", "ATLA", 180, 135),
     P("Arcus tendineus fasciae pelvis", "ATFP", 165, 215),
     P("Canalis obturatorius", "circle", 225, 62),
     P("Arcus tendineus musculi levatoris ani", "ATLA", 555, 140),
     P("Arcus tendineus fasciae pelvis", "ATFP", 505, 210),
     P("Canalis obturatorius", "circle", 605, 62),
     P("Fascia obturatoria", "", 200, 320),
     P("Arcus tendineus musculi levatoris ani", "ATLA", 150, 410),
     P("Arcus tendineus fasciae pelvis", "ATFP", 225, 485),
     P("Canalis obturatorius", "circle", 50, 355),
     P("Arcus tendineus musculi levatoris ani", "ATLA", 545, 460),
     P("Arcus tendineus fasciae pelvis", "ATFP", 605, 510),
     P("Canalis obturatorius", "circle", 510, 335)]),
   "41598_2021_89041_Fig4_HTML.jpg": ("human cadaver (embalmed); panel B whole-body frontal section",
    "A: right hemipelvis with the obturator fascia reflected (held by forceps, ATLA on its edge) exposing obturator internus (OIM) and "
    "puborectalis (PRM); B: whole-body frontal section through uterus and rectum showing the funnel of the levator ani (LAM) between "
    "the ischioanal fossa (IAF) and pelvic cavity; white arrows = fusion of levator fascia with obturator fascia above the ATLA.",
    "A, B, PRM, OIM, ATLA, circle, Ut, Rc, LAM (x2), OIM (x2), IAF, two white arrows",
    [P("M. puborectalis", "PRM", 95, 265),
     P("M. obturatorius internus", "OIM", 240, 180),
     P("Arcus tendineus musculi levatoris ani (on reflected fascia obturatoria)", "ATLA", 330, 330),
     P("Canalis obturatorius", "circle", 525, 150),
     P("Uterus", "Ut", 240, 532),
     P("Rectum", "Rc", 320, 700),
     P("M. levator ani", "LAM", 195, 712),
     P("M. levator ani", "LAM", 440, 640),
     P("M. obturatorius internus", "OIM", 95, 720),
     P("M. obturatorius internus", "OIM", 560, 705),
     P("Fossa ischioanalis", "IAF", 478, 742),
     P("Fascia obturatoria / fascia m. levatoris ani fusion", "white arrow", 112, 668),
     P("Fascia obturatoria / fascia m. levatoris ani fusion", "white arrow", 565, 603)])},
  "10 embalmed cadavers (4 F, 6 M). 'the average thickness of obturator fascia in male (0.167 ± 0.031 mm) was thinner than in female (0.228 ± 0.036 mm) (Fig. 2E, p < 0.01, t-test).' 'Some skeletal muscle fibers were found above the ATLA within the obturator fascia ... the attachment of LAM aponeurosis extended beyond ATLA to the inferior border of the superior ramus of the pubic bone.'",
  "'The new discovered attachment of LAM could provide a reference position for clinical diagnosis and treatment of MFPP or CPP' (myofascial pelvic pain / chronic pelvic pain).",
  "CC BY. Best real-cadaver source for the two arcus tendinei and fascia obturatoria. Fig 3 (fibres above ATLA + histology) was downloaded, judged redundant and deleted. Fig 4B is a frontal section - use as topographic overview of the levator funnel only."),
 ("pelvis_lecture", "Fascia diaphragmatis pelvis superior (parietal pelvic fascia) and arcus tendineus fasciae pelvis - male cadaver hemipelvis", "PMC12452807",
  {"PROS-85-1440-g001.jpg": ("human cadaver (sagittally bisected male pelvis)",
    "Medial view of a bisected male pelvis: (A) superior fascia of the pelvic diaphragm (SFPD) covering the pelvic wall, obturator "
    "canal, prostate, rectum, coccyx; (B) prostate retracted to show the TAPF; (C) SFPD removed lateral to the prostate exposing the "
    "levator ani (LA) muscle surface.",
    "A, B, C; OC, SFPD, Pu, Pr, Ur, Cx, R, CSP, CS1, CS2 (red), TAPF, LA, white asterisks, Superior/Anterior arrows",
    [P("Canalis obturatorius", "OC", 66, 91),
     P("Fascia diaphragmatis pelvis superior (fascia pelvis parietalis)", "SFPD", 86, 106),
     P("Urethra", "Ur", 115, 124),
     P("Os pubis / symphysis pubica (cut surface)", "Pu", 35, 132),
     P("Prostata", "Pr", 97, 127),
     P("Rectum", "R", 133, 172),
     P("Os coccygis", "Cx", 192, 125),
     P("Corpus spongiosum penis", "CSP", 67, 200),
     P("Arcus tendineus fasciae pelvis", "TAPF", 334, 127),
     P("Fascia diaphragmatis pelvis superior", "SFPD", 353, 124),
     P("Arcus tendineus fasciae pelvis", "TAPF", 574, 127),
     P("M. levator ani", "LA", 614, 128)])},
  "3 cadavers. 'The SFPD was identified as a fibrous membrane covering the superior surface of the LA muscle, with the TAPF as its thickened part.' Histology: smooth muscle interposed between SFPD, LA and external urethral sphincter.",
  "'During robot-assisted radical prostatectomy, selection of the dissection plane should consider preservation of these supportive structures to maintain postoperative urinary function.'",
  "CC BY-NC - flag. Leader-line tips used as xy. Image is 702 px wide with three panels (~234 px each): use one panel per half-slide."),
 # ---------------- pelvis_variation ----------------
 ("pelvis_variation", "Levator ani architecture from serial sections: puborectal vs 'pubovisceral' parts, coccygeus (3D reconstruction)", "PMC4549266",
  {"pone.0132226.g001.jpg": ("3D reconstruction from undeformed serial anatomical sections (Chinese Visible Human, real cadaver sections)",
    "A-E transverse/oblique and F midsagittal cryosection images with outlined muscles; G left-lateral and H anterosuperior 3D "
    "reconstructions of levator ani subdivisions: coccygeus (Co), pubovisceral (PV, bilayered), puborectal (PR), rectococcygeal (RC), "
    "obturator internus (OI), external anal sphincter (EAS). Use panel H (and G) only for the topographic lecture.",
    "A-H; Ant, Post, B, U, V, R, OI, GM, P, EAS, Fat; G: Co, RC, PV, AL, PR-D, PR-S, EAS, Ant, red lines A-E; H: Co, RC, PV, OI, E-A-S, PR",
    [P("M. coccygeus (m. ischiococcygeus)", "Co", 545, 607),
     P("M. coccygeus (m. ischiococcygeus)", "", 660, 600),
     P("'M. rectococcygeus' (smooth muscle)", "RC", 597, 642),
     P("M. pubococcygeus + m. iliococcygeus ('pubovisceral muscle')", "PV", 561, 682),
     P("M. obturatorius internus", "OI", 520, 707),
     P("M. puborectalis", "PR", 627, 740),
     P("M. sphincter ani externus", "EAS", 597, 710)])},
  "6 young adults (4 F, 2 M). 'we observed no perimysial septa between puborectal and pubococcygeal portions that would allow a separation as shown in virtually all textbooks.' 'The LAM had a common anterior attachment to the pubic bone, but separated posteriorly into puborectal and \"pubovisceral\" muscles.' 'The pubovisceral muscle comprised the pubo- and iliococcygeal muscles that are shown in most atlases'. 'the post-mortem levator hiatus was ~61 mm longer and ~23 mm narrower, and had descended 3–5 mm more ... than measured in life'. Attachment to the obturator internus ('tendinous' arch) 'was remarkably inconspicuous'.",
  "Challenges the textbook three-part levator ani; puborectal loops define the levator (urogenital) hiatus - relevant to obstetric levator avulsion and continence.",
  "CC BY. Panels A-F are cross-sections (deck is topographic) - crop to G/H. Shared folder: the anal-triangle agent may reference the same figure."),
 ("pelvis_variation", "Levator ani anterior part divides into anterior and posterior bundles (slings) - female cadaver, medial view", "PMC6942605",
  {"12565_2019_492_Fig5_HTML.jpg": ("human cadaver (female, hemisected pelvic floor block)",
    "(a) medial aspect: levator ani (LA) with its anterior bundle (square) and posterior bundle (circle) above the external anal "
    "sphincter (EAS); dashed/solid/curved lines outline a triangular space through which the superficial transverse perineal (STP) "
    "passes; (b) lateral aspect of the same specimen.",
    "A, B; LA, IC, BS, STP, EAS, white circle, white square, dashed/solid/curved white lines, Superior/Posterior/Anterior arrows",
    [P("M. levator ani", "LA", 205, 123),
     P("M. levator ani, pars anterior - fasciculus anterior", "square", 205, 213),
     P("M. levator ani, pars anterior - fasciculus posterior", "circle", 122, 195),
     P("M. sphincter ani externus", "EAS", 145, 240),
     P("M. transversus perinei superficialis", "STP", 185, 225),
     P("M. levator ani", "LA", 552, 130),
     P("M. sphincter ani externus", "EAS", 590, 198)])},
  "28 pelvic halves from 16 female cadavers (mean age 79.75 years). 'From the medial aspect, the anterior part of the levator ani was divided into anterior and posterior bundles to form the anterior and posterior slings, respectively.' 'This study proposes that three muscular slings could be important in supporting the pelvic floor in women.'",
  "Supports a sling concept of pelvic-floor support anterior to the anal canal (obstetric perineal injury / incontinence).",
  "CC BY. Small image (708x284). Folder shared with the urogenital-triangle agent, which keeps Figs 2-4 of the same article; this entry uses Fig 5 only."),
 ("pelvis_variation", "Levator ani subdivisions on MRI: 3D origin-insertion vectors, controls vs prolapse (morphometry)", "PMC12287122",
  {"192_2025_6082_Fig1_HTML.jpg": ("MRI-derived 3D vectors on a generic bone model",
    "Table of renderings (sagittal, transverse, coronal) showing origin-insertion vectors of levator subdivisions (colour-coded: "
    "pubovisceral origin bright red, pubovaginal dark red, puboperineal orange, puboanal yellow, puborectal green, iliococcygeus blue, "
    "coccygeus grey) for one participant, all participants, and controls (blue) vs cases (red).",
    "column heads 'xy (sagittal)', 'xz (transverse)', 'yz (coronal)'; rows 'An example participant', 'All', 'Controls: blue / Cases: red'; colour code only",
    [P("M. iliococcygeus (blue vectors)", "", 390, 255),
     P("M. pubococcygeus / pubovisceralis origin (bright red)", "", 427, 245)])},
  "22 nulliparous controls vs 22 symptomatic parous women (POP-Q >= II). 'Insertions differed notably in the vertically oriented pubovaginal, puboperineal, and puboanal muscles, with patients exhibiting lower positions along the superior–inferior axis by 6.1–7.7, 8.8, and 8.0–8.2 mm respectively.' 'Muscle lengths were also 4% to 24% longer in cases.' PVM length difference '11.5 (24%)/10.5 (22%) mm on the left/right side'; coccygeus 'the smallest difference, with 2.3 mm (4%)'.",
  "Quantitative levator geometry as a basis for imaging-based pelvic organ prolapse diagnostics.",
  "CC BY. In-vivo MRI, not a dissection; no text labels on structures - label_points are colour-coded vectors only (low confidence for slide labels; use mainly for the numbers)."),
]


def meta(pmcid):
    d = RAW / pmcid
    x = next(d.glob(f"{pmcid}.*.xml")); j = json.loads(next(d.glob(f"{pmcid}.*.json")).read_text())
    root = ET.parse(x).getroot(); m = root.find(".//article-meta")
    au = []
    for c in m.findall(".//contrib[@contrib-type='author']"):
        n = c.find("name")
        if n is not None:
            gn = t(n.find("given-names")); ini = " ".join(p[0] + "." for p in re.split(r"[\s\-]+", gn) if p)
            au.append(f"{t(n.find('surname'))} {ini}".strip())
    caps = {}
    for f in root.iter("fig"):
        for g in f.iter("graphic"):
            caps[g.get(XL)] = (t(f.find("label")), t(f.find("caption")))
    yr = re.search(r"\b(19|20)\d{2}\b", j.get("citation", "")).group(0)
    return d, x, j, root, m, au, caps, yr


out = []
for use, topic, pmcid, figs, kf, cr, notes in E:
    d, x, j, root, m, au, caps, yr = meta(pmcid)
    flist = []
    for fn, (spec, what, labels, pts) in figs.items():
        p = d / fn
        assert p.exists(), p
        lab, cap = next(v for g, v in caps.items() if g and (fn == g or fn.startswith(g + ".") or fn.rsplit(".", 1)[0] == g.rsplit(".", 1)[0]))
        w, h = Image.open(p).size
        for q in pts:
            assert 0 <= q["xy"][0] < w and 0 <= q["xy"][1] < h, (fn, q)
        flist.append({"file": fn, "label": lab, "caption": cap, "specimen": spec, "what_it_shows": what,
                      "labels_visible_in_image": labels, "label_points": pts, "pixels": f"{w}x{h}",
                      "local_path": str(p.relative_to(ROOT))})
    out.append({"use": use, "topic": topic, "pmcid": pmcid, "version": int(x.stem.rsplit(".", 1)[1]),
                "doi": j.get("doi"), "citation": j.get("citation"), "title": t(m.find(".//article-title")),
                "authors": ", ".join(au[:3]) + (" et al." if len(au) > 3 else ""), "year": yr,
                "journal": t(root.find(".//journal-title")), "license_code": j.get("license_code"),
                "figures": flist, "key_findings": kf, "clinical_relevance": cr, "notes": notes})

(ROOT / "sources/perine_pelvis.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(len(out), "entries;", sum(len(e["figures"]) for e in out), "figures;",
      sum(len(f["label_points"]) for e in out for f in e["figures"]), "label points")
for e in out:
    print(f"{e['use']:17} {e['pmcid']:12} {e['license_code']:10} {[(f['file'], len(f['label_points'])) for f in e['figures']]}")
