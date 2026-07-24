import os
import re

# Comprehensive mapping of filename to clean alt text / caption
CAPTIONS = {
    "202111271004.jpg": "Stevens Peak & West Willow Ridge",
    "12152021651p.jpg": "Mount Hood from White Salmon, WA",
    "12182021658p.jpg": "Harrison Peak (7,292') - American Selkirks",
    "12182021653p.jpg": "Chimney Rock (7,124') & Mount Roothaan (7,326')",
    "12152021654p_orig.jpeg": "Stevens Lake & Stevens Peak (6,838')",
    "12182021648p.jpg": "The American Selkirks from Shorty Peak (6,515')",
    "12182021716p.jpg": "Fisher Peak (9,336') - BC, Canada",
    "12182021659p.jpg": "Southern Part of American Selkirks, ID",
    "12182021700p.jpg": "American Selkirks from Blacktail Mountain",
    "12182021720p.jpg": "Unnamed Mountain near Lower Ibex Lake - Cabinet Mountains Wilderness",
    "12182021717p.jpg": "American Selkirks & Priest Lake from Blacktail Mountain",
    "12182021712p.jpg": "Canadian Rockies & Nicol Lake from Fisher Peak (9,336')",
    "12182021721p.jpg": "Selkirk Crest & SMI Hikers",
    "12182021722p.jpg": "Sawtooth Mountain - Proposed Scotchman Peaks Wilderness",
    "12182021724p.jpg": "American Selkirks from Bottleneck Ridge",
    "12182021735p.jpg": "Fisher Peak (9,336') - BC, Canada",
    "12182021739p.jpg": "Lookout Mountain (6,727') - American Selkirks",
    "12182021736p.jpg": "Chicago Peak (7,018') - Cabinet Mountains Wilderness",
    "12182021740p.jpg": "Upper Ball Lake & American Selkirk Crest",
    "12182021741p.jpg": "Sawtooth Mountain (6,763') - Proposed Scotchman Peaks Wilderness, MT",
    "12182021747p.jpg": "St. Paul Peak (7,714') from Cliff Lake Trail - Cabinet Mountains Wilderness",
    "12182021752p.jpg": "North Twin Peak above Beehive Lake - American Selkirks",
    "12182021748p.jpg": "East Face of A Peak (8,634') - Cabinet Mountains Wilderness, MT",
    "12182021750p.jpg": "Parker Peak (7,670') - American Selkirks",
    "12182021753p.jpg": "Scotchman Peak (7,709') - Proposed Scotchman Peaks Wilderness, MT",
    "121820217531p.jpg": "Ibex Peak (7,146') - Cabinet Mountains Wilderness",
    "12182021751p.jpg": "Abandon Peak (7,022') - American Selkirks",
    "12182021754p.jpg": "Leigh Lake & Scrambling Bockman Peak (8,174') - Cabinet Mountains Wilderness",
    "12182021755p.jpg": "Chicago Peak (7,018') & Cliff Lake - Cabinet Mountains Wilderness",
    "12182021756p.jpg": "The Lion Head (7,288') - American Selkirks",
    "12182021800p.jpg": "West Fork Peak (6,416') Lookout Tower - American Selkirks",
    "121820218001p.jpg": "Lookout Mountain (6,727') Lookout Towers - American Selkirks",
    "12182021808p.jpg": "Smith Peak (7,653') from near Lion Head Peak - American Selkirks",
    "12182021814p.jpg": "South Twin Peak to Gunsight Peak (7,352') - American Selkirks",
    "121920211224p.jpg": "Abandon Mountain & Trail Guide - American Selkirks",
    "121920211225p.jpg": "Lenz Peak (7,298'), Alaska Peak (7,006'), and Dad Peak (6,790') - Cabinet Mountains Wilderness",
    "121920211226p.jpg": "The Lion Head from West Fork Lookout - American Selkirks",
    "121920211228p.jpg": "Selkirk Crest from Little Harrison Lake - American Selkirks",
    "121920211229p.jpg": "The Lion Head (7,288') - American Selkirks",
    "121920211230p.jpg": "Ibex Peak (7,676') - Cabinet Mountains Wilderness",
    "121920211231p.jpg": "Scotchman Peak (7,709') from Sawtooth Mountain",
    "121920211238p.jpg": "Engle Peak (7,583') - Cabinet Mountains Wilderness",
    "121920211239p.jpg": "Ibex Peak (7,676') - Cabinet Mountains Wilderness",
    "121920211240p.jpg": "Middle Mountain in Proposed Scotchman Peaks Wilderness from Sawtooth Mountain",
    "121920211241p.jpg": "Peak 7,171' & Harrison Peak (7,292') - American Selkirks",
    "121920211242p.jpg": "Aerial View of Chimney Rock (7,124') & Mount Roothaan (7,326')",
    "121920211243p.jpg": "Chicago Peak (7,018') - Cabinet Mountains Wilderness",
    "121920211244p.jpg": "Lookout Mountain (6,727') Towers - American Selkirks",
    "121920211245p.jpg": "A Peak (8,634') & Snowshoe Peak (8,736') - Cabinet Mountains Wilderness",
    "1219202112451p.jpg": "Scotchman Peaks & Cabinet Mountains from The Mollies",
    "1221920211246p.jpg": "Cabinet Mountains Wilderness & HWY 56 from Pillick Ridge",
    "121920211247p.jpg": "Billiard Table Mountain (6,622') - Proposed Scotchman Peaks Wilderness",
    "121920211249p.jpg": "Mineral Ridge & Silver Tip Overlook",
    "121920211248p.jpg": "A Peak (8,634') & Snowshoe Peak (8,736') - Cabinet Mountains Wilderness",
    "121920211250p.jpg": "A Peak (8,634') - Cabinet Mountains Wilderness",
    "121920211251p.jpg": "Selkirk Crest - American Selkirks",
    "121920211252p.jpg": "Route to Parker Peak (7,670') - American Selkirks",
    "121920211253p.jpg": "Harrison Lake & Harrison Peak (7,292') - American Selkirks",
    "12192021103p.jpg": "Southern Selkirk Crest from Harrison Peak",
    "122220211132a.jpg": "A Peak (8,634') from Blackwell Glacier - Cabinet Mountains Wilderness",
    "122220211135a.jpg": "Lion Head Peak (7,288') from West Side - American Selkirks",
    "122220211121a.jpg": "Leigh Lake from Summit of Snowshoe Peak (8,638')",
    "122220211139a.jpg": "North Twin (7,599') & Hiker above Little Beehive Lake",
    "122220211155a.jpg": "Cirque of Spires Ridge on Climber's Trail to Lion Head",
    "122220211157a.jpg": "North End of Selkirks with Little Harrison Lake Below",
    "12232021708p.jpg": "Snowpatch Spire in the Canadian Bugaboos",
    "12232021709p_orig.jpeg": "Unnamed Mountain West of Rock Peak, Cliff Lake Area - Cabinet Mountains Wilderness",
    "12232021710p.jpg": "Stevens Peak (6,838') from Upper Stevens Lake",
    "12232021711p.jpg": "Abandon Peak (7,022') & Trail Guide - American Selkirks",
    "12232021712p.jpg": "Family Hiking to Stevens Peak from Gold Hill Trail, Idaho",
    "12232021713p.jpg": "North Face of Sawtooth Peak - South Fork Ross Creek Drainage",
    "12232021714p_orig.jpeg": "Stevens Peak (6,838') from Upper Stevens Lake",
    "12232021715p.jpg": "Scrambling South Face of Bockman Peak (8,174') above Leigh Lake",
    "12232021717p.jpg": "Lower Geiger Lake - Cabinet Mountains Wilderness",
    "12232021716p.jpg": "Burton Peak (6,844') above Kootenai National Wildlife Refuge",
    "12232021718p.jpg": "Pear Lake near Blossom Lakes, ID/MT Border",
    "12232021719p.jpg": "Stevens Peak (6,838') & Avalanche Paths",
    "12232021720p.jpg": "SE Face of Chicago Peak (7,018') above Cliff Lake - Cabinet Mountains Wilderness",
    "12232021721p.jpg": "Elephant Peak (7,938') from St. Paul Lake - Cabinet Mountains Wilderness",
    "3312022846p.jpg": "Phoebe's Tip, The Mollies, and Joe Peak from Priest Lake",
    "3312022847p.jpg": "The Lion Head Group - American Selkirks",
    "3312022851p.jpg": "Stevens Lake & Peak from State Line Ridge",
    "3312022859p.jpg": "Hooknose Mountain (7,210') above Pend Oreille River",
    "3312022903p.jpg": "Ward Peak (7,312') - Idaho/Montana Border",
    "3312022900p.jpg": "Chicago Peak (7,018') - Cabinet Mountains Wilderness",
    "3312022855p.jpg": "Leigh Lake, Snowshoe Peak (8,736'), & A Peak (8,634') - Cabinet Mountains Wilderness",
    "3312022853p.jpg": "Cedar Lake & Dome Mountain (7,560') - Cabinet Mountains Wilderness",
    "dscn0493.jpg": "East Face of Ridge between Chimney Rock & Mount Roothaan",
    "dscn0490.jpg": "Chimney Rock from East Pack River",
    "3272026600p.jpg": "Fitz Roy Massif - Patagonia, Argentina"
}

# Sub-categories
SELKIRKS = [
    "12182021658p.jpg", "12182021653p.jpg", "12182021648p.jpg", "12182021659p.jpg", "12182021700p.jpg",
    "12182021717p.jpg", "12182021721p.jpg", "12182021724p.jpg", "12182021739p.jpg", "12182021740p.jpg",
    "12182021752p.jpg", "12182021750p.jpg", "12182021751p.jpg", "12182021756p.jpg", "12182021800p.jpg",
    "121820218001p.jpg", "12182021808p.jpg", "12182021814p.jpg", "121920211224p.jpg", "121920211226p.jpg",
    "121920211228p.jpg", "121920211229p.jpg", "121920211241p.jpg", "121920211242p.jpg", "121920211244p.jpg",
    "121920211251p.jpg", "121920211252p.jpg", "121920211253p.jpg", "12192021103p.jpg", "122220211135a.jpg",
    "122220211139a.jpg", "122220211155a.jpg", "122220211157a.jpg", "12232021711p.jpg", "12232021716p.jpg",
    "3312022846p.jpg", "3312022847p.jpg", "3312022859p.jpg", "dscn0493.jpg", "dscn0490.jpg"
]

CABINETS = [
    "12182021720p.jpg", "12182021736p.jpg", "12182021747p.jpg", "12182021748p.jpg", "121820217531p.jpg",
    "12182021754p.jpg", "12182021755p.jpg", "121920211225p.jpg", "121920211230p.jpg", "121920211238p.jpg",
    "121920211239p.jpg", "121920211243p.jpg", "121920211245p.jpg", "121920211248p.jpg", "121920211250p.jpg",
    "122220211132a.jpg", "122220211121a.jpg", "12232021709p_orig.jpeg", "12232021715p.jpg", "12232021717p.jpg",
    "12232021720p.jpg", "12232021721p.jpg", "3312022900p.jpg", "3312022855p.jpg", "3312022853p.jpg"
]

SCOTCHMANS = [
    "12182021722p.jpg", "12182021741p.jpg", "12182021753p.jpg", "121920211231p.jpg", "121920211240p.jpg",
    "1219202112451p.jpg", "1221920211246p.jpg", "121920211247p.jpg", "12232021713p.jpg"
]

BITTERROOTS = [
    "202111271004.jpg", "12152021654p_orig.jpeg", "121920211249p.jpg", "12232021710p.jpg", "12232021712p.jpg",
    "12232021714p_orig.jpeg", "12232021718p.jpg", "12232021719p.jpg", "3312022851p.jpg", "3312022903p.jpg"
]

OTHER = [
    "12152021651p.jpg", "12182021716p.jpg", "12182021712p.jpg", "12182021735p.jpg", "12232021708p.jpg", "3272026600p.jpg"
]

def format_grid(img_list):
    out = ["<div class=\"grid cards\" markdown>", ""]
    for fn in img_list:
        cap = CAPTIONS.get(fn, "Mountain View")
        out.append(f"- ![{cap}](../assets/images/{fn})")
        out.append(f"  _{cap}_")
        out.append("")
    out.append("</div>")
    return "\n".join(out)

md = f"""---
title: Regional Mountains Photo Gallery
tags:
  - Peaks & Mountains
---

# Regional Mountains Photo Gallery

Explore high-resolution photography showcasing the rugged mountain ranges across North Idaho, Northwest Montana, Washington, and surrounding alpine regions. Click any image to view in high resolution via GLightbox.

---

## Featured Mountain Ranges Overview

| Mountain Range / Region | High Point / Peak Highlights | Primary Guides |
| :--- | :--- | :--- |
| **American Selkirks** | Parker Peak (7,670'), Chimney Rock (7,124') | [Selkirks Guide](../american-selkirks.md) |
| **Cabinet Mountains Wilderness** | Snowshoe Peak (8,736'), A Peak (8,634') | [Cabinet Wilderness Guide](../blog/posts/34-cabinet-mountain-wilderness.md) |
| **Proposed Scotchman Peaks** | Scotchman Peak (7,709') | [Scotchman Guide](../blog/posts/blog-58-proposed-scotchman-peak-wilderness.md) |
| **Bitterroots & State Line** | Stevens Peak (6,838'), Ward Peak (7,312') | [Silver Valley Guide](../silver-valley-area.md) |
| **Cascades & Canadian Rockies** | Fisher Peak (9,336'), Mount Hood (11,249') | [Regional Routes](../index.md) |

---

## American Selkirks Range

The American Selkirks stretch north from Coeur d'Alene into the Panhandle of Idaho, featuring iconic granite spires, alpine lakes, and rugged crests.

{format_grid(SELKIRKS)}

---

## Cabinet Mountains Wilderness

Located in Northwest Montana, the Cabinet Mountains Wilderness contains some of the highest, most glaciated peaks in the region, including Snowshoe Peak and A Peak.

{format_grid(CABINETS)}

---

## Proposed Scotchman Peaks Wilderness

Straddling the Idaho-Montana border near Clark Fork, the Scotchman Peaks feature steep vertical drops above Lake Pend Oreille and rugged alpine ridges.

{format_grid(SCOTCHMANS)}

---

## Bitterroot Mountains & State Line Peaks

Spanning the Coeur d'Alene and St. Joe river drainages along the Idaho-Montana border, the Bitterroot Mountains feature dramatic cirques, historic trail systems, and high elevation passes.

{format_grid(BITTERROOTS)}

---

## Cascades, Canadian Rockies & Further Afield

Highlights from neighboring ranges including the Canadian Rockies, the Cascades, the Bugaboos, and international expeditions.

{format_grid(OTHER)}
"""

with open("docs/mountains/index.md", "w", encoding="utf-8") as fp:
    fp.write(md)

print("Successfully generated docs/mountains/index.md")
