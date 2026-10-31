#!/usr/bin/env python3
"""Build sources/bolge_el.json (EL = wrist & hand) from downloaded PMC OA files.

Citation, DOI, licence, title, authors, journal, year, verbatim captions and pixel sizes are read
from the files in topografik/images/raw/PMC<id>/ ; only the descriptive fields below are hand-written
(after viewing every figure). Run: python3 -I scripts/build_bolge_el.py
"""
import json, pathlib, re, xml.etree.ElementTree as ET
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "topografik/images/raw"
XL = "{http://www.w3.org/1999/xlink}href"


def t(e):
    return " ".join("".join(e.itertext()).split()) if e is not None else ""


# (use, topic, pmcid, {file: (specimen, what_it_shows, labels_visible)}, key_findings, clinical_relevance, notes)
E = [
 # ---------------- topo_lecture ----------------
 ("topo_lecture", "Carpal tunnel opened: flexor retinaculum, median nerve, FPL; FCR outside the tunnel", "PMC8569728",
  {"turkjmedsci-51-1912-fig002.jpg": ("human cadaver",
    "Fresh-frozen wrist dissection: flexor retinaculum (black *) with median nerve (yellow *) and FPL tendon (green *) passing deep to it, while the FCR tendon (red *, lifted on a probe) and palmaris longus (blue *) lie superficial to the retinaculum.",
    "colour-coded asterisks only (black, red, blue, yellow, green *); no text labels")},
  "MRI part: 118 wrists (74 female, 44 male) without pathology on axial T1 at the pisiform level; 'the tendon of the flexor carpi radialis was found above the flexor retinaculum within its own septal compartment in all patients.' Cadaveric part: 3 fresh-frozen upper limbs dissected.",
  "Authors conclude FCR crosses the wrist superficial to the carpal tunnel and 'doesn't have any effect on the carpal tunnel syndrome'.",
  "Turkish authors (Turk J Med Sci). Fig 1 (axial MRI) of the same article is used under kesit_lecture as well (see next entry). Labels are colour asterisks only: the slide needs a Turkish legend."),
 ("kesit_lecture", "Axial MRI at pisiform level: carpal tunnel contents, flexor retinaculum, FCR compartment", "PMC8569728",
  {"turkjmedsci-51-1912-fig001.jpg": ("MRI",
    "Axial T1 MRI of a normal wrist at the pisiform level: flexor retinaculum (yellow arrow) roofing the carpal tunnel full of flexor tendons (green *), and the FCR tendon (red arrow) in its own compartment radial/superficial to the retinaculum.",
    "red arrow, yellow arrow, green asterisk; no text")},
  "Same study: 118 normal wrists on MRI; FCR tendon above the flexor retinaculum in its own septal compartment in all patients.",
  "Useful for defining carpal tunnel boundaries/contents on cross-sectional imaging.",
  "XML caption is itself truncated ('Green asterix; tendons of flexor dig') - reproduced verbatim; meaning: tendons of flexor digitorum. Bones (scaphoid, lunate/capitate, pisiform/triquetrum) visible but unlabelled."),
 ("topo_lecture", "Ulnar nerve in Guyon's canal: superficial/deep branches, palmaris brevis branches (normal pattern)", "PMC5250657",
  {"402_2016_2616_Fig1_HTML.jpg": ("human cadaver",
    "Fresh cadaver dissection of Guyon's canal showing the classic bifurcation of the ulnar nerve into deep (motor) and superficial branches, the superficial branch giving a cutaneous branch, nerves to palmaris brevis, the common palmar digital nerve to digits 4-5 and the medial palmar digital nerve.",
    "Ulnar nerve; Superficial branch; Deep branch; Cutaneus branch; Common palmar digital nerve to 4th and 5th fingers; Nerves to palmaris brevis; Medial palmar digital nerve")},
  "50 fresh cadavers dissected bilaterally (100 hands). 'Three major branching patterns were found, with division into deep and superficial UN being the most common (85%).' Cutaneous branch within the canal in 70%; UN-MN anastomosis in 57%.",
  "'additional branches and anastomoses are common and should be taken into careful consideration when approached during surgery in the area, particularly during decompression procedures of Guyon's canal.'",
  "Same article supplies the variation figures (Fig 2-3) in the topo_variation entry below. Image text is English and spells 'Cutaneus'."),
 ("topo_lecture", "Superficial palmar arch (complete) with common palmar digital arteries/nerves and Berrettini anastomosis", "PMC12823052",
  {"cureus-0017-00000099862-i02.jpg": ("human cadaver",
    "Embalmed palm dissection showing a complete superficial palmar arch from the ulnar artery, common palmar digital arteries 1-4 and common palmar digital nerves I-IV from the median and ulnar nerves, with a bidirectional (type III) Berrettini communicating branch (cb).",
    "UA, UN, MN, spa, cb, 1, 2, 3, 4, I, II, III, IV, 1/2; handwritten tags '5K 1' and '5K 2'")},
  "36 embalmed upper limbs (18 right, 18 left). 'Complete SPAs were observed in 55.6% (n=20) of specimens ... while 44.4% (n=16) showed incomplete patterns'. 'The Berrettini anastomosis was present in 33.3% (n=12) of hands, with Type III being most common (66.7%, n=8/12), and no Type I anastomoses were identified.'",
  "'The frequent occurrence of complex Berrettini anastomoses underscores the importance of detailed anatomical awareness to avoid complications in hand surgery and to enhance diagnostic procedures.'",
  "Doubles as a variation source (SPA completeness + Berrettini prevalence). Pink specimen tags ('5K') are visible in the photo - consider cropping or leave as authentic."),
 ("topo_lecture", "Deep palmar arch and palmar metacarpal arteries", "PMC8808664",
  {"cureus-0014-00000020873-i01.jpg": ("human cadaver",
    "Deep palm dissection: deep palmar arch formed by the radial artery and the superior deep palmar branch of the ulnar artery, giving palmar metacarpal arteries; orientation cross (D/P/R/U).",
    "PMAs; SDPBUA; D, P, U, R (orientation)"),
   "cureus-0014-00000020873-i02.jpg": ("human cadaver",
    "Deep palmar arch completed by the inferior deep palmar branch of the ulnar artery (alternative type), with palmar metacarpal arteries.",
    "PMAs; IDPBUA; D, P, R, U (orientation)")},
  "30 formalin-fixed hands (16 right, 14 left). 'All deep palmar arches were complete.' Arch length '4.2 ± 0.47 cm on the right side and 4.0 ± 0.6 cm on the left side'; deep palmar branch diameters of radial and ulnar arteries '4.02 ± 0.48 mm and 1.90 ± 0.36 mm, respectively'.",
  "'it can be safe to sacrifice the radial artery in procedures such as radial artery harvesting and radial artery flap transfer.'",
  "Two arch types (superior vs inferior deep branch of ulnar artery) can be shown side by side."),
 ("topo_lecture", "Lumbricals 1-4 arising from FDP tendons distal to the carpal tunnel; thenar/hypothenar eminences", "PMC2527548",
  {"1757-1626-1-103-1.jpg": ("human cadaver",
    "Palmar dissection after removal of the palmar aponeurosis: four lumbricals (1-4) on the FDP tendons, FDS tendon to the index, flexor retinaculum over the carpal tunnel, thenar and hypothenar eminences; a star marks an extra belly of the first lumbrical from the FDS tendon.",
    "1, 2, 3, 4, FDS, TE, HE, FR, FR, CT; 4-point star; small arrows along FDS")},
  "Single case (adult male cadaver): additional belly of the first lumbrical arising from the FDS tendon to the index 'close to the proximal margin of the flexor retinaculum'.",
  "'The presence of such an additional muscle in the carpal tunnel should be considered in the aetiology of carpal tunnel syndrome (CTS).'",
  "Case report, but the figure is a clear labelled overview of all four lumbricals, so it serves the lecture; the star can also illustrate lumbrical-origin variation."),
 ("topo_lecture", "Digital flexor pulleys A1/A2 on four fingers (cadaver)", "PMC13047401",
  {"cios-18-329-g002.jpg": ("human cadaver",
    "Dissected palmar fingers 2-5 with skin and fat removed showing the annular pulleys over the flexor tendons; arrows mark the gap between A1 and A2 pulleys on each finger.",
    "white arrows only; no text labels")},
  "156 fingers from 39 Korean adult cadavers. 'the A1 pulley averaging 7.2 mm (range, 6.9-7.4 mm) and the A2 pulley averaging 17.1 mm (range, 15.5-18.6 mm) in fingers 2 to 4. The gap between the A1 and A2 pulleys was relatively narrow (average, 3.4 mm). The A1 pulley was located distal to the PC in all cases.'",
  "Provides skin-crease references for percutaneous A1 release 'while minimizing the risk of A2 pulley injury.'",
  "LICENCE CC BY-NC (acceptable but flagged). No CC BY cadaver photo of the full pulley system was found in the OA bucket; the slide needs A1/A2 labels added by us."),
 ("topo_lecture", "Dorsal branch of ulnar nerve and dorsal branch of ulnar artery in the dorsomedial triangle (6R/6U portals)", "PMC10427770",
  {"cureus-0015-00000041981-i03.jpg": ("human cadaver",
    "Two dissections of the distal medial forearm/wrist with matching line diagrams: the dorsal branch of the ulnar nerve (star) dividing into three (3a-b) or two (3c-d) branches proximal to the ulnar styloid between ECU and FCU, with the dorsal branch of the ulnar artery (arrowheads).",
    "ECU, FCU, U N, U A, a, b, c, star, P, 3a, 3b, 3c, 3d")},
  "40 adult cadaveric upper limbs (20 right, 20 left). 'Four branching patterns have been mapped, with one dominant pattern in 67.5% of limbs. In three-fourths of cases, one branch of the dorsal branch of the ulnar nerve consistently overlies the 6U portal'.",
  "Proposes the subcutaneous dorsomedial triangle as a landmark for 'reconstructive microsurgery for distal hand defects' and to avoid nerve injury at wrist arthroscopy portals.",
  "Panel letters/labels are small at 750 px wide; acceptable on a half-slide. Overlaps the forearm region (distal forearm), but its content is wrist level."),
 ("topo_lecture", "Superficial branch of the radial nerve and cephalic vein at the radial styloid (snuffbox region)", "PMC3269985",
  {"1754-9493-5-28-1.jpg": ("human cadaver",
    "Dissected distal radial forearm and wrist with a ruler: superficial branch of the radial nerve (SB) running toward the radial styloid (O) beside the cephalic vein (V).",
    "SB, V, O (yellow letters); ruler scale")},
  "25 forearms. 'The mean distance to the point of emergence of the nerve from the radial styloid was 8.54 cm (SD = 1.32). The nerve branched at a mean distance of 5.57 cm (SD = 1.43)'. 'In 17 specimens(68%) cephalic vein crossed the SBRN superficially once.'",
  "'We recommend avoiding transverse incisions in the snuffbox region between 2.51 cm and 3.90 cm from the Listers tubercle. We also recommend avoiding cannulation of the cephalic vein in the distal forearm.'",
  "Labels are few and small; best used as a supporting image. No CC BY labelled cadaver photo of the snuffbox floor (scaphoid + radial artery) was found - see gaps."),
 ("topo_lecture", "Extensor mechanism of the finger: central slip, lateral slips, terminal tendon; sagittal bands (schematic + US)", "PMC10716571",
  {"AJUM-26-216-g006.jpg": ("schematic",
    "Author diagram of the ED tendon trifurcating into the central slip (to the base of the middle phalanx) and lateral slips (to the distal phalanx via the terminal tendon), plus a sagittal MCP joint diagram and long-axis ultrasound of the ED tendon, dorsal plate and cartilage.",
    "(a) Central slip ED tendon, Lateral slip, DP, MP, PP, MC; (b) Dorsal plate, Palmar plate, PP, MC; (c) Central slip ED tendon, Dorsal plate, Articular cartilage, PP, MC")},
  "Review (single author). 'Injuries to the dorsal hood account for 16% of all hand and wrist injuries in boxers.' Describes the ED tendon trifurcation and the sagittal, transverse and oblique bands of the dorsal hood.",
  "Sagittal band tears ('boxer's knuckle') cause extensor tendon instability/subluxation at the MCP joint that ultrasound can assess dynamically.",
  "Fig 9 (US sagittal bands) of the same article is listed under kesit_lecture. The schematic is simplified (no intrinsic contribution drawn)."),
 ("kesit_lecture", "Ultrasound of the sagittal bands over the 3rd MCP joint", "PMC10716571",
  {"AJUM-26-216-g003.jpg": ("US",
    "Short-axis ultrasound over the uninjured 3rd MCP joint: ED tendon centred by the radial and ulnar sagittal bands, superficial and deep portions of the band, dorsal plate and metacarpal head cartilage; panel b is the unlabelled image.",
    "Ulnar sagittal band; Superficial midline portion sagittal band; Radial sagittal band; ED; Dorsal plate; Deep portion sagittal band; Metacarpal head; Articular cartilage Metacarpal head; (a), (b)")},
  "Same review; normal sonographic anatomy of the dorsal hood.",
  "Baseline for recognising sagittal band tears and extensor tendon subluxation.",
  ""),
 # ---------------- topo_variation ----------------
 ("topo_variation", "Ulnar nerve branching variations in Guyon's canal (trifurcation; radial/ulnar trunks)", "PMC5250657",
  {"402_2016_2616_Fig2_HTML.jpg": ("human cadaver",
    "Trifurcation of the ulnar nerve in Guyon's canal into a deep branch, a common palmar digital nerve to digits 4-5 and a medial palmar digital nerve to digit 5.",
    "Common palmar digital nerve to 4th and 5th fingers; Ulnar nerve; Medial palmar digital nerve to 5th finger; Deep branch of ulnar nerve"),
   "402_2016_2616_Fig3_HTML.jpg": ("human cadaver",
    "Rare pattern: the ulnar nerve divides into a radial trunk and an ulnar trunk, the deep branch arising from the radial trunk.",
    "Radial trunk; Ulnar nerve; Deep branch; Ulnar trunk; Medial palmar digital nerve to 5th digit")},
  "50 fresh cadavers, bilateral. Bifurcation 85%; 'Trifurcation of the UN into a deep branch, a common palmar digital nerve (to digits 4 and 5), and a medial palmar digital nerve (digit 5) was seen in 13% of cases'; 'a division of the UN into a radial trunk and ulnar trunk was seen in only 2% of cases'. Cutaneous branch in canal 70%; UN-MN anastomosis 57%; '78% of all the cadavers studied showed symmetry in their branching patterns.'",
  "Variable branching and anastomoses must be anticipated during Guyon's canal decompression.",
  "Original series; CC BY 4.0."),
 ("topo_variation", "Superficial palmar arch types and communicating branch (corrosion casts) and persistent median artery", "PMC10762056",
  {"41598_2023_50935_Fig2_HTML.jpg": ("human cadaver",
    "Corrosion casts (four hands) of medium-length complete SPA (type 2) giving three common palmar digital arteries, with the communicating branch (yellow arrows) to the superficial palmar branch of the radial artery, doubled CB in one (red arrows).",
    "1, 2, 3, 4, 5, 6, 8, 9, 10, 11 (numbers with leader lines); A, B, C, D; yellow/green and red arrows")},
  "20 dissected hands plus 40 corrosion casts. 'The mean diameter of the SPA, between the second and third common palmar digital arteries, was 1.86 ± 0.08 mm. We identified the persistent median artery (PMA) in 5% of hands.' 'Type 2 Medium-length SPA was present in 14 (35%) casts'; 'The short SPA was found in 11 (27.5%) specimens'.",
  "'That short SPA is potentially inadequate for restoring circulation after occlusion or radial artery harvesting for coronary artery bypass.'",
  "Fig 1 NOT downloaded: panel A is a drawing 'modified from Radojević and Bošković' (reproduced third-party material). Fig 2 is the authors' own casts. Note the caption says yellow arrows = CB; in the image the CB arrows in panels B/C are yellow-green."),
 ("topo_variation", "Riché-Cannieu anastomosis in the thenar region relative to Kaplan's cardinal line", "PMC11193595",
  {"10-1055-s-0044-1785512-i2300184en-1.jpg": ("human cadaver",
    "Deep palm dissection showing the Riché-Cannieu communication between the recurrent/thenar branches of the median nerve and the deep branch of the ulnar nerve, with Kaplan's cardinal line (white) and the Y line (yellow, axis of 3rd metacarpal) superimposed.",
    "KCL (x2), Y (x2), MN, UN; double-headed measurement arrows"),
   "10-1055-s-0044-1785512-i2300184en-5.jpg": ("human cadaver",
    "Another hand: anastomotic fascicles from the main trunk of the median nerve joining the deep ulnar branch in the thenar muscles; KCL/Y intersection proximal to the anastomosis.",
    "Y (x2), KCL (x2), MN, UN")},
  "20 hands of 10 fresh adult male cadavers. 'In the present study, we identified the RCA in all dissected hands.' 'The crossing between the KCL and the Y line occurred proximal to the RCA in 18 limbs'; the Y line lay radial to the most distal RCA point in 14 limbs and ulnar in 6.",
  "'Knowledge of these anatomical relationships can prevent damage to nerve branches and thus also prevent paralysis of intrinsic muscles in surgical procedures in the palm of the hand.'",
  "Small series (20 hands, all male). 100% prevalence here contrasts with wider literature ranges; present as 'frequent communication'. PMC6855928 (larger RCA review, Rev Bras Ortop 2019) rejected: CC BY-NC-ND."),
 ("topo_variation", "Berrettini anastomosis: prevalence, types and 'probable zone'", "PMC11910384",
  {"cureus-0017-00000078967-i02.jpg": ("human cadaver",
    "Fresh hand dissection: type I Berrettini anastomosis - a single communicating branch from the ulnar nerve's 4th common palmar digital nerve to the median nerve's 3rd common palmar digital nerve.",
    "CDN3, CDN4, BA")},
  "104 fresh cadaveric hands (52 donors). 'The BA was identified in 80% (83/104) of hands. Type I, with a single connection from the UN to the MN, was the most common (38%).' 'The average BA length was 22.03 ± 7.68 mm, with its \"probable zone\" spanning 26.11-44.21% of hand width and 36.63-50.21% of hand length.'",
  "'Identifying its \"probable zone\" provides valuable guidance for surgical procedures, minimizing the risk of sensory deficits in the hand.'",
  "Fig 1 (type diagrams) and Fig 7 (zone diagram) NOT used: captions state 'Image created in BioRender'. Contrast with PMC12823052 (33.3%, 36 embalmed limbs) - prevalence depends on method/definition."),
 ("topo_variation", "First dorsal (extensor) compartment: separate EPB subcompartment and multiple APL slips", "PMC2586286",
  {"eplasty08e53_fig1.jpg": ("human cadaver",
    "Radial wrist dissection marking the first dorsal compartment and its landmarks: Lister's tubercle, radial styloid and scaphoid tubercle, with the APL-Lister's-Scaphoid (ALS) juncture; EPB and APL tendons distal to the retinaculum.",
    "Lister's tubercle; First dorsal compartment; Radial syloid [sic]; ALS juncture; EPB; APL; Scaphoid tubercle; dotted line"),
   "eplasty08e53_fig2.jpg": ("human cadaver",
    "Opened first dorsal compartment showing a longitudinal septum creating a separate subcompartment for the EPB tendon.",
    "Septation within the compartment"),
   "eplasty08e53_fig3.jpg": ("human cadaver",
    "APL with three separate tendon slips beside the single EPB tendon, separated over a white card.",
    "APL; EPB; Slip 3; Slip 2; Slip 1")},
  "32 cadaveric wrists. 'The average length of the extensor retinaculum from its proximal to distal extent measured approximately 2.2 cm.' 'A separate compartment for the extensor pollicis brevis was noted in 35% of the specimens. The abductor pollicis longus tendon demonstrated great variability with 1, 2, 3, or 4 slips in 9%, 30%, 43%, or 26% of the specimens, respectively.'",
  "Landmarks 'can assist clinicians with management of de Quervain's disease' (septation relevant to failed injection/release).",
  "Fig 1 also usable in topo_lecture for the extensor retinaculum/1st compartment. Images are 450 px wide (above the 350 px floor) and carry an 'ePlasty' watermark. 'Radial syloid' is a typo printed on the image."),
 ("topo_variation", "Extensor digitorum brevis manus on the dorsum of the hand", "PMC6449591",
  {"acb-52-97-g001.jpg": ("human cadaver",
    "Dorsum of the right hand: an extensor digitorum brevis manus muscle belly (on black card) lying between the extensor tendons, with photograph (A) and tracing (B); dorsal branch of the ulnar nerve also visible.",
    "ED, APL, EPB, EPL, EIP, EDBM, ED, EDM, DBUN; A, B")},
  "Single 78-year-old male cadaver among 22 cadavers ('bilateral extensor variations were found in one of 22 cadavers (4.5%)'). Literature cited: 'EDBM has 4% of crude cadaveric prevalence ... and has 2.5% of true cadaveric prevalence'; EMP frequency '0.8% to 10.4%'.",
  "'Awareness of these combined muscular variation would be helpful in understanding the identification of digital extensors and in requiring careful consideration for the reconstruction surgery of the hand.'",
  "LICENCE CC BY-NC (Anat Cell Biol; flagged). Case report - prevalence numbers are literature-derived (Yammine meta-analysis, not OA in bucket). Caption calls it 'extensor digitorum minimi (EDBM)' - text error in the original caption."),
 ("topo_variation", "Accessory head from FPL to the first lumbrical with FPL tendinous interconnection (Linburg-Comstock-related)", "PMC9981488",
  {"276_2023_3084_Fig1_HTML.jpg": ("human cadaver",
    "Palmar dissection (A) and scheme (B): an accessory muscle head from FPL whose tendon (tAMHL1) passes through the carpal tunnel to join the first lumbrical; asterisk/star marks the tendinous interconnection with the FPL tendon.",
    "L1, tAMHL1, AMHL1, FPL, four-point star; A, B")},
  "Case report (formalin-embalmed Central European cadaver). Literature cited in text: 'The prevalence of the Linburg-Comstock variation is moving around 21% as reported by Yammine'; first-lumbrical variations 'occur in 17.3%' (Mehta and Gardner).",
  "'Such variation has a clinical significance ranging from the functional limitation of the thumb and index finger movement to the potential median nerve compression.'",
  "Surg Radiol Anat article that IS CC BY 4.0 (bucket licence_code CC BY). Only a case, but no OA original series on Linburg-Comstock was found (Thai 130-limb series and PMC8590423 reverse-LCV not usable: PMC8590423 has no licence)."),
 ("topo_variation", "Flexor digiti minimi longus through Guyon's canal; anomalous lumbrical; dorsal ulnar nerve aberrant branch", "PMC6920165",
  {"gr1.jpg": ("human cadaver",
    "Anterior wrist/palm of a 94-year-old cadaver: an extra muscle (FDML) arising in the forearm and passing through Guyon's canal deep to the palmar carpal ligament and palmaris brevis; (B) hypothenar muscles ADM and FDMB visible after reflection.",
    "A: PB, PCL, PL, FCU, FDML, PL, FCR, FCR, FDS; B: ADM, FDMB, PB, PCL, FCU, FDML"),
   "gr3.jpg": ("human cadaver",
    "(A) Ulnar side of palm: superficial branch of ulnar nerve, ulnar artery, FDMB and an aberrant palmar branch of the dorsal ulnar nerve (arrow/arrowheads); (B) isolated median and ulnar nerves with ulnar-median communication and an hourglass constriction of the median nerve.",
    "A: FDML, FDMB, SUN, PB, SPA, DUN, UN, UA, MN; black arrow and arrowheads; B: DUN, SUN, MN; white arrows; red dashed lines")},
  "Single case. Highlights: 'The additional flexor muscle (Flexor Digiti Minimi Longus m.) passing through Guyon's canal is the first to be described.' 'The anomalous first lumbrical muscle with three origins is the first to be described.' 'Berretini's and Kaplan's anastomosis was also noted.'",
  "Accessory muscles in Guyon's canal are a potential cause of ulnar nerve compression (discussed in the article).",
  "Case report (no prevalence). Fig 1B is also a good labelled hypothenar view (ADM, FDMB) for the lecture."),
 # ---------------- kesit_lecture ----------------
 ("kesit_lecture", "Ultrasound of the median nerve at carpal tunnel inlet/outlet; ulnar nerve branches in Guyon's canal", "PMC10253229",
  {"diagnostics-13-01928-g002.jpg": ("US",
    "Short-axis ultrasound of the median nerve (*) under the flexor retinaculum at the tunnel inlet (scaphoid-pisiform) and outlet (trapezium-hook of hamate); lower panels show retinaculum hypertrophy for comparison; small hand icons show probe position.",
    "A, B, C, D; FCR; S; P; T; H; *; arrowheads; Radial; Ulnar"),
   "diagnostics-13-01928-g013.jpg": ("US",
    "Short-axis ultrasound of the ulnar nerve in Guyon's canal (A), branching at the pisohamate hiatus (B), deep branch between the hypothenar muscles distal to the hook of hamate (C) and within adductor pollicis (D).",
    "A: MN, UA, P, arrowhead; B: MN, A, A, A, H, *, white/black/orange arrows; C: A, FDM, Opp DM, AbDM, L; D: AdP, AdP, black arrows; Radial, Ulnar")},
  "Pictorial review (no cohort). Covers median nerve trunk, palmar cutaneous and recurrent motor branches, ulnar nerve branches (superficial, deep, palmar and dorsal cutaneous), superficial radial nerve and digital nerves.",
  "'sonographic findings complement electrodiagnostic studies ... while ultrasound-guided interventions are safe and effective for treating relevant nerve pathologies.'",
  "Panels C/D of Fig 2 show pathology (retinaculum hypertrophy) - crop to A/B for normal anatomy. Fig 4 of the same review is listed under kesit_variation. Other normal-anatomy figures available but not downloaded: Fig 7 (palmar cutaneous branch), Fig 10 (recurrent motor branch), Fig 19 (dorsal ulnar cutaneous nerve), Fig 21 (superficial radial nerve)."),
 ("kesit_lecture", "Guyon's canal: zonal illustration and ultrasound anatomy", "PMC11899079",
  {"diagnostics-15-00592-g001.jpg": ("schematic",
    "Author illustration of Guyon's canal in coronal view (A) and axial sections at proximal (B, pisiform) and distal (C, hook of hamate) levels: roof (volar carpal ligament), floor (flexor retinaculum), ulnar nerve/artery and their superficial/deep branches, fibrotendinous arch of hypothenar muscles, and the adjacent carpal tunnel.",
    "A: dUN, dUA, FDMB, TM, FR, PL, HoH, PHL, UA, UN, FTA-HM, VCL, MN, ODM, sUN, ADMB, FCR; B: PB, UN, GC, UA, VCL, CT, FR, MN, SB, TB; C: dUN, dUA, FTA-HM, sUN, sUA, ScF, CT, FR, PHL, HoH, HM"),
   "diagnostics-15-00592-g003.jpg": ("US",
    "Axial ultrasound at proximal Guyon's canal (pisiform) with ulnar artery and nerve, at the distal canal (hook of hamate) where the nerve divides, and longitudinal view over the retinaculum; with probe-position photos.",
    "A: UA, UN, Pisiform, open triangles; C: Hypothenar, Hook Of Hamate, open triangles/arrow; E: Ulnar Nerve, Flexor Retinaculum, Flexor Tendons In Carpal Tunnel, Hook Of Hamate; B, D, F")},
  "Narrative review. 'The canal's intricate anatomy is defined by surrounding ligaments and bones, divided into three zones, each containing distinct neural structures.'",
  "'ultrasound provides real-time, dynamic assessments, while magnetic resonance imaging (MRI) offers detailed visualisation of soft tissues and bony structures, aiding in pre-surgical documentation and pathology evaluation.'",
  "Fig 1 is an original author illustration (caption gives no external source / BioRender attribution). Fig 4 (accessory ADM) is listed under kesit_variation."),
 ("kesit_lecture", "TFCC and ulnocarpal ligaments on 3T MRI", "PMC5600038",
  {"mrms-16-003-g6.jpg": ("MRI",
    "Three isotropic 3D coronal fat-suppressed PD slices (dorsal to volar) showing the dorsal radioulnar ligament, the central disc of the TFC, the volar radioulnar ligament and the ulnomeniscal homologue.",
    "L, T, R, U on each panel; white arrowhead; red arrow; yellow arrow; white dotted arrow"),
   "mrms-16-003-g9.jpg": ("MRI",
    "Ulnotriquetral ligament (dotted arrow) on 3D coronal FS PD (a) and 2D sagittal PD (b) images.",
    "a: T, L, R, dotted arrow; b: 'Volar side', P, T, dotted arrow")},
  "Review. 'The TFCC is composed of the articular disc (disc proper), the triangular ligament, the dorsal and volar radioulnar ligaments, the meniscus homologue, the ulnar collateral ligament (UCL), the extensor carpi ulnaris (ECU) tendon sheath, and the ulnolunate and ulnotriquetral ligaments.'",
  "High-resolution 3T imaging enables classification of TFCC lesions (Palmer type 1 traumatic / type 2 degenerative).",
  "Panel letters a/b/c are cropped at the top of Fig 6. Images are small (667 and 674 px wide) but legible."),
 ("kesit_lecture", "Ultrasound of digital annular pulleys A1/A2 and their entheses", "PMC11534144",
  {"kead614f3.jpg": ("US",
    "High-frequency ultrasound of the 2nd finger: A1 pulley over the flexor tendons with its enthesis at the volar plate (A) and sesamoid (B), and A2 pulley enthesis at the proximal phalanx ridge (C).",
    "A: A1, FT, VP, MCH; B: A1, SB, FT, MCH; C: A2, FT, PP; white boxes")},
  "20 cadaveric hands + 20 healthy controls. 'A total of 1200 DAPs (400 cadaveric, 800 HCs) were analysed. The cadaveric study demonstrated strong correlation between anatomical and US measurement of DAPs (r = 0.96).' 'US assessment of A1, A2 and A4 DAPs in HCs allowed the identification of 718/720 (99.73%) entheses.'",
  "'US is an effective tool to detect and study DAPs.'",
  "Fig 2 (dissection + histology) dropped: 769x211 composite with tiny panels."),
 # ---------------- kesit_variation ----------------
 ("kesit_variation", "Bifid median nerve and persistent median artery on ultrasound (prevalence)", "PMC5463256",
  {"cln-72-06-358-g001.jpg": ("US",
    "Paired transverse ultrasound images (raw and outlined) at the proximal carpal tunnel showing bifid median nerve trunks (arrowheads/outlines) with a persistent median artery (thick arrow) in different positions, including colour Doppler.",
    "white outlines, thick arrows, triangular arrowheads; red Doppler signal; no text")},
  "160 wrists. 'a bifid median nerve was observed in 15 (9.4%) wrists, and a persistent median artery was observed in 12 (7.5%) wrists.' 'the probability of coexistence (6.3%) was higher than the probability of existing independently (bifid median nerve only 3.1%, persistent median artery only 1.3%).' 'Persistent median vein was observed in 9 wrists (5.6%).'",
  "'Their positional relationship in carpal tunnel is uncertain, and thus, preoperative ultrasound is necessary. These three variations do not present any additional risk for the development of carpal tunnel syndrome.'",
  "Complements repo entry PMC10343151 (persistent median artery). XML label is 'Figure 1 and Figure 2' (two figures in one image)."),
 ("kesit_variation", "Ultrasound of median nerve variants and accessory muscles: bifid MN, PMA, accessory FDS", "PMC10253229",
  {"diagnostics-13-01928-g004.jpg": ("US",
    "Short-axis ultrasound at the wrist: bifid median nerve (A), bifid median nerve with persistent median artery on Doppler (B), accessory FDS muscle belly (*) beside the nerve (C), and a PL tendon laceration compressing the nerve in long axis (D).",
    "A: PL, arrowheads; B: PL, red Doppler, white arrow, arrowheads; C: FCR, S, PL, *, arrowhead; D: PL, arrowhead, Distal, Proximal; Radial, Ulnar")},
  "Review figure (no prevalence in this article).",
  "Recognising these variants avoids misdiagnosis and iatrogenic injury in carpal tunnel procedures.",
  "Panel D shows pathology (laceration) - crop to A-C. Prevalence for the slide should come from PMC5463256 and PMC5635084."),
 ("kesit_variation", "Accessory abductor digiti minimi overlying Guyon's canal on ultrasound", "PMC11899079",
  {"diagnostics-15-00592-g004.jpg": ("US",
    "Axial ultrasound at the pisiform: an accessory abductor digiti minimi muscle belly lying superficial to the ulnar nerve within Guyon's canal, with the ulnar artery volar to it.",
    "UA, aADM, UN, Pisiform")},
  "Review: describes the aADM as 'an anatomical variant in the hand, where an extra muscle lies adjacent to the ulnar nerve as it passes through Guyon's canal'; dynamic US during little-finger abduction distinguishes asymptomatic from compressive variants. No prevalence given in this article.",
  "'This dynamic evaluation is crucial for distinguishing between the asymptomatic presence of the accessory muscle and its pathological variant'.",
  "Prevalence figures (e.g. 22-35% in older cadaver/US series, Harvie 2004, Dodds 1990) are NOT in an OA article we could verify - do not cite numbers from this entry."),
 ("kesit_variation", "Ultrasound vs dissection for median nerve / thenar motor branch variants (Lanz types)", "PMC5635084",
  {"330_2017_4882_Fig2_HTML.jpg": ("US",
    "Cadaver dissection (a) and matching long-axis ultrasound (b) of a Lanz type 1 median nerve with an extraligamentous thenar motor branch curling around the distal flexor retinaculum.",
    "a: FR, MN, MB, dashed lines; b: Prox, Dist, FR (double arrow), BM, MN, star, yellow outline/arrows"),
   "330_2017_4882_Fig3_HTML.jpg": ("US",
    "Cadaver dissection (a) and short-axis ultrasound (b) of a Lanz type 3 (bifid/high-division) median nerve; arrows mark the two trunks.",
    "a: FR, BM, star, 'High division of the MN', MN, dashed lines; b: two white arrows")},
  "30 wrists (15 fresh cadavers). 'By dissection, type 1, 2 and 3 variants were found in 84%, 3%, and 13% of wrists'. 'extra-, sub-, and transligamentous courses were recorded in 65%, 31%, and 4% of cases'. Ultrasound vs dissection agreement 'kappa =0.9' for variant type and 'kappa =1' for MBMN course; 'the bifid nerve, hypertrophic muscles, and bilateral symmetry ... 13.3%, 13.3%, and 86.7%'.",
  "'Ultrasound can be used reliably to identify anatomic variations of the MN and MBMN. It could be a useful tool before carpal tunnel release surgery.'",
  "Image labels write 'BM' where caption says 'MB' (motor branch). Each figure combines a cadaver photo (also usable in topo slides) with US."),
 ("kesit_variation", "Lunotriquetral coalition on radiograph (Minnaar type II)", "PMC2893531",
  {"eplasty10e47_fig1.jpg": ("radiograph",
    "AP radiograph of the right wrist: incomplete osseous fusion of lunate and triquetrum with a distal notch (Minnaar type II).",
    "no labels (ePlasty watermark only)")},
  "Case report (21-year-old woman, bilateral). Background cited: 'the most common coalition representing nearly 90% of all carpal fusions ... The prevalence in the general population averages 0.1% but is thought to be 100 times higher in Africans.' 'This anomaly is found more often in females with a ratio of 2:1'. Complete form (Minnaar III) 46.8%, distal notch type 28.1% (literature).",
  "'not only incomplete but also complete luno-triquetral coalitions can cause wrist pain.'",
  "Image 425x450, unlabelled - we must add an arrow. MRI Fig 3 dropped (unlabelled, adds little). Prevalence numbers are literature citations, not original data."),
 ("kesit_variation", "Os styloideum (carpal boss) on radiograph, CT and MRI", "PMC5487237",
  {"rb-50-03-0200-g01.jpg": ("CT",
    "Four-panel case: PA radiograph (A), 3D CT (B) and axial CT (C) showing an os styloideum fused to the trapezoid at the dorsal 2nd/3rd CMC region, and axial T1 MRI (D) with adjacent bone oedema.",
    "A, B, C, D; TRAPEZOID; OS STYLOIDEUM (x2 each); yellow arrows")},
  "Case report. 'the os styloideum is fused to the trapezoid, which occurs in only 0.5% of cases. More commonly (in 94.0% of cases), it is fused to the base of the second and third metacarpal, merged with the capitate (in 3.5%) or (in 2.0%) isolated'.",
  "Carpal boss is often confused clinically with a dorsal ganglion; 'The true incidence of carpal boss syndrome is unknown'.",
  "Panels include radiograph + CT + MRI, so one figure covers three modalities."),
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
    for fn, (spec, what, labels) in figs.items():
        p = d / fn
        assert p.exists(), p
        lab, cap = next(v for g, v in caps.items() if g and (fn == g or fn.startswith(g + ".") or fn.rsplit(".", 1)[0] == g.rsplit(".", 1)[0]))
        w, h = Image.open(p).size
        flist.append({"file": fn, "label": lab, "caption": cap, "specimen": spec, "what_it_shows": what,
                      "labels_visible_in_image": labels, "pixels": f"{w}x{h}",
                      "local_path": str(p.relative_to(ROOT))})
    out.append({"use": use, "topic": topic, "pmcid": pmcid, "version": int(x.stem.rsplit(".", 1)[1]),
                "doi": j.get("doi"), "citation": j.get("citation"), "title": t(m.find(".//article-title")),
                "authors": ", ".join(au[:3]) + (" et al." if len(au) > 3 else ""), "year": yr,
                "journal": t(root.find(".//journal-title")), "license_code": j.get("license_code"),
                "figures": flist, "key_findings": kf, "clinical_relevance": cr, "notes": notes})

(ROOT / "sources/bolge_el.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(len(out), "entries;", sum(len(e["figures"]) for e in out), "figures")
for e in out:
    print(f"{e['use']:15} {e['pmcid']:12} {e['license_code']:10} {[f['file'] for f in e['figures']]}")
