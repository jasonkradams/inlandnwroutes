import os

content = """---
title: "West Medical Lake Launch"
tags:
  - Lakes
  - Paddling
  - Washington Scablands
  - Spokane County
  - Medical Lake
stats:
  - label: Paddle Distance
    icon: map-marker-distance
    value: 3.7 miles round-trip
  - label: Elevation
    icon: terrain
    value: 2,438'
  - label: Dimensions
    icon: vector-square
    value: 1.6 miles long & 205.8 acres
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°33'49" N 117°42'15" W
  - label: Maps
    icon: map
    value: USGS Medical Lake Topo Map
notes:
  - label: "Spokane County Sheriff Emergency: 911 or (509) 477-2240"
    url: tel:5094772240
  - label: NOAA Weather Forecast for West Medical Lake
    url: https://forecast.weather.gov/MapClick.php?lat=47.5645&lon=-117.7018
---

West Medical Lake is a tranquil 205.8-acre body of water situated immediately west of the city of Medical Lake in Spokane County. Spanning 1.6 miles long, the lake offers quiet non-motorized paddling along largely undeveloped, tree-lined shorelines.

!!! info "Public Launch Access"

    Access is provided via a public WDFW boat launch on the east shore off West Fancher Road. The lake features very light residential development compared to surrounding Spokane County lakes.

---

## Description & Lake Overview

West Medical Lake is renowned for its quiet waters, trout fishing, and abundant waterfowl. Paddlers exploring the 3.7-mile perimeter can enjoy views of rocky outcroppings, surrounding ponderosa pine hillsides, and the historic brick campus of Eastern State Hospital rising in the distance.

---

## Driving Directions

1. **From Spokane, WA:** Drive west on I-90 for approximately 12 miles to **Exit 272 (WA-902 / Medical Lake)**.
2. **Follow WA-902:** Continue on WA-902 West into the town of Medical Lake.
3. **Turn onto Fancher Road:** At the south end of town, turn left onto **Fancher Road**.
4. **Access Launch:** Continue onto **West Fancher Road** and turn right into the WDFW public boat launch parking lot.

---

## Nearby Attractions & Provisions

- **Nearby Waterways:** Combine your paddle with visits to Medical Lake, Clear Lake, Silver Lake, or Turnbull National Wildlife Refuge.
- **Rest & Provisions:** Local dining, coffee, and supplies are available in downtown Medical Lake and nearby Cheney, WA (Lenny's).
"""

with open("docs/paddle/washington/scablands/west-medical-lake.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized west-medical-lake.md successfully")
