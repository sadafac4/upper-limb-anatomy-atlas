#!/usr/bin/env python3
"""Build sources/topografik_kaynaklar.json from the files downloaded by pmc_oa_fetch.py.

Bibliographic fields, licence, captions, image size and md5 checks are read from the
downloaded bucket .json/.xml/.jpg files; only topic assignment, specimen type,
what_it_shows, key_findings and notes are written by hand below (from the captions/text).
Run: python3 -I scripts/build_topografik_sources.py
"""
import glob, hashlib, json, os, pathlib, re, xml.etree.ElementTree as ET
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "topografik/images/raw"
XL = "{http://www.w3.org/1999/xlink}href"

# (topic_no, topic, pmcid, {file: (specimen, what_it_shows)}, key_findings, notes)
SPEC = [
 (1, "Brachial plexus / axilla (infraclavicular part) dissection", "PMC12578619", {
   "BMRI-2025-6650184-g012.jpg": ("diagram", "Schematic of the normal infraclavicular brachial plexus: trunks, divisions, lateral/medial/posterior cords and their terminal branches (MCN, MN, UN, RN, AN, TDN, subscapular and pectoral nerves)."),
   "BMRI-2025-6650184-g001.jpg": ("human cadaver", "Two right-axilla dissections of the posterior cord: (A) trifurcation into radial, axillary and thoracodorsal nerves; (B) quadfurcation with the axillary nerve's anterior/posterior divisions."),
   "BMRI-2025-6650184-g011.jpg": ("human cadaver", "Right-axilla dissections of median nerve formation: (A) an accessory lateral root between main and aberrant axillary arteries; (B) low fusion of the roots with a medial cord–lateral root communicating branch."),
  },
  "36 upper limbs from 18 donors were dissected following Grant's Dissector. \"Variations were found in 16 brachial plexuses (44.4%) from nine donors. In total, 32 variations were identified\"; \"Bilateral variations were more common (77.8%) than unilateral ones (22.2%)\". The authors note that the reported prevalence of brachial plexus variability \"has been reported to range from 13.3% to 90%\".",
  "Fig. 1 (schematic) is the clean normal-anatomy reference; Figs. 2 and 12 are numbered real axillary dissections (normal axillary region topography with variant branching). NB: file numbering is reversed relative to figure labels (g012 = Figure 1, g001 = Figure 12)."),
 (2, "Cubital fossa (fossa cubitalis) dissection", "PMC10823296", {
   "cureus-0015-00000051350-i06.jpg": ("human cadaver", "Left elbow region with labelled biceps brachii, bicipital aponeurosis, brachioradialis, pronator teres, brachial/radial/ulnar arteries, median and ulnar nerves (high brachial bifurcation)."),
   "cureus-0015-00000051350-i05.jpg": ("human cadaver", "Right elbow region showing the level of brachial artery bifurcation, radial and ulnar arteries, median and ulnar nerves, pronator teres and biceps brachii."),
  },
  "Bilateral case in which median nerve and brachial artery were absent from the cubital fossa: \"pronator teres originating from the distal third of the humerus, associated with the bifurcation of the brachial artery at the middle third of the humerus into the ulnar and radial arteries. The median nerve ran beneath the pronator teres along with the ulnar artery\". Cited literature: \"an incidence of high divisions in the brachial artery ranging between 5% and 14% of the cadavers\".",
  "No CC BY cadaver photo of a NORMAL cubital fossa was found in the PMC OA bucket; this is a variant specimen, but the photos are labelled in plain English and show the cubital-fossa boundaries/contents (bicipital aponeurosis, pronator teres, brachioradialis). Use with a 'variation' caption, or as a contrast to a normal diagram. Also relevant to topic 7 (high division of brachial artery)."),
 (3, "Carpal tunnel / palm: thenar (recurrent) branch of median nerve", "PMC6834099", {
   "cureus-0011-00000005859-i01.jpg": ("human cadaver", "Opened carpal tunnel with transverse carpal ligament (TCL) and median nerve; two motor thenar branches (arrowheads, dotted course) arise from the lateral division of the median nerve distal to the TCL."),
   "cureus-0011-00000005859-i02.jpg": ("human cadaver", "Further palmar dissection showing the five terminal muscular branches of the double motor thenar branches entering the thenar muscles."),
  },
  "Case of double muscular thenar branches arising from the first common palmar digital nerve with five terminal muscular branches. The discussion notes that for the motor thenar branch \"typical anatomy is reported in less than 75% of cases studied in the literature\".",
  "Clear, well-lit photographs; labelling is minimal (MN, TCL, arrows/asterisks) so Turkish labels can be added."),
 (3, "Carpal tunnel / palm: recurrent branch and safe zone at the flexor retinaculum", "PMC3931286", {
   "1754-9493-8-8-1.jpg": ("human cadaver", "Palmar dissection with skin flap reflected, showing an intraligamentous recurrent branch of the median nerve (pointer)."),
   "1754-9493-8-8-2.jpg": ("human cadaver", "Palmar dissection showing multiple extraligamentous recurrent branches of the median nerve (pointer)."),
  },
  "Study of 26 hands from thirteen Sri Lankan cadavers: \"In a majority of specimens the recurrent branch was a single trunk (n =20, 76.9%). Similarly 84.6% (n = 22) were extra ligamentous in location. Mean distance from the distal border of the TCL to the recurrent branch was 7.75 mm. Mean distance from the distal border of TCL to the superficial palmar arch was 11.48 mm.\"",
  "Secondary source for topic 3. Photos are unlabelled except for a probe/pointer; orientation is less clear than PMC6834099. Figure 4 of this article was NOT downloaded: it is a photograph of a textbook-style drawing (third-party artwork, provenance unclear)."),
 (4, "Shoulder / scapular region: quadrangular space (spatium axillare laterale)", "PMC8958867", {
   "cureus-0014-00000022619-i03.jpg": ("human cadaver", "Anterior (deltopectoral) approach: quadrangular space with axillary nerve (AXN) and posterior humeral circumflex artery (PHCA) on forceps; deltoid, conjoint tendon, cephalic vein and pectoralis major labelled."),
   "cureus-0014-00000022619-i04.jpg": ("human cadaver", "Posterior approach: quadrangular space bounded by teres minor, teres major, long head of triceps and humerus, with AXN and PHCA passing through it."),
  },
  "Eight upper limbs from four cadavers were dissected by anatomy and orthopaedic residents using anterior and posterior approaches. \"the posterior approach was recognized as the easier and quicker method ... however, it may result in increased postoperative morbidity. Although the anterior (deltopectoral) approach involves more skill, it reduces postoperative morbidity.\"",
  "Figure 4 is an excellent teaching image of the posterior boundaries of the quadrangular space (English text-box labels). Figures 1 (authors' drawing) and 2 (third-party AO Surgery Reference image) were deliberately NOT downloaded."),
 (4, "Shoulder / scapular region: suprascapular notch", "PMC4555201", {
   "167_2014_2937_Fig2_HTML.jpg": ("human cadaver + diagram", "Type I arrangement at the suprascapular notch: (a) cadaver photo with suprascapular artery above and vein/nerve below the superior transverse scapular ligament; (b) matching schematic."),
  },
  "106 formalin-fixed cadaveric shoulders: \"type I (61.3 %) (suprascapular artery was running above ligament, while suprascapular vein and nerve below it), type II (17 %) (both vessels pass above ligament, while nerve passes under it), type III (12.3 %) (suprascapular vessels and nerve lie under ligament) and type IV (9.4 %)\". \"Anterior coracoscapular ligaments were present in 55 from 106 shoulders.\"",
  "Photo panel is dark (close-up with 1 mm scale bar, numeric labels); the paired schematic (panel b) is very clear and could be used alone for the slide."),
 (5, "Forearm: radial nerve bifurcation, posterior interosseous nerve and arcade of Frohse / supinator", "PMC12500735", {
   "276_2025_3728_Fig4_HTML.jpg": ("human cadaver", "Radial nerve dividing at the radiocapitellar joint (needle) into the superficial radial nerve (star) and posterior interosseous nerve (square), with the branch to ECRB (circle)."),
   "276_2025_3728_Fig6_HTML.jpg": ("human cadaver", "Supinator elevated to show the posterior interosseous nerve running between the superficial and deep heads of the supinator, near the radial tuberosity and biceps tendon."),
   "276_2025_3728_Fig1_HTML.jpg": ("human cadaver", "Anterolateral elbow/forearm dissection marking the posterior interosseous nerve (square), distal biceps tendon (circle) and supinator (star)."),
  },
  "29 fresh cadaveric upper extremities: \"The radial nerve bifurcated approximately 5 ± 3 mm proximal to the RCJ. The PIN entered the supinator (Arcade of Frohse) at 22 ± 1 mm distal to the RCJ. It was located a mean of 13 ± 2 mm from the radial border of the radial tuberosity in pronation and 19 ± 2 mm in supination.\"",
  "Fresh (unembalmed, colourful) specimens on blue background, symbol labels plus directional arrows; good for adding Turkish labels."),
 (6, "Variation: axillary arch muscle (Langer's arch)", "PMC12206543", {
   "cureus-0017-00000085096-i01.jpg": ("human cadaver", "Right axilla: axillary arch from the latissimus dorsi crossing anterior to the axillary neurovascular bundle to the short head of biceps, with slips to coracobrachialis and deltoid."),
   "cureus-0017-00000085096-i02.jpg": ("human cadaver", "Left axilla: a single thin axillary arch slip from latissimus dorsi inserting into the fascia between coracobrachialis and deltoid."),
  },
  "Bilateral axillary arch in one cadaver: \"On the right side, the muscle originated from the latissimus dorsi and merged with the short head of the biceps brachii, deltoid, and coracobrachialis muscles. On the left, it originated from the latissimus dorsi but was inserted into the fascia between the coracobrachialis and deltoid muscles.\" The article gives no prevalence figure of its own (only that frequency \"varies depending on the diverse groups of populations\").",
  "High-quality, clearly labelled photos with orientation compass."),
 (7, "Variation: superficial brachial artery / brachial artery trifurcation", "PMC10599095", {
   "cureus-0015-00000045903-i01.jpg": ("human cadaver (digitally coloured)", "Right arm: axillary artery continuing below the latissimus dorsi tendon and trifurcating into a superficial brachial artery, the main brachial artery and a common trunk; median nerve with two lateral roots."),
   "cureus-0015-00000045903-i02.jpg": ("human cadaver (digitally coloured)", "Course and termination of the superficial brachial artery (ending as radial artery) and the main brachial artery (ending as ulnar artery) at the elbow."),
  },
  "Findings in one formalin-embalmed donor included \"a BA bilateral trifurcation, below the tendon of the latissimus dorsi muscle\" and \"the coexistence of an SBA with the main BA\". Discussion: \"The SBA has a prevalence ranging from 1.07% to 19.7%\" and \"De Garis and Swartley supported that the SBA is more frequent in African Americans (13.4%) than in Caucasians (4.6%)\".",
  "Arteries painted red and nerves yellow on the photograph (digital colouring), abbreviation labels."),
 (8, "Variation: absent musculocutaneous nerve (median nerve supplies arm flexors)", "PMC11026042", {
   "1806-9460-spmj-126-05-288-gf1.jpg": ("human cadaver", "Lateral view of the right axilla: the lateral cord continues as the lateral root of the median nerve without giving off a musculocutaneous nerve (numbered legend)."),
   "1806-9460-spmj-126-05-288-gf2.jpg": ("human cadaver", "Anterior right arm: branches from the lateral margin of the median nerve to biceps brachii and brachialis (numbered legend)."),
  },
  "Right arm of a male cadaver with no musculocutaneous nerve; the median nerve gave branches to coracobrachialis, biceps brachii and brachialis, the last continuing as the lateral antebrachial cutaneous nerve. Cited prevalence: \"Beheiry dissected 60 arms and noted absence of the nerve in only one of them (1.7%). Prasada Rao and Chaudhary did not find this nerve in 8% of the 24 arms they dissected.\"",
  "Sao Paulo Med J 2008 article deposited to PMC in 2024 (PMC11026042) under CC BY 4.0 per bucket metadata. Numbered arrow labels; clean, sharp photos."),
 (9, "Variation: third (accessory) head of biceps brachii", "PMC5752815", {
   "IJABMR-7-266-g001.jpg": ("human cadaver", "Right arm: third head of biceps (THB) and the musculocutaneous nerve dividing into anterior and posterior branches; biceps, coracobrachialis, median nerve and brachial artery labelled."),
   "IJABMR-7-266-g002.jpg": ("human cadaver", "Left arm: third head of biceps with the musculocutaneous nerve piercing coracobrachialis; bicipital aponeurosis, median nerve and brachial artery labelled."),
  },
  "Bilateral three-headed biceps brachii: \"The third-headed biceps brachii emerged from the deep investing fascia of the brachialis muscle on both the sides. The musculocutaneous nerve (MCN) did not pierce the coracobrachialis muscle on the right side\". The article states that \"the three-headed biceps brachii is described to be the most common variation\" but gives no prevalence number.",
  "LICENCE FLAG: CC BY-NC-SA 3.0 (non-commercial, share-alike; derivative slides must carry the same licence). No CC BY alternative with a cadaver photo was found in the OA bucket. Small images (~539 px wide); labels legible but small."),
 (10, "Variation: persistent median artery with bifid median nerve (and reversed palmaris longus)", "PMC10343151", {
   "cureus-0015-00000040324-i01.jpg": ("human cadaver", "Left forearm and hand: persistent median artery, bifid median nerve (radial and medial branches) and reversed palmaris longus, with the palmar arches."),
   "cureus-0015-00000040324-i02.jpg": ("human cadaver", "Left forearm and hand showing the origin of the persistent median artery from the radial artery and its course to the superficial palmar arch; flexor retinaculum cut."),
  },
  "Male cadaver with \"a persistent median artery, reversed palmaris longus muscle, and bifid median nerve\"; the PMA \"branched off the radial artery, anastomosing with the ulnar artery to give rise to the SPA\". Cited data: \"PMA was identified in five of the 125 upper limbs (4% of the total number of limbs)\" and in an Australian sample \"a total of 26 median arteries were discovered, with a prevalence rate of 33.3%\".",
  "Wide panoramic images (750 px wide, ~290 px tall): labels small; crop to the wrist region for slides. Also illustrates topic 12 (reversed palmaris longus)."),
 (11, "Variation: Martin-Gruber anastomosis", "PMC11867591", {
   "cureus-0017-00000078139-i01.jpg": ("human cadaver", "Forearm dissection showing a type I Martin-Gruber anastomosis between median and ulnar nerves over flexor digitorum profundus; medial epicondyle for orientation."),
   "cureus-0017-00000078139-i04.jpg": ("diagram", "BioRender diagram of the three MGA pattern types relative to FDP."),
  },
  "101 cadaveric forearms: \"The Martin-Gruber anastomosis prevalence found within the study was 37.6% (n = 38/101), with type I being the most common at 58% (n = 22/38), followed by type III at 32% (n = 12/38), and type II at 11% (n = 4/38).\" \"most patterns were intramuscularly embedded in the flexor digitorum profundus (FDP) muscle.\"",
  "Photo is labelled in colour (UN, MN, FDP, ME, 'Anastomosis'). Diagram created by an author in BioRender and published under the article's CC BY licence."),
 (12, "Variation: reversed palmaris longus (bilateral)", "PMC7033050", {
   "276_2019_2363_Fig1_HTML.jpg": ("human cadaver", "Right (a) and left (b) anterior forearm compartments with reversed palmaris longus: proximal tendon and distal muscle belly; FDS, FCR, BR, PT and radial artery labelled."),
  },
  "90-year-old male cadaver with bilateral reversed palmaris longus plus systematic review: \"The average length of the muscle belly and tendon of reversed palmaris longus was 135 mm and 126 mm, respectively\"; \"bilateral reversed palmaris longus has only been reported in males\"; \"A high proportion (70.8%) of reversed palmaris longus were discovered in the right upper limb\". Text notes PL \"complete agenesis, which is prevalent in 20.25% of the global population\".",
  "Clean whole-forearm photos; abbreviation labels are small."),
 (13, "Variation: accessory head of flexor pollicis longus (Gantzer's muscle)", "PMC4636409", {
   "peerj-03-1255-g001.jpg": ("human cadaver", "Anterior forearm with the accessory head of flexor pollicis longus (AHFPL) arising from flexor digitorum profundus and joining FPL; FCR labelled."),
  },
  "Meta-analysis of 24 cadaveric studies (n = 2,358 upper limbs): \"The pooled prevalence of an AHFPL was 44.2%\"; it \"inserted into the flexor pollicis longus muscle (94.6%...)\" and \"was innervated by the AIN (97.3%...)\".",
  "Single high-contrast photo on black background with large white labels; very suitable for slides."),
 (13, "Variation: ligament of Struthers / supracondylar process", "PMC5608727", {
   "1413-7852-aob-25-04-00137-gf1.jpg": ("human cadaver", "Right and left arms with high insertion of pronator teres and a cord-shaped Struthers' ligament related to the median nerve and brachial artery."),
   "1413-7852-aob-25-04-00137-gf4.jpg": ("human cadaver", "Two cases of a laminar Struthers' ligament from the medial epicondyle passing over the median nerve and brachial artery (fresh and fixed cadaver)."),
  },
  "60 arms from 30 cadavers: \"The supracondylar humeral process was not found in any of the 60 dissected arms. Struthers' ligament was identified in six arms (two bilateral); in all cases high insertion of the pronator teres muscle was observed.\"",
  "LICENCE FLAG: CC BY-NC 4.0 (non-commercial). Small images (~390 x 480 px), letter labels (a-d)."),
 (14, "Variation: axillary artery course and branching", "PMC10363335", {
   "cureus-0015-00000040852-i01.jpg": ("human cadaver (painted vessels/nerves)", "Left axilla: axillary artery with anteromedial course relative to the brachial plexus and variant branches (common trunks CT1/CT2, accessory branches) with insets."),
   "cureus-0015-00000040852-i02.jpg": ("diagram", "Schematic of the same axillary artery branching variations and brachial plexus relations."),
  },
  "88-year-old male donor with unilateral left axillary artery variation: \"an abnormal anteromedial course with respect to the divisions and cords of the brachial plexus\"; \"A total of four branches arose from the second part of the artery\" and \"No branches arose from the third part of the artery.\" Cited: \"an aberrant positional relationship between the AA and the brachial plexus in 2.0% of cases\".",
  "Excellent, fully labelled photo + matching schematic; nerves painted yellow and arteries red on the specimen."),
]


def text(el):
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


def build():
    out = []
    for topic_no, topic, pmcid, figs, findings, notes in SPEC:
        d = RAW / pmcid
        jpath = next(d.glob(f"{pmcid}.*.json")); xpath = next(d.glob(f"{pmcid}.*.xml"))
        j = json.loads(jpath.read_text()); r = ET.parse(xpath).getroot()
        meta = r.find(".//article-meta")
        auth = [f"{text(c.find('name/surname'))} {text(c.find('name/given-names'))}".strip()
                for c in meta.findall(".//contrib[@contrib-type='author']") if c.find("name") is not None]
        authors = ", ".join(auth[:3]) + (" et al." if len(auth) > 3 else "")
        years = [p.findtext("year") for p in meta.iter("pub-date") if p.findtext("year")]
        lic = meta.find(".//license")
        lic_url = lic.get(XL) if lic is not None else None
        if lic is not None and not lic_url:  # Cureus/Elsevier style: <ali:license_ref> or <ext-link> inside <license-p>
            refs = [text(e) for e in lic.iter() if e.tag.endswith("license_ref")] + [e.get(XL) for e in lic.iter("ext-link")]
            lic_url = next((u for u in refs if u), None)
        md5 = {re.sub(r"\?.*", "", u).split("/")[-1]: u.split("md5=")[-1] for u in j.get("media_urls", [])}
        fig_by_graphic = {}
        for f in r.iter("fig"):
            for g in f.iter("graphic"):
                fig_by_graphic[g.get(XL)] = f
        flist, res = [], []
        for fn, (specimen, what) in figs.items():
            p = d / fn
            f = fig_by_graphic.get(fn)
            if f is None:
                f = fig_by_graphic.get(fn.rsplit(".", 1)[0])
            assert f is not None, (pmcid, fn)
            assert hashlib.md5(p.read_bytes()).hexdigest() == md5[fn], (pmcid, fn, "md5 mismatch")
            w, h = Image.open(p).size
            res.append(f"{text(f.find('label'))}: {w}x{h} px")
            flist.append({"file": fn, "label": text(f.find("label")), "caption": text(f.find("caption")),
                          "specimen": specimen, "what_it_shows": what,
                          "local_path": str(p.relative_to(ROOT)), "pixels": f"{w}x{h}"})
        out.append({
            "topic_no": topic_no, "topic": topic, "pmcid": pmcid, "version": j["version"], "doi": j["doi"],
            "citation": j["citation"], "title": text(meta.find(".//article-title")), "authors": authors,
            "year": min(years) if years else None, "journal": text(r.find(".//journal-title")),
            "license_code": j["license_code"],
            "license_url_or_text": (lic_url + " | " if lic_url else "") + text(lic.find("license-p") if lic is not None else None),
            "figures": flist, "key_findings": findings,
            "notes": notes + " Resolution (as served by PMC OA bucket; no larger version available there): " + "; ".join(res) + ". md5 of each image verified against bucket JSON media_urls.",
        })
    dst = ROOT / "sources/topografik_kaynaklar.json"
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(dst, len(out), "articles")


if __name__ == "__main__":
    build()
