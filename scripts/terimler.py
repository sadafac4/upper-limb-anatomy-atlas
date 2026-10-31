# -*- coding: utf-8 -*-
"""Şekillerde basılı İngilizce kısaltmaların Terminologia Anatomica (Latince) / Türkçe karşılıkları.
lej("MN", "UN") → "**MN** n. medianus; **UN** n. ulnaris"  (yalnız şekilde gerçekten görünen etiketler verilir)."""

T = {
 # sinirler
 "MN": "n. medianus", "UN": "n. ulnaris", "RN": "n. radialis", "AN": "n. axillaris", "AXN": "n. axillaris",
 "MCN": "n. musculocutaneus", "TDN": "n. thoracodorsalis", "LTN": "n. thoracicus longus",
 "SSN": "n. suprascapularis", "PIN": "n. interosseus posterior", "AIN": "n. interosseus anterior",
 "SBRN": "r. superficialis n. radialis", "DBRN": "r. profundus n. radialis", "SRN": "r. superficialis n. radialis",
 "SB": "r. superficialis n. radialis", "MBCN": "n. cutaneus brachii medialis", "MCNF": "n. cutaneus antebrachii medialis",
 "RBMN": "n. medianus'un radial dalı", "MBMN": "n. medianus'un medial dalı", "MB": "motor (tenar) dal",
 "DUN": "r. profundus n. ulnaris", "SUN": "r. superficialis n. ulnaris", "DBUN": "r. dorsalis n. ulnaris",
 "CDN3": "3. n. digitalis palmaris communis", "CDN4": "4. n. digitalis palmaris communis",
 "LR": "radix lateralis n. mediani", "MR": "radix medialis n. mediani",
 "LC": "fasciculus lateralis", "MC": "fasciculus medialis", "PC": "fasciculus posterior",
 "ST": "truncus superior", "MT": "truncus medius", "IT": "truncus inferior",
 "UT": "truncus superior", "LT": "truncus inferior",
 "U1": "1. n. subscapularis superior", "U2": "2. (aksesuar) n. subscapularis superior", "L": "n. subscapularis inferior",
 "BA": "a. brachialis", "RA": "a. radialis", "UA": "a. ulnaris", "AA": "a. axillaris", "SA": "a. subclavia",
 # arterler / venler
 "SBA": "a. brachialis superficialis", "BRA": "a. brachioradialis (yüksek çıkışlı a. radialis)", "hBRA": "yüksek çıkışlı a. brachioradialis",
 "DBA": "a. profunda brachii", "PMA": "a. mediana persistens", "SUA": "a. ulnaris superficialis", "SRA": "a. radialis superficialis",
 "CIA": "a. interossea communis", "AIA": "a. interossea anterior", "PIA": "a. interossea posterior",
 "TCA": "a. transversa cervicis", "DSA": "a. dorsalis scapulae", "SSA": "a. suprascapularis", "CCA": "a. carotis communis",
 "ACHA": "a. circumflexa humeri anterior", "ACHP": "a. circumflexa humeri posterior", "PHCA": "a. circumflexa humeri posterior",
 "APB": "a. profunda brachii", "ASS": "a. subscapularis", "ABS": "a. brachialis superficialis", "TPC": "truncus profundocircumflexus",
 "PMAs": "aa. metacarpales palmares", "SDPBUA": "a. ulnaris'in üst derin palmar dalı", "IDPBUA": "a. ulnaris'in alt derin palmar dalı",
 "spa": "arcus palmaris superficialis", "SPA": "arcus palmaris superficialis", "cb": "iletişim dalı",
 "BV": "v. basilica", "CV": "v. cephalica", "MCV": "v. mediana cubiti", "BaV": "v. basilica", "BrV": "vv. brachiales",
 "PURA": "a. recurrens ulnaris posterior",
 # kaslar
 "BB": "m. biceps brachii", "BBsh": "caput breve m. bicipitis brachii", "BBlh": "caput longum m. bicipitis brachii",
 "SH": "caput breve m. bicipitis", "LH": "caput longum m. bicipitis / caput laterale", "BT": "tendo m. bicipitis",
 "CB": "m. coracobrachialis", "CBM": "m. coracobrachialis", "TM": "m. teres major",
 "SSC": "m. subscapularis", "SSP": "m. supraspinatus", "SS": "m. supraspinatus", "ISP": "m. infraspinatus", "TMi": "m. teres minor",
 "TRI": "m. triceps brachii", "PMM": "m. pectoralis minor", "PMi": "m. pectoralis minor",
 "AS": "m. scalenus anterior", "MS": "m. scalenus medius", "SCM": "m. sternocleidomastoideus",
 "PT": "m. pronator teres", "hhPT": "caput humerale m. pronatoris teretis", "FCR": "m. flexor carpi radialis", "PL": "m. palmaris longus",
 "R-PL": "m. palmaris longus reversus", "FCU": "m. flexor carpi ulnaris", "FDS": "m. flexor digitorum superficialis",
 "FDP": "m. flexor digitorum profundus", "f.FDP": "m. flexor digitorum profundus", "FPL": "m. flexor pollicis longus", "PQ": "m. pronator quadratus",
 "BR": "m. brachioradialis", "Br": "m. brachioradialis / m. brachialis", "ECRL": "m. extensor carpi radialis longus", "ECRB": "m. extensor carpi radialis brevis",
 "ED": "m. extensor digitorum", "EDM": "m. extensor digiti minimi", "ECU": "m. extensor carpi ulnaris", "APL": "m. abductor pollicis longus",
 "EPB": "m. extensor pollicis brevis", "EPL": "m. extensor pollicis longus", "EIP": "m. extensor indicis", "S": "m. supinator",
 "SLSM": "m. supinator yüzeyel tabaka", "DLSM": "m. supinator derin tabaka", "AF": "arcus Frohse", "BRM": "m. brachioradialis",
 "EDBM": "m. extensor digitorum brevis manus", "ADM": "m. abductor digiti minimi", "aADM": "aksesuar m. abductor digiti minimi",
 "FDMB": "m. flexor digiti minimi brevis", "FDML": "m. flexor digiti minimi longus (aksesuar)", "PB": "m. palmaris brevis",
 "AdP": "m. adductor pollicis", "L1": "1. m. lumbricalis", "AMHL1": "1. lumbrikalin aksesuar kas başı",
 # kemik / bağ / diğer
 "ME": "epicondylus medialis", "MEC": "epicondylus medialis", "LE": "epicondylus lateralis", "Olc": "olecranon", "O": "lig. Osborne",
 "CP": "processus coracoideus", "A": "acromion", "H": "humerus / os hamatum", "CAL": "lig. coracoacromiale",
 "IOM": "membrana interossea", "DOB": "distal oblik demet", "AB": "aksesuar demet", "DOAC": "dorsal oblik aksesuar kordon",
 "ER": "retinaculum extensorum", "FR": "retinaculum flexorum", "CT": "canalis carpi / kesik tendon", "TE": "eminentia thenaris", "HE": "eminentia hypothenaris",
 "KCL": "Kaplan kardinal çizgisi", "Y": "Y çizgisi", "P": "os pisiforme", "T": "os trapezium / os triquetrum",
 "A-MCL": "lig. collaterale ulnare – ön bant", "P-MCL": "lig. collaterale ulnare – arka bant", "T-MCL": "lig. collaterale ulnare – transvers bant",
 "RCL": "lig. collaterale radiale", "AL": "lig. anulare radii", "LUCL": "lateral ulnar kollateral bağ",
 "SGHL": "lig. glenohumerale superius", "MGHL": "lig. glenohumerale medium", "IGHL": "lig. glenohumerale inferius", "LHBT": "caput longum m. bicipitis tendonu",
 "LHBBM": "caput longum m. bicipitis", "GL": "labrum glenoidale", "CLMGHL": "kordon benzeri MGHL",
 "STD": "üst transvers çap", "MD": "orta derinlik", "VP": "lamina palmaris (volar plak)", "FT": "fleksör tendon", "MCH": "caput ossis metacarpi",
 "PP": "phalanx proximalis", "DP": "phalanx distalis", "SB_US": "sesamoid kemik",
}

def lej(*kisaltmalar, ozel=None):
    ozel = ozel or {}
    out = []
    for k in kisaltmalar:
        v = ozel.get(k) or T.get(k)
        if v is None:
            raise KeyError(f"Sözlükte yok: {k}")
        out.append(f"**{k}** {v}")
    return "; ".join(out)
