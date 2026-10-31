# OMUZ bölgesi – arama günlüğü (search log)

Date: 2026-10-31. Discovery via WebSearch (server-side); verification only through the AWS PMC OA bucket
(`https://pmc-oa-opendata.s3.amazonaws.com/`) using `scripts/pmc_oa_fetch.py info|get`.
Licence = `license_code` from bucket JSON. Curated output: `sources/bolge_omuz.json` (built by `scripts/build_bolge_omuz.py`).
Every kept figure was opened and inspected visually; full text (`.txt` from the bucket) was read for the quoted numbers.

## Searches run (WebSearch)
1. `site:pmc.ncbi.nlm.nih.gov cadaver dissection rotator cuff suprascapular nerve spinoglenoid notch figure`
2. `site:pmc.ncbi.nlm.nih.gov triangular interval triangular space radial nerve cadaveric study shoulder`
3. `Insights into Imaging shoulder MRI anatomy rotator cuff labelled review`
4. `site:pmc.ncbi.nlm.nih.gov os acromiale prevalence MRI CT study`
5. `site:pmc.ncbi.nlm.nih.gov brachial plexus MRI anatomy review normal anatomy labelled`
6. `site:pmc.ncbi.nlm.nih.gov Buford complex sublabral foramen prevalence MR arthrography`
7. `site:pmc.ncbi.nlm.nih.gov long thoracic nerve cadaveric study course variations serratus anterior`
8. `site:pmc.ncbi.nlm.nih.gov brachial plexus formation variations prefixed postfixed cadaveric study prevalence`
9. `site:pmc.ncbi.nlm.nih.gov pectoralis minor variations cadaveric study prevalence accessory pectoral muscle`
10. `site:pmc.ncbi.nlm.nih.gov shoulder ultrasound normal anatomy rotator cuff tendons labelled images`
11. `site:pmc.ncbi.nlm.nih.gov suprascapular notch types computed tomography 3D prevalence Rengachary`
12. `site:pmc.ncbi.nlm.nih.gov axillary nerve quadrilateral space cadaver dissection posterior shoulder deltoid figure`
13. `site:pmc.ncbi.nlm.nih.gov glenohumeral joint capsule labrum cadaveric dissection anatomy glenohumeral ligaments figure`
14. `site:pmc.ncbi.nlm.nih.gov cephalic vein deltopectoral groove cadaveric study variations`
15. `site:pmc.ncbi.nlm.nih.gov acromion morphology Bigliani type prevalence MRI rotator cuff tear`
16. `site:pmc.ncbi.nlm.nih.gov shoulder MRI normal anatomy axial coronal sagittal labelled pictorial`
17. `site:pmc.ncbi.nlm.nih.gov axillary arch muscle MRI CT prevalence imaging study`
18. `site:pmc.ncbi.nlm.nih.gov subscapular artery circumflex humeral artery variations cadaveric study`
19. `site:pmc.ncbi.nlm.nih.gov supraclavicular brachial plexus roots trunks cadaveric dissection posterior triangle figure scalene`
20. `site:pmc.ncbi.nlm.nih.gov axillary nerve deltoid anterior branch posterior branch cadaver study distance acromion`
21. `site:pmc.ncbi.nlm.nih.gov scapular anastomosis cadaveric dorsal scapular artery suprascapular artery`
22. `site:pmc.ncbi.nlm.nih.gov brachial plexus variations systematic review meta-analysis prevalence cadaveric`
23. `site:pmc.ncbi.nlm.nih.gov long thoracic nerve anatomy cadaver dissection serratus anterior ...`
24. `site:pmc.ncbi.nlm.nih.gov clavipectoral fascia OR thoracoacromial artery cadaveric study pectoral nerves dissection`
25. `Insights into Imaging axilla anatomy imaging review CT MRI axillary lymph nodes brachial plexus pictorial`
26. `Insights into Imaging quadrilateral space syndrome suprascapular nerve entrapment MRI anatomy pictorial review`
27. `site:pmc.ncbi.nlm.nih.gov axilla cadaver dissection axillary artery cords brachial plexus labelled anatomy teaching`
28. `site:pmc.ncbi.nlm.nih.gov rotator interval coracohumeral ligament MRI anatomy normal labelled review CC BY`
29. `long thoracic nerve cadaveric dissection Cureus OR "Translational Research in Anatomy" OR Medicina ...`
30. `site:pmc.ncbi.nlm.nih.gov deltopectoral groove cephalic vein thoracoacromial cadaver dissection labeled figure CC BY`

## Selected (see bolge_omuz.json)
topo_lecture: PMC5992113, PMC10924754, PMC9223225, PMC5617940 (Fig 1), PMC5790210, PMC4603045, PMC6026816 (CC BY-NC)
topo_variation: PMC10183034, PMC7664784, PMC6588231, PMC4392958, PMC7601857, PMC7656716, PMC12206475
kesit_lecture: PMC8695258, PMC6251069, PMC3097811, PMC5617940 (Fig 3)
kesit_variation: PMC6251069, PMC13051579 (CC BY-NC), PMC9166870, PMC4044447, PMC10491707, PMC5617940 (Fig 4)

## Rejected / not used candidates
| PMCID | Reason |
|---|---|
| PMC4202880 (Torres, BP MRI technique) | Not in OA bucket |
| PMC7964914 (MR neurography BP) | Not in OA bucket |
| PMC4969373 (Iranian BP variations) | Not in OA bucket |
| PMC3553044 (shoulder US anatomy review) | Not in OA bucket |
| PMC5568533 (rotator interval US) | Not in OA bucket |
| PMC3592271 (SSN Indian scapulae) | Not in OA bucket |
| PMC4413059 (axillary nerve 50 specimens) | Not in OA bucket |
| PMC2526027 (axillary nerve transfer) | Not in OA bucket |
| PMC7000014 (acromion morphology) | Not in OA bucket |
| PMC5484444 (axillary nerve) | Not in OA bucket |
| PMC5698352, PMC3792775 (pectoral nerves) | Not in OA bucket |
| PMC8883301 (os acromiale Thai MRI) | CC BY-NC-ND |
| PMC10382883 (long thoracic nerve palsy) | CC BY-NC-ND; clinical photos only |
| PMC7058845 (acromial parameters) | CC BY-NC-ND |
| PMC7509696 (Pol J Radiol shoulder MRI) | CC BY-NC-ND; mostly pathology |
| PMC9200469 (coracoid ligaments MRI) | CC BY-NC-ND |
| PMC8142010 (axillary nerve anterior branch) | CC BY-NC-ND |
| PMC12064265 (suprascapular neurovascular variant) | CC BY-NC-SA, single case; PMC9223225 preferred (CC BY) |
| PMC5823154 (BP anatomy normal & variant, 2009) | No figures in XML |
| PMC9791892 (Bigliani reliability MRI) | Only a classification drawing + one unlabeled MR slice; Bigliani schematic available elsewhere; not taken |
| PMC9446281 (LHB / RC tear MRI) | Pathology images, not normal anatomy |
| PMC9556688 (Insights Imaging nerve entrapment) | CC BY but shoulder figures are pathology (denervation); not normal anatomy |
| PMC3483739 (entrapment neuropathies MRI) | CC BY; shoulder figures pathology + simple drawings; kept as backup only |
| PMC4544516 (axillary nerve anterosuperior approach) | CC BY but Fig 2 unlabeled, low-contrast greyscale |
| PMC2840821 (safe deltoid split) | Single simple diagram only |
| PMC9036714 (acromion–axillary nerve, clinical) | Intra-operative measurement photo, no anatomy labels |
| PMC6026816 Fig 1 | Unlabeled; Fig 2 kept instead |
| PMC5990267 (suprascapular artery variant) | Hand-drawn, low-quality schematic; better material in PMC12206475/PMC10183034 |
| PMC10317871 (aberrant suprascapular artery, Surg Radiol Anat) | CC BY; viable backup, not downloaded to repo (enough vascular variation material) |
| PMC11673361 (bilateral vascular variations) | CC BY; mainly a forearm/arm case; left for KOL/ÖNKOL agents |
| PMC5841078 (cephalic vein termination variant) | CC BY; neck/clavicle case report; not prioritised |
| PMC4603045 Fig 1 | Intra-operative (living patient) photo; only schematic Fig 2 kept |
| PMC7702999 (pectoralis quartus + chondroepitrochlearis) | CC BY-NC single case; downloaded to scratch only, not kept (PMC6588231 has series data) |
| PMC9747332 (variant pectoralis minor) | CC BY-NC single case series of 3 cadavers; not kept |
| PMC4927432, PMC4691663 (axillary arch) | CC BY-NC case reports; axillary arch already covered by PMC12206543 in repo |
| PMC6588231 Fig 1 | Caption: "Modified from Lee 2014" → third-party derived, rejected |
| PMC7664784 Fig 2 | Reproduced terminology scheme (Rodríguez-Niedenführ et al. 2003) → rejected |
| PMC6251069 Fig 14 | Caption "(Courtesy of Dr Deepu Alex Thomas)" → not taken; Fig 15 is also "Courtesy of" and is kept but FLAGGED |
| PMC11001262 (SSN meta-analysis, Cureus) | CC BY but Fig 2 caption cites ref [4] (drawing after Polguj) and Fig 3 is a small 2-panel; PMC4044447 preferred |
| PMC10924754 Fig 2 | Only 500 px, redundant with Fig 1 |

## Gaps
- No CC BY labelled cadaver photo of the whole axilla content (a./v. axillaris with cords in situ) beyond those already in repo (PMC12578619, PMC10363335); PMC4392958 Fig 2 partly fills it.
- Triangular space / triangular interval: no OA cadaver figure found (Tubbs et al. not OA).
- Spinoglenoid notch: only indirectly (PMC9223225 nerve, PMC6251069 text).
- No CC BY labelled NORMAL axial/coronal shoulder MRI atlas-type figure (Pol J Radiol review is ND; Insights into Imaging hits were pathology). kesit_lecture relies on BP MRI (PMC8695258), MR arthrography (PMC6251069) and low-res US (PMC3097811). The project's own CT/cryosection series (kesitsel_kaynaklar.json) should cover normal axial anatomy.
- Bigliani acromion type on imaging with OA licence and good image: not secured (PMC6251069 Fig 8 schematic exists, CC BY, not downloaded).
- Accessory muscles on MRI/CT (axillary arch imaging prevalence, Guy et al. AJR) not OA.
- Prefixed/postfixed plexus meta-analysis (2021) not in PMC OA.
