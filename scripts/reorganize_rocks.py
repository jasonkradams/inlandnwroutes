import os

md_content = """---
tags:
  - Rocks & Geology
  - Photo Gallery
---

# Rocks

Click any image to enlarge and view high-resolution photo and caption.

## Photo Gallery

- ![Rock Face of North Twin, A.S. (Image by Chris H.)](../../assets/images/122220211159a.jpg)
- !["Lunar Landscape" on Top of Myrtle's Turtle East of Upper Two Mouth Lake (Image by Chris H.)](../../assets/images/122220211217p.jpg)
- ![Odd Rocks Along the Wigwams Trail, American Selkirks](../../assets/images/12262021343p.jpg)
- ![Cairns Along Ross Creek Cedars, P.S.P.W.](../../assets/images/12262021346p.jpg)
- ![Monkey Face in the Smith Rocks Climbing Area, Oregon](../../assets/images/12262021344p.jpg)
- ![The Chief Along Whisker Ridge Route Above Roman Nose Lakes, A.S.](../../assets/images/12262021347p.jpg)
- ![East-West Willow Ridge North of Stevens Peak from Upper Sanctuary at Lone Lake](../../assets/images/12262021350p_orig.jpeg)
- ![Beehive Dome at the Start of Beehive Lake Trail from Bottleneck Peak, A.S.](../../assets/images/1520221207p.jpg)
- ![Myrtle's Turtle Dome Above Upper Two Mouth Lake, A.S.](../../assets/images/1520221208p.jpg)
- ![Very Unusual Orbicular Rock Discovered Above Ball Lakes](../../assets/images/1520221119a.jpg)
- ![Gnarled Granite Rock Along the Trail Above Ball Lakes, A.S.](../../assets/images/1520221120a.jpg)
- ![Orbicular Rock Discovery in the American Selkirks Verified by USGS](../../assets/images/1520221118a.jpg)
- ![Bent Rocks at Hunt Lake, American Selkirks](../../assets/images/3312022858p.jpg)
- ![Granite Arch from The Mollies, American Selkirks](../../assets/images/3312022843p.jpg)
- ![The "Castles" at Palouse Falls, WA Scablands](../../assets/images/3312022848p.jpg)
- ![The Fin Between Little Harrison Lake (L) and Beehive Lake (R), American Selkirks](../../assets/images/3312022850p.jpg)
- ![A Whale Breaches the Surface of Trout Lake, A.S.](../../assets/images/3312022849p.jpg)
- ![Big Rock at Dishman Hills Conservancy with Ravens Overhead](../../assets/images/112026237p.jpg)
- ![Granite Rock Formations in the American Selkirks](../../assets/images/112026428p.jpg)
- ![Heart-Shaped Granite Rock Formation](../../assets/images/112026431p.jpg)

---

## Rare Orbicular Rock Discovery

![Rare Orbicular Rock (Orbiculite) specimen discovered above Ball Lakes in the American Selkirks](../../assets/images/img-1729.jpg)
_Rare Orbicular Rock (Orbiculite) specimen discovered above Ball Lakes in the American Selkirks._

On an exploratory hike led in the American Selkirks above Ball Lakes, fellow hiker Darcy Varone discovered a rock formation that none of us had ever encountered before. Detailed field photographs and geological research revealed that this specimen is an **Orbicular Rock** (or *Orbiculite*)—an exceedingly rare igneous rock texture characterized by concentric spherical shells, documented in slightly more than 100 locations worldwide.

Dr. Steven Box, PhD Research Geologist with the U.S. Geological Survey (USGS) in Spokane, officially verified the specimen as authentic orbicular rock. USGS technical papers confirm that this American Selkirks discovery is extraordinarily rare, with the nearest documented regional occurrence located in Nevada.
"""

target_path = "docs/gallery/categories/rocks.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized rocks.md successfully")
