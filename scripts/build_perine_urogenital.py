#!/usr/bin/env python3
"""Build sources/perine_urogenital.json (PERINE - urogenital triangle + perineal fasciae, male & female).

Citation, DOI, licence, title, authors, journal, year, verbatim captions and pixel sizes are read from the
files in perine/images/raw/PMC<id>/ ; only the descriptive fields below are hand-written (after viewing every
figure). label_points xy are pixel coordinates in the ORIGINAL image (checked on gridded zoom crops).
Run: python3 -I scripts/build_perine_urogenital.py
"""
import json, pathlib, re, xml.etree.ElementTree as ET
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "perine/images/raw"
XL = "{http://www.w3.org/1999/xlink}href"


def t(e):
    return " ".join("".join(e.itertext()).split()) if e is not None else ""


def P(latin, label, x, y):
    return {"latin": latin, "author_label": label, "xy": [x, y]}


# (use, topic, pmcid, {file: (specimen, what_it_shows, labels_visible, [label_points])}, key_findings, clinical_relevance, notes)
E = [
 # ---------------- perine_lecture ----------------
 ("perine_lecture", "Layered dissection of the MALE urogenital triangle: superficial muscles -> perineal membrane -> deep perineal space (smooth-muscle 'DTP') and external urethral sphincter", "PMC12229694",
  {"41598_2025_9585_Fig1_HTML.jpg": ("human cadaver (formalin-perfused, 8%; elderly donors)",
    "Four-step inferior view of a male perineum: (A,B) after removal of skin/fat the bulbospongiosus over the bulb, the ischiocavernosus on the ischiopubic ramus and a slender band-like superficial transverse perineal muscle (outlined) in front of the external anal sphincter; (C) deeper, after removing the superficial muscles, the firm perineal membrane between the ischiopubic rami below the bulb of penis; (D) after removing the perineal membrane, the external urethral sphincter around the urethra and a triangular smooth-muscle plate (SM) continuous with the longitudinal muscle of the rectum (dashed arrows).",
    "A: Ic, Bs, STP, EAS, Anterior; B: Bs, Ic, STP (red dashed outline), EAS x2; C: BP, IPR, PM, LA, EAS; D: EUS, Ur, SM, LA, LM, green dashed lines, white dashed arrows",
    [P("Musculus ischiocavernosus", "Ic", 128, 62), P("Musculus bulbospongiosus", "Bs", 160, 47),
     P("Musculus transversus perinei superficialis", "STP", 137, 117), P("Musculus sphincter ani externus", "EAS", 194, 189),
     P("Musculus ischiocavernosus", "Ic", 434, 84), P("Musculus bulbospongiosus", "Bs", 509, 42),
     P("Musculus transversus perinei superficialis", "STP", 447, 179), P("Musculus sphincter ani externus", "EAS", 444, 247),
     P("Bulbus penis", "BP", 161, 312), P("Ramus ossis ischii / ramus inferior ossis pubis (ramus ischiopubicus)", "IPR", 49, 362),
     P("Membrana perinei", "PM", 112, 387), P("Musculus levator ani", "LA", 106, 456), P("Musculus sphincter ani externus", "EAS", 232, 525),
     P("Musculus sphincter urethrae externus", "EUS", 469, 331), P("Urethra (pars membranacea)", "Ur", 497, 344),
     P("Musculus transversus perinei profundus (smooth-muscle plate per authors)", "SM", 441, 382),
     P("Musculus levator ani", "LA", 431, 437), P("Stratum longitudinale tunicae muscularis recti", "LM", 491, 484)]),
   "41598_2025_9585_Fig7_HTML.jpg": ("schematic",
    "Authors' oblique inferior schematic of male (A,C) and female (B,D) perineum showing the three layers: superficial striated STP/Bs/Ic, the perineal membrane (blue sheet) between the ischiopubic rami, and above it the smooth-muscle plate (SM) of the deep perineal space continuous with the rectal longitudinal muscle (and vaginal wall in females).",
    "C: Ur, Bs, Ic, PM, STP, SM, LM, R, EAS; D: Bl, Ur, Va, SM, LM, R, Bs, PM, Ic, STP, EAS; A, B, C, D",
    [P("Urethra", "Ur", 200, 324), P("Musculus bulbospongiosus", "Bs", 206, 354), P("Musculus ischiocavernosus", "Ic", 244, 394),
     P("Membrana perinei", "PM", 216, 400), P("Musculus transversus perinei superficialis", "STP", 187, 447),
     P("Musculus transversus perinei profundus (smooth-muscle plate per authors)", "SM", 137, 353),
     P("Stratum longitudinale tunicae muscularis recti", "LM", 94, 389), P("Rectum", "R", 109, 434),
     P("Musculus sphincter ani externus", "EAS", 131, 498),
     P("Vesica urinaria", "Bl", 503, 298), P("Urethra feminina", "Ur", 516, 328), P("Vagina", "Va", 503, 369),
     P("Musculus bulbospongiosus", "Bs", 537, 381), P("Membrana perinei", "PM", 578, 409), P("Musculus ischiocavernosus", "Ic", 634, 388),
     P("Musculus transversus perinei superficialis", "STP", 572, 474),
     P("Musculus transversus perinei profundus (smooth-muscle plate per authors)", "SM", 466, 334),
     P("Musculus sphincter ani externus", "EAS", 481, 497)])},
  "'Perineal muscle shape and location from nine cadavers (five males; average age, 79 years) were macroscopically examined.' 'An overall layered perineum structure was revealed in both sexes. A slender, band-like striated muscle was observed near the surface. Beneath this layer was a dense connective tissue membrane that provides separation. A triangular, plate-like shaped smooth muscle with transversely oriented fibers occupied the deep perineal space, which, unlike the striated muscle, was continuous with the rectal wall and was identified as the deep transverse perineal muscle.'",
  "'Findings indicate that the deep transverse perineal muscle may be a distinct pelvic smooth muscle component.' Relevant to the classic 'urogenital diaphragm' concept, to perineal/obstetric repair and to transperineal surgery (layer-by-layer anatomy).",
  "Sci Rep 2025, CC BY 4.0. Same group (Muro/Akita, Tokyo) as PMC8373982, PMC6942605, PMC7182620, PMC12003430. Fig 1 panels A-B are the male SUPERFICIAL POUCH; C = PERINEAL MEMBRANE; D = DEEP POUCH. Fig 7 is the authors' own schematic (good for the 'layers' slide). The interpretation of the DTP as smooth muscle is the authors' view (contrast PMC13069139)."),
 ("perine_lecture", "Layered dissection of the FEMALE urogenital triangle: Bs/Ic/STP, bulb of vestibule, perineal membrane, deep smooth-muscle plate", "PMC12229694",
  {"41598_2025_9585_Fig2_HTML.jpg": ("human cadaver (formalin-perfused, 8%; elderly donors)",
    "Inferior view of a female perineum in four dissection steps: (A,B) Ic and Bs lateral to the vestibule, slender STP posterolateral to the vaginal opening; (C) after removal of Bs, the bulb of the vestibule (BV) and the perineal membrane (PM) lateral to urethra and vagina; (D) after removing the PM, the smooth-muscle plate (SM) continuous with the vaginal wall and rectal longitudinal muscle (dashed arrow).",
    "A: Ic, Bs, Va, STP, EAS, Anterior; B: Ic, Bs, Ur, Va, STP (red dashed); C: IPR, BV, PM, Ur, Va; D: IPR, BV, Ur, Va, SM, LA, LM, EAS",
    [P("Musculus ischiocavernosus", "Ic", 91, 68), P("Musculus bulbospongiosus", "Bs", 125, 72), P("Vagina (ostium vaginae)", "Va", 159, 94),
     P("Musculus transversus perinei superficialis", "STP", 80, 124), P("Musculus sphincter ani externus", "EAS", 178, 231),
     P("Musculus ischiocavernosus", "Ic", 438, 56), P("Musculus bulbospongiosus", "Bs", 488, 81),
     P("Ostium urethrae externum", "Ur", 550, 86), P("Ostium vaginae", "Va", 550, 97),
     P("Musculus transversus perinei superficialis", "STP", 418, 150),
     P("Ramus ischiopubicus", "IPR", 62, 322), P("Bulbus vestibuli", "BV", 166, 336), P("Membrana perinei", "PM", 92, 386),
     P("Urethra feminina", "Ur", 225, 358), P("Vagina", "Va", 230, 369),
     P("Bulbus vestibuli", "BV", 508, 322), P("Musculus transversus perinei profundus (smooth-muscle plate per authors)", "SM", 425, 394),
     P("Musculus levator ani", "LA", 467, 474), P("Stratum longitudinale tunicae muscularis recti", "LM", 581, 519),
     P("Musculus sphincter ani externus", "EAS", 534, 534)])},
  "Female donors = 4 of the 9 cadavers (five males). 'The smooth muscle was continuous with the longitudinal rectal muscle and, in females, with the vaginal muscular wall.'",
  "Female perineal layers relevant to obstetric perineal trauma, perineal body and vestibular-bulb haemorrhage.",
  "Same article as the male entry; female superficial pouch (Bs, Ic, STP, BV) + PM shown on cadaver."),
 ("perine_lecture", "Perineal membrane and the 'deep transverse perineal muscle' question: embalmed male/female dissection + excised membrane plate", "PMC13069139",
  {"JOA-248-755-g004.jpg": ("human cadaver (embalmed, elderly)",
    "Male perineum from below after removal of fat: ischioanal fossa (green circle) dorsally; ventrally the urogenital region with bulbospongiosus (5), ischiocavernosus (4) and the perineal membrane/'DTP' plate (3); arrow marks the loose connective tissue extending cranial to the deep pouch; 1 levator ani, 2 coccygeus.",
    "ventral, dorsal, right, left, 1, 2, 3, 4, 5, white arrow, green circle",
    [P("Musculus bulbospongiosus", "5", 384, 117), P("Musculus ischiocavernosus", "4", 457, 173),
     P("Membrana perinei / musculus transversus perinei profundus", "3", 412, 226),
     P("Musculus levator ani", "1", 467, 442), P("Musculus coccygeus", "2", 512, 511),
     P("Textus connectivus laxus supra spatium profundum perinei", "white arrow", 297, 251)]),
   "JOA-248-755-g001.jpg": ("human cadaver (embalmed, elderly)",
    "Female (a) and male (b) perineum from below with branches of the internal pudendal artery and pudendal nerve still covering the deep perineal pouch: ischioanal fossa (1), levator ani (2), perineal membrane/DTP (3), STP (4, visible only in the male), ischiocavernosus (5), bulbospongiosus (6).",
    "(a) ventral, dorsal, right, left, 1, 2, 3, 5, 6; (b) ventral, dorsal, right, left, 1, 2, 3, 4, 5, 6",
    [P("Musculus bulbospongiosus", "6", 290, 186), P("Musculus ischiocavernosus", "5", 381, 159),
     P("Membrana perinei / musculus transversus perinei profundus", "3", 435, 308), P("Musculus levator ani", "2", 412, 445),
     P("Fossa ischioanalis", "1", 465, 412),
     P("Musculus bulbospongiosus", "6", 377, 858), P("Musculus ischiocavernosus", "5", 436, 946),
     P("Membrana perinei / musculus transversus perinei profundus", "3", 290, 995),
     P("Musculus transversus perinei superficialis", "4", 396, 1031), P("Musculus levator ani", "2", 273, 1112),
     P("Fossa ischioanalis", "1", 448, 1118)]),
   "JOA-248-755-g005.jpg": ("human cadaver (embalmed, elderly)",
    "The whole tissue plate of the deep perineal pouch including the perineal membrane, excised from a female (a-c) and a male (d-f) donor: inner and outer views and frontal views; blue lines mark the free lateral part used for histology. The female plate is broad and trapezoid with a central opening; the male plate is narrower and triangular.",
    "(a)-(f), ventral, dorsal, cranial, caudal, blue lines; no anatomical text labels",
    [P("Membrana perinei (feminina, pars libera)", "", 105, 150), P("Membrana perinei (masculina, pars libera)", "", 615, 150)])},
  "'Investigations were performed on embalmed human donors of both sexes (n = 10, mean age at death: 82 years).' 'A relatively thick tissue plate (diameter: 4-5 mm) located superior to a fascia-like structure, the perineal membrane, was observed running transversally to the ischiopubic rami. Macroscopically, a clearly visible transverse running muscle was not observed in both sexes.' 'In both sexes, the volume densities of the connective tissue were approximately 80%.' 'In females, the proportion of the striated muscle cells was less than 1%.'",
  "'There was no evidence of the existence of a clearly definable striated DTP muscle, not only in females but also in males. Muscle cells decreased with increasing age.' Supports teaching the deep pouch as a fibromuscular plate rather than a distinct striated 'urogenital diaphragm'.",
  "J Anat 2025, CC BY 4.0. Fig 3 (posterior/inner view) downloaded, viewed and deleted (crowded numbering, hard to read). Fig 1 also shows the anal triangle (ischioanal fossa) - overlap with the anal-triangle agent only as context. Numbers in the images are white digits."),
 ("perine_lecture", "Male superficial and deep pouch around the bulb: STP superior/inferior bundles, perineal membrane, Cowper's (bulbourethral) gland, DTP", "PMC8373982",
  {"41598_2021_96130_Fig1_HTML.jpg": ("human cadaver (formalin-perfused, 8%)",
    "Inferior (A,B) and inferolateral (C) views of the male perineum: bulbospongiosus over the bulb, ischiocavernosus on the ischiopubic ramus, STP from the ischial tuberosity dividing medially into superior (STPs) and inferior (STPi) bundles, EAS around the anus; Bs and EAS continuous.",
    "A: Bs, IPR, Ic, STP, IT, EAS, Anus, 20 mm, Anterior/R/L, Inferior aspect; B: Ic, STPs, STPi, 10 mm; C: Bs, Ic, IPR, STPs, STPi, IT, EAS, 20 mm, Inferolateral aspect",
    [P("Musculus bulbospongiosus", "Bs", 203, 80), P("Ramus ischiopubicus", "IPR", 125, 137), P("Musculus ischiocavernosus", "Ic", 170, 135),
     P("Musculus transversus perinei superficialis", "STP", 172, 212), P("Tuber ischiadicum", "IT", 67, 273),
     P("Musculus sphincter ani externus", "EAS", 160, 327), P("Anus", "Anus", 223, 397),
     P("Musculus transversus perinei superficialis, fasciculus superior", "STPs", 630, 65),
     P("Musculus transversus perinei superficialis, fasciculus inferior", "STPi", 633, 122),
     P("Musculus bulbospongiosus", "Bs", 580, 285)]),
   "41598_2021_96130_Fig2_HTML.jpg": ("human cadaver (formalin-perfused, 8%)",
    "(A) After removal of Bs and Ic the perineal membrane is seen on both sides of the corpus spongiosum attached to the ischiopubic rami; STPi runs superficial, STPs passes deep to the membrane. (B) After removal of the PM, the deep perineal pouch: paired Cowper's glands posterior to the corpus spongiosum/urethra, DTP deeper and lateral, STPs extending around the glands.",
    "A: CSP, IPR, PM (x2), STPs, STPi, IT, EAS, 10 mm, Anterior/R/L; B: Ur (arrow), CSP, IPR, DTP (x2), CG (x2), STPs, STPi, IT, EAS, dotted lines, 10 mm",
    [P("Corpus spongiosum penis (bulbus penis)", "CSP", 350, 65), P("Ramus ischiopubicus", "IPR", 122, 128),
     P("Membrana perinei", "PM", 230, 155), P("Membrana perinei", "PM", 490, 155),
     P("Musculus transversus perinei superficialis, fasciculus superior", "STPs", 238, 305),
     P("Musculus transversus perinei superficialis, fasciculus inferior", "STPi", 247, 348),
     P("Musculus sphincter ani externus", "EAS", 348, 410),
     P("Urethra", "Ur", 330, 500), P("Corpus spongiosum penis", "CSP", 335, 580),
     P("Glandula bulbourethralis", "CG", 320, 662), P("Glandula bulbourethralis", "CG", 398, 670),
     P("Musculus transversus perinei profundus", "DTP", 232, 660), P("Musculus transversus perinei profundus", "DTP", 482, 650),
     P("Musculus sphincter ani externus", "EAS", 338, 872)])},
  "'In this study, seven male corpses of body donors were used to conduct macroscopic anatomy, histology, and three-dimensional reconstruction. The Cowper's gland was surrounded laterally and posterosuperiorly by striated and smooth muscles, respectively. The striated muscle bundle was connected from the superficial transverse perineal muscle, levator ani, and external anal sphincter to the external urethral sphincter (rhabdosphincter). The smooth muscle was part of the deep transverse perineal muscle and entered between the bilateral Cowper's glands and lobules.'",
  "'Our findings indicate that the secretion and emission of the Cowper's gland in humans are carried out through the cooperation of striated and smooth muscles.' Bulbourethral glands sit in the deep pouch at the bulb - relevant to bulbar urethroplasty and APR/perineal prostatectomy planes.",
  "Sci Rep 2021, CC BY 4.0. Only cadaver photo of the bulbourethral gland in situ found in the OA bucket. Fig 2 is the best single image of PM + deep pouch contents (male)."),
 ("perine_lecture", "Female superficial perineal muscles: bulbospongiosus attaching to the lateral EAS; STP crossing the midline deep to EAS", "PMC6942605",
  {"12565_2019_492_Fig3_HTML.jpg": ("human cadaver (formalin-perfused, 8%)",
    "Lateral (mirror-image) view of a female right perineum: ischiocavernosus, bulbospongiosus and STP; star = bundles between BS and STP; asterisk = STP extending posteriorly along the EAS; hash = medial STP passing along the inner surface of the EAS.",
    "IC, BS, STP, EAS, white star, white asterisk, #, Superior/Anterior arrows",
    [P("Musculus ischiocavernosus", "IC", 150, 118), P("Musculus bulbospongiosus", "BS", 186, 180),
     P("Musculus transversus perinei superficialis", "STP", 302, 183), P("Musculus sphincter ani externus", "EAS", 399, 242),
     P("Fasciculi musculares inter m. bulbospongiosum et m. transversum perinei superficialem", "star", 242, 128),
     P("Musculus transversus perinei superficialis (pars posterior)", "*", 342, 224),
     P("Musculus transversus perinei superficialis (pars medialis)", "#", 309, 243)]),
   "12565_2019_492_Fig4_HTML.jpg": ("human cadaver (formalin-perfused, 8%)",
    "Anteroinferior view of a female pelvis: IC and BS on each side of the vagina, STP on both sides converging toward the anal canal; (B) after reflecting the anterior EAS the STP is seen crossing the midline (arrow) to the contralateral muscle.",
    "A and B: Vagina, BS x2, IC x2, STP (arrows), EAS, Anal, Anterior/Lateral; B also STP with downward arrow at midline",
    [P("Musculus ischiocavernosus", "IC", 441, 73), P("Musculus bulbospongiosus", "BS", 470, 63), P("Ostium vaginae", "Vagina", 532, 55),
     P("Musculus bulbospongiosus", "BS", 586, 60), P("Musculus ischiocavernosus", "IC", 624, 73),
     P("Musculus transversus perinei superficialis (pars mediana)", "STP", 535, 129),
     P("Musculus transversus perinei superficialis", "STP", 469, 118), P("Musculus transversus perinei superficialis", "STP", 593, 126),
     P("Musculus sphincter ani externus", "EAS", 536, 148), P("Anus", "Anal", 525, 179)])},
  "'The pelvic floor muscles of 28 pelvic halves from 16 female cadavers (mean age 79.75 years) were dissected'. 'The bulbospongiosus muscle was found to be attached to the lateral surface of the external anal sphincter. The superficial transverse perineal muscle crossed superiorly to the bulbospongiosus and coursed medially toward its contralateral muscle bundle deep to the anterior portion of the external anal sphincter. The superficial transverse perineal muscle formed the middle sling.'",
  "'This study proposes that three muscular slings could be important in supporting the pelvic floor in women.' Challenges the textbook 'all muscles insert into the perineal body' model - relevant to perineal repair after obstetric tears.",
  "Anat Sci Int 2019, CC BY 4.0. Fig 2 (inferior view) not used here (dark; adds little beyond Fig 3/4) - file kept in the folder because the anal-triangle agent uses it. Fig 4 is small (708x226) but both panels are legible; panel B used for label points."),
 ("perine_lecture", "Male perineal muscles in continuity (lateral view): IC, BS, STP, EAS and their link to levator ani", "PMC7182620",
  {"12565_2019_521_Fig1_HTML.jpg": ("human cadaver (formalin 10%)",
    "Lateral view of a male pelvic floor (A) and after reflecting STP (B): bulbospongiosus and ischiocavernosus anteriorly, STP with its lateral tendon (star) joining BS and EAS (arrows), BS-EAS connection (black asterisk), levator ani above; (B) anterior/posterior LA bundles (arrowheads) reaching BS and EAS.",
    "A: pubis bone, tendinous arch, LA, IC, BS, STP, star, white/black arrows, black asterisk, EAS, ACL, coccyx, yellow arrow, Sup./Ant./Post., Lateral aspect; B: LA, STP, BS, white asterisk, white/black arrowheads, black triangle, circle, black asterisk, EAS, ACL",
    [P("Musculus ischiocavernosus", "IC", 24, 351), P("Musculus bulbospongiosus", "BS", 68, 418),
     P("Musculus transversus perinei superficialis", "STP", 268, 367), P("Tendo lateralis m. transversi perinei superficialis", "star", 341, 333),
     P("Musculus sphincter ani externus", "EAS", 318, 462), P("Musculus levator ani", "LA", 294, 227),
     P("Junctio m. bulbospongiosi et m. sphincteris ani externi", "black asterisk", 156, 441)])},
  "'Fifteen male pelvises were used for microscopic dissection, and three male pelvises were used for histological examination. On the lateral aspect, the perineal muscles were connected to each other. Bundles of the levator ani muscle extended to connect to the perineal muscles. In addition, the extended muscle bundle from the levator ani muscle and the perineal muscles surround the external urethral sphincter.'",
  "'The connection between the perineal muscles and levator ani muscle indicates a possible close relationship between the functions of the urethra and anus.'",
  "Anat Sci Int 2019, CC BY 4.0. Figure is dominated by levator ani (pelvic-floor territory) - use panel A for the perineal-muscle continuity concept; coordinates given only for panel A."),
 ("perine_lecture", "Female external genitalia & superficial pouch on cadaver: crus/body/glans clitoridis, bulb of vestibule, STP, suspensory ligament; perineal body", "PMC7913006",
  {"diagnostics-11-00221-g004.jpg": ("human cadaver (embalmed: 3% formaldehyde/phenol/glycerin)",
    "Dissected female perineum after continuing a mediolateral episiotomy incision: body, glans and crus of the clitoris, suspensory ligament of the clitoris, the bulb of the vestibule overlain by bulbospongiosus (*), superficial (S) and deep (D) perineal neurovascular bundles and the superficial transverse perineal muscle.",
    "Suspensory ligament of the clitoris; Body of the clitoris; Crus of the clitoris (2 arrows); Glans clitoridis; Neurovascular bundles; S; D; *; Labum majus [sic]; Superficial transverse perineal m.",
    [P("Ligamentum suspensorium clitoridis", "Suspensory ligament of the clitoris", 357, 43),
     P("Corpus clitoridis", "Body of the clitoris", 316, 193), P("Glans clitoridis", "Glans clitoridis", 256, 320),
     P("Crus clitoridis", "Crus of the clitoris", 387, 229), P("Crus clitoridis", "Crus of the clitoris", 500, 261),
     P("Bulbus vestibuli sub m. bulbospongioso", "*", 455, 321),
     P("Nervus perinealis, rami superficiales (fasciculus neurovascularis)", "S", 389, 350),
     P("Nervus perinealis, rami profundi (fasciculus neurovascularis)", "D", 500, 354),
     P("Musculus transversus perinei superficialis", "Superficial transverse perineal m.", 551, 464),
     P("Labium majus pudendi", "Labum majus", 200, 420)]),
   "diagnostics-11-00221-g003.jpg": ("schematic",
    "Authors' illustration of the female perineum based on their dissections: body and crus of the clitoris, bulb of the vestibule with the greater vestibular (Bartholin) gland at its posterior end, bulbospongiosus continuous with the superficial EAS, subcutaneous EAS, and the perineal/posterior labial/inferior rectal branches of the pudendal nerve.",
    "Body of the clitoris; Crus; Bulb of the vestibule; Greater vestibular gland; Superficial EAS; Subcutaneous EAS; Bulbospongiosus m.; Posterior labia nn.; Deep perineal n.; Superficial perineal n.; Inferior rectal n.; Pudendal n.",
    [P("Corpus clitoridis", "Body of the clitoris", 353, 133), P("Crus clitoridis", "Crus", 299, 179),
     P("Bulbus vestibuli", "Bulb of the vestibule", 319, 257), P("Glandula vestibularis major", "Greater vestibular gland", 330, 284),
     P("Musculus bulbospongiosus", "Bulbospongiosus m.", 387, 155), P("Nervi labiales posteriores", "Posterior labia nn.", 380, 203),
     P("Nervus perinealis, rami profundi", "Deep perineal n.", 414, 229), P("Nervus perinealis, rami superficiales", "Superficial perineal n.", 407, 302),
     P("Musculus sphincter ani externus, pars superficialis", "Superficial EAS", 328, 344),
     P("Musculus sphincter ani externus, pars subcutanea", "Subcutaneous EAS", 355, 394),
     P("Nervi anales (rectales) inferiores", "Inferior rectal n.", 413, 374), P("Nervus pudendus", "Pudendal n.", 452, 365)]),
   "diagnostics-11-00221-g002.jpg": ("human cadaver (embalmed)",
    "External view of a cadaver female perineum with a midline and a low-angle mediolateral episiotomy incision: vaginal orifice, perineal body (between vestibule and anus), posterior edge of the bulb of the vestibule exposed by the mediolateral cut, and anal orifice.",
    "Labum majus [sic]; Vaginal orifice; Mediolateral episiotomy incision; Midline episiotomy incision; Perineal body; Posterior edge of the bulb of the vestubule [sic]; Anal orifice",
    [P("Ostium vaginae", "Vaginal orifice", 335, 668), P("Corpus perineale", "Perineal body", 415, 1005),
     P("Bulbus vestibuli (margo posterior)", "Posterior edge of the bulb of the vestubule", 225, 965),
     P("Anus", "Anal orifice", 390, 1113)])},
  "'We performed 61 incisions on 47 female cadavers and dissected around the incision site.' 'Midline IncisionIn 100% of cadavers, the midline incision damaged the connective tissue of the perineal body and overlying skin' 'In 16.6% of cadavers, we identified gracile muscle fibers inserting onto the perineal body, while 83.4% had only connective tissue within the incision.' 'In 14.3% of cadavers, the incision was of sufficient length to completely bisect the perineal body and extend to some muscle fibers of the subcutaneous portion of the external anal sphincter'. 'Low-Angle Mediolateral IncisionIn 75% of cadavers, the bulbospongiosus muscle, greater vestibular gland, and posterior labial nerves were in the plane of the incision.'",
  "'Mediolateral incisions posed greater risk of iatrogenic injury to ipsilateral nerve, muscle, erectile, and gland tissues.' Direct link of superficial-pouch anatomy (bulb, Bartholin gland, perineal nerves) and perineal body to episiotomy complications.",
  "Diagnostics 2021, CC BY 4.0. Fig 3 is the only labelled image of the greater vestibular (Bartholin) gland found (schematic, authors' own; no third-party attribution in caption). Fig 2 is an external cadaver view (hair/skin) - consider audience. Text typos 'Labum', 'vestubule' are printed in the images. Doubles as variation source (perineal body composition percentages)."),
 ("perine_lecture", "Clitoris as a 3D organ: excised clitoris (body, crura, suspensory ligament, prepuce) and microCT reconstruction with vestibular bulbs", "PMC11452485",
  {"41598_2024_72898_Fig1_HTML.jpg": ("human cadaver (formalin-fixed vulva samples)",
    "(A) Excised vulva block from the front (mons pubis, labia majora/minora); (B) the dissected clitoris in lateral view: body with suspensory ligament and prepuce, and the two crura descending; dashed lines = sampling levels; (C,D) cross-sections of crus and body with corpora cavernosa and dorsal neurovascular bundles.",
    "A: Mons Pubis, Labia Majora, Labia Minora; B: Suspensory ligament, Prepuce, Crura (2 leaders), dashed lines, 1 cm; C: Neurovascular bundle, CC, arrowheads, dashed circle, 1 cm; D: CC x2, arrowheads, dashed circle, 1 cm",
    [P("Mons pubis", "Mons Pubis", 183, 55), P("Labium majus pudendi", "Labia Majora", 265, 155),
     P("Labium minus pudendi", "Labia Minora", 225, 228), P("Ligamentum suspensorium clitoridis", "Suspensory ligament", 395, 140),
     P("Preputium clitoridis", "Prepuce", 683, 185), P("Crus clitoridis", "Crura", 460, 290), P("Crus clitoridis", "Crura", 480, 340)]),
   "41598_2024_72898_Fig2_HTML.jpg": ("human cadaver (microCT of iodine-stained formalin-fixed specimen; 3D reconstruction)",
    "MicroCT of a cadaver vulva (A) with volume-rendered segmentation (B frontal, C lateral) of corpora cavernosa (blue: body + crura), corpus spongiosum (orange), vestibular bulbs (green) and glans clitoridis (pink); (D,E) microCT sections labelled CC, CS, VB; (F) azan histology.",
    "A-F; D: CC x2, CS; E: CS, VB x2; colour coding explained only in caption",
    [P("Corpus cavernosum clitoridis (crus)", "", 370, 50), P("Corpus spongiosum (pars intermedia bulborum)", "", 318, 72),
     P("Glans clitoridis", "", 338, 90), P("Bulbus vestibuli", "", 280, 140), P("Bulbus vestibuli", "", 375, 145),
     P("Corpus cavernosum clitoridis", "CC", 125, 372), P("Corpus spongiosum", "CS", 115, 430),
     P("Corpus spongiosum", "CS", 390, 442), P("Bulbus vestibuli", "VB", 338, 507), P("Bulbus vestibuli", "VB", 415, 492)])},
  "'We counted on avarage 2917 axons in the crus of the clitoris (76% of which are myelinated) and 3137 axons in the hemibody of the clitoris (71% of which are myelinated).' 'In the crus of the clitoris, about 12 such bundles can be recognized while about 32 bundles are present in the clitoral hemi-body.' 'clitoris has approximately 6 times denser innervation compared to the penis.' Specimens: 'Formalin-fixed vulva samples were collected from 6 female cadavers'.",
  "Dorsal nerve of clitoris runs as loose bundles - relevant to vulvar/cosmetic surgery, FGM reconstruction and gender-affirming surgery.",
  "Sci Rep 2024, CC BY 4.0 (O'Connell-type 3D clitoral anatomy). O'Connell's own papers (J Urol 1998/2005) are not in the PMC OA bucket. 'avarage' typo is verbatim. In Fig 2B the blue CC rendering includes the crura; colours carry the meaning - Turkish legend needed."),
 ("perine_lecture", "Penile root suspension: fundiform ligament (from the membranous superficial fascia) and suspensory ligament with its three bundles", "PMC10594829",
  {"12610_2023_202_Fig5_HTML.jpg": ("human cadaver (formalin-fixed)",
    "Anterior view of the penopubic region after removing skin and superficial fascia: right and left bundles of the fundiform ligament embracing the penis, the deeper suspensory ligament in the midline, and both spermatic cords laterally.",
    "1, 2, 3, 4, 5 (black digits)",
    [P("Ligamentum fundiforme penis, fasciculus dexter", "1", 287, 236), P("Ligamentum fundiforme penis, fasciculus sinister", "2", 371, 237),
     P("Ligamentum suspensorium penis", "3", 316, 241), P("Funiculus spermaticus dexter", "4", 157, 150), P("Funiculus spermaticus sinister", "5", 481, 154)]),
   "12610_2023_202_Fig9_HTML.jpg": ("human cadaver (formalin-fixed)",
    "Suspensory ligament of the penis dissected into a median bundle and two lateral bundles attaching to the dorsum of the penile body, with the reflected right/left fascicles of the fundiform ligament and both spermatic cords.",
    "1-9 (black digits)",
    [P("Ligamentum suspensorium penis", "1", 263, 383), P("Ligamentum suspensorium penis, fasciculus lateralis", "2", 230, 448),
     P("Ligamentum suspensorium penis, fasciculus lateralis", "3", 303, 445), P("Ligamentum suspensorium penis, fasciculus medianus", "4", 268, 453),
     P("Corpus penis", "5", 292, 620), P("Ligamentum fundiforme penis, fasciculus dexter", "6", 140, 268),
     P("Ligamentum fundiforme penis, fasciculus sinister", "7", 310, 263), P("Funiculus spermaticus dexter", "8", 32, 513),
     P("Funiculus spermaticus sinister", "9", 450, 508)])},
  "'We dissected the ligaments providing the suspension of the penis in 7 formalized corpses.' 'We have identified three types of fundiform ligament: A unique triangular structure; A double structure accompanied by accessory fascicles; A ligament structure with the aspect of an undifferentiated fibrous connective band.' 'For the suspensory ligament, we identified three groups of fibers through which it is attached to the penile body.' 'the suspensory ligament is represented by three blades: two superficial blades sharing the role of the fundiform ligament and a deep blade on the midline, which is continued by the deep fascia of the penis'.",
  "Ligament sectioning in penile lengthening risks the dorsal neurovascular bundle and penile instability; the fundiform ligament is a derivative of the membranous layer of the abdominal superficial fascia (Scarpa) - the Scarpa-Colles-dartos continuum at the penile root.",
  "Basic Clin Androl 2023, CC BY 4.0. Closest OA cadaver material to the 'fascia penis / Scarpa continuity' topic. Fig 1 (unexplained numbers in caption) and Fig 12 (dorsal NV bundle - pudendal territory of another agent) downloaded, viewed, deleted. The caption of Fig 5 lists numbers; '4/5' spermatic cords are the tubular structures lateral to the penis."),
 ("perine_lecture", "Sex differences of the deep pouch: rhabdosphincter, compressor urethrae, urethrovaginal sphincter, perineal membrane, Cowper's gland, DTP (author diagrams)", "PMC4022307",
  {"BMRI2014-906921.011.jpg": ("schematic",
    "Female, lateral view through the bony pelvis: rhabdosphincter (RS) around the urethra, compressor urethrae (CU) and urethrovaginal sphincter (UVS) continuous with the thick perineal membrane (PM) that anchors them to the ischiopubic ramus; levator ani attaches to the upper surface of the PM; vestibular bulb and bulbospongiosus below.",
    "Uterus, Bladder, Vagina, Pubis, RS, CU, Levator ani (x2), Urethra, PM, UVS, External anal sphincter, Vestibular bulb, Bulbospongiosus muscle, Anus",
    [P("Musculus sphincter urethrae externus (rhabdosphincter)", "RS", 190, 302), P("Urethra feminina", "Urethra", 154, 385),
     P("Musculus sphincter urethrovaginalis", "UVS", 237, 446), P("Musculus compressor urethrae", "CU", 275, 375),
     P("Membrana perinei", "PM", 283, 492), P("Bulbus vestibuli", "Vestibular bulb", 137, 525),
     P("Musculus bulbospongiosus", "Bulbospongiosus muscle", 171, 500), P("Musculus levator ani", "Levator ani", 404, 354),
     P("Musculus sphincter ani externus", "External anal sphincter", 383, 588), P("Os pubis", "Pubis", 104, 204), P("Vagina", "Vagina", 417, 196)]),
   "BMRI2014-906921.010.jpg": ("schematic",
    "Male, lateral view: rhabdosphincter (RS) around the membranous urethra continuing up as prostatocapsular RS, Cowper's gland in the deep pouch below RS, deep transverse perineal muscle behind it, levator ani lateral with veins and nerves between; stars = connection of RS to perineal muscles.",
    "Prostatocapsular RS, Bladder, Pubis, Prostate, RS, Levator ani, Veins and nerves, Urethra, Cowper's gland, Deep transverse perineal muscle, External anal sphincter, Anus, stars",
    [P("Musculus sphincter urethrae externus (rhabdosphincter)", "RS", 158, 358), P("Urethra (pars spongiosa)", "Urethra", 183, 483),
     P("Glandula bulbourethralis", "Cowper's gland", 250, 483), P("Musculus transversus perinei profundus", "Deep transverse perineal muscle", 296, 467),
     P("Prostata", "Prostate", 175, 263), P("Musculus levator ani", "Levator ani", 442, 229),
     P("Musculus sphincter ani externus", "External anal sphincter", 433, 467), P("Os pubis", "Pubis", 121, 217)])},
  "Review of the authors' serial-section studies in elderly cadavers: 'The male perineal membrane was thin but solid and extends along the inferior margin or bottom of the rhabdosphincter area. In contrast, the female rhabdosphincter, including the compressor urethrae and urethrovaginal sphincter muscles, was embedded in the elastic fiber mesh that is continuous with the thick, multilaminar perineal membrane. The inferomedial edge of the female LA was attached to the upper surface of the perineal membrane and not directly attached to the rhabdosphincter.'",
  "Continence anatomy for radical prostatectomy and female anti-incontinence surgery: 'We presented new diagrams showing the gender differences in topographical anatomy of the LA and rhabdosphincter.'",
  "Biomed Res Int 2014, CC BY 3.0. Author diagrams (no cadaver photo of CU/UVS exists in the OA bucket); histology figures of the same article not used (cross-sectional)."),
 ("perine_lecture", "Female external urethral sphincter: horseshoe-shaped skeletal muscle around the mid-urethra (3D reconstruction from cadaver serial sections)", "PMC12003430",
  {"192_2025_6045_Fig3_HTML.jpg": ("human cadaver (formalin; 3D reconstruction of serial histology)",
    "3D reconstructions (anterior A,C,E,G; posterior B,D,F,H) of the female urethral muscle coats: inner longitudinal (uLM) and circular (uCM) smooth muscle, the red horseshoe-shaped external urethral sphincter open dorsally, and an outer smooth-muscle layer continuous with the vaginal wall (Vm).",
    "A: Ur, uLM, 20mm, axes; B: Ur, uLM; C: Ur, uCM, uLM; D: uCM; E: Ur, EUS, dagger; F: uCM, EUS; G: Ur, sm, Vm, EUS, uCM, triangles; H: sm, Vm, EUS",
    [P("Musculus sphincter urethrae externus", "EUS", 416, 95), P("Urethra feminina", "Ur", 432, 22),
     P("Musculus sphincter urethrae externus (pars posterior, aperta)", "EUS", 402, 267),
     P("Musculus sphincter urethrae externus", "EUS", 591, 105), P("Tunica muscularis externa (stratum leve)", "sm", 595, 52)])},
  "'Pelvises from five female cadavers were collected for histological analysis.' 'The female urethra was surrounded by four muscle layers arranged from inner to outer layers in the following order: longitudinal smooth muscle, circular smooth muscle, the external urethral sphincter (EUS), and an outermost smooth muscle layer.' 'Moreover, smooth muscle fibers extending from the vagina were found between the LA and EUS.'",
  "'This study clarified the distribution of muscle tissue surrounding the female urethra, showing that the EUS is connected to the LA through the outermost smooth muscle layer. Thus, urination control likely involves both the urethral muscle layers and the pelvic floor muscles.'",
  "Int Urogynecol J 2025, CC BY 4.0. Reconstruction, not a dissection photo; supporting figure for the deep-pouch sphincter slide."),
 # ---------------- perine_variation ----------------
 ("perine_variation", "Perineal body size on transperineal ultrasound: normal nulliparous vs prolapse (morphometry)", "PMC7270988",
  {"192_2019_4166_Fig1_HTML.jpg": ("US",
    "2D transperineal ultrasound (midsagittal): (a) normal perineal body (red arrows) between urethra/bladder anteriorly and anal canal posteriorly; (b) outline of PB length, height, perimeter and area; (c) measurements in a healthy volunteer; (d) small PB in a prolapse patient.",
    "a: Bladder, Ur, AC, PB, red arrows; b: PB Height, PB Perimeter and Area, PB Length, Anal canal; c: A, measurement box 1 D 33.7mm, 2 D 25.5mm, 3 A 5.05cm2, C 11.93cm; d: B, 1 D 5.6mm, 2 D 9.7mm, 3 A 0.51cm2, C 2.96cm",
    [P("Vesica urinaria", "Bladder", 115, 102), P("Urethra feminina", "Ur", 150, 117), P("Canalis analis", "AC", 238, 117),
     P("Corpus perineale", "PB", 217, 146)])},
  "'A total of 101 participants were recruited of which 22 were nulliparous healthy volunteers. Mean perineal body measurements in controls were height 22.5 ± 3.3 mm, length 17.4 ± 2.7 mm, perimeter 7.5 ± 0.9 mm, and area 2.8 ± 0.38 cm2. Perineal body measurements in 79 prolapse patients: height 16.9 ± 1.7 mm, length 16.0 ± 1.4 mm, perimeter 6.5 ± 0.5 mm and area 2.1 ± 0.5 cm2.'",
  "'A small perineal body was strongly associated with posterior compartment prolapse (paired t test, p < 0.0001)'. 'A perineal body mid-sagittal area of less than 2.4 cm2 has been shown to be associated strongly with posterior compartment prolapse.'",
  "Int Urogynecol J 2020, CC BY 4.0. IMAGING (US) - used because no OA cadaver morphometry of the perineal body was found. NOTE: abstract states perimeter in 'mm' (7.5 ± 0.9) but the on-screen values (11.93 cm) indicate cm - quote verbatim and flag."),
 ("perine_variation", "Female external genital morphometry in 208 Turkish women (clitoral glans, prepuce, clitoris-urethra, perineal body length)", "PMC7538817",
  {"TJOG-17-175-g1.jpg": ("schematic",
    "Author drawing of the vulva with dashed measurement lines: clitoral glans width/length, clitoral prepuce length, clitoris-to-urethra, labia majora/minora length and width, vagina-to-perineum and perineal body length.",
    "clitoral glans width; clitoral prepuce lenght [sic]; clitoral glans lenght [sic]; clitoris to urethra; labia majora length; labia minora lenght [sic]; vagina to perineum; perineal body lenght [sic]; labia minora width; labia majora width",
    [P("Glans clitoridis", "clitoral glans width", 235, 99), P("Ostium urethrae externum", "clitoris to urethra", 235, 170),
     P("Ostium vaginae", "", 235, 255), P("Corpus perineale", "perineal body lenght", 235, 325),
     P("Labium minus pudendi", "labia minora width", 265, 225)])},
  "'This prospective cohort study consisted of 208 healthy premenopausal women.' 'The external female genital measurements were (cm, mean ± standard deviation): clitoral prepuce length 2.05±0.48; clitoral glans length 0.87±0.21; clitoral glans width 0.60±0.15; clitoris to urethra 2.24±0.55; anterior fornix depth 7.75±0.92; posterior fornix depth 9.25±0.75; labia minora width, right 2.12±0.86, left 2.20±0.96.'",
  "'The female genital measurements were found to be distributed over a wide range.' '...no significant relationship was found between genital measurements and sexual functions or orgasm. These findings suggest that a more cautious approach should be taken towards genital surgeries for cosmetic purposes.'",
  "Turk J Obstet Gynecol 2020 (Turkish population!), CC BY 2.5. Living women, not cadaver. Perineal body length was measured (definition: 'The length from the posterior fourchette to mid-anal orifice') but its value is only in Table 1, which is an image not in the XML - do not cite a number. Drawing is low-resolution (450x423)."),
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

(ROOT / "sources/perine_urogenital.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(len(out), "entries;", sum(len(e["figures"]) for e in out), "figures;",
      sum(len(f["label_points"]) for e in out for f in e["figures"]), "label points")
for e in out:
    print(f"{e['use']:16} {e['pmcid']:12} {e['license_code']:8} {[(f['file'], len(f['label_points'])) for f in e['figures']]}")
