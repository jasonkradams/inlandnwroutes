import os

content = """---
title: "Marshall Lake Launch"
tags:
  - Lakes
  - Paddling
  - Pend Oreille County
  - Eastern Washington
  - Selkirk Foothills
stats:
  - label: Paddle Distance
    icon: map-marker-distance
    value: 3.5 miles round-trip
  - label: Elevation
    icon: terrain
    value: 1,990'
  - label: Dimensions
    icon: vector-square
    value: 190 acres (1.0 mile to North Bay, 0.75 mile to Northeast Bay)
  - label: Launch GPS
    icon: crosshairs-gps
    value: 48°15'23" N 117°41'38" W
  - label: Maps
    icon: map
    value: USGS Bead Lake Topo Map
notes:
  - label: "Pend Oreille County Sheriff Emergency: 911 or (509) 447-3151"
    url: tel:5094473151
  - label: NOAA Weather Forecast for Marshall Lake
    url: https://forecast.weather.gov/MapClick.php?lat=48.2564&lon=-117.2023
---

Marshall Lake is a peaceful, tree-lined mountain lake nestled in the timbered foothills of the American Selkirk Range north of Newport, Washington. Spanning 190 acres at 1,990 feet of elevation, the lake offers quiet paddling away from heavy motorboat traffic.

!!! info "Public Launch & Bay Exploration"

    The public boat launch provides access to two scenic arms: North Bay (extending 1.0 mile north) and Northeast Bay (extending 0.75 miles northeast). The combined paddle shoreline totals approximately 3.5 miles round-trip.

---

## Description & Lake Overview

Surrounded by mixed conifer forests of Douglas fir, western red cedar, and larch, Marshall Lake is ideal for canoes, kayaks, and stand-up paddleboards. Paddlers can explore hidden coves, observe nesting waterfowl, and enjoy scenic views toward the nearby Selkirk Mountains.

---

## Driving Directions

1. **From Newport, WA:** Travel south on US-2 for 0.5 miles.
2. **Le Clerc Road:** Turn left onto **Le Clerc Road (County Rd 9305)** and continue for 2.7 miles.
3. **Bead Lake Road:** Turn right onto **Bead Lake Road (USFS Rd 3029)** and drive 2.5 miles.
4. **Marshall Lake Road:** Turn right onto **Marshall Lake Road** and proceed for 1.4 miles.
5. **Marshall Lake Drive:** Turn left onto **Marshall Lake Drive** and drive 0.6 miles to the public launch at Marshall Lake.

---

## Nearby Attractions & Provisions

- **Nearby Waterways:** Combine your paddle with visits to nearby [Bead Lake Launch Guide](../eastern-washington/bead-lake-launch.md), Diamond Lake, or the Pend Oreille River.
- **Scenic Highlights:** Explore Sweet Creek Falls near Ione, WA, or drive scenic USFS backcountry roads into the Kaniksu National Forest.
- **Rest & Provisions:** Full services, groceries, gas, and dining are available 15 minutes south in Newport, WA.
"""

with open("docs/paddle/washington/scablands/marshall-lake-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized marshall-lake-launch.md successfully")
