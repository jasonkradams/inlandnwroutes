import os

md_content = """---
description: >-
  Your comprehensive guide to hiking, scrambling, skiing, paddling, and exploring the wilderness of the Inland
  Northwest.
---

# Welcome to Inland NW Routes

## Your Comprehensive Guide to Hiking, Scrambling, Skiing, and Paddling in the Inland Northwest

Welcome to Inland NW Routes—your community resource for exploring the alpine peaks, glaciated lakes, rivers, and
backcountry trails of North Idaho, Western Montana, Eastern Washington, Oregon, and the Canadian Rockies.

---

!!! danger "Red Alert: Active Forest & Trail Closures"

    - **Hawk Creek Falls S.P.:** Closed April 16 through October 6 for park improvements (includes water access).
    - **Forest Road #239:** Closed at Jeru Creek.
    - **Lightning Creek Road #419 & Trestle Creek Road #275:** Closed through December 11, 2026 or longer (includes
      Beetop Mountain access).
    - **Forest Road #805 (Settlers Grove):** Washed out and closed to vehicular traffic.
    - **Harrison Lake & Peak Access Note:** Harrison Lake and Peak can be accessed via Trail #6 from the Myrtle Creek
      drainage via Forest Road #633.

    *Safety Notice:* Please consult the USFS Ranger District links and contact numbers provided on each route guide
    before heading into the field. Access violations carry heavy fines and endanger search and rescue personnel.

---

## Explore Our Wilderness Portals

<div class="grid cards" markdown>

- :material-hiking: __Hiking & Scrambling__

    ---

    Explore detailed trail stats, summit routes, and geology reports for the Selkirks, Cabinets, Bitterroots, and
    Canadian Rockies.

    [:octicons-arrow-right-24: View Hiking Guides](hike/index.md)

- :material-kayaking: __Paddling & Kayaking__

    ---

    Launch sites, quiet water routes, and river paddling guides across CDA Lake, the Chain Lakes, Pend Oreille, and
    Spokane River.

    [:octicons-arrow-right-24: View Paddling Guides](paddle/index.md)

- :material-ski: __Skiing & Winter Sports__

    ---

    Backcountry powder routes, alpine ski resort guides, Nordic trails, and avalanche safety resources across the US
    and BC.

    [:octicons-arrow-right-24: View Ski Guides](ski/index.md)

- :material-waterfall: __Regional Waterfalls__

    ---

    Comprehensive guide to stunning cascades, waterfall hikes, and hidden river falls throughout Washington, Idaho,
    and Montana.

    [:octicons-arrow-right-24: View Waterfall Guides](waterfalls/index.md)

</div>

---

## Our Mission & Trip Preparation

!!! info "🌲 Our Purpose & Mission"

    Our purpose is to show outdoor enthusiasts where to hike, scramble, ski, paddle, and explore in the Inland
    Northwest. By sharing our knowledge, we hope to inspire people to recreate responsibly and advocate for the
    preservation of these special wilderness places.

!!! tip "🥾 Before Heading Out: Call the Ranger District"

    Please contact the relevant USFS Ranger District or Forest Supervisor's office a few days before your trip to
    verify current trail conditions, road washouts, and active wildfire alerts. Managing agency contact numbers are
    listed on each route page.

---

## Words of Inspiration

!!! quote "Inland NW Routes Philosophy"

    > *"Wondering is wanderful."*
    > — **Chic Burge**

    > *"If you are working on something that you really care about, you don't have to be pushed. The vision pulls you."*
    > — **Steve Jobs**

*This shared passion guided Chic Burge and David Crafton while building Inland NW Routes. Thank you for exploring with us!*
"""

with open("docs/index.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Updated docs/index.md for linting compliance")
