#!/usr/bin/env python3
"""Build sources/bolge_onkol.json (ÖNKOL region: elbow & forearm) from downloaded PMC OA files.

Bibliographic fields (citation, doi, licence, version), figure labels and captions are read verbatim
from the bucket .json/.xml saved in topografik/images/raw/PMC<id>/; pixel sizes from the image files.
Interpretive fields (what_it_shows, labels_visible_in_image, key_findings ...) are curated below after
viewing every figure.   Run:  python3 -I scripts/build_bolge_onkol.py
"""
import json, pathlib, re, xml.etree.ElementTree as ET
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "topografik/images/raw"
XL = "{http://www.w3.org/1999/xlink}href"


def t(e):
    return " ".join("".join(e.itertext()).split()) if e is not None else ""


def F(file, specimen, shows, labels):
    return {"file": file, "specimen": specimen, "what_it_shows": shows, "labels_visible_in_image": labels}


E = []
# ---------------------------------------------------------------- topo_lecture
E.append(dict(pmcid="PMC10235925", use="topo_lecture",
    topic="Superficial flexor layer of the forearm (normal right side) - pronator teres, FCR, palmaris longus, FDS, FCU, radial artery",
    figures=[F("cureus-0015-00000038424-i04.jpg", "human cadaver",
               "Anterior view of the dissected right forearm with the normal superficial flexor layer; numbered structures include palmaris longus, FCU, FCR, pronator teres, FDS, brachioradialis, radial artery and brachial artery.",
               "1, 2, 3, 4, 5, 6, 7, 8, B, * (numbers only; key is in caption)"),
             F("cureus-0015-00000038424-i01.jpg", "human cadaver",
               "Opposite (left) forearm of the same cadaver with a reversed palmaris longus (fleshy distally) alongside FCU, FCR, PT, FDS, brachioradialis, radial artery and median nerve.",
               "1 (red and white), 2, 3, 4, 5, 6, 7, 8, 9, B, *, black star")],
    key_findings="Single-cadaver case report: \"a unilaterally reversed palmaris longus muscle in the left forearm of a 55-year-old male cadaver, discovered in a routine teaching session.\" The right forearm (Figure 4) shows the normal superficial flexor arrangement.",
    clinical_relevance="The authors note palmaris longus variations \"may have clinical implications on different pathologies such as Guyon's syndrome or Carpal tunnel syndrome based on the nerves and vessels surrounding it\".",
    notes="Used here for the NORMAL right-side Figure 4 (superficial flexor layer, numbered key). Figures are wide but short (750x205 and 750x243); numbers are legible but crop/enlarge for slides. Reversed PL itself is already covered by PMC7033050 in topografik_kaynaklar.json."))

E.append(dict(pmcid="PMC12055948", use="topo_lecture",
    topic="Deep flexor layer: anterior interosseous nerve with branches to FDP, FPL and pronator quadratus",
    figures=[F("68_2025_2869_Fig1_HTML.jpg", "human cadaver (fresh, non-embalmed)",
               "Anterior forearm dissection between the bi-epicondylar and bi-styloid lines exposing the anterior interosseous nerve and its motor branches to FDP, FPL and pronator quadratus.",
               "AIN, FDP, PQ, FPL, Biepicondylar line, Bistyloid line"),
             F("68_2025_2869_Fig2_HTML.jpg", "schematic",
               "Author schematic (AP and lateral views of radius/ulna) of AIN origin and FDP/FPL branch origins with mean distances (mm) to the bi-epicondylar and bi-styloid lines and to the radius.",
               "bi-epicondylar line, bi-styloid line, AIN origin, FDP origin, FPL origin, Pronator quadratus, 44, 73, 83, 13, 8, 184, 170, proximal, lateral, anterior")],
    key_findings="\"A cadaveric study was conducted on ten fresh, non-embalmed forearms.\" \"The AIN originated, on average, 13 mm from the radius\"; \"The first branch to the flexor pollicis longus emerged at an average of 8 mm from the radius\". \"The highest risk zone for AIN injury was identified at the junction of the proximal and middle thirds of the forearm.\"",
    clinical_relevance="\"To minimize iatrogenic injury, care should be taken when exposing the anterior radius, particularly by avoiding excessive traction or deep retractor placement in this region.\"",
    notes="Fig 1 is a tall narrow image (473x1142); labels large and legible."))

E.append(dict(pmcid="PMC8521140", use="topo_lecture",
    topic="Anterior interosseous nerve origin and course; deep flexor compartment (FDP, FPL, PQ)",
    figures=[F("gr1.jpg", "schematic + human cadaver",
               "(a) Line drawing of the median nerve giving off the AIN deep to pronator teres and running on FDP/FPL to pronator quadratus, with measured distances a and b; (b) matching cadaveric dissection of a right forearm.",
               "1a, 1b, MN, BA, Br, PT, FPL, FDP, AIN, PQ, a, b, Point of origin of AIN"),
             F("gr3.jpg", "human cadaver",
               "Distal forearm dissection showing the AIN running toward pronator quadratus and giving two muscular branches (arrows) to FPL.",
               "Lateral, Medial, PQ, FPL, MN, AIN, arrows")],
    key_findings="\"44 cadaveric upper limbs\". \"The nerve originated at a mean distance of 41.56 mm from the bi-epicondylar line. In 12 upper limbs, FDP received two branches and in two limbs, it received three branches. In 13 upper limbs, FPL received two branches from AIN.\" \"Gantzer muscle was observed in 18 (40%) specimens and was found superficial to the nerve.\"",
    clinical_relevance="\"These branches to FPL and FDP would aid as a source of nerve grafting and nerve transfer in the cases of upper extremity nerve palsies.\"",
    notes="Fig 1a drawing appears to be the authors' own (caption: 'Drawing showing the origin and course of the AIN'); no reproduction statement found."))

E.append(dict(pmcid="PMC5383373", use="topo_lecture",
    topic="Cubital tunnel: Osborne's ligament between the two heads of flexor carpi ulnaris and the ulnar nerve",
    figures=[F("cureus-0009-00000001080-i01.jpg", "human cadaver",
               "Posterior-medial right elbow dissection: the ulnar nerve (crossed by a pin) passes deep to Osborne's ligament, the fibrous band joining the humeral and ulnar heads of FCU.",
               "FCU, FCU, O, M")],
    key_findings="Review article (no new series). \"This band of tissue connects the two heads of the flexor carpi ulnaris and thus forms the roof of the cubital tunnel.\" Synonyms listed: \"arcuate ligament of Osborne\", \"cubital tunnel retinaculum\", \"Osborne's fascia\", \"Osborne's band\".",
    clinical_relevance="The ligament is \"often implicated and surgically transected to decompress the ulnar nerve at the elbow.\"",
    notes="Only Figure 1 taken. Figure 2 (drawing) was REJECTED: 'Published with permission from [5]' (third-party copyright). Label key O/M = olecranon/medial epicondyle per caption."))

E.append(dict(pmcid="PMC11270274", use="topo_lecture",
    topic="Posterior (extensor) compartment of the forearm - classical anatomy and extensor retinaculum",
    figures=[F("jfmk-09-00109-g001.jpg", "human cadaver",
               "Dissection of the normal right posterior forearm showing ECRL, ECRB, extensor digitorum, APL and EPB emerging in the outcropping group, and tendons of ECRL/ECRB/EPL passing under the extensor retinaculum.",
               "Tendon of ECRL, Tendon of ECRB, Tendon of EPL, ER, EPB, APL, ECRB, ED, ECRL, Distal/Proximal/Left/Right compass")],
    key_findings="Case report of bilateral ECRL accessory tendon with ECRB agenesis in a 75-year-old female cadaver; \"Thirty-two additional forearms were assessed for similar variations, with none being observed.\" Figure 1 is the authors' reference image of classical anatomy.",
    clinical_relevance="Relevant \"regarding tendon reconstructive procedures as well as accessing the distal radial artery via the anatomical snuffbox.\"",
    notes="Used for the NORMAL extensor compartment (Fig 1). Labels are arrows with abbreviations, very legible."))

E.append(dict(pmcid="PMC6850211", use="topo_lecture",
    topic="Medial elbow: common flexor-pronator origin from the medial epicondyle, layers (PT, FCR, PL, FDS, FCU), median and ulnar nerves",
    figures=[F("CA-32-379-g001.jpg", "human cadaver (embalmed)",
               "Three-step medial view of a left elbow: (a) superficial flexor-pronator muscles from the medial epicondyle; (b) PL/FCR removed showing FDS and the tendinous septa; (c) muscle bellies removed showing median and ulnar nerves and the septa (dotted lines).",
               "(a), (b), (c), Triceps, Brachialis, PT, FCR, PL, FCU, FDP, FDS, MEC, MN, UN, Prox, Dist")],
    key_findings="\"We conducted a descriptive anatomical study of 23 embalmed cadaveric elbows.\" \"The two tendinous septa (TS) were found: between the pronator teres (PT) and flexor digitorum superficial (FDS) muscles, and between the FDS and flexor carpi ulnaris (FCU) muscles.\" \"the capsule of the humeroulnar joint under the tendinous complex had attachment on the ST of 7 mm width.\"",
    clinical_relevance="\"These anatomical findings could lead to a paradigm shift in the prevention, diagnosis, and treatment of UCL injuries in baseball players.\"",
    notes="Excellent layered teaching image of the superficial/intermediate flexor layers at the medial epicondyle."))

E.append(dict(pmcid="PMC7156465", use="topo_lecture",
    topic="Membrana interossea antebrachii (interosseous membrane) - central band and accessory bands",
    figures=[F("41598_2020_63436_Fig1_HTML.jpg", "human cadaver (fresh-frozen)",
               "Forearm with all muscles removed exposing the interosseous membrane between radius and ulna (a), and close-ups of its ligamentous parts marked with clips: distal oblique bundle, accessory band, central band and dorsal oblique accessory cord (b-e).",
               "(a)-(e), IOM, Ulna, Radius, DOB, AB, DOAC, U, R")],
    key_findings="\"five fresh-frozen annotated cadaveric forearms\". \"Four different IOM ligament structures were identified across the five forearms (from distal to proximal): the distal oblique bundle (DOB), the distal accessory band (AB), the central band (CB) and the dorsal oblique accessory cord (DOAC)\".",
    clinical_relevance="\"Previous studies have shown that the interosseous membrane (IOM) influences forearm motion and stability\"; the 3D data are intended for \"functional planning simulation of the forearm.\"",
    notes="Image 656x282 - panel (a) is usable full-width; panels b-e are small. Panel (d) has no printed CB tag (only identified in caption)."))

E.append(dict(pmcid="PMC3919107", use="topo_lecture",
    topic="Radial tunnel, mobile wad and leash of Henry (anterior approach to the posterior interosseous nerve)",
    figures=[F("eplasty14ic04_fig2.jpg", "intraoperative photograph (living patient)",
               "Anterior forearm approach, superficial layer: brachioradialis with the radial artery medially and the superficial radial nerve.",
               "RA, BR, SRN, ePlasty logo"),
             F("eplasty14ic04_fig3.jpg", "intraoperative photograph (living patient)",
               "Deeper exposure showing the radial recurrent vessels (leash of Henry) forming part of the roof of the radial tunnel beside brachioradialis.",
               "LH, RT, BR, ePlasty logo")],
    key_findings="Images-in-clinical-medicine article (single patient with radial tunnel lipoma). \"The radial tunnel is a potential space that extends 5 cm from the radial head to the distal margin of supinator.\" \"The Arcade of Frohse is a connection between the deep and superficial heads of supinator and is fibrotendinous in 30% of the population.\"",
    clinical_relevance="\"Motor dysfunction is not a feature in radial tunnel syndrome. In contrast, posterior interosseous nerve entrapment is always associated with motor weakness.\"",
    notes="Intraoperative (not cadaver) photos; no identifiable patient features. Fig 4 REJECTED: caption says 'Adapted from Ref 1'. Journal watermark (ePlasty) on images."))

E.append(dict(pmcid="PMC9925568", use="topo_lecture",
    topic="Radial nerve at the elbow: five compression points of the PIN and the arcade of Frohse (schematic)",
    figures=[F("10143_2023_1944_Fig1_HTML.jpg", "schematic",
               "Rendered schematic of the lateral elbow showing the radial nerve dividing into SBRN and PIN and the five classic compression points (1 fibrous tissue, 2 radial recurrent vessels, 3 ECRB margin, 4 arcade of Frohse, 5 distal supinator).",
               "RN, SBRN, PIN, S, ECRB, 1, 2, 3, 4, 5"),
             F("10143_2023_1944_Fig3_HTML.jpg", "schematic",
               "Rendered schematic of the PIN entering the supinator beneath the arcade of Frohse between the superficial and deep layers of supinator, with brachioradialis.",
               "PIN, AF, SLSM, DLSM, BRM, *")],
    key_findings="Review. Arcade of Frohse subtypes tabulated: \"Type A The tendinous type 64.10%\", \"Type B The mixed musculo-tendinous type 21.70\", \"Type C The muscular type 12.30%\", \"Type D The membranous type 1.90%\". \"The AF can adopt three shapes: semicircular in 64%, oblique elongated in 29%, and semioval in 7% of specimens\". \"The thickness varies from 0.43 to 0.8 mm (mean: 0.67)\".",
    clinical_relevance="\"Entrapment of the radial nerve at the elbow is the third most common compressive neuropathy of the upper limb after carpal tunnel and cubital tunnel syndromes.\" \"The most common of the compressive neuropathies related to the radial nerve is the posterior interosseus nerve syndrome.\"",
    notes="Illustrations: no source/permission statement and no BioRender mention found in XML; appear to be the authors' own. Complements PMC12500735 (already in repo) which has the cadaver photos of Frohse."))

# ---------------------------------------------------------------- topo_variation
E.append(dict(pmcid="PMC5797209", use="topo_variation",
    topic="Pronator teres head variations and the course of the median nerve (pronator syndrome)",
    figures=[F("12565_2017_413_Fig3_HTML.jpg", "human cadaver",
               "Three types of median nerve course relative to the pronator teres: (a) between humeral and ulnar heads, (b) and (c) variant courses deep to/through the muscle.",
               "a, b, c, hhPT, PT, MN, * (ulnar head), scale bar '1 mm'")],
    key_findings="\"In 50 isolated, formalin-fixed upper limbs\". Humeral head from medial epicondyle and medial intermuscular septum in \"(72%)\". \"The ulnar head was present in 43 limbs (86%). The MN passed between the heads of the PT muscle (74%) or under the muscle (26%). In the majority of cases, it provided two motor branches (66%).\"",
    clinical_relevance="\"There is an association between the morphologic variation of the PT muscle heads and the course and branching pattern of the MN... This may have an impact on the risk of PT syndrome and the performance of MN electrostimulation.\"",
    notes="Scale bars printed '1 mm' are implausible for the field of view (probably 1 cm) - do not quote scale. Fig 4 (innervation variants) downloaded then dropped (less useful)."))

E.append(dict(pmcid="PMC6016218", use="topo_variation",
    topic="High origin of the radial artery (brachioradial artery) and cubital crossover",
    figures=[F("BMRI2018-1520929.002.jpg", "human cadaver",
               "Two upper limbs with a brachioradial artery arising in the arm and running superficial to the median nerve in the medial bicipital groove down to the cubital fossa.",
               "(a), (b), MN, BA, BV, BRA, CV, MCV, MCNF, UN, arrowheads, *"),
             F("BMRI2018-1520929.003.jpg", "human cadaver",
               "Anterior cubital fossa of a right limb: dominant-type 'cubital crossover' anastomosis (arrowheads) between a hypoplastic brachioradial artery and the brachial artery giving the radial artery.",
               "BA, MN, hBRA, RA, arrowheads")],
    key_findings="\"One hundred and twenty randomly selected, isolated upper limbs fixed in 10% formalin solution were dissected.\" \"The radial artery was found to have a high origin in 9.2% of total number of the limbs: two cases from the axillary artery; nine cases from the brachial artery.\" Cubital anastomosis \"(54.6%)\": \"dominant in one case, balanced in three cases, minimal in two cases, and absent in five cases.\"",
    clinical_relevance="\"A complete radioulnar arch was found more often when the brachioradial artery was present as a variant.\" The variant matters for transradial access and radial forearm flaps (discussed in the article).",
    notes="Original cadaver series; complements PMC10599095/PMC10823296 (brachial variants already in repo)."))

E.append(dict(pmcid="PMC12286150", use="topo_variation",
    topic="High-origin superficial ulnar artery and superficial radial artery (US + dissection screen of 150 limbs)",
    figures=[F("jfmk-10-00246-g005.jpg", "human cadaver (fresh-frozen)",
               "Cubital fossa dissection: superficial ulnar artery and superficial radial artery under the bicipital aponeurosis, with median nerve, biceps tendon, brachialis and brachioradialis.",
               "ME, MEP, SUA, SRA, MN, BBT, B, BR"),
             F("jfmk-10-00246-g003.jpg", "US + human cadaver",
               "Left: transverse ultrasound of the distal forearm showing SUA and SRA relative to FCU, ulnar nerve, FDS, FDP, FCR and pronator; right: matching dissection with PL, SUA, SRA, FCU.",
               "FCU, UN, SUA, FDS, f.FDP, FCR, PT, SRA, PL, white arrow")],
    key_findings="\"A cross-sectional ultrasound and anatomical study was conducted on 150 upper limbs from fresh-frozen cadavers.\" \"One case (0.66%) of concurrent superficial ulnar artery and superficial radial artery was identified in the left arm of a 79-year-old male cadaver. The superficial ulnar artery originated from the axillary artery\".",
    clinical_relevance="\"The presence of superficial ulnar and radial arteries, especially when originating from high levels, increases the risk of iatrogenic injury, misdiagnosis, and surgical complications.\" \"Ultrasound serves as a reliable, non-invasive method for detecting such variations preoperatively.\"",
    notes="Caption of Fig 3 says 'pronator quadratus muscle (PT)'; image label reads 'PT'. Could also serve kesit_variation (US)."))

E.append(dict(pmcid="PMC12375367", use="topo_variation",
    topic="Anconeus epitrochlearis (typical single-headed vs rare three-headed) over the ulnar nerve in the cubital tunnel",
    figures=[F("cureus-0017-00000088743-i01.jpg", "human cadaver",
               "Right medial elbow: typical single-headed anconeus epitrochlearis from medial epicondyle to olecranon, with the ulnar nerve passing beneath it through the cubital tunnel.",
               "Proximal, Distal, Medial Epicondyle, Olecranon, blue arrows, black arrow"),
             F("cureus-0017-00000088743-i02.jpg", "human cadaver",
               "Left medial elbow of the same cadaver: atypical three-headed anconeus epitrochlearis (arrows) with the ulnar nerve (asterisks) beneath; FCU and triceps labelled.",
               "Proximal, Distal, MEC, FCU, FCU, Triceps brachii, Olecranon, *, white arrows")],
    key_findings="Case report (82-year-old female). Right AEM: \"width of 8.5 mm and a length of 1.6 cm\"; left: three heads (middle head \"7.5 mm and 1.4 cm\", proximal head \"5.5 mm in width and 1.6 cm in length\"), \"with the proximal head located deep to the ulnar nerve\".",
    clinical_relevance="\"Clinically, the AEM has been associated with cubital tunnel syndrome due to potential ulnar nerve compression. However, some studies suggest it might protect the ulnar nerve compared to the more rigid Osborne's ligament.\"",
    notes="No PMC-OA cadaveric PREVALENCE series of anconeus epitrochlearis was found (Dolenšek 2024 Folia Morphol 4.3% is OA on publisher site but not in PMC OA bucket - not verifiable here). This case report gives the clearest labelled images."))

E.append(dict(pmcid="PMC12892004", use="topo_variation",
    topic="Persistent median artery: cadaveric prevalence and variants (antebrachial/palmar), relation to median nerve and common interosseous artery",
    figures=[F("cureus-0018-00000101320-i02.jpg", "human cadaver",
               "Left forearm and hand: persistent median artery arising near the ulnar/radial bifurcation and piercing the median nerve in the proximal forearm, running to the carpal tunnel.",
               "BA, RA, PMA, PMA, MN, UA, CT"),
             F("cureus-0018-00000101320-i05.jpg", "human cadaver",
               "Proximal forearm: antebrachial-type PMA from the common interosseous artery region alongside AIA/PIA, blending with the median nerve; also a good image of the common interosseous trunk.",
               "MN, UA, PMA, BA, RA, CIA, PIA, AIA, MB")],
    key_findings="\"In a cadaveric study of 23 upper limbs from 12 donated adult cadavers, PMA was identified in eight limbs (34.8%). Half of these (4/8 limbs, 17.4%) pierced the median nerve in the proximal forearm\". \"Two palmar-type PMAs were identified ... (2/23 limbs, 8.7%).\"",
    clinical_relevance="\"These anatomical variations may contribute to median nerve compression syndromes, such as carpal tunnel syndrome, and pose risks during surgical procedures of the forearm and wrist.\"",
    notes="PMA is already illustrated by PMC10343151 (case); this adds a small prevalence series. Fig 5 also usable for a. interossea communis/anterior/posterior in topo_lecture."))

E.append(dict(pmcid="PMC7345276", use="topo_variation",
    topic="Radial nerve branching in the forearm: variable origin of branches to brachioradialis and ECRB (SBRN vs deep branch)",
    figures=[F("diagnostics-10-00366-g001.jpg", "human cadaver",
               "Lateral elbow/forearm: radial nerve dividing into SBRN and DBRN beneath brachioradialis, with a branch to BR arising from the SBRN (*) plus a smaller branch from the radial nerve proper (dagger).",
               "Radial N., DBRN, SBRN, BR, *, dagger, Proximal, Distal"),
             F("diagnostics-10-00366-g002.jpg", "human cadaver",
               "Variant in which the nerve to ECRB (*) arises from the superficial branch of the radial nerve.",
               "Radial N., SBRN, DBRN, ECRB, *, Proximal, Distal")],
    key_findings="\"Thirty-five cadavers were dissected\". \"Notably, the radial nerve often innervated brachialis (60%), and its superficial branch often innervated extensor carpi radialis brevis (25.7%).\" \"The ECRB's branch arose proximal to that of supinator in 27 specimens (77.1%)\".",
    clinical_relevance="\"These findings may also need to be considered when planning surgical approaches to the distal arm, elbow and proximal forearm to prevent an undue loss of motor function.\"",
    notes="Fills the PIN/radial-nerve-branching variation slot (arcade of Frohse series in PMC OA were CC BY-NC-ND - rejected)."))

# ---------------------------------------------------------------- kesit_lecture
E.append(dict(pmcid="PMC6447645", use="kesit_lecture",
    topic="Elbow collateral ligaments (MCL and LCL complexes, annular ligament) on MRI with schematic",
    figures=[F("13244_2019_725_Fig4_HTML.jpg", "schematic",
               "Author illustration: (A) medial view of MCL complex (anterior bundle, posterior bundle, transverse ligament); (B) lateral view of LCL complex (RCL, annular ligament, LUCL).",
               "A, B, A-MCL, P-MCL, T-MCL, RCL, AL, LUCL"),
             F("13244_2019_725_Fig5_HTML.jpg", "MRI",
               "Consecutive coronal fat-suppressed PD MRI of the intact anterior bundle of the MCL from the medial epicondyle to the sublime tubercle.",
               "A, B, C, ME, *, arrowheads, arrows"),
             F("13244_2019_725_Fig7_HTML.jpg", "MRI",
               "Consecutive coronal FS PD MRI of the intact LUCL and RCL, annular ligament and common extensor origin at the lateral epicondyle; LUCL to the supinator crest.",
               "A, B, C, D, LE, SC, *, arrows, arrowheads")],
    key_findings="Pictorial review. \"the anterior bundle of the medial or ulnar collateral ligament complex, which provides about 54% of valgus stability\"; ulnohumeral joint \"provides about 33% of valgus stability\". \"Twenty-three percent of people have an accessory ulnar collateral ligament\".",
    clinical_relevance="\"Conventional MRI and MR arthrography are the imaging modalities of choice in the evaluation of elbow ligament injuries.\" \"The most important static soft-tissue constraints are the lateral ulnar collateral ligament and the anterior bundle of the medial collateral ligament\".",
    notes="Insights into Imaging, CC BY. Fig 8 (annular ligament, axial) downloaded then dropped to keep 3 figs; can be fetched later if needed (13244_2019_725_Fig8_HTML.jpg)."))

E.append(dict(pmcid="PMC10093241", use="kesit_lecture",
    topic="Ulnar nerve in the cubital tunnel: ultrasound correlated with dissection (Osborne's fascia, arcuate ligament, FCU heads)",
    figures=[F("diagnostics-13-01332-g004.jpg", "US + human cadaver",
               "(A) Transverse US of the ulnar nerve in the osteofibrous retroepicondylar tunnel under Osborne's fascia beside the medial epicondyle; (B) matching dissection with olecranon and medial epicondyle.",
               "A, B, UN, ME, Olc, arrows, * * *, Proximal-Arm, Distal-Forearm"),
             F("diagnostics-13-01332-g007.jpg", "US + human cadaver",
               "(A) US of the ulnar nerve leaving the tunnel between the medial and lateral heads of FCU; (B) dissection showing the nerve passing beneath Osborne's (arcuate) ligament.",
               "A, B, LH, MH, ME, + (nerve outline), UN, FCU, *, arrows")],
    key_findings="\"Eleven upper limbs from eight adult corpses were ultrasonographically examined and subsequently dissected\". Relationships observed with \"the medial intermuscular septum, the triceps aponeurosis, Osborne's fascia at the elbow, the arcuate ligament of Osborne and the intermuscular aponeurosis between the flexor carpi ulnaris and the flexor digitorum superficialis muscles.\" \"a fourth head of the triceps brachii muscle was found in some specimens.\"",
    clinical_relevance="\"Results demonstrate that ultrasound is a good tool to investigate ulnar nerve entrapment neuropathy and to identify other anatomical points where the nerve can remain compressed.\"",
    notes="Fig 4 is wide/short (743x238) - legible but small."))

E.append(dict(pmcid="PMC8630951", use="kesit_lecture",
    topic="Forearm compartments in cross-section (superficial/deep volar, superficial/deep dorsal, mobile wad) with HRUS",
    figures=[F("rb-54-06-0388-g05.jpg", "schematic (cross-sectional)",
               "Four colour-coded axial diagrams of the forearm (proximal to distal) showing compartments, muscles, numbered nerves and vessels, radius and ulna.",
               "A, B, C, D, Compartments legend (Superficial Volar, Deep Volar, Superficial Dorsal, Deep Dorsal, Lateral (mobile wad)), PR, FCR, PL, FDS, FCU, FDP, Br, ECRL, ECRB, ED, EDM, ECU, A, S, APL, EPL, EPB, EI, FPL, PQ, R, U, CV, BV, MV, LAbCN, MAbCN, PAbCN, 1-15, 'Mohana-Borges'"),
             F("rb-54-06-0388-g06.jpg", "US",
               "Transverse HRUS panels of the lateral compartment (ECRL, ECRB, Br with SBRN, ECRB branch, radial artery) and the posterior compartment (ECU, EDM, ED, APL, supinator with PIN and PIA), with probe-position icons.",
               "C, B, ECRL, ECRB, Br, ECRBb, SBRN, RA, FCR, R, U, ECU, EDM, ED, APL, PIA, S, PIN, L18-5 scanner text")],
    key_findings="Pictorial review (normal anatomy, volunteers). Images \"obtained with a high-resolution broadband 18-5 MHz linear transducer.\" \"the median nerve, the ulnar nerve, and the superficial branch of the radial nerve are easily visualized throughout\" the forearm.",
    clinical_relevance="\"Knowledge of the normal anatomy of the forearm improves the technical quality of the examinations, contributing to better diagnoses, as well as improving the performance and safety of interventional procedures.\"",
    notes="Fig 6 file in bucket contains only panels C and B (no panel A visible; lower ~30% of the image is blank) - crop before use. Fig 5 diagram is the best substitute for an axial forearm MRI atlas (no CC BY labelled axial forearm MRI found)."))

E.append(dict(pmcid="PMC8630952", use="kesit_lecture",
    topic="Forearm vessels on Doppler HRUS: brachial bifurcation, leash of Henry, interosseous arteries with AIN/PIN",
    figures=[F("rb-54-06-0398-g01.jpg", "US (colour Doppler)",
               "Long-axis Doppler of the brachial artery bifurcating into radial and ulnar arteries; (B) ulnar artery giving the posterior ulnar recurrent artery and continuing toward the common interosseous artery.",
               "A, B, BA, RA, UA, PURA, CIA, S/I/A/P orientation"),
             F("rb-54-06-0398-g05.jpg", "US (colour Doppler)",
               "Transverse Doppler at the radial neck showing the leash of Henry (radial recurrent branches) crossing the deep branch of the radial nerve, with the SBRN superficial.",
               "Leash of Henry, SBRN, DBRN, L/M/A/P orientation"),
             F("rb-54-06-0398-g06.jpg", "US (colour Doppler)",
               "(A) Posterior compartment: PIA between supinator and APL, with DBRN, ECU, EDM, ED; (B) anterior interosseous nerve and artery on the interosseous membrane between FPL and FDP.",
               "A, B, ECU, EDM, ED, APL, PIA, S, DBRN, R, U, Br, FCR, ECRL, FPL, AIN, AIA, FDP")],
    key_findings="Pictorial essay on \"the relationships between arteries, satellite veins and nerves\". \"The posterior interosseous artery enters the posterior compartment above the interosseous membrane, emerging in the posterior compartment between the supinator and abductor pollicis longus muscles\".",
    clinical_relevance="Familiarity with vessel-nerve relationships improves \"the performance and safety of interventional procedures.\"",
    notes="Companion to PMC8630951 (same authors, CC BY). Fig 7 shows a persistent median artery on Doppler (not downloaded)."))

# ---------------------------------------------------------------- kesit_variation
E.append(dict(pmcid="PMC10378300", use="kesit_variation",
    topic="Flexor digitorum superficialis tendon crossing ('chiasma antebrachii') on forearm MRI - prevalence and variant",
    figures=[F("diagnostics-13-02406-g002.jpg", "MRI",
               "Series of axial contrast-enhanced fat-suppressed T1 forearm images (distal forearm to carpal tunnel) tracking the FDS tendons to digits 2 and 3 (white/black arrows) as they cross.",
               "A, B, C, D, E, F, white arrows, black arrows"),
             F("diagnostics-13-02406-g003.jpg", "MRI",
               "Axial series in a patient with a variant FDS arrangement without a typical distal chiasma.",
               "A, B, C, D, E, F, white arrows, black arrows"),
             F("diagnostics-13-02406-g004.jpg", "human cadaver",
               "Dissected distal forearms of two body donors showing the FDS tendons (numbered by digit) and the chiasma antebrachii (dotted red/yellow lines).",
               "Chiasma antebrachii, FDS, 2, 3, 4, 5")],
    key_findings="\"In 89 patients (41 women, 39.3 ± 21.3 years), MRI examinations of the forearm (2010–2021) were reviewed\". \"The chiasma antebrachii was identified in the distal third of the forearm in 88 patients (98.9%), while one intersection was located more proximally\". \"median length of 28 mm (interquartile range: 24–35 mm)\"; distances to DRUJ and elbow \"16 mm (8–25 mm) and 215 mm (187–227 mm)\".",
    clinical_relevance="\"the chiasma antebrachii is part of the standard FDS anatomy. Knowledge of its morphology is important, e.g., in targeted injections of therapeutics or reconstructive surgery.\"",
    notes="MRI images have arrows only (no text labels) - add our own labels on slides."))

E.append(dict(pmcid="PMC8748762", use="kesit_variation",
    topic="Accessory flexor carpi radialis brevis on MRI - prevalence in 849 subjects",
    figures=[F("41598_2021_4445_Fig2_HTML.jpg", "MRI",
               "Axial T1 MRI of the distal forearm/wrist at pronator quadratus level showing the accessory FCRB muscle (arrow) beside the FCR tendon, FPL, carpal tunnel contents and median nerve.",
               "VOLAR, DORSAL, CT, PQ, RAD, ULNA, star, arrowhead, arrow, dotted arrow"),
             F("41598_2021_4445_Fig3_HTML.jpg", "MRI",
               "Coronal T1 MRI showing the FCRB tendon (arrows) inserting on the second metacarpal next to the FCR tendon (arrowhead).",
               "2. MC, RAD, ULNA, arrows, arrowhead")],
    key_findings="\"Forearm, wrist, and hand magnetic resonance images of 849 individuals aged 18–65 years were retrospectively evaluated\". \"FCRB prevalence of 4%, with a prevalence of 3.6% among women and of 4.7% among men\" (p = 0.629). \"The origin of all 34 FCRBs identified was the distal third of the anterior aspect of the radius; the insertion site of 28 was the second metacarpal bone, whereas that of the remaining 6 was the os trapezium.\"",
    clinical_relevance="FCRB \"is usually asymptomatic but may cause various pathologies, such as radial-sided wrist pain.\"",
    notes="An Addendum (PMC9458718) corrected figure annotations of this article; the bucket files are the current version - check addendum before final use. Distal forearm/wrist level - shared interest with El region."))

E.append(dict(pmcid="PMC11783411", use="kesit_variation",
    topic="Palmaris longus present vs absent on axial MRI and median nerve depth",
    figures=[F("10.1177_15589447251314145-fig3.jpg", "MRI",
               "Axial wrist MRI at DRUJ level WITH palmaris longus: measured distances from the median nerve centre to skin, radius and FCR.",
               "10.31 mm, 6.02 mm, 8.47 mm"),
             F("10.1177_15589447251314145-fig4.jpg", "MRI",
               "Axial wrist MRI at DRUJ level WITHOUT palmaris longus: same measurements, median nerve much closer to skin.",
               "12.39 mm, 9.68 mm, 3.58 mm")],
    key_findings="\"1193 wrist magnetic resonance imaging (MRI) studies were retrospectively reviewed from 2019 to 2023. One hundred adults ... 50 wrist axial plane MRIs (distal radial-ulnar joint level) with PL and 50 without PL.\" \"Individuals with PL had a greater distance between the median nerve and skin volar surface.\" Example: \"Distance of 8.47 mm\" (with PL, Fig 3) vs \"Distance of 3.58 mm\" (without PL, Fig 4).",
    clinical_relevance="\"PL presence results in a deeper median nerve position within the wrist in relation to the skin volar surface. This knowledge is crucial ... during volar approach wrist surgeries and when administering anesthetic or therapeutic injections to the median nerve.\"",
    notes="Not a prevalence study (case-control selection). No anatomical text labels on images - only measurement callouts. DRUJ level (border with El region)."))

E.append(dict(pmcid="PMC5463256", use="kesit_variation",
    topic="Persistent median artery and bifid median nerve on ultrasound - prevalence in 160 wrists",
    figures=[F("cln-72-06-358-g001.jpg", "US",
               "Paired transverse US images (raw and outlined) at the proximal carpal tunnel showing bifid median nerve trunks (arrowheads) and the persistent median artery (arrows), one panel with colour Doppler.",
               "white outlines, arrows, arrowheads (no text)")],
    key_findings="\"One hundred and sixty median nerves were examined using ultrasonography and colour Doppler\". \"a bifid median nerve was observed in 15 (9.4%) wrists, and a persistent median artery was observed in 12 (7.5%) wrists\"; coexistence \"(6.3%)\"; \"Persistent median vein was observed in 9 wrists (5.6%).\"",
    clinical_relevance="\"Their positional relationship in carpal tunnel is uncertain, and thus, preoperative ultrasound is necessary. These three variations do not present any additional risk for the development of carpal tunnel syndrome.\"",
    notes="Image quality modest (800x286, small panels, no text labels). Level = carpal tunnel (El overlap)."))

E.append(dict(pmcid="PMC4754593", use="kesit_variation",
    topic="Anconeus epitrochlearis on ultrasound compressing the ulnar nerve (double crush)",
    figures=[F("jkns-59-75-g001.jpg", "US",
               "(A) Transverse US of the cubital tunnel: anconeus epitrochlearis (arrowhead) over a swollen ulnar nerve (arrow); (B) ganglion compressing the ulnar nerve at Guyon's canal next to the hamate hook.",
               "A, B, arrowhead, arrow, +, G, HAM")],
    key_findings="Single case (55-year-old man): \"ultrasonography revealed a ganglion compressing the ulnar nerve at the hypothenar area and the anconeus epitrochlearis muscle lying in the cubital tunnel.\"",
    clinical_relevance="\"Careful physical examination and ultrasound assessment of the elbow and wrist confirmed the clinical diagnosis prior to surgery.\"",
    notes="LICENCE CC BY-NC (flag). Weak: case report, no prevalence, small unlabeled US (784x207). Kept only because no PMC-OA MRI/US anconeus-epitrochlearis prevalence study exists in the bucket (Nascimento 2018 Rev Bras Ortop and others are CC BY-NC-ND or not OA). Operative photo (Fig 2) dropped."))


def build():
    out = []
    for e in E:
        d = RAW / e["pmcid"]
        js = sorted(d.glob(f"{e['pmcid']}.*.json"))[-1]
        j = json.loads(js.read_text())
        root = ET.parse(js.with_suffix(".xml")).getroot()
        meta = root.find(".//article-meta")
        au = []
        for c in meta.findall(".//contrib[@contrib-type='author']"):
            n = c.find("name")
            if n is not None:
                au.append(f"{t(n.find('surname'))} {t(n.find('given-names'))}".strip())
        authors = ", ".join(au[:3]) + (" et al." if len(au) > 3 else "")
        figmap = {}
        for f in root.iter("fig"):
            for g in f.iter("graphic"):
                figmap[g.get(XL)] = (t(f.find("label")), t(f.find("caption")))
        figs = []
        for fx in e["figures"]:
            p = d / fx["file"]
            assert p.exists(), p
            stem = fx["file"].rsplit(".", 1)[0]
            label, cap = figmap.get(stem) or figmap.get(fx["file"])
            w, h = Image.open(p).size
            figs.append({"file": fx["file"], "label": label, "caption": cap, "specimen": fx["specimen"],
                         "what_it_shows": fx["what_it_shows"], "labels_visible_in_image": fx["labels_visible_in_image"],
                         "pixels": f"{w}x{h}", "local_path": str(p.relative_to(ROOT))})
        year = re.search(r"\b(19|20)\d\d\b", j["citation"]).group(0)
        out.append({"use": e["use"], "topic": e["topic"], "pmcid": e["pmcid"], "version": j["version"],
                    "doi": j.get("doi"), "citation": j["citation"], "title": t(meta.find(".//article-title")),
                    "authors": authors, "year": year, "journal": t(root.find(".//journal-title")),
                    "license_code": j["license_code"], "figures": figs, "key_findings": e["key_findings"],
                    "clinical_relevance": e["clinical_relevance"], "notes": e["notes"]})
    (ROOT / "sources/bolge_onkol.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    for o in out:
        print(o["use"], o["pmcid"], o["license_code"], [f["file"] for f in o["figures"]])


if __name__ == "__main__":
    build()
