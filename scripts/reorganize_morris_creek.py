import os

md_content = """---
tags:
  - Trails & Scrambles
  - Easy
  - Old Growth & Cedars
  - Day Hiking
stats:
  - label: Activity Type
    value: Old-Growth Cedar Forest Walk
  - label: Distance
    value: 0.75 Miles RT
  - label: Elevation Gain
    value: Minimal
  - label: Trail Difficulty
    value: Easy (Accessible Nature Trail)
  - label: Reserve Size
    value: 80 Acres
  - label: Topo Maps
    value: Elk Creek Falls Quad / USFS
  - label: Trailhead GPS
    value: '46°51''20"N 116°12''37"W'
  - label: Managing District
    value: Palouse Ranger District
notes:
  - label: Nez Perce-Clearwater National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/nezperceclearwater/alerts-notices
  - label: USFS Palouse Ranger District
    url: https://www.fs.usda.gov/nezperceclearwater
---

# Morris Creek Old Growth Cedar Grove

![Morris Creek Old Growth Cedar Grove near Elk River, Idaho](../../../assets/images/img-0081_88.jpg)
_Morris Creek Old Growth Cedar Grove near Elk River, Idaho._

Nestled in the lush river drainages near Elk River, Idaho, the **Morris Creek Old Growth Cedar Grove** is an 80-acre
protected botanical sanctuary featuring towering western red cedars over **500 years old**. An easy 0.75-mile round-trip
interpretive trail weaves through the ancient rainforest, offering an accessible nature walk suitable for all ages.

---

## Overview & Trail Description

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of an emergency, injury, or search and rescue request, immediately dial **911** or contact the Clearwater
    County Sheriff Dispatch at **[208-476-4521](tel:2084764521)**.

    - **USFS Managing Office:** Palouse Ranger District (Potlatch, ID) — **[208-875-1131](tel:2088751131)**.

!!! info "500-Year-Old Ancient Forest Sanctuary"

    Although modest in size at just 80 acres, the Morris Creek Cedar Grove stands as one of North Idaho's premier
    remnants of primeval inland rainforest. The short 0.75-mile loop trail wanders beneath a dense canopy of ancient
    cedars, ferns, and mosses along the banks of Morris Creek.

Combining a stop at Morris Creek with nearby destinations like **Elk Creek Falls** or the **Giant Western Red Cedar**
makes a rewarding day trip through the Clearwater region.

---

## Trailhead Directions

1. From **Elk River, Idaho**, head north along **Forest Road 382** (Elk River Road).
2. Continue past the Elk Creek Falls National Recreation Area turn-off.
3. Turn onto **Forest Road 1969** and proceed a short distance to the signed trailhead parking area for Morris Creek.

---

## Nearby Destinations & Ancient Cedar Groves

- **Elk Creek Falls National Recreation Area:** 3-tiered waterfall trail system located just minutes south.
- **Giant Western Red Cedar:** Champion-sized western red cedar tree located nearby in the Clearwater National Forest.
- **Hobo Cedar Grove Botanical Area:** 240-acre ancient cedar sanctuary with an accessible boardwalk loop.
- **Dworshak Reservoir:** Major recreational lake offering boating, fishing, and shoreline camping.

---

## Seasonal Hazards & Trail Advice

!!! warning "Inland Rainforest Insects & Layering"

    - **Summer Mosquitoes:** The damp, shaded old-growth creek basin breeds heavy mosquito populations during late
      spring and early summer. Long sleeves, pants, insect repellent, and a head net are strongly recommended.
    - **Trail Surface:** The forest floor trail remains damp year-round; wear sturdy footwear with good traction over
      exposed tree roots.

---

## Trip Planning & Weather

Check local weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Elk River / Orofino Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Nez Perce-Clearwater National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/nezperceclearwater/alerts-notices)
"""

target_path = "docs/hike/idaho/north-idaho-hikes/morris-creek-old-growth-cedar-grove.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized morris-creek-old-growth-cedar-grove.md successfully")
