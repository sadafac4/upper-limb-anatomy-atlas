#!/usr/bin/env python3
"""Build sources/bolge_omuz.json (OMUZ / shoulder region figure provenance).

Bibliographic fields (citation, doi, licence, title, authors, journal, year) and figure
captions/labels/pixel sizes are read from the downloaded PMC OA bucket files in
topografik/images/raw/PMC<id>/ ; the curated fields (use, topic, what_it_shows,
labels_visible_in_image, key_findings, clinical_relevance, notes) are written below after
visual inspection of every figure and reading of the article full text (.txt from the bucket).
Run with: python3 -I scripts/build_bolge_omuz.py
"""
import json, pathlib, re, struct, xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "topografik/images/raw"
XL = "{http://www.w3.org/1999/xlink}href"


def text(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


def jpeg_size(p):
    b = p.read_bytes()
    i = 2
    while i < len(b):
        if b[i] != 0xFF:
            i += 1; continue
        m = b[i + 1]
        if m in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", b[i + 5:i + 9]); return f"{w}x{h}"
        i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
    return "?"


def meta(pmcid):
    d = RAW / pmcid
    j = json.loads(next(d.glob(f"{pmcid}.*.json")).read_text())
    xp = next(d.glob(f"{pmcid}.*.xml"))
    ver = int(xp.name.split(".")[1])
    root = ET.fromstring(xp.read_bytes())
    am = root.find(".//article-meta")
    auth = []
    for c in am.findall(".//contrib[@contrib-type='author']"):
        n = c.find("name")
        if n is not None:
            auth.append(f"{text(n.find('surname'))} {text(n.find('given-names'))}".strip())
    figs = {}
    for f in root.iter("fig"):
        for g in f.iter("graphic"):
            figs[g.get(XL)] = (text(f.find("label")), text(f.find("caption")))
    cit = j.get("citation", "")
    yr = re.search(r"\b(19|20)\d{2}\b", cit)
    return dict(version=ver, doi=j.get("doi"), citation=cit, title=text(am.find(".//article-title")),
                authors=", ".join(auth[:3]) + (" et al." if len(auth) > 3 else ""),
                year=yr.group(0) if yr else "", journal=text(root.find(".//journal-title")),
                license_code=j.get("license_code"), figs=figs)


# (file, specimen, what_it_shows, labels_visible_in_image)
E = []


def add(use, topic, pmcid, figures, key_findings, clinical_relevance, notes=""):
    E.append(dict(use=use, topic=topic, pmcid=pmcid, figures=figures, key_findings=key_findings,
                  clinical_relevance=clinical_relevance, notes=notes))


# ---------------- A. topo_lecture ----------------
add("topo_lecture", "Rotator cuff muscles and glenohumeral joint capsule with cuff footprints (cadaver)", "PMC5992113", [
    ("40634_2018_134_Fig1_HTML.jpg", "human cadaver",
     "Right shoulder, acromion and coracoid removed: (A) anterior view of subscapularis; (B) posterior view of supraspinatus, infraspinatus and teres minor near their humeral insertions.",
     ["A", "B", "CP", "Subscapularis", "SS", "Supraspinatus", "Infraspinatus", "Teres minor", "Sup", "Lat"]),
    ("40634_2018_134_Fig2_HTML.jpg", "human cadaver",
     "Glenohumeral joint capsule after removal of the cuff muscles, with dotted outlines of the insertions of SSC, SSP, ISP, TMi and origin of long head of triceps (TRI) in anterior, posterior, superior and inferior views.",
     ["A", "B", "C", "D", "CP", "SSC", "Capsule", "SSP", "ISP", "TMi", "Humerus", "TRI", "Sup", "Med", "Lat", "Ant", "Post", "red arrow"]),
], "Anatomical study of 13 shoulders (9 macroscopic, 4 Thiel-embalmed for micro-CT). \"On the humerus, the articular capsule was widely attached to areas without overlying rotator cuffs, with the widest width (17.3 ± 0.9 mm) attached to the axillary pouch.\" The inferior capsule was consistently thicker than the superior part.",
    "The authors state that anatomical knowledge of the whole capsule is necessary to treat capsular disorders such as humeral avulsion of the glenohumeral ligament or capsular elongation after Bankart-type instability.",
    "Excellent clean labelled photos for rotator cuff / capsule slides. Fig 4 (glenoid capsular attachment widths G1–G5) also available in the bucket if needed.")

add("topo_lecture", "Glenohumeral capsule: posterior band of the inferior glenohumeral ligament (cadaver)", "PMC10924754", [
    ("JEO2-11-e12014-g001.jpg", "human cadaver",
     "Six-panel posterior view of the shoulder capsule showing the posterior band of the IGHL lying under the posterior intermediate capsular zone, the axillary pouch and humeral head, with acromion/coracoid as landmarks.",
     ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "symbols only: ❖ (PB of IGHL)", "◆ (intermediate capsular zone)", "✪ (humeral head)", "✚ (acromion)", "★ (coracoid process)"]),
], "Twelve fresh cadaveric shoulders. \"Concerning the PB, mean length and width were 54 ± 7 (50–60) and 16 ± 5 mm (10–25), respectively.\" Bands tensioned first: \"in ER1, the AB at 97 ± 9° ... in IR, the PB at 64 ± 9° ... and in ABD, the PB at 87 ± 10°\".",
    "\"In the case of an isolated lesion to the AB, the PB participates in anterior stabilization of the shoulder by wrapping around the humeral head\" — relevant to Bankart/instability surgery.",
    "Image uses symbols instead of text labels; slide needs a legend. Only 600 px wide but sharp.")

add("topo_lecture", "Suprascapular nerve at the suprascapular notch (incisura scapulae) — dissection", "PMC9223225", [
    ("ijerph-19-07065-g001.jpg", "human cadaver",
     "Left shoulder (specimen C) showing the suprascapular nerve passing under the superior transverse scapular ligament, with its acromioclavicular sensory branch and supraspinatus/infraspinatus motor branches (here dividing proximal to the ligament).",
     ["1", "2", "3", "4", "5", "6"]),
], "Twelve shoulders (six subjects) dissected. \"In two of the six subjects, the suprascapular nerve was divided into two motor branches proximal to the superior transverse scapular ligament.\" Estimated diameter increase \"of 2.008 mm at the suprascapular notch level and 2.047 mm at the spinoglenoid notch level\".",
    "Division of the motor branches proximal to the notch \"may be relevant in the diagnosis and treatment of suprascapular neuropathy and arthroscopic procedures\" (suprascapular block, notch decompression).",
    "Numbers only (1–6) in image; legend from caption. Specimen shows an anatomical variant (proximal division), so caption must say so if used as a 'normal' slide. Complements PMC4555201 already in repo.")

add("topo_lecture", "Brachial plexus trunks in the interscalene triangle / posterior triangle (cadaver)", "PMC5617940", [
    ("diagnostics-07-00040-g001.jpg", "human cadaver",
     "Classic arrangement: superior, middle and inferior trunks with the subclavian artery passing between anterior and middle scalene muscles.",
     ["AS", "ST", "MS", "MT", "IT", "SA"]),
], "Eighty-two cadaveric necks dissected: \"In 62.1%, C5, superior trunk, or superior + middle trunks pierced the anterior scalene.\"",
    "Piercing variants predispose to neurogenic thoracic outlet syndrome; ultrasonography can identify them (see kesit entries for the same article).",
    "Same article also used under kesit_lecture (Fig 3) and kesit_variation (Fig 4).")

add("topo_lecture", "Long thoracic nerve on serratus anterior (lateral chest wall / medial axillary wall)", "PMC5790210", [
    ("cureus-0009-00000001898-i02.jpg", "human cadaver",
     "Lateral chest wall after skin flap retraction: long thoracic nerve running on the serratus anterior, posterior to the pectoralis major edge.",
     ["Pectoral Fascia", "Pectoralis Major", "Serratus Anterior", "Long Thoracic Nerve"]),
    ("cureus-0009-00000001898-i03.jpg", "human cadaver",
     "Deeper dissection exposing the digitations of serratus anterior with the long thoracic nerve along its lateral surface.",
     ["Pectoralis Major", "Serratus Anterior", "Long Thoracic Nerve"]),
], "Ten embalmed cadavers (20 sides). \"Within the operative site, the mean proximal and distal diameters of the LTN were 1.6 and 1.1 mm, respectively. The adjacent ICN had a mean diameter of 1.3 mm.\"",
    "Feasibility of intercostal-to-long-thoracic nerve transfer \"might offer a new technique for restoring protraction following an LTN injury\" (winged scapula).",
    "Clear English text labels; good for 'fossa axillaris medial wall' slide.")

add("topo_lecture", "Deltopectoral groove: cephalic vein and deltoid branches of thoracoacromial vessels (schematic)", "PMC4603045", [
    ("medi-94-e728-g002.jpg", "schematic",
     "Author line drawing of the deltopectoral groove with pectoralis major cut, showing the cephalic vein and the deltoid branches of the thoracoacromial artery and vein.",
     ["Deltoid br. of thoracoacromial artery", "Deltoid br. of thoracoacromial vein", "Cephalic vein", "Deltoid muscle", "Pectoralis major muscle ( cut)"]),
], "Clinical series of 802 consecutive oncology patients (intravenous port implantation). \"The majority of patients (93.6%) could be identified as thoracoacromial vessel. The deltoid branch of the thoracoacromial vein is located on the medial aspect of the deltopectoral groove beneath the pectoralis major muscle (85.8%) and in the deep part of the deltopectoral groove (14.2%).\"",
    "\"It is a safe alternative entry vessel for intravenous port implantation\" when the cephalic vein is not usable.",
    "Not a cadaver study (intra-operative clinical series); Fig 1 is an intra-operative photo and was not taken. Schematic is the authors' own (no reproduction note).")

add("topo_lecture", "Axillary nerve under the deltoid: acromio-axillary distance and safe zone (regio deltoidea)", "PMC6026816", [
    ("acb-51-93-g002.jpg", "human cadaver",
     "Deltoid replaced in position; course of the axillary nerve marked with pins and the anterior/posterior acromio-axillary distances drawn from the acromial edges.",
     ["AEA", "PEA", "AD", "PD", "AXILLARY NERVE"]),
], "Sixty shoulders of thirty cadavers. \"The mean of anterior and posterior AA distance was 5.22 cm and 4.17 cm, respectively.\" \"The minimum AA distance was found to be 3.50 cm. So this should be considered as the maximum permissible length of the deltoid split.\"",
    "Defines a safe area for deltoid-splitting approaches; the axillary nerve's anterior branch is at particular risk of iatrogenic injury.",
    "LICENCE CC BY-NC (flag). Fig 1 (inner deltoid surface) had no labels and was not kept.")

# ---------------- B. topo_variation ----------------
add("topo_variation", "Dorsal scapular artery origin and its relation to the brachial plexus (scapular anastomosis)", "PMC10183034", [
    ("41598_2023_35054_Fig1_HTML.jpg", "human cadaver",
     "(a) Dorsal scapular artery (*) from the transverse cervical artery passing over the trunks; (b) DSA (*) passing between the plexus trunks when arising directly from the subclavian artery.",
     ["a", "b", "AS", "TCA", "T", "S", "M", "I", "SA", "*", "●"]),
], "79 sides of 41 cadavers. \"the dorsal scapular artery originated most frequently from the transverse cervical artery (48%), followed by the direct branch from the third part (25%) and the second part (22%) of the subclavian artery and from the axillary artery (5%).\" \"Only 3% of the dorsal scapular artery passed through the brachial plexus if its origin was the transverse cervical artery\" vs \"100% and 75%\" for second/third-part origins.",
    "Variations matter for \"supraclavicular brachial plexus block and head and neck reconstruction with pedicled or free flaps.\"",
    "Original series with prevalence; good for scapular anastomosis lecture.")

add("topo_variation", "Axillary artery branching variations: common trunks of circumflex/subscapular/profunda arteries (423 limbs)", "PMC7664784", [
    ("BJBMS-20-502-g001.jpg", "schematic",
     "Diagram of the usual (textbook) branching of the axillary artery with Latin labels.",
     ["a. subclavia", "a. thoracoacromialis", "a. thoracica superior", "a. thoracica lateralis", "a. circumflexa humeri anterior", "a. circumflexa humeri posterior", "a. subscapularis", "a. circumflexa scapulae", "a. thoraco dorsalis", "a. brachialis"]),
    ("BJBMS-20-502-g008.jpg", "human cadaver",
     "Truncus profundocircumflexus: posterior circumflex humeral artery and profunda brachii arising by a common trunk from the axillary artery below the fused teres major/latissimus tendons.",
     ["superior", "lateral", "ACHA", "MCB", "NM", "AA", "FT", "ACHP", "TPC", "APB"]),
    ("BJBMS-20-502-g010.jpg", "human cadaver (latex-injected)",
     "Arteria brachialis superficialis together with a truncus profundosubscapulocircumflexus (T) giving ACHP, ASS and APB.",
     ["AA", "ACHP", "T", "ABS", "ASS", "APB", "superior", "medial"]),
], "423 embalmed upper limbs (Central European). \"Truncus subscapulocircumflexus (22.9%), truncus profundocircumflexus (13.75%), and truncus bicircumflexus (13.95%).\" \"Arteria thoracodorsalis aberrans We found this unusually originating artery in 5.91% (25/423) of cases.\" Superficial brachial artery 9.5%.",
    "Prevalence data are needed for \"safe performance\" of catheterization and flap procedures and proposes a standard terminology.",
    "Fig 1 is an unattributed diagram (presumably authors'); Fig 2 of the paper is a reproduced terminology scheme (Rodríguez-Niedenführ) and was NOT taken. Figure 4 (file g010) also relevant to KOL (superficial brachial artery).")

add("topo_variation", "Ectopic insertion of pectoralis minor tendon over the coracoid (pectoralis minor variants)", "PMC6588231", [
    ("pone.0218715.g002.jpg", "human cadaver",
     "Right shoulder from superior: ectopic pectoralis minor tendon (*) crossing the coracoid and passing through the coracoacromial ligament towards the humerus.",
     ["A", "SSM", "H", "CAL", "CP", "PMM", "*"]),
    ("pone.0218715.g003.jpg", "human cadaver",
     "Coracoid insertion areas colour-marked in a shoulder with ectopic tendon (A, A') vs normal (B, B'), cranial and lateral views.",
     ["A", "A'", "B", "B'", "*", "colour-coded areas (red PMM, black CAL, blue CHL, violet CGL, green CB/SHB), yellow line"]),
], "45 shoulders dissected. \"The prevalence of PMM variations was 37.84%.\" \"Shoulders with variations showed a statistically significant smaller coracopectoral distance (p<0.001) and larger insertion areas (p<0.003)\".",
    "\"Especially in patients experiencing shoulder pain and stiffness in whom the commoner pathologies have been ruled out the possibility of ectopic PMT should be kept in mind\"; imaging is insufficiently sensitive.",
    "Fig 1 of this paper is 'Modified from Lee 2014' and was NOT taken. Fig 3 has no text labels (colour code only).")

add("topo_variation", "Posterior cord of brachial plexus and its branches: variations (axilla)", "PMC4392958", [
    ("ISRN.ANATOMY2013-501813.002.jpg", "human cadaver",
     "Infraclavicular plexus dissection: axillary nerve arising from the posterior division of the upper trunk and posterior cord lateral to the second part of the axillary artery; roots C5–T1, trunks, cords and terminal branches visible.",
     ["AN", "RN", "PC", "MCN", "AA", "LC", "MN", "UT", "MT", "LT", "C5", "C6", "C7", "T1", "1", "2", "3", "4", "5", "6", "8"]),
    ("ISRN.ANATOMY2013-501813.003.jpg", "human cadaver",
     "Thoracodorsal nerve arising from the axillary nerve.",
     ["AA", "AN", "TDN", "RN"]),
], "37 cadavers (74 upper extremities). Posterior cord formed without an upper trunk \"in 16.2%\"; \"Posterior cord of brachial plexus was present lateral to the second part of axillary artery in 18.9%\"; \"Axillary nerve was taking origin from posterior division of upper trunk in 10.8% upper extremities and thoracodorsal nerve arising from axillary nerve in 22.9% upper extremities.\"",
    "\"It is important to be aware of such variations while planning a surgery in the region of axilla as these nerves are more liable to be injured during surgical procedures.\"",
    "Images ~658 px wide, somewhat JPEG-soft; labels legible.")

add("topo_variation", "Accessory subscapular nerves (subscapularis innervation variants)", "PMC7601857", [
    ("medicina-56-00532-g001.jpg", "human cadaver",
     "Left axilla with pectoralis major removed and plexus everted: three subscapular nerves (U1, U2, L) to subscapularis highlighted in yellow from the posterior cord.",
     ["PC", "U1", "U2", "L", "SSC", "m", "cd", "cr", "l", "**"]),
], "31 cadaveric specimens. \"Accessory subscapular nerves were found in three cases (9.7%).\" All three were accessory upper subscapular nerves; \"No accessory lower subscapular nerves were found.\"",
    "\"Accessory nerves occur rather commonly and need to be considered during surgery, nerve blocks, and imaging procedures.\"",
    "Labels partly red on dark background; legible at 774 px.")

add("topo_variation", "Suprascapular notch types and ossified superior transverse scapular ligament (dry scapulae)", "PMC7656716", [
    ("12891_2020_3769_Fig1_HTML.jpg", "dry bone",
     "Six dry scapulae illustrating Rengachary types 1–6 of the suprascapular notch, from absent notch to completely ossified ligament with bony foramen, with an on-image key.",
     ["Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6", "Key (type descriptions)"]),
], "50 Ugandan dry scapulae. \"Superior transverse scapular ligament (STSL) was completely ossified in 8% of cases.\"",
    "SSN anatomy is \"vital in diagnosis, prevention, and assessment of suprascapular nerve entrapment syndrome\".",
    "Complements PMC4555201 (already in repo) with a full six-type photographic key.")

add("topo_variation", "Suprascapular artery arising from the axillary artery; dorsal scapular artery supplying supraspinatus (case)", "PMC12206475", [
    ("cureus-0017-00000085095-i02.jpg", "human cadaver",
     "Right root of neck/axilla: SSA arising from the first part of the axillary artery and passing between plexus trunk contributions; DSA, TCA and subclavian artery (3rd part) shown; dashed line = first rib.",
     ["Cephalad", "Caudad", "Lateral", "Medial", "DSA", "UT", "MT", "LT", "SSA", "AA", "TCA", "CCA", "SA (3rd part)"]),
    ("cureus-0017-00000085095-i03.jpg", "human cadaver",
     "Posterior scapular region with rhomboids reflected: dorsal scapular artery and suprascapular artery branches (scapular anastomosis territory).",
     ["Cephalad", "Caudad", "Medial", "Lateral", "LSM", "RMM and RmM (reflected)", "DSA", "SSA", "SSA branches to SSM"]),
], "Single 75-year-old male donor (case report). \"The SSA arose directly from the first part of the axillary artery instead of the thyrocervical trunk\"; the DSA \"provided branches to the supraspinatus muscle in addition to its normal blood supply to the rhomboid and levator scapulae muscles.\"",
    "\"Awareness and prior identification of variations such as those presented in this report can help avoid potential complications in surgical procedures.\"",
    "Case report, no prevalence. Very clear labelled photos; Fig 3 also usable to illustrate the scapular anastomosis vessels (state that the specimen is variant).")

# ---------------- C. kesit_lecture ----------------
add("kesit_lecture", "Brachial plexus MRI (roots, trunks, cords) with cadaver/plastinate correlation", "PMC8695258", [
    ("gr5.jpg", "MRI",
     "Right brachial plexus on coronal T2 DIXON fat-suppressed images, MPR of C8 root and MR neurography; numbered roots C5–Th1, trunks and cords.",
     ["a", "b", "c", "d", "1", "2", "3", "3a", "4", "5", "6", "7", "8", "9", "10"]),
    ("gr7.jpg", "MRI + plastinated specimen",
     "Cords and terminal nerves of left brachial plexus on MR neurography (a–d) correlated with a plastinated anterior dissection (e).",
     ["a", "b", "c", "d", "e", "1", "2", "3", "4", "5", "6", "7", "8", "8a", "8b", "9", "10", "11", "12", "13", "14", "15", "16"]),
    ("gr4.jpg", "MRI + human cadaver",
     "Roots and trunks of the normal plexus on MRI (a–c) and cadaver specimen anterolateral view (d).",
     ["a", "b", "c", "d", "1–15", "sup.", "inf.", "post.", "ant."]),
], "Review (Part 1) of BP MRI: anatomy, technique and non-traumatic lesions. \"Some nerves show a relatively high variation rate, like the long thoracic nerve or medial antebrachial cutaneous nerve\".",
    "\"MRI allows narrowing the list of differential diagnoses of brachial plexus lesions\" and distinguishes neoplastic infiltration from radiation neuropathy on T2-weighted images.",
    "Images are ~730 px wide with small multi-panel frames (gr4, gr7 especially small: 739x302 / 739x287) — usable at half-slide width; gr5 is best. Numbered labels only; legend from caption.")

add("kesit_lecture", "Glenohumeral ligaments on MR/CT arthrography (normal anatomy)", "PMC6251069", [
    ("jbsr-101-2-1467-g16.jpg", "schematic + MRI arthrography",
     "(A) Drawing of anterior glenohumeral ligaments (SGHL, MGHL, IGHL, spiral GHL); (B) sagittal MR arthrogram showing the ligaments (arrows).",
     ["A", "B", "coracoid", "SGHL", "MGHL", "spiral GHL", "IGHL", "humerus", "scapula", "arrows"]),
    ("jbsr-101-2-1467-g22.jpg", "MRI arthrography",
     "Inferior glenohumeral ligament and axillary recess on coronal oblique (A) and axial (B) fat-sat T1 MR arthrograms.",
     ["A", "B", "arrows (white/black)"]),
], "Review of shoulder anatomy and normal variants on radiography, MRI, MR/CT arthrography. Labrum \"may appear thickened and cordlike ... as in the Buford complex ... or completely absent in 30% of healthy subjects\" (MGHL).",
    "Normal variants must be recognised to avoid misdiagnosis as pathology (labral tear, fracture, osteophyte).",
    "Arrow-based labels; anatomical names only on schematic (A of g16). Same article used in kesit_variation.")

add("kesit_lecture", "Rotator cuff ultrasound: supraspinatus/infraspinatus longitudinal view with labelled line drawing", "PMC3097811", [
    ("biij-02-e58-g13.jpg", "US",
     "Frozen US image of the supraspinatus (anterior) and infraspinatus (posterior) tendons over the humeral head.",
     ["LT COR ANT", "POST", "depth scale"]),
    ("biij-02-e58-g14.jpg", "schematic",
     "Labelled line drawing matching the US image: BT, SST, IST over the humeral head.",
     ["ANTERIOR", "POSTERIOR", "BT", "SST", "IST", "HUMERAL HEAD"]),
], "Technical pictorial (no study population): standard technique for imaging SUBSCAP, BT, SST, IST and ACJ; \"Frozen US images with labelled line drawings are given to explain the structures seen.\"",
    "Standardised technique for learning normal appearance \"will later assist in the recognition of pathology.\"",
    "LOW RESOLUTION: US image 450x314 (below ideal); drawing 628x437. Use only if nothing better; licence CC BY 2.5.")

add("kesit_lecture", "Brachial plexus trunks in the interscalene groove on ultrasound (normal)", "PMC5617940", [
    ("diagnostics-07-00040-g003.jpg", "US",
     "Transverse US of the interscalene region, unlabeled (A) and labelled (B): ST, MT, IT between anterior and middle scalene, SCM superficial.",
     ["A", "B", "MS", "ST", "MT", "IT", "AS", "SCM"]),
], "Ultrasound screening of 22 subjects (see kesit_variation entry).",
    "Ultrasound visualises the trunks and their fascial separation from the anterior scalene.",
    "Width 713 px, two panels (each ~350 px) — small but legible.")

# ---------------- D. kesit_variation ----------------
add("kesit_variation", "Normal variants on imaging: os acromiale (CT) and anterosuperior labral variants incl. Buford complex (MR arthrography)", "PMC6251069", [
    ("jbsr-101-2-1467-g9.jpg", "CT (arthrography)",
     "Axial CT arthrogram through the AC joint: os acromiale (arrow) with synchondrosis (arrowhead).",
     ["arrow", "arrowhead"]),
    ("jbsr-101-2-1467-g12.jpg", "schematic",
     "Lateral view of the glenoid: (a) normal capsulolabral complex; (b) sublabral recess; (c) sublabral foramen; (d) Buford complex.",
     ["a", "b", "c", "d", "LHBT", "SGHL", "MGHL", "ant IGHL", "post IGHL", "11", "1", "3"]),
    ("jbsr-101-2-1467-g15.jpg", "MRI arthrography",
     "Buford complex: cord-like MGHL (white arrow) with absent anterosuperior labrum (black arrow) on axial and sagittal MR arthrograms.",
     ["A", "B", "white arrow", "black arrow", "arrowhead"]),
], "\"The incidence of this variant [os acromiale] can reach up to 15% of the population\"; the anterosuperior labrum/MGHL may be cord-like as in the Buford complex.",
    "\"An os acromiale should not be confused with a fracture fragment and the synchondrosis with a pseudarthrosis\"; Buford complex mimics a labral tear.",
    "Review article without original prevalence. Fig 15 caption ends '(Courtesy of Dr Henri Guerini)' — published under the article's CC BY, but flag third-party image origin; prefer g12 + g9 if in doubt. Fig 14 (sublabral foramen) is also 'Courtesy of' and was not taken.")

add("kesit_variation", "Os acromiale prevalence on MRI (3697 shoulder MRIs) and coexistence with rotator cuff tears", "PMC13051579", [
    ("aott-60-1-25714_f001.jpg", "MRI",
     "Os acromiale on T2 axial (A) and T1 sagittal oblique (B): unfused ossification centre producing a 'double AC joint' appearance (arrow).",
     ["A", "B", "white arrows"]),
], "3697 shoulder MRIs. \"Os acromiale was identified in 26 cases, corresponding to a prevalence of 0.7%. Only 11 cases were mentioned in the original radiology reports.\" \"Subtypes included 12 preacromion, 13 mesoacromion, and 1 metaacromion.\" Rotator cuff tears in \"20 of 26 patients with os acromiale (77%)\".",
    "Focused evaluation \"documented more cases than routine radiology reports, underscoring the added value of targeted assessment.\"",
    "LICENCE CC BY-NC (flag). Panel A is very dark; panel B is the useful one.")

add("kesit_variation", "Os acromiale in a general population MRI cohort (SHIP, 3050 participants) — type scheme", "PMC9166870", [
    ("264_2022_5406_Fig1_HTML.jpg", "schematic",
     "Outline scheme of the acromion ossification centres: pre-, meso-, meta- and basi-acromion.",
     ["Pre", "Meso", "Meta", "Basi"]),
], "\"In total, 1.9% (58/3050) had an os acromiale, while 21 were unilateral left, 23 were unilateral right, and 14 were bilateral. Sixty-eight meso-acromions, three pre-acromions, and one meta-acromion were detected.\" More frequent in men.",
    "\"it is important to be aware of possible os acromiale before surgery\"; prevalence lower than worldwide range \"(1.9 to 7%)\", supporting a genetic aetiology.",
    "CC BY. Article has no MR image figure (only scheme + flowchart); pair the scheme with PMC13051579 or PMC6251069 images.")

add("kesit_variation", "Suprascapular notch types on 3D-volume-rendered MDCT (311 patients, 622 scapulae)", "PMC4044447", [
    ("BMRI2014-196896.002.jpg", "CT (3D VR) + schematic",
     "Types I–III of the suprascapular notch on 3D VR MDCT with matching schematic of maximal depth (MD) vs superior transverse diameter (STD).",
     ["Type I", "Type II", "Type III", "(a)", "(b)", "(c)", "STD", "MD", "MD > STD", "MD = STD", "MD < STD"]),
    ("BMRI2014-196896.003.jpg", "CT (3D VR)",
     "Type IV (bony foramen) and type V (discrete notch) on 3D VR MDCT.",
     ["Type IV", "Type V", "(a)", "(b)"]),
], "311 patients / 622 CT scapulae. \"Suprascapular notch was recognized as a symmetrical feature in 53.45% of the patients.\" Symmetric type III \"(111/166, 66.9%)\", type I \"15.6% (26/166)\", type IV \"5 of the 166 patients (3.0%)\", type V \"13.9%\".",
    "\"The most important risk factor of suprascapular nerve entrapment is probably the shape of the suprascapular notch\"; bilateral symmetry cannot be assumed.",
    "Uses Polguj 5-type classification (not Rengachary).")

add("kesit_variation", "Anterosuperior labral variants (sublabral recess, sublabral foramen, Buford complex): meta-analysis", "PMC10491707", [
    ("402_2023_4932_Fig1_HTML.jpg", "schematic",
     "Three drawings of the glenoid showing (A) sublabral recess, (B) sublabral foramen, (C) Buford complex with cord-like MGHL.",
     ["A", "B", "C", "LHBBM", "GL", "SSM", "CLMGHL"]),
], "20 studies, 7601 upper limbs. Pooled prevalence: sublabral recess \"57.2% (95% CI 30.0–84.4%)\", sublabral foramen \"13.5% (95% CI 8.2–18.9%)\", Buford complex \"3.0% (95% CI 1.5–4.5)\"; \"individuals with Buford complex have RR 2.4 (95% CI 1.3–4.7) of developing SLAP lesions\".",
    "Differentiating these variants from pathology avoids unnecessary iatrogenic complications; Buford complex \"may be a predisposing factor for sustaining a SLAP lesion.\"",
    "Schematic only 669x193 (three panels ~220 px each) — small; usable as a strip. Pooled data mix arthroscopy, MRI and cadaver studies.")

add("kesit_variation", "Brachial plexus piercing variants of the anterior scalene on ultrasound (and cadaver prevalence)", "PMC5617940", [
    ("diagnostics-07-00040-g004.jpg", "US",
     "Superior piercing variant on US, unlabeled (A) and labelled (B): superior trunk not separated from the anterior scalene.",
     ["A", "B", "MS", "AS", "ST", "MT", "IT", "SCM"]),
], "Cadaver part: 82 necks, \"In 62.1%, C5, superior trunk, or superior + middle trunks pierced the anterior scalene.\" US screening of 22 subjects (44 plexuses): \"Eight of these were classified as piercing variants ... (18.2%)\"; superior piercing \"n = 4; 9.1%\", multiple piercing \"n = 3; 6.8%\", C5 piercing \"n = 1; 2.3%\". nTOS symptoms in 50% of piercing variants vs 13.9% of normal plexuses.",
    "\"The addition of ultrasonography to nTOS diagnosis, especially for patients with BP branching variation, would allow clinicians to visualize and identify atypical patient anatomy.\"",
    "Two-panel US image 716 px wide; labels small but legible. Fig 2 (cadaver variants A–C) is also in the bucket if a topo slide is wanted.")


out = []
for e in E:
    m = meta(e["pmcid"])
    figs = []
    for f, spec, what, labels in e["figures"]:
        p = RAW / e["pmcid"] / f
        lab, cap = m["figs"].get(f.rsplit(".", 1)[0], m["figs"].get(f, ("", "")))
        figs.append(dict(file=f, label=lab, caption=cap, specimen=spec, what_it_shows=what,
                         labels_visible_in_image=labels, pixels=jpeg_size(p),
                         local_path=str(p.relative_to(ROOT))))
    out.append(dict(use=e["use"], topic=e["topic"], pmcid=e["pmcid"], version=m["version"], doi=m["doi"],
                    citation=m["citation"], title=m["title"], authors=m["authors"], year=m["year"],
                    journal=m["journal"], license_code=m["license_code"], figures=figs,
                    key_findings=e["key_findings"], clinical_relevance=e["clinical_relevance"], notes=e["notes"]))

dst = ROOT / "sources/bolge_omuz.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(dst, len(out), "entries")
for o in out:
    for f in o["figures"]:
        if not f["caption"]:
            print("MISSING CAPTION", o["pmcid"], f["file"])
