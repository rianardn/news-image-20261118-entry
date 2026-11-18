#!/usr/bin/env python3
"""Render the 18 November 2026 world-news front page (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 246, 238)
INK = (18, 24, 38)
CRIMSON = (164, 32, 40)
NAVY = (24, 48, 88)
GOLD = (176, 128, 32)
RULE = (150, 148, 138)
MUTED = (92, 96, 104)

def font(path, size):
    return ImageFont.truetype(path, size)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

canvas = Image.new("RGB", (W, H), PAPER)
pen = ImageDraw.Draw(canvas)

def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if pen.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(text, fnt, x, y, width, leading, color=INK):
    for ln in wrap(text, fnt, width):
        pen.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y

# ---- masthead ----
pen.rectangle([0, 0, W, 112], fill=NAVY)
pen.text((36, 18), "THE WORLD TODAY", font=font(FB, 54), fill=(255, 255, 255))
pen.text((36, 76), "WEDNESDAY, 18 NOVEMBER 2026  ·  SIX STORIES THAT DEFINED THE DAY",
         font=font(FB, 17), fill=(214, 188, 110))
pen.rectangle([0, 112, W, 118], fill=CRIMSON)
pen.rectangle([0, 118, W, 121], fill=GOLD)

# ---- lead story: Iran strikes back ----
pen.rectangle([28, 138, 996, 452], outline=RULE, width=2)
pen.rectangle([28, 138, 996, 182], fill=CRIMSON)
pen.text((48, 148), "MIDDLE EAST  —  ESCALATION", font=font(FB, 19), fill=(255, 255, 255))
y = 196
y = para("Iran strikes US bases in Kuwait and Bahrain",
         font(FS, 44), 48, y, 920, 54, color=INK)
y += 6
y = para("Tehran fired drones at Ali Al Salem air base in Kuwait and radar sites in "
         "Bahrain, hours after American jets hit a missile site on Qeshm Island. "
         "Bahrain says it intercepted the drones; no US casualties reported.",
         font(FR, 21), 48, y, 920, 29, color=(58, 62, 72))
pen.text((48, 418), "Sources: Reuters · Just Security · 18 Nov", font=font(FR, 15), fill=MUTED)

# ---- 2x2 grid of secondary stories ----
grid = [
    ("US POLITICS", "Peltola wins Alaska — Democrats take the Senate",
     "Mary Peltola beat Dan Sullivan in Alaska, giving Democrats a projected "
     "56–44 Senate majority in the incoming chamber.", NAVY),
    ("HEALTH", "Ebola in Congo more than doubles",
     "Over 11,000 cases and 5,400 deaths in three months. Nearly three in four "
     "infected children under five do not survive.", CRIMSON),
    ("RUSSIA", "Military plane crashes in Siberia — 19 dead",
     "A Russian military aircraft went down in the Kemerovo region, killing all "
     "19 people on board, officials said.", NAVY),
    ("EUROPE", "146,000 march across France over living costs",
     "Unions called a nationwide strike as crowds filled streets in Paris and "
     "beyond to protest prices and pay.", CRIMSON),
]
gx0, gy0, cw, ch, gap = 28, 472, 472, 196, 24
for i, (tag, head, body, accent) in enumerate(grid):
    x = gx0 + (i % 2) * (cw + gap)
    yy = gy0 + (i // 2) * (ch + gap)
    pen.rectangle([x, yy, x + cw, yy + ch], outline=RULE, width=2)
    pen.rectangle([x, yy, x + cw, yy + 34], fill=accent)
    pen.text((x + 14, yy + 7), tag, font=font(FB, 16), fill=(255, 255, 255))
    ty = yy + 44
    ty = para(head, font(FS, 22), x + 14, ty, cw - 28, 28, color=INK)
    para(body, font(FR, 16), x + 14, ty + 4, cw - 28, 22, color=(58, 62, 72))
    # Pinned dateline footer: the cards' text ends at uneven heights, so a
    # fixed footer rule + date anchors the grid and fills the dead space.
    pen.line([(x + 14, yy + ch - 30), (x + cw - 14, yy + ch - 30)], fill=RULE, width=1)
    pen.text((x + 14, yy + ch - 24), "18 NOVEMBER 2026", font=font(FB, 11), fill=MUTED)

# ---- bottom strip: Cyclone Xavier ----
pen.rectangle([28, 908, 996, 996], fill=(22, 34, 52))
pen.text((48, 922), "PACIFIC", font=font(FB, 16), fill=GOLD)
pen.text((48, 944), "Cyclone Xavier, Category 5, slams the Northern Cook Islands",
         font=font(FS, 22), fill=(255, 255, 255))
pen.text((48, 974), "The day in one page · Wednesday 18 November 2026",
         font=font(FR, 13), fill=(170, 178, 190))

canvas.save("/home/hatch/workspace/makefun/news-image-20261118-entry/entry.png")
print("saved entry.png", canvas.size)
