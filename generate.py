#!/usr/bin/env python3
"""Draw The Daily Globe — Saturday 21 November 2026 (1024x1024, deterministic).

Renders entry.png from stories.py with PIL only: no network, no clock,
no randomness. Same input always produces byte-identical output.
Run: python3 generate.py  (writes entry.png next to this file)
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from stories import LEADS, SMALL, NUMBERED, TIMELINE, DATE_CHECK, CONTINENTS

W, H = 1024, 1024
M = 14                      # outer margin
CW = W - 2 * M              # content width

PAPER = (247, 243, 232)
INK = (24, 24, 22)
RED = (176, 30, 36)
NAVY = (31, 58, 95)
TEAL = (18, 110, 110)
GREY = (110, 106, 96)
LIGHT = (233, 227, 211)
SEA = (168, 196, 214)
LAND = (232, 220, 192)
LAND_LINE = (138, 122, 90)

CHIP_COLORS = {"CONFIRMED": (27, 120, 60), "REPORTED": (31, 90, 160),
               "CLAIM": (176, 120, 10)}

FONT_DIR = "/usr/share/fonts/truetype/noto"
SERIF_B = os.path.join(FONT_DIR, "NotoSerif-Bold.ttf")
SERIF_R = os.path.join(FONT_DIR, "NotoSerif-Regular.ttf")
SANS_B = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS_R = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit in width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def trunc(draw, text, fnt, width):
    """Shorten text with an ellipsis so it fits on one line."""
    if draw.textlength(text, font=fnt) <= width:
        return text
    words = text.split()
    out = ""
    for w in words:
        trial = (out + " " + w).strip()
        if draw.textlength(trial + " \u2026", font=fnt) <= width:
            out = trial
        else:
            break
    return (out + " \u2026") if out else "\u2026"


def chip(draw, x, y, label, size=9):
    """Draw a small coloured tag; returns width used."""
    fnt = font(SANS_B, size)
    tw = draw.textlength(label, font=fnt)
    w = int(tw) + 8
    h = size + 6
    draw.rounded_rectangle([x, y, x + w, y + h], radius=3,
                           fill=CHIP_COLORS[label])
    draw.text((x + 4, y + 2), label, font=fnt, fill=(255, 255, 255))
    return w


def draw_gulf(draw, x, y, w, h):
    """Stylised Gulf scene: sea, tankers, missile arcs, island."""
    draw.rectangle([x, y, x + w, y + h], fill=(207, 227, 238))
    draw.ellipse([x + w - 52, y + 8, x + w - 22, y + 38], fill=(240, 200, 90))
    sea_y = y + int(h * 0.52)
    draw.rectangle([x, sea_y, x + w, y + h], fill=(47, 111, 159))
    draw.rectangle([x, sea_y, x + w, sea_y + 3], fill=(120, 170, 200))
    # Kharg island
    draw.ellipse([x + 18, sea_y - 14, x + 66, sea_y + 10], fill=(150, 140, 100))
    draw.rectangle([x + 30, sea_y - 30, x + 34, sea_y - 12], fill=(90, 84, 70))
    draw.rectangle([x + 44, sea_y - 26, x + 48, sea_y - 12], fill=(90, 84, 70))
    # tankers
    for tx, tw in ((92, 86), (196, 104), (268, 60)):
        draw.rectangle([x + tx, sea_y + 12, x + tx + tw, sea_y + 30],
                       fill=(30, 32, 38))
        draw.rectangle([x + tx + tw - 18, sea_y - 2, x + tx + tw - 8,
                        sea_y + 12], fill=(30, 32, 38))
        draw.rectangle([x + tx, sea_y + 30, x + tx + tw, sea_y + 33],
                       fill=(176, 30, 36))
    # missile arcs (red, dashed by short segments)
    for (ax, ay, bx, by) in ((70, sea_y - 34, 210, 6),
                             (250, sea_y - 30, 150, 2)):
        for t in range(0, 11):
            if t % 2 == 0:
                continue
            px = ax + (bx - ax) * t / 10.0
            py = ay + (by - ay) * (t / 10.0) ** 2 - 14 * (t / 10.0) * (1 - t / 10.0) * 4
            draw.ellipse([x + px - 2, y + py - 2, x + px + 2, y + py + 2],
                         fill=RED)


def draw_summit(draw, x, y, w, h):
    """Three flags over a podium and skyline."""
    draw.rectangle([x, y, x + w, y + h], fill=(207, 227, 238))
    # skyline
    for bx, bw, bh in ((8, 34, 42), (48, 26, 58), (80, 40, 36), (126, 30, 52),
                       (162, 34, 40), (202, 28, 60), (236, 32, 44), (272, 30, 54)):
        draw.rectangle([x + bx, y + h - 18 - bh, x + bx + bw, y + h - 18],
                       fill=(90, 105, 130))
    draw.rectangle([x, y + h - 18, x + w, y + h], fill=(120, 110, 95))
    # podium
    draw.rectangle([x + w // 2 - 34, y + h - 62, x + w // 2 + 34, y + h - 18],
                   fill=(70, 60, 55))
    draw.rectangle([x + w // 2 - 44, y + h - 68, x + w // 2 + 44, y + h - 62],
                   fill=(50, 44, 40))
    # flags: US (stripes), China (red + stars), Russia (tricolour)
    flags = [
        (x + 52, [(176, 30, 36), (255, 255, 255), (176, 30, 36),
                  (255, 255, 255), (176, 30, 36)], (31, 58, 95)),
        (x + 142, [(200, 22, 22)] * 5, None),
        (x + 232, [(255, 255, 255), (31, 90, 180), (200, 30, 30)], None),
    ]
    for fx, stripes, canton in flags:
        for i, col in enumerate(stripes):
            draw.rectangle([fx, y + 8 + i * 7, fx + 46, y + 8 + (i + 1) * 7],
                           fill=col)
        if canton:
            draw.rectangle([fx, y + 8, fx + 20, y + 29], fill=canton)
            for sx, sy in ((fx + 6, y + 13), (fx + 13, y + 19), (fx + 6, y + 24)):
                draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
        if stripes[0] == (200, 22, 22):
            for sx, sy in ((fx + 8, y + 14), (fx + 20, y + 12), (fx + 26, y + 18),
                           (fx + 20, y + 24), (fx + 8, y + 22)):
                draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 220, 60))
        draw.rectangle([fx - 2, y + 8, fx, y + h - 62], fill=(60, 55, 50))


def draw_quake(draw, x, y, w, h):
    """Andes ridge, seismic rings, cracked ground, buildings."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 214, 188))
    # mountains
    peaks = [(0, 70), (60, 34), (110, 66), (160, 26), (220, 62), (270, 40), (324, 68)]
    draw.polygon([(x + px, y + h - 26 - (h - 26 - py) * 0.55) for px, py in peaks]
                 + [(x + w, y + h - 26), (x, y + h - 26)], fill=(120, 110, 90))
    draw.polygon([(x + 150, y + 26), (x + 172, y + 52), (x + 150, y + 52),
                  (x + 128, y + 52)], fill=(250, 250, 248))
    # ground + buildings
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(90, 84, 70))
    for bx, bw, bh in ((16, 26, 20), (52, 20, 14), (240, 24, 18), (276, 22, 12)):
        draw.rectangle([x + bx, y + h - 26 - bh, x + bx + bw, y + h - 26],
                       fill=(60, 58, 54))
    # seismic rings from epicentre
    cx, cy = x + w // 2, y + 44
    for r in (12, 24, 36, 48):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED, width=2)
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=RED)
    # crack
    draw.line([(x + 96, y + h - 26), (x + 116, y + h - 14), (x + 104, y + h - 4),
               (x + 128, y + h)], fill=(40, 36, 30), width=2)


ART = {"gulf": draw_gulf, "summit": draw_summit, "quake": draw_quake}


def draw_map(draw, x, y, w, h, pins):
    """Stylised equirectangular world map with numbered pins."""
    draw.rectangle([x, y, x + w, y + h], fill=SEA)
    # graticule
    for lon in range(-150, 181, 30):
        gx = x + (lon + 180) / 360.0 * w
        draw.line([(gx, y), (gx, y + h)], fill=(140, 170, 190), width=1)
    for lat in (-30, 0, 30, 60):
        gy = y + (84 - lat) / 142.0 * h
        draw.line([(x, gy), (x + w, gy)], fill=(140, 170, 190), width=1)

    def proj(lon, lat):
        return (x + (lon + 180) / 360.0 * w, y + (84 - lat) / 142.0 * h)

    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        draw.polygon(pts, fill=LAND, outline=LAND_LINE)
    draw.text((x + 6, y + 4), "WHERE IT HAPPENED — 15 PINNED STORIES",
              font=font(SANS_B, 10), fill=NAVY)
    for n, (lat, lon) in pins:
        px, py = proj(lon, lat)
        draw.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED,
                     outline=(255, 255, 255), width=1)
        fnt = font(SANS_B, 10 if n < 10 else 9)
        tw = draw.textlength(str(n), font=fnt)
        draw.text((px - tw / 2, py - 7), str(n), font=fnt, fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    y = 10

    # ---- Masthead ----
    d.text((M, y), "THE DAILY GLOBE", font=font(SERIF_B, 46), fill=INK)
    d.text((W - M, y + 2), "SATURDAY", font=font(SANS_B, 19), fill=RED, anchor="ra")
    d.text((W - M, y + 26), "21 NOVEMBER 2026", font=font(SANS_B, 22),
           fill=INK, anchor="ra")
    d.text((W - M, y + 52), "ONE DAY  \u00b7  ONE PAGE", font=font(SANS_B, 10),
           fill=GREY, anchor="ra")
    y = 84
    d.line([(M, y), (W - M, y)], fill=RED, width=3)
    y += 6
    d.text((M, y), "51 STORIES  \u2022  7 REGIONS  \u2022  17 FIELDS  \u2022  EVERY STORY HAPPENED OR WAS FIRST REPORTED ON 21 NOVEMBER 2026",
           font=font(SANS_B, 11), fill=NAVY)
    y = 108

    # ---- UTC timeline ----
    d.text((M, y), "UTC TIMELINE \u2014 FIRST HOURS  (00:00\u201304:30 UTC, DAY IN PROGRESS)",
           font=font(SANS_B, 11), fill=RED)
    y += 16
    cell = CW / len(TIMELINE)
    for i, (t, txt) in enumerate(TIMELINE):
        cx = M + i * cell
        d.line([(cx + cell / 2, y + 2), (cx + cell / 2, y + 8)], fill=RED, width=2)
        d.text((cx + 4, y + 10), t, font=font(SANS_B, 11), fill=RED)
        for j, ln in enumerate(wrap(d, txt, font(SANS_R, 10), cell - 8)[:1]):
            d.text((cx + 4, y + 24 + j * 12), ln, font=font(SANS_R, 10), fill=INK)
    y = 158

    # ---- By-field bar ----
    fields = {}
    for s in LEADS + SMALL:
        fields[s["field"]] = fields.get(s["field"], 0) + 1
    for n, _h, _c, _s, f, _r in NUMBERED:
        fields[f] = fields.get(f, 0) + 1
    order = sorted(fields.items(), key=lambda kv: (-kv[1], kv[0]))
    top = ["%s %d" % (k.upper(), v) for k, v in order if v >= 3]
    rest = sum(1 for _k, v in order if v < 3)
    bar = "BY FIELD   " + "  \u2022  ".join(top) + "  \u2022  +%d MORE AT 1 EACH" % rest
    d.text((M, y), bar, font=font(SANS_B, 10), fill=INK)
    y = 176

    # ---- Three illustrated leads ----
    col_w = (CW - 16) // 3
    for i, lead in enumerate(LEADS):
        lx = M + i * (col_w + 8)
        ART[lead["art"]](d, lx, y, col_w, 88)
        ty = y + 94
        d.text((lx, ty), lead["kicker"], font=font(SANS_B, 10), fill=RED)
        ty += 14
        for ln in wrap(d, lead["headline"], font(SANS_B, 17), col_w):
            d.text((lx, ty), ln, font=font(SANS_B, 17), fill=INK)
            ty += 19
        ty += 2
        for ln in wrap(d, lead["body"], font(SANS_R, 11), col_w)[:5]:
            d.text((lx, ty), ln, font=font(SANS_R, 11), fill=(40, 40, 38))
            ty += 13
        ty += 3
        cw = chip(d, lx, ty, lead["chip"])
        d.text((lx + cw + 6, ty + 1), lead["source"], font=font(SANS_R, 9),
               fill=GREY)
    y = 414

    # ---- 12 small stories: 4 cols x 3 rows ----
    scw = (CW - 24) // 4
    for i, s in enumerate(SMALL):
        r, c = divmod(i, 4)
        sx = M + c * (scw + 8)
        sy = y + r * 58
        d.text((sx, sy), "%d." % s["n"], font=font(SANS_B, 12), fill=RED)
        lines = wrap(d, s["headline"], font(SANS_B, 12.5), scw - 20)
        ly = sy
        for ln in lines[:2]:
            d.text((sx + 18, ly), ln, font=font(SANS_B, 12.5), fill=INK)
            ly += 15
        cw = chip(d, sx + 18, ly + 1, s["chip"], size=8)
        d.text((sx + 18 + cw + 5, ly + 2), s["source"], font=font(SANS_R, 8.5),
               fill=GREY)
        if c < 3:
            d.line([(sx + scw + 4, sy), (sx + scw + 4, sy + 52)], fill=LIGHT, width=1)
    y = 594

    # ---- World map (left) + DATE CHECK (right) ----
    map_w = 620
    pins = [(s["n"], s["pin"]) for s in LEADS + SMALL]
    draw_map(d, M, y, map_w, 184, pins)
    dx = M + map_w + 8
    dw = W - M - dx
    d.rectangle([dx, y, dx + dw, y + 184], outline=RED, width=2)
    d.rectangle([dx, y, dx + dw, y + 26], fill=RED)
    d.text((dx + 8, y + 5), "DATE CHECK \u2014 LEFT OUT AS OLDER NEWS",
           font=font(SANS_B, 12), fill=(255, 255, 255))
    dy = y + 32
    for story, when in DATE_CHECK:
        d.text((dx + 8, dy), "\u2715", font=font(SANS_B, 11), fill=RED)
        lines = wrap(d, story, font(SANS_B, 11), dw - 30)
        ly = dy
        for ln in lines[:1]:
            d.text((dx + 22, ly), ln, font=font(SANS_B, 11), fill=INK)
            ly += 13
        d.text((dx + 22, ly), when, font=font(SANS_R, 9.5), fill=GREY)
        dy += 19
    y = 784

    # ---- Numbered list: 36 more stories, 3 columns x 12 ----
    d.text((M, y), "THE REST OF THE DAY \u2014 36 MORE STORIES",
           font=font(SANS_B, 14), fill=NAVY)
    d.line([(M, y + 20), (W - M, y + 20)], fill=NAVY, width=1)
    y += 26
    ncw = (CW - 16) // 3
    for i, (n, headline, _chip, source, _f, _r) in enumerate(NUMBERED):
        col, row = divmod(i, 12)
        nx = M + col * (ncw + 8)
        ny = y + row * 15
        d.text((nx, ny), "%d." % n, font=font(SANS_B, 10.5), fill=RED)
        txt = trunc(d, "%s \u2014 %s" % (headline, source),
                    font(SANS_R, 10.5), ncw - 26)
        d.text((nx + 24, ny), txt, font=font(SANS_R, 10.5), fill=INK)

    # ---- Footer ----
    fy = H - 20
    d.line([(M, fy - 4), (W - M, fy - 4)], fill=GREY, width=1)
    d.text((M, fy), "Sources: Al Jazeera \u2022 Reuters \u2022 BBC \u2022 NDTV \u2022 White House \u2022 IGP/GFZ \u2022 UN \u2022 EU \u2022 US courts  \u2014  Built by an AI agent for make.fun's news-image-20261121 bounty.",
           font=font(SANS_R, 9.5), fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
