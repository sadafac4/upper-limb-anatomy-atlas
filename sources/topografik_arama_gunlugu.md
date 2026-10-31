# Topografik görseller: arama günlüğü (search log)

Date: 2026-10-31. Discovery used WebSearch only. Every candidate was checked against the AWS PMC Open Access bucket
(`https://pmc-oa-opendata.s3.amazonaws.com/`) with `scripts/pmc_oa_fetch.py info <PMCID>`, which reads `license_code`
from the bucket JSON and the figure list and captions from the JATS XML. Selected files were saved with
`scripts/pmc_oa_fetch.py get <PMCID> <files>`. `scripts/build_topografik_sources.py` then builds
`topografik_kaynaklar.json` and checks each image's md5 against the bucket JSON.
NCBI, Europe PMC, doi.org and similar hosts are blocked by the proxy, so the bucket is the only source of truth used here.

## Searches run (WebSearch, standard mode)
1. `site:pmc.ncbi.nlm.nih.gov axillary arch muscle cadaver case report`
2. `site:pmc.ncbi.nlm.nih.gov superficial brachial artery cadaver dissection`
3. `site:pmc.ncbi.nlm.nih.gov communication musculocutaneous median nerve cadaver`
4. `site:pmc.ncbi.nlm.nih.gov third head biceps brachii cadaver`
5. `site:pmc.ncbi.nlm.nih.gov persistent median artery bifid median nerve cadaver`
6. `site:pmc.ncbi.nlm.nih.gov Martin-Gruber anastomosis cadaveric study`
7. `site:pmc.ncbi.nlm.nih.gov reversed palmaris longus cadaver`
8. `site:pmc.ncbi.nlm.nih.gov supracondylar process ligament of Struthers cadaver`
9. `site:pmc.ncbi.nlm.nih.gov cadaver dissection brachial plexus infraclavicular axilla anatomical study photograph`
10. `site:pmc.ncbi.nlm.nih.gov cubital fossa cadaveric dissection anatomy`
11. `site:pmc.ncbi.nlm.nih.gov carpal tunnel cadaver dissection transverse carpal ligament median nerve recurrent branch`
12. `site:pmc.ncbi.nlm.nih.gov quadrangular space cadaveric study axillary nerve`
13. `site:pmc.ncbi.nlm.nih.gov arcade of Frohse cadaveric study posterior interosseous nerve`
14. `site:pmc.ncbi.nlm.nih.gov Gantzer muscle accessory head flexor pollicis longus cadaver`
15. `site:pmc.ncbi.nlm.nih.gov axillary artery variation branching cadaver Cureus`
16. `site:pmc.ncbi.nlm.nih.gov suprascapular notch cadaver suprascapular nerve transverse scapular ligament`
17. `site:pmc.ncbi.nlm.nih.gov antecubital fossa cadaver median cubital vein brachial artery dissection photograph` (no PMC hits)
18. `site:pmc.ncbi.nlm.nih.gov Cureus cadaveric radial nerve deep branch supinator Frohse dissection`
19. `site:pmc.ncbi.nlm.nih.gov cadaveric study lateral antebrachial cutaneous nerve cubital fossa venipuncture`
20. `site:pmc.ncbi.nlm.nih.gov posterior interosseous nerve cadaver dissection supinator CC BY anatomical study`
21. `Cureus cadaveric lacertus fibrosus bicipital aponeurosis median nerve dissection` (no usable PMC hit)
22. `site:pmc.ncbi.nlm.nih.gov "cubital fossa" cadaver case report brachial artery median nerve ...`
23. `site:pmc.ncbi.nlm.nih.gov cadaveric anatomy cubital fossa contents dissection figure brachial artery bifurcation radial recurrent`
24. `site:pmc.ncbi.nlm.nih.gov fresh cadaver axillary fossa dissection axillary artery cords brachial plexus normal anatomy figure regional anesthesia`
25. `Cureus "third head" OR "accessory head" biceps brachii cadaver case report` (no CC BY PMC hit)

## Selected (17 articles; details in `topografik_kaynaklar.json`)
PMC12578619, PMC10823296, PMC6834099, PMC3931286, PMC8958867, PMC4555201, PMC12500735, PMC12206543, PMC10599095,
PMC11026042, PMC5752815 (CC BY-NC-SA, flagged), PMC10343151, PMC11867591, PMC7033050, PMC4636409,
PMC5608727 (CC BY-NC, flagged), PMC10363335.

## Candidates rejected
| PMCID | Topic | Reason |
|---|---|---|
| PMC4362564 | SBA incidence | Not in the OA bucket |
| PMC4079987 | bilateral absent MCN | Not in the OA bucket |
| PMC4800503 | MGA (North India) | Not in the OA bucket |
| PMC4843237 | reversed PL | Not in the OA bucket |
| PMC3738618 | PL compressing median nerve | Not in the OA bucket |
| PMC4969373 | brachial plexus variations | Not in the OA bucket |
| PMC4413059 | axillary nerve / quadrangular space | Not in the OA bucket |
| PMC3619716 | radial tunnel | Not in the OA bucket |
| PMC5403734, PMC5380404 | cubital fossa | Not in the OA bucket |
| PMC5742017 | MCN–median communication (IJSCR) | CC BY-NC-ND (ND not allowed) |
| PMC4887445 | MCN–median union (Rev Bras Ortop) | CC BY-NC-ND |
| PMC7048573 | radial tunnel / arcade of Frohse | CC BY-NC-ND |
| PMC4783087 | cubital fossa (phlebotomy review) | No licence in bucket (`license_code` None); figures are diagrams |
| PMC5391251 | cubital fossa nerves (Cureus, CC BY) | Only figure is an original drawing, not a cadaver photo |
| PMC9256478 | cubital fossa veins (CC BY-NC) | Diagrams and living-subject photos, no dissection |
| PMC8342828 | LACN venipuncture injury | Ultrasound images only |
| PMC5396015 | PIN localisation (CC BY-NC) | Boxplots and drawings only |
| PMC12409753 | recurrent thenar branch (Cureus, CC BY) | Downloaded then removed: single 750x107 px strip, too small to read |
| PMC11380754 | bilateral PMA + bifid MN (Cureus, CC BY) | Downloaded then removed: 750x175 px panorama marked only with coloured symbols; PMC10343151 has numbered labels and was used instead |
| PMC4813407 | Gantzer muscle (Acta Ortop Bras, CC BY) | Downloaded then removed: specimen occupies a ~230 px wide area in grey padding; PMC4636409 has a much better photo |
| PMC10514158 | PMA + bifid MN (SRA, CC BY) | Valid alternative for topic 10, not needed |
| PMC12456898, PMC4775498 | MGA (Acta Ortop Bras, CC BY) | Valid alternatives for topic 11, not needed |
| PMC12790809, PMC10235925 | reversed PL (Cureus, CC BY) | Valid alternatives for topic 12, not needed |
| PMC4927432 | Langer's arch with MCN variation (CC BY-NC) | CC BY alternative PMC12206543 preferred |
| PMC4292133 | latissimus dorsi slips (CC BY-NC-SA) | CC BY alternative preferred |
| PMC7702999 | pectoralis quartus (CC BY-NC) | Off-target |
| PMC2772267 | superficial brachio-ulno-radial artery + PMA (CC BY 2.0) | Valid alternative for topic 7/10, not needed |
| PMC4226802 | axillary artery high bifurcation (SpringerPlus, CC BY) | Valid alternative for topic 7/14, not needed |
| PMC8169239 | axillary artery topography (CC BY) | Figures are diagrams/charts |
| PMC11760582 | terminal branches in axillary fossa (CC BY) | Valid alternative for topics 1/8, not needed |
| PMC4002576 | combined arterial/venous/neural variation (CC BY 2.0) | Valid alternative, not needed |
| PMC10997832 | high bifurcation of brachial artery (Cureus, CC BY) | Single figure; PMC10823296 covers the elbow better |
| PMC4075226 | median nerve variations at wrist (CC BY-NC-SA) | CC BY sources preferred for topic 3 |
| PMC10787799 | axillary nerve branching (Sci Rep, CC BY) | Valid alternative for topic 4, not needed |
| PMC3460084 | bifid superior transverse scapular ligament (CC BY) | Valid alternative for topic 4, not needed |
| PMC12064265 | suprascapular neurovascular variant (CC BY-NC-SA) | CC BY PMC4555201 preferred |
| PMC7345276 | radial nerve branching (Diagnostics, CC BY) | Valid alternative for topic 5, not needed |
| PMC9981488 | accessory FPL head joining 1st lumbrical (CC BY) | Unusual variant; PMC4636409 shows the classic Gantzer muscle |
| PMC5035692 | MCN–median communication | Fetal specimens, not checked further |
| Figure 4 of PMC3931286 | carpal tunnel landmarks | Not downloaded: photo of a textbook-style drawing (third-party artwork) |
| Figures 1–2 of PMC8958867 | quadrangular space | Not downloaded: author drawing and a third-party AO Surgery Reference image |

## Gaps and caveats
- **Normal cubital fossa:** no CC BY cadaver photo of a normal cubital fossa was found in the OA bucket. Topic 2 uses PMC10823296, a bilateral variant specimen (high brachial-artery bifurcation; median nerve under pronator teres) with clearly labelled elbow photos.
- **Third head of biceps:** the only usable cadaver photos are in PMC5752815, licensed CC BY-NC-SA 3.0. A deck that includes them must be non-commercial and carry the same licence.
- **Ligament of Struthers:** PMC5608727 is CC BY-NC 4.0 (non-commercial). Gantzer's muscle (PMC4636409, CC BY) covers topic 13 without restriction.
- **Image resolution:** the bucket holds only web-resolution JPEGs, roughly 390–775 px wide. Each image's size is recorded in the JSON `notes` and `pixels` fields. They work as half-slide images but not as full-screen ones.
