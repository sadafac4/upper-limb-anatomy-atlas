#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OpenStax Anatomy & Physiology (1. baskı, CC BY) atlas çizimlerinin İngilizce etiketlerini Latince (TA) karşılıklarıyla değiştirir.

Kaynak: github.com/philschatz/anatomy-book (OpenStax College A&P, 2013; LICENSE: CC BY) → perine/images/atlas_raw/
İngilizce yazıların kutuları RapidOCR ile bulundu (perine/images/atlas_raw/ocr_kutular.json) ve aşağıya elle
eşlendi. Yazı silinir (beyaz), aynı yere Latince terim yazılır; çizim ve kılavuz çizgileri değiştirilmez.
Mod: L = metin sağa yaslı (kutunun sağ kenarında biter, sola uzar), R = sola yaslı (sağa uzar), C = ortalı.
Çıktı: perine/images/atlas/<ad>.jpg  +  sources/perine_atlas.json        Çalıştır: python3 -I scripts/atlas_latince.py
"""
import json, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "perine/images/atlas_raw"; OUT = ROOT / "perine/images/atlas"
FONT = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
RENK = (31, 42, 68)
ATIF = ("OpenStax College. Anatomy & Physiology. OpenStax CNX, 2013 (1. baskı), {sekil}. "
        "Lisans: CC BY (openstax.org/details/books/anatomy-and-physiology). Uyarlama: İngilizce etiketler Latinceye çevrildi.")

# ad: (dosya, ölçek, kırpma(özgün px) veya None, şekil adı, [ (latince, [kutu...], mod, maks_genişlik_px(özgün)) ])
F = {
 "pelvis": ("807_Pelvis.jpg", 2.0, (0, 150, 1153, 785), "Şekil 8.12 'Pelvis'", [
    ("Os coxae", [[996, 300, 1084, 320]], "R", 0),
    ("Art. sacroiliaca", [[2, 340, 141, 364]], "L", 0),
    ("Promontorium", [[1, 395, 179, 421]], "L", 0),
    ("Os sacrum", [[997, 467, 1073, 488]], "R", 0),
    ("Linea terminalis", [[994, 539, 1101, 563]], "R", 0),
    ("Acetabulum", [[1, 564, 113, 587]], "L", 0),
    ("Os coccygis", [[0, 593, 74, 620]], "L", 0),
    ("Foramen obturatum", [[2, 650, 175, 674]], "L", 0),
    ("Symphysis pubica", [[993, 664, 1152, 693]], "R", 0),
    ("Tuber ischiadicum", [[2, 705, 159, 727]], "L", 0),
    ("Ramus ischiopubicus", [[126, 760, 296, 783]], "C", 0)]),
 "pelvis_cinsiyet": ("809_Male_Female_Pelvic_Girdle.jpg", 2.5, None, "Şekil 8.13 'Kadın ve erkek pelvisi'", [
    ("Kadın", [[208, 1, 271, 18]], "C", 0),
    ("Erkek", [[716, 0, 760, 19]], "C", 0),
    ("Os coxae", [[428, 269, 519, 290]], "C", 0),
    ("Os sacrum", [[437, 315, 512, 335]], "C", 0),
    ("Apertura pelvis sup.", [[421, 369, 526, 389]], "C", 125),
    ("Angulus subpubicus", [[408, 427, 541, 447]], "C", 0)]),
 "pelvis_bag": ("817_Ligaments_of_Pelvis.jpg", 2.5, None, "Şekil 8.14 'Pelvis bağları'", [
    ("Os sacrum", [[0, 2, 68, 21]], "L", 0),
    ("Spina iliaca posterior superior", [[0, 57, 85, 119]], "L", 0),
    ("Lig. sacroiliacum posterius", [[793, 90, 872, 155]], "R", 0),
    ("Os ilium", [[0, 143, 45, 165]], "L", 0),
    ("Foramen ischiadicum majus", [[788, 194, 864, 257]], "R", 0),
    ("Lig. sacrospinale", [[0, 269, 116, 311]], "L", 0),
    ("Lig. sacrospinale", [[744, 276, 862, 318]], "R", 0),
    ("Spina ischiadica", [[1, 321, 105, 340]], "L", 0),
    ("Os pubis", [[0, 354, 50, 374]], "L", 0),
    ("Foramen ischiadicum minus", [[744, 355, 862, 395]], "R", 0),
    ("Os ischii", [[0, 387, 71, 406]], "L", 0),
    ("Tuber ischiadicum", [[0, 421, 82, 464]], "L", 0),
    ("Lig. sacrotuberale", [[747, 421, 871, 461]], "R", 0),
    ("Angulus\nsubpubicus", [[395, 465, 476, 508]], "C", 0),
    ("Foramen\nobturatum", [[190, 477, 288, 520]], "C", 0),
    ("Ramus ischiopubicus", [[552, 503, 701, 522]], "R", 0)]),
 "diaphragma_pelvis": ("1115_Muscles_of_the_Pelvic_Floor.jpg", 1.0, None, "Şekil 11.12 'Pelvis tabanı kasları'", [
    ("Crista pubica", [[688, 133, 874, 168]], "C", 0),
    ("Urethra", [[16, 285, 162, 367]], "L", 0),
    ("Vagina (kadında)", [[19, 423, 255, 506]], "L", 0),
    ("M. pubococcygeus", [[1345, 531, 1626, 570]], "C", 0),
    ("Canalis analis", [[20, 565, 232, 598]], "L", 0),
    ("M. levator ani", [[1690, 652, 1898, 682]], "R", 0),
    ("Os sacrum", [[17, 692, 159, 731]], "L", 0),
    ("M. iliococcygeus", [[1339, 767, 1581, 806]], "C", 0),
    ("M. iliacus", [[728, 1090, 838, 1128]], "C", 0),
    ("Cristae iliacae", [[691, 1231, 870, 1268]], "C", 0),
    ("Diaphragma pelvis – üstten bakış", [[517, 1337, 1054, 1376]], "C", 0)]),
 "perine_kaslari": ("1116_Muscle_of_the_Perineum.jpg", 1.0, None, "Şekil 11.13 'Perine kasları'", [
    ("Penis", [[448, 41, 547, 76]], "R", 0),
    ("Clitoris", [[1582, 117, 1702, 156]], "C", 0),
    ("M. ischiocavernosus", [[814, 194, 1122, 226]], "C", 0),
    ("M. bulbospongiosus", [[773, 341, 1163, 420]], "C", 0),
    ("Urethra", [[1013, 458, 1144, 497]], "C", 0),
    ("Ostium vaginae", [[1012, 563, 1139, 606]], "C", 250),
    ("M. transversus perinei\nsuperficialis", [[790, 639, 1140, 719]], "C", 0),
    ("Anus", [[926, 770, 1021, 809]], "C", 0),
    ("M. sphincter ani externus", [[784, 879, 1170, 915]], "C", 0),
    ("M. levator ani", [[862, 965, 1062, 998]], "C", 0),
    ("Os coccygis", [[897, 1047, 1029, 1090]], "C", 0),
    ("M. gluteus maximus", [[820, 1134, 1122, 1168]], "C", 0),
    ("Erkek perinesi – alttan bakış", [[82, 1253, 677, 1291]], "C", 0),
    ("Kadın perinesi – alttan bakış", [[1339, 1253, 1979, 1290]], "C", 0)]),
 "sagittal_kadin": ("2602_Female_Urethra.jpg", 1.0, (0, 150, 1729, 1200), "Şekil 25.17a 'Kadın üretrası'", [
    ("Ureter", [[1581, 185, 1695, 224]], "R", 0),
    ("Uterus", [[8, 448, 124, 486]], "L", 0),
    ("Vesica urinaria", [[13, 650, 269, 686]], "L", 0),
    ("Cervix uteri", [[1585, 691, 1697, 727]], "R", 0),
    ("Os pubis", [[11, 762, 199, 797]], "L", 0),
    ("Rectum", [[1586, 808, 1717, 843]], "R", 0),
    ("Urethra", [[10, 834, 139, 873]], "L", 0),
    ("Vagina", [[1585, 877, 1706, 920]], "R", 0),
    ("Clitoris", [[11, 906, 127, 941]], "L", 0),
    ("Labium minus pudendi", [[10, 982, 259, 1017]], "L", 0),
    ("Anus", [[1583, 988, 1676, 1027]], "R", 0),
    ("Labium majus pudendi", [[10, 1071, 259, 1111]], "L", 0)]),
 "erkek_genital": ("Figure_28_01_01.jpg", 2.5, (0, 420, 805, 876), "Şekil 27.2c 'Erkek üreme sistemi – lateral görünüm'", [
    ("Prostata", [[350, 430, 445, 450]], "C", 0),
    ("Ductus deferens", [[10, 483, 148, 500]], "L", 0),
    ("Lig. suspensorium penis", [[10, 504, 194, 520]], "L", 0),
    ("Ampulla ductus deferentis", [[634, 505, 804, 521]], "R", 0),
    ("Vesica urinaria", [[10, 525, 109, 542]], "L", 0),
    ("Gl. vesiculosa", [[635, 537, 733, 552]], "R", 0),
    ("Symphysis pubica", [[8, 549, 116, 569]], "L", 0),
    ("Ductus ejaculatorius", [[634, 574, 737, 590]], "R", 0),
    ("Pars prostatica urethrae", [[633, 594, 739, 611]], "R", 0),
    ("Spatium perinei profundum (kaslar)", [[632, 613, 802, 634]], "R", 0),
    ("Gl. bulbourethralis (Cowper)", [[632, 634, 758, 652]], "R", 0),
    ("M. sphincter ani externus", [[633, 655, 765, 688]], "R", 0),
    ("Corpus cavernosum penis", [[10, 680, 138, 697]], "L", 0),
    ("Pars membranacea urethrae", [[633, 689, 766, 706]], "R", 0),
    ("Pars spongiosa urethrae", [[466, 711, 563, 728]], "R", 0),
    ("Testis", [[463, 736, 505, 753]], "R", 0),
    ("Epididymis", [[464, 756, 537, 774]], "R", 0),
    ("Corpus spongiosum penis", [[10, 784, 139, 800]], "L", 0),
    ("Scrotum", [[464, 781, 521, 798]], "R", 0),
    ("Ostium urethrae externum", [[92, 852, 253, 872]], "C", 0)]),
 "vulva": ("Figure_28_02_02.jpg", 2.5, (0, 50, 729, 428), "Şekil 27.11 'Vulva'", [
    ("Preputium clitoridis", [[313, 62, 371, 79]], "R", 0),
    ("Glans clitoridis", [[315, 88, 397, 101]], "R", 0),
    ("Labium minus pudendi", [[314, 114, 398, 127]], "R", 0),
    ("Corpus cavernosum clitoridis", [[317, 140, 442, 155]], "R", 0),
    ("Bulbus vestibuli", [[316, 168, 418, 181]], "R", 0),
    ("Ostium urethrae externum", [[314, 189, 421, 207]], "R", 0),
    ("Labium majus pudendi", [[312, 208, 398, 225]], "R", 0),
    ("Ostium vaginae", [[314, 233, 415, 250]], "R", 0),
    ("Gl. vestibularis major\n(sağ, ağzı)", [[316, 266, 417, 298]], "R", 0),
    ("Anus", [[198, 339, 235, 353]], "R", 0),
    ("Gll. vestibulares majores (Bartholin)", [[442, 352, 553, 368]], "C", 0),
    ("Dıştan önden bakış", [[56, 406, 244, 420]], "C", 0),
    ("İçten anterolateral bakış", [[479, 406, 697, 420]], "C", 0)]),
}


# figüre özgü ayarlar: beyaz = özgün pikselde boyanacak alanlar (ilgisiz küçük görseller), fk = yazı ölçek katsayısı
OPS = {"pelvis": {"beyaz": [[0, 150, 170, 300]], "fk": 1.3}, "erkek_genital": {"beyaz": [[0, 420, 230, 448]], "fk": 1.0},
       "pelvis_bag": {"fk": 0.85}, "diaphragma_pelvis": {"fk": 1.5}, "perine_kaslari": {"fk": 1.3},
       "pelvis_cinsiyet": {"fk": 1.3}, "sagittal_kadin": {"fk": 1.3}, "vulva": {"fk": 1.0}}


def font(px):
    return ImageFont.truetype(FONT, max(10, int(px)))


def isle(ad, dosya, olcek, kirp, sekil, etiketler):
    im = Image.open(RAW / dosya).convert("RGB")
    op = OPS.get(ad, {})
    for b in op.get("beyaz", []):
        ImageDraw.Draw(im).rectangle(b, fill="white")
    ox, oy = (kirp[0], kirp[1]) if kirp else (0, 0)
    if kirp:
        im = im.crop(kirp)
    if olcek != 1.0:
        im = im.resize((int(im.width * olcek), int(im.height * olcek)), Image.LANCZOS)
    S = lambda b: [(b[0] - ox) * olcek, (b[1] - oy) * olcek, (b[2] - ox) * olcek, (b[3] - oy) * olcek]
    d = ImageDraw.Draw(im)
    import statistics
    lh = statistics.median([(b[3] - b[1]) for _, ks, _, _ in etiketler for b in ks if (b[3] - b[1]) < 45]) * olcek
    plan = []
    for lat, kutular, mod, maxw in etiketler:
        bs = [S(b) for b in kutular]
        for b in bs:
            d.rectangle([b[0] - 2, b[1] - 2, b[2] + 2, b[3] + 2], fill="white")
        x0 = min(b[0] for b in bs); y0 = min(b[1] for b in bs); x1 = max(b[2] for b in bs); y1 = max(b[3] for b in bs)
        f0 = font(lh * 1.08 * op.get("fk", 1.0))
        f = f0
        if mod == "C" and maxw:
            while d.multiline_textbbox((0, 0), lat, font=f, spacing=2)[2] > maxw * olcek and f.size > 12:
                f = font(f.size - 1)
        plan.append((lat, (x0, y0, x1, y1), mod, f))
    # gerekli kenar boşluğu
    solp = sagp = 0
    for lat, (x0, y0, x1, y1), mod, f in plan:
        w = d.multiline_textbbox((0, 0), lat, font=f, spacing=2)[2]
        if mod == "L": solp = max(solp, w - x1 + 6)
        if mod == "R": sagp = max(sagp, x0 + w - im.width + 6)
        if mod == "C":
            cx = (x0 + x1) / 2; solp = max(solp, w / 2 - cx + 6); sagp = max(sagp, cx + w / 2 - im.width + 6)
    ustp = altp = 0
    for lat, (x0, y0, x1, y1), mod, f in plan:
        bb = d.multiline_textbbox((0, 0), lat, font=f, spacing=2); h = bb[3] - bb[1]; cy = (y0 + y1) / 2
        ustp = max(ustp, h / 2 - cy + 8); altp = max(altp, cy + h / 2 - im.height + 8)
    solp, sagp, ustp, altp = (int(max(0, v)) for v in (solp, sagp, ustp, altp))
    yeni = Image.new("RGB", (im.width + solp + sagp, im.height + ustp + altp), "white"); yeni.paste(im, (solp, ustp))
    d = ImageDraw.Draw(yeni)
    for lat, (x0, y0, x1, y1), mod, f in plan:
        x0 += solp; x1 += solp; y0 += ustp; y1 += ustp
        bb = d.multiline_textbbox((0, 0), lat, font=f, spacing=2); w, h = bb[2] - bb[0], bb[3] - bb[1]
        cy = (y0 + y1) / 2
        tx = x1 - w if mod == "L" else (x0 if mod == "R" else (x0 + x1) / 2 - w / 2)
        ty = cy - h / 2 - bb[1]
        d.rectangle([tx - 4, ty + bb[1] - 3, tx + w + 4, ty + bb[3] + 3], fill="white")
        d.multiline_text((tx, ty), lat, font=f, fill=RENK, spacing=2, align={"L": "right", "R": "left", "C": "center"}[mod])
    OUT.mkdir(parents=True, exist_ok=True)
    yol = OUT / f"{ad}.jpg"; yeni.save(yol, quality=92)
    return dict(ad=ad, kaynak_dosya=f"perine/images/atlas_raw/{dosya}", local_path=str(yol.relative_to(ROOT)), pixels=f"{yeni.width}x{yeni.height}",
                sekil=sekil, atif=ATIF.format(sekil=sekil), license_code="CC BY",
                etiketler=[e[0].replace("\n", " ") for e in etiketler])


if __name__ == "__main__":
    kayit = [isle(ad, *v) for ad, v in F.items()]
    json.dump(kayit, open(ROOT / "sources/perine_atlas.json", "w"), ensure_ascii=False, indent=1)
    for k in kayit: print(k["local_path"], k["pixels"])
