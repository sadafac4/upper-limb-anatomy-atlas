#!/usr/bin/env python3
"""Build sources/perine_anal.json (PERINE - anal triangle, pudendal neurovasculature, perineal surface/boundaries)
from downloaded PMC OA files in perine/images/raw/PMC<id>/.

Citation, DOI, licence, title, authors, journal, year, verbatim captions and pixel sizes are read from the files;
only the descriptive fields and label_points below are hand-written (after viewing every figure and verifying every
coordinate on zoomed PIL crops). label_points xy are pixel coordinates in the ORIGINAL image (x right, y down) at the
author's arrow tip / leader-line end / printed label on the structure.
Run: python3 -I scripts/build_perine_anal.py
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
 # ======================= perine_lecture =======================
 ("perine_lecture", "Deep gluteal approach: pudendal neurovascular bundle crossing the ischial spine/sacrospinous ligament, sacrotuberous ligament (cut), ischioanal fossa roof (levator ani), anococcygeal ligament, EAS", "PMC8713160",
  {"etm-23-02-11036-g01.jpg": ("human cadaver (embalmed), posterior view of right deep gluteal region",
    "Gluteus maximus removed and sacrotuberous ligament cut (16): the internal pudendal neurovascular bundle (11) leaves the pelvis below piriformis (1), crosses the ischial spine (10) / sacrospinous ligament (17) and re-enters through the lesser sciatic foramen medial to obturator internus (2) and the ischial tuberosity (3); medially the ischioanal fossa is opened showing levator ani as its supero-medial wall (4), the anococcygeal ligament (5) and the external anal sphincter (14).",
    "numbers only: 1-17 (black/orange digits printed on structures)",
    [P("M. piriformis", "1", 310, 248), P("M. obturatorius internus", "2", 326, 420),
     P("Tuber ischiadicum", "3", 330, 552), P("M. levator ani (paries superomedialis fossae ischioanalis)", "4", 135, 492),
     P("Lig. anococcygeum", "5", 36, 510), P("N. ischiadicus", "9", 388, 366), P("Spina ischiadica", "10", 318, 348),
     P("Vasa pudenda interna et n. pudendus (fasciculus neurovascularis pudendus internus)", "11", 258, 433),
     P("M. gluteus maximus", "12", 580, 152), P("M. sphincter ani externus", "14", 70, 660),
     P("Lig. sacrotuberale (insertiones resectae)", "16", 148, 278), P("Lig. sacrotuberale (insertio resecta)", "16", 296, 517),
     P("Lig. sacrospinale", "17", 225, 272)])},
  "Romanian dissection + MRI study. 'The anterior divisions of the S2, S3 and S4 spinal nerves give rise to the pudendal nerve.' 'This nerve, together with the internal pudendal artery, are closely associated with the rigid superior border of the sacrospinous ligament, actually passing between the piriformis muscle and the sacrospinous ligament and then between the ligament and the upper border of the sciatic spine.' 'The elements of the internal pudendal neurovascular bundle follow their extrapelvic course surrounding the ischial spine in the deep gluteal region in order to reenter the pelvis through the lesser sciatic notch.'",
  "Shows the interligamentous (sacrospinous-sacrotuberous) segment - the commonest entrapment site - and the transgluteal landmark (ischial spine) used for pudendal block and decompression.",
  "LICENCE CC BY-NC-ND: non-commercial, no derivatives - use unmodified (no overlay labels drawn onto the image; place Turkish legend beside it). Best single topographic figure of the set (646x781)."),
 ("perine_lecture", "Pelvic (internal) view: pudendal nerve and internal pudendal artery at the sacrospinous ligament, branches in the ischioanal fossa, anococcygeal ligament", "PMC8713160",
  {"etm-23-02-11036-g00.jpg": ("human cadaver (embalmed), medial view of hemipelvis, levator ani reflected",
    "Internal view of the lateral pelvic wall with levator ani reflected (6) and cut (7): the internal pudendal artery (red dotted line) and pudendal nerve (green arrows) from S2-S4 pass over the sacrospinous ligament (9)/coccygeus (10), then run forward below obturator internus (5) giving inferior rectal, perineal and dorsal clitoral branches; anococcygeal ligament (11) and coccyx (12) posteriorly.",
    "numbers 1-15, LST, S1-S4; red dotted line (internal pudendal artery); green arrows (pudendal nerve and branches)",
    [P("N. pudendus", "green arrow", 213, 378), P("A. pudenda interna", "red dotted line", 180, 330),
     P("Rami n. pudendi (n. dorsalis clitoridis / n. perinealis / nn. rectales inferiores)", "green arrow", 470, 330),
     P("Rami n. pudendi (n. dorsalis clitoridis / n. perinealis / nn. rectales inferiores)", "green arrow", 468, 395),
     P("Rami n. pudendi (n. dorsalis clitoridis / n. perinealis / nn. rectales inferiores)", "green arrow", 391, 442),
     P("M. obturatorius internus", "5", 340, 268), P("Lig. sacrospinale", "9", 232, 474), P("M. coccygeus", "10", 340, 512),
     P("Lig. anococcygeum", "11", 402, 575), P("Os coccygis", "12", 360, 615), P("Rectum", "13", 600, 490)])},
  "Same study as above (see key findings).",
  "Internal view complements the gluteal view: the pudendal canal contents seen from the pelvic side after levator ani reflection.",
  "LICENCE CC BY-NC-ND. Caption does not say which green arrow is which branch; only generic 'branches' are labelled. Female specimen (dorsal nerve of clitoris)."),
 ("perine_lecture", "Pudendal (Alcock's) canal opened on a female cadaver", "PMC529451",
  {"1471-2482-4-15-3.jpg": ("human cadaver (female), perineal (trans-ischioanal) approach, operative-style photo",
    "Left Alcock's canal opened (tip of forceps) from the medial side through the ischioanal fossa: pudendal nerve on the left of the image; the inferior rectal nerve is said to be on the finger at right (not clearly discernible).",
    "no printed labels (forceps and a black suture only)",
    [P("N. pudendus", "", 60, 145), P("Canalis pudendalis (Alcock)", "tip of the forceps", 182, 200)])},
  "Retrospective series of 'bilateral PND' in 74 women. 'When bilateral PND was the only procedure done to treat the symptoms, the cure rates of perineodynia, anal incontinence and urinary incontinence were 8/14, 4/5 and 3/5, respectively.' Anatomy as stated by the authors: 'In the canal the nerve crosses the sharp edge of the sacro-tuberous ligament (falciform process)'. Shafik trans-perineal technique: 'Vertical incision of the skin between the anus and the ischial tuberosity.- Opening of the ischio-rectal fossa with scissors.- The inferior rectal nerve is hooked under the finger and followed to the entrance of the Alcock's canal'.",
  "Pudendal canal syndrome (entrapment) and trans-perineal (Shafik) decompression via the ischioanal fossa; the inferior rectal nerve is the guide to the canal entrance.",
  "Small (347x287) video-still; use at half-slide. Companion Fig 4 (view from below) was rejected - nerve not identifiable with confidence. Only cadaver figure in our set that is centred on the opened canal itself; also the only OA source here mentioning the falciform process."),
 ("perine_lecture", "Transgluteal exposure: surface landmarks, sacrotuberous ligament, pudendal nerve in Alcock's canal beside the sciatic nerve", "PMC6785340",
  {"10-1055-s-0039-1688513_00198_01.jpg": ("human cadaver (formalin-fixed), prone, surface",
    "Skin markings for the O'Bichere gluteal approach: midpoint of the lateral border of the sacrum, both ischial tuberosities and the greater trochanter joined by lines (posterior/prone view of the perineum-gluteal region).",
    "Mid point of sacrum; Gr. trochanter; Ischial tuberosity (two arrows)",
    [P("Tuber ischiadicum (dextrum)", "Ischial tuberosity", 175, 262), P("Tuber ischiadicum (sinistrum)", "Ischial tuberosity", 322, 272),
     P("Os sacrum (punctum medium marginis lateralis)", "Mid point of sacrum", 258, 172), P("Trochanter major", "Gr. trochanter", 482, 214)]),
   "10-1055-s-0039-1688513_00198_03.jpg": ("human cadaver (formalin-fixed), prone, gluteal approach",
    "Gluteus maximus split, retracted, exposing the white band of the sacrotuberous ligament (red arrow).",
    "Sacrotuberous ligament (red arrow)",
    [P("Lig. sacrotuberale", "Sacrotuberous ligament", 285, 368)]),
   "10-1055-s-0039-1688513_00198_04.jpg": ("human cadaver (formalin-fixed), prone, gluteal approach",
    "After division of the sacrotuberous ligament: pudendal nerve exposed in Alcock's canal (medial) and sciatic nerve lateral to the ischial tuberosity, with a ruler between them.",
    "Pudendal nerve; Sciatic nerve (red arrows); ruler",
    [P("N. pudendus (in canali pudendali)", "Pudendal nerve", 276, 231), P("N. ischiadicus", "Sciatic nerve", 322, 246)])},
  "'Pudendal and sciatic nerves were exposed in 5 (4 male and 1 female) human cadavers (10 sites).' 'Mean pudendal nerve diameter was 2.94 mm (range = 2.7–3.1 mm) on the right side and 2.82 mm (range = 2.5–3 mm) on the left.' 'The distance between the two nerves was 23.4 mm (range = 20–26 mm) on both sides'.",
  "Gluteal (transgluteal) route to the pudendal nerve used for decompression; proposed sciatic-to-pudendal nerve transfer for continence.",
  "LICENCE CC BY-NC-ND. Fig 1 is in the PRONE position (not lithotomy) but still gives the bony landmarks (ischial tuberosities, sacrum) in a cadaver. Indian J Plast Surg."),
 ("perine_lecture", "Anal triangle from below (male): EAS, ischial tuberosity, ischiopubic ramus, coccyx, anus - perineal boundaries in a dissected cadaver", "PMC7898478",
  {"CA-34-272-g001.jpg": ("human cadaver (male, formalin), inferior aspect = lithotomy-like view after removal of subcutaneous tissue",
    "Panel a: whole perineum from below with skin/fat removed: ischial tuberosity (IT), ischiopubic ramus (IPR), ischiocavernosus (Ic), bulbospongiosus (Bs), superficial transverse perineal muscle (STP), external anal sphincter (EAS) around the anus and coccyx (Co) - i.e. both perineal triangles and their bony boundaries; ischioanal fossae open lateral to the EAS. Panels b-c: magnified EAS-STP continuity and the median 'columnar structure'.",
    "(a) Inferior aspect, Bs, IPR, Ic, IT, STP, EAS, Anus, Co, arrowheads, R/L/Anterior; (b) IPR, Ic, Bs, IT, n, STP, EAS; (c) IPR, Ic, CSP, IT, STP, EAS, circle",
    [P("Tuber ischiadicum", "IT", 28, 244), P("Ramus ischiopubicus", "IPR", 86, 156), P("M. ischiocavernosus", "Ic", 131, 169),
     P("M. bulbospongiosus", "Bs", 210, 82), P("M. transversus perinei superficialis", "STP", 138, 229),
     P("M. sphincter ani externus", "EAS", 149, 301), P("Anus", "Anus", 195, 369), P("Os coccygis", "Co", 205, 457)])},
  "'Three male cadavers (ages at death, 64, 75, and 89 years) were used for the macroscopic examination.' Caption: 'A portion of the muscle bundles of the EAS extends anteriorly and continues to the Bs in the midline' and 'The EAS and STP share muscle bundles and are continuous'.",
  "The cleanest cadaveric 'map' of the perineal outlet: tuber ischiadicum - ramus ischiopubicus - coccyx frame, the line between the tuberosities separating trigonum urogenitale and trigonum anale.",
  "LICENCE CC BY-NC-ND. Panel a carries the anal-triangle content; ND licence means the figure must be shown unmodified (no cropping/overlays). Shared interest with the urogenital-triangle agent (Bs/Ic/STP)."),
 ("perine_lecture", "Female perineum from below: EAS and ischioanal fat body lateral to it", "PMC6942605",
  {"12565_2019_492_Fig2_HTML.jpg": ("human cadaver (female, formalin), inferior aspect",
    "Left half of a female perineum from below: EAS posteromedially, STP crossing anterior to the ischioanal fossa whose yellow fat body (unlabelled) has been exposed lateral to the EAS; BS and IC anteriorly.",
    "IC, BS, STP, EAS; Anterior / Medial orientation arrows",
    [P("M. ischiocavernosus", "IC", 328, 378), P("M. bulbospongiosus", "BS", 225, 428),
     P("M. transversus perinei superficialis", "STP", 360, 585), P("M. sphincter ani externus", "EAS", 140, 900),
     P("Corpus adiposum fossae ischioanalis", "", 430, 750)])},
  "'A total of 28 pelvic halves from 16 female cadavers (age range 54–99 years, mean age 79.75 years) were used for dissection.' Caption: 'The muscle bundle of the BS fuses with the lateral surface of the EAS.'",
  "Ischioanal fat body (corpus adiposum) is the space of ischioanal abscess spread; its anterior boundary is the STP/perineal membrane level.",
  "Article folder shared with another agent (Figs 3-5 belong to them); only Fig 2 used here. Fat body is unlabelled by the authors - Turkish legend must say so."),
 ("perine_lecture", "Schematic: EAS, anococcygeal ligament and levator ani 'posterior sling' (puborectalis) seen from below", "PMC10256674",
  {"12565_2023_717_Fig1_HTML.jpg": ("author schematic (based on cadaver dissections)",
    "A: medial view of female pelvic outlet muscles; B: inferior view showing levator ani anterior and posterior slings around the anal canal (posterior sling = classic puborectalis), STP as 'middle sling', EAS and the anococcygeal ligament (ACL) attaching to the coccyx.",
    "A: Pubis, LA, Coccyx, ACL, Bs, Ic, Anterior sling, LA, STP (Middle sling), EAS, Posterior sling, Anus; B: Anterior sling, Posterior sling, ACL, Coccyx, V, AC, Pubis, Bs, Ic, LA, EAS, STP (Middle sling), Inferior aspect",
    [P("M. levator ani - ansa anterior", "Anterior sling", 516, 137), P("M. puborectalis (ansa posterior m. levatoris ani)", "Posterior sling", 610, 132),
     P("Lig. anococcygeum", "ACL", 635, 150), P("Os coccygis", "Coccyx", 650, 157), P("Canalis analis", "AC", 570, 155),
     P("M. sphincter ani externus", "EAS", 585, 185), P("M. levator ani", "LA", 558, 205),
     P("M. transversus perinei superficialis", "STP (Middle sling)", 525, 205), P("M. bulbospongiosus", "Bs", 495, 192),
     P("M. ischiocavernosus", "Ic", 472, 204)])},
  "Review of the authors' cadaver work. 'It is widely known that some muscle bundles of the LA form a sling that goes around the posterior to the anal canal, which is generally called “puborectalis”'. 'The more posterior muscle bundles of the LA attach to the connective tissue that is called as the anococcygeal raphe when the bilateral LA meets the posterior median plane'.",
  "Explains continence mechanics and why 'anococcygeal raphe/ligament' terminology varies (Courtney's coccygeal muscular raphe, levator plate, dorsal layer of the ACL).",
  "Schematic, CC BY. Points are for panel B only. Caption notes 'Modified from: Baramee et al. 2020'."),
 ("perine_lecture", "Schematic: pudendal nerve branches in the female anal/urogenital triangles (lithotomy view)", "PMC7913006",
  {"diagnostics-11-00221-g003.jpg": ("author illustration (based on dissection of 47 embalmed female cadavers)",
    "Lithotomy-view drawing of the female perineum: pudendal nerve entering lateral to the anus, giving the inferior rectal nerve to the subcutaneous EAS/perianal skin, then superficial and deep perineal nerves and posterior labial nerves; superficial and subcutaneous EAS, bulb of vestibule, greater vestibular gland.",
    "Body of the clitoris, Bulbospongiosus m., Crus, Posterior labia nn., Deep perineal n., Bulb of the vestibule, Superficial perineal n., Greater vestibular gland, Inferior rectal n., Superficial EAS, Pudendal n., Subcutaneous EAS",
    [P("N. pudendus", "Pudendal n.", 453, 365), P("Nn. anales (rectales) inferiores", "Inferior rectal n.", 412, 372),
     P("N. perinealis - ramus superficialis", "Superficial perineal n.", 407, 302), P("N. perinealis - ramus profundus", "Deep perineal n.", 414, 229),
     P("Nn. labiales posteriores", "Posterior labia nn.", 380, 203),
     P("M. sphincter ani externus - pars superficialis", "Superficial EAS", 328, 343),
     P("M. sphincter ani externus - pars subcutanea", "Subcutaneous EAS", 355, 393)])},
  "'We obtained 47 donated female human cadavers'. Caption: 'The bulbospongiosus muscle was continuous with the superficial portion of the external anal sphincter (EAS), both innervated by branches of the perineal nerves. The inferior rectal nerve innervated the subcutaneous EAS and skin around the anus.' 'In 40% of cadavers, there was damage to branches of the deep perineal nerve, branches of the superficial perineal nerve, and the main trunk of the superficial perineal nerve' (mediolateral episiotomy).",
  "Episiotomy risk anatomy; illustrates the distribution of n. pudendus branches in the anal and urogenital triangles.",
  "CC BY. Article folder shared with the urogenital-triangle agent (g002/g004 theirs). Labels printed in English ('Posterior labia nn.' sic)."),
 # ======================= perine_variation =======================
 ("perine_variation", "Pudendal nerve trunking variations (types I, IIa, IIb, III) at the sacrospinous ligament - gluteal approach", "PMC9492552",
  {"cureus-0014-00000028281-i01.jpg": ("human cadaver (formalin), prone, gluteal approach",
    "Type I: single pudendal nerve trunk with internal pudendal vessels, medial to the sciatic nerve; no sciatic communication.",
    "PN(I), IPV, SN",
    [P("N. pudendus (truncus unicus, typus I)", "PN(I)", 428, 204), P("Vasa pudenda interna", "IPV", 430, 224), P("N. ischiadicus", "SN", 460, 275)]),
   "cureus-0014-00000028281-i03.jpg": ("human cadaver (formalin), prone, gluteal approach",
    "Type IIa: two-trunked pudendal nerve, one trunk (inferior rectal nerve) piercing the sacrospinous ligament.",
    "PN(IIa) (two leader lines), IPV, SSL",
    [P("N. pudendus - truncus 1 (typus IIa)", "PN(IIa)", 438, 250), P("N. pudendus - truncus 2 / n. rectalis inferior (typus IIa)", "PN(IIa)", 458, 222),
     P("Vasa pudenda interna", "IPV", 400, 281), P("Lig. sacrospinale", "SSL", 505, 272)]),
   "cureus-0014-00000028281-i04.jpg": ("human cadaver (formalin), prone, gluteal approach",
    "Type IIb: two-trunked pudendal nerve, inferior rectal nerve not piercing the ligament; nerve to obturator internus and sciatic nerve lateral.",
    "IPV, PN(IIb) (two leader lines), NOI, SN",
    [P("Vasa pudenda interna", "IPV", 465, 289), P("N. pudendus - truncus 1 (typus IIb)", "PN(IIb)", 499, 269),
     P("N. pudendus - truncus 2 (typus IIb)", "PN(IIb)", 487, 300), P("N. musculi obturatorii interni", "NOI", 479, 321),
     P("N. ischiadicus", "SN", 541, 370)]),
   "cureus-0014-00000028281-i06.jpg": ("human cadaver (formalin), prone, gluteal approach",
    "Type III: three-trunked pudendal nerve; internal pudendal vessels and nerve to obturator internus lateral, sciatic nerve further lateral.",
    "PN(III) (three leader lines), IPV, NOI, SN",
    [P("N. pudendus - truncus 1 (typus III)", "PN(III)", 392, 252), P("N. pudendus - truncus 2 (typus III)", "PN(III)", 415, 260),
     P("N. pudendus - truncus 3 (typus III)", "PN(III)", 444, 267), P("Vasa pudenda interna", "IPV", 466, 277),
     P("N. musculi obturatorii interni", "NOI", 461, 315), P("N. ischiadicus", "SN", 530, 319)])},
  "26 formalin-embalmed cadavers (16 M, 10 F), 52 hemipelves. 'In the present study, 27 out of 52 hemipelves (51.9%) were identified as type I having a single pudendal nerve trunk'. Type IIa: 'This branching pattern was observed in 7 out of 52 hemipelves (13.5%).' 'Twelve out of 52 hemipelves (23.1%) were type IIb ... but the inferior rectal nerve did not pass through the sacrospinous ligament.' 'Three trunked pudendal nerve (type III) was observed in 11.5% of hemipelves. In 14/52 hemipelves (26.9%), communication with the sciatic nerve was noted'. Literature (Mahakkanukrauh 2005, 73 nerves): 'type I is defined as one-trunked (41/73; 56.2%) ... type III is two-trunked with one trunk as an inferior rectal nerve piercing through the sacrospinous ligament (8/73; 11%) ... type V is three-trunked (9/73;12.3%)'.",
  "Multiple trunks / an inferior rectal nerve piercing the sacrospinous ligament matter for sacrospinous colpopexy, transgluteal pudendal block (incomplete block) and decompression surgery.",
  "CC BY (Cureus). The Abstract erroneously writes 'inferior gluteal nerve' for types IIa/IIb; the Results body and captions say 'inferior rectal nerve' - quote the body. The table of earlier studies gives the Mahakkanukrauh classification (requested 'Mahakkanukrauh type' data). i02/i05/i07 (sciatic-communication subtypes) downloaded and deleted (redundant)."),
 ("perine_variation", "Pudendal nerve formation (S3-S4) and 2-, 3-, 4-trunk variants with sciatic communication", "PMC12519013",
  {"acb-58-3-388-f2.jpg": ("human cadaver (embalmed), 4-panel",
    "A: pelvic view of sacral plexus with pudendal nerve (highlighted) formed from S3-S4; B: two-trunked; C: three-trunked; D: four-trunked pudendal nerve (red numbers 1-4); yellow arrows = communication with the sciatic nerve.",
    "A: LST, S1, S2, S3, S4, PN, orientation cross; B: 1, 2, yellow arrow; C: 1, 2, 3; D: 1, 2, 3, 4, yellow arrow; panel letters A-D",
    [P("Truncus lumbosacralis", "LST", 179, 52), P("N. spinalis S1 (ramus anterior)", "S1", 171, 74),
     P("N. spinalis S2 (ramus anterior)", "S2", 160, 90), P("N. spinalis S3 (ramus anterior)", "S3", 160, 106),
     P("N. spinalis S4 (ramus anterior)", "S4", 160, 119), P("N. pudendus", "PN", 109, 135),
     P("N. pudendus - truncus 1 (B)", "1", 146, 279), P("N. pudendus - truncus 2 (B)", "2", 134, 283),
     P("Ramus communicans n. pudendi cum n. ischiadico (B)", "yellow arrow", 146, 289),
     P("N. pudendus - truncus 1 (D)", "1", 628, 191), P("N. pudendus - truncus 2 (D)", "2", 626, 220),
     P("N. pudendus - truncus 3 (D)", "3", 617, 209), P("N. pudendus - truncus 4 (D)", "4", 609, 210),
     P("Ramus communicans n. pudendi cum n. ischiadico (D)", "yellow arrow", 577, 194)])},
  "10 cadavers (5 M, 5 F; East Indian). 'In 6 cadaveric specimen we found 1 trunk (60%), in 2 (1 male and 1 female) cadaveric specimens we found two trunked pudendal nerve bilaterally (20%), in 1 male cadaver we found 3 trunks of pudendal nerve (10%), and in 1 male cadaver 4 trunks of pudendal nerve were present bilaterally.' 'There was communication of pudendal nerve with sciatic nerve in 9 cadavers bilaterally.' 'The maximum CSA was found below the piriformis (4.04 mm2).' Literature: 'Gruber et al. [4] found multiple trunks in 40.5% and Maldonado et al. [5] found multiple trunks in 38%.'",
  "'This communication would lead to aberrant blockade of both the nerves when one of the nerves is blocked intentionally'. Abstract: ischial spine-to-PN and pubic symphysis-to-dorsal nerve distances larger in females (pudendal block landmarks).",
  "LICENCE CC BY-NC (Anat Cell Biol 2025). Panel C trunk numbers too small to localise reliably - not given points. Fig 4 (caliper measurements) downloaded and rejected (nerves not discernible)."),
 ("perine_variation", "Inferior rectal nerve arising directly from the S3 ventral ramus", "PMC6449584",
  {"acb-52-100-g001.jpg": ("human cadaver (fresh-looking, pelvis opened from posterior after sacrotuberous ligament reflection)",
    "Nerves dyed purple: the S3 ventral ramus gives pelvic splanchnic nerves and continues as an independent inferior rectal nerve, which sends a branch to the pudendal nerve.",
    "S3 nerve root; Inferior rectal nerve; Pelvic splanchnics; Branch to pudendal nerve; Pudendal nerve (white arrows)",
    [P("Ramus anterior n. spinalis S3", "S3 nerve root", 265, 128), P("Nn. rectales inferiores (variatio, ex S3)", "Inferior rectal nerve", 362, 148),
     P("Nn. splanchnici pelvici", "Pelvic splanchnics", 275, 178), P("Ramus communicans ad n. pudendum", "Branch to pudendal nerve", 400, 215),
     P("N. pudendus", "Pudendal nerve", 375, 300)])},
  "Case report. 'the S3 ventral ramus was found giving off pelvic splanchnics, then continuing as the inferior rectal nerve.' 'Common alterations in the path of the inferior rectal nerve involve its independent derivation from the fourth sacral root (S4), and more distally, piercing of the sacrospinous ligament'.",
  "'understanding the path of the inferior rectal nerve and being aware of its variants is necessary for procedures such as pudendal nerve blocks, pudendal nerve anastomoses, sacrospinous colpopexy, and various surgical exposures of this region'; injury may cause fecal incontinence.",
  "LICENCE CC BY-NC (Anat Cell Biol 2019; Dupont, Iwanaga, Oskouian, Tubbs). Orientation of the photo is not stated; bloody field."),
 ("perine_variation", "Internal pudendal and inferior gluteal arteries from a common trunk in the gluteal region (stellate pattern), relation to sacrotuberous ligament", "PMC5829714",
  {"jvb-15-02-168-g02.jpg": ("human cadaver (male), left gluteal region, gluteus maximus reflected",
    "A common trunk (CT2) emerges below piriformis and divides in a star-shaped pattern into the internal pudendal artery, inferior gluteal artery and muscular branches; sciatic nerve laterally, sacrotuberous ligament medially.",
    "Gluteus medius, Piriformis, Gluteus maximus (reflected), CT2, MB (x2), IPA, IGA (two arrows), SN, STL",
    [P("Truncus communis (a. pudenda interna + a. glutea inferior)", "CT2", 470, 195), P("Rami musculares", "MB", 515, 205),
     P("Rami musculares", "MB", 445, 230), P("A. pudenda interna", "IPA", 510, 260), P("A. glutea inferior", "IGA", 470, 265),
     P("A. glutea inferior (ramus)", "IGA", 250, 405), P("Lig. sacrotuberale", "STL", 510, 405), P("N. ischiadicus", "SN", 365, 345)])},
  "Case report (one male cadaver). 'The inferior gluteal artery (IGA) and internal pudendal artery (IPA) did not arise as separate branches from the internal iliac artery; rather, they arose from the second CT.' 'The second, smaller, common trunk entered the gluteal region through the greater sciatic foramen, below the piriformis muscle and presented a stellate branching pattern deep to the gluteus maximus muscle.'",
  "Relevant to gluteal/transgluteal approaches to the pudendal canal and to pelvic embolisation; authors discuss Adachi/Yamaki classifications of internal iliac branching.",
  "CC BY (J Vasc Bras). The internal pudendal artery itself runs normally toward the lesser sciatic foramen; the variation is its origin."),
 ("perine_variation", "Artery of the penis arising inside the pelvis (accessory-pudendal-type origin) with a hypoplastic internal pudendal artery", "PMC3971847",
  {"CRIVAM2014-193194.001.jpg": ("human cadaver (male), superior view of left hemipelvis",
    "Second common trunk of the internal iliac artery gives obturator and inferior vesical arteries and the artery of the penis (AOP), which runs forward on the lateral pelvic wall above the pelvic floor.",
    "Urinary bladder, U, SVA, MRA, IIA, ILA, IVA, CT2, AOP, CT1, SGA, OA, ON, IIV",
    [P("A. penis (origo intrapelvica; a. pudenda accessoria-typus)", "AOP", 112, 240), P("Truncus communis 2", "CT2", 300, 275),
     P("Aa. vesicales inferiores", "IVA", 228, 262), P("A. obturatoria", "OA", 190, 350), P("N. obturatorius", "ON", 270, 382),
     P("Truncus communis 1", "CT1", 380, 295), P("A. glutea superior", "SGA", 445, 305), P("A. rectalis media", "MRA", 420, 212)]),
   "CRIVAM2014-193194.002.jpg": ("human cadaver (male), median sagittal hemisection of pelvis",
    "The intrapelvic artery of the penis descends below the puboprostatic ligaments behind the pubic symphysis and divides into the dorsal and deep arteries of the penis near the bulb and right crus.",
    "Rectum, Urinary bladder, AOP, Pubis, Prostate, DOA, DEP, RCP, Anal canal, BP",
    [P("A. penis (origo intrapelvica)", "AOP", 372, 198), P("A. dorsalis penis", "DOA", 380, 305), P("A. profunda penis", "DEP", 355, 318),
     P("Crus penis dextrum", "RCP", 420, 365), P("Bulbus penis", "BP", 330, 405), P("Prostata", "Prostate", 270, 297),
     P("Canalis analis", "Anal canal", 195, 375), P("Os pubis", "Pubis", 465, 265)])},
  "Case report. 'The artery of the penis arose from a common arterial trunk from the left internal iliac artery.' 'The artery of the penis coursed forwards between the bladder and lateral pelvic wall until the pubis. Thereafter it passed below the puboprostatic ligaments and divided into deep and dorsal arteries of the penis just behind the lower border of the pubic symphysis'. 'The left internal pudendal artery was reduced in size and it supplied the musculature of the perineum and the anal canal. It also supplied the bulb of the penis.'",
  "Such intrapelvic penile supply runs near the prostate/puboprostatic ligaments - at risk in radical prostatectomy; relevant to erectile dysfunction and penile revascularisation.",
  "CC BY. The authors do NOT use the term 'accessory pudendal artery'; the slide may say 'aksesuar pudendal arter ile aynı paternde' but must not attribute the term to them. Fig 2 is a sagittally hemisected pelvis (gross specimen, not a cross-sectional image series)."),
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

(ROOT / "sources/perine_anal.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(len(out), "entries;", sum(len(e["figures"]) for e in out), "figures;",
      sum(len(f["label_points"]) for e in out for f in e["figures"]), "label points")
for e in out:
    print(f"{e['use']:16} {e['pmcid']:12} {e['license_code']:10} {[(f['file'], len(f['label_points'])) for f in e['figures']]}")
