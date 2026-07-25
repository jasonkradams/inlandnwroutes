import os

content = """---
title: "Upper Twin Lakes Launch"
tags:
  - Lakes
  - Paddling
  - North Idaho
  - Twin Lakes
  - Kootenai County
stats:
  - label: Activity
    icon: bicycle
    value: Non-Motorized & Motorized Paddling / Fishing
  - label: Location
    icon: map-marker
    value: Upper Twin Lake, Rathdrum Prairie / Spirit Lake, ID
  - label: Elevation
    icon: terrain
    value: 2,313'
  - label: Dimensions
    icon: vector-square
    value: 525 acres (connected to Lower Twin Lake via 0.5-mile channel)
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°53'45" N 116°54'30" W
  - label: Maps
    icon: map
    value: USGS Spirit Lake & Rathdrum Topo Maps
notes:
  - label: "Kootenai County Sheriff Emergency: 911 or (208) 446-1300"
    url: tel:2084461300
  - label: Idaho Department of Fish and Game Access Info
    url: https://idfg.idaho.gov/access/twin-lakes
  - label: NOAA Weather Forecast for Twin Lakes
    url: https://forecast.weather.gov/MapClick.php?lat=47.8856&lon=-116.8978
---

Upper Twin Lake (525 acres) is the northern basin of the Twin Lakes system in Kootenai County, Idaho. Tucked beneath the timbered slopes of Mt. Spokane's eastern foothills and the Rathdrum Prairie, Upper Twin Lake is connected to Lower Twin Lake (390 acres) by a scenic 0.5-mile serpentine channel known as "The Narrows."

!!! info "IDFG Public Boat Ramp & Access"

    Public water access is available at the Idaho Department of Fish and Game (IDFG) boat launch on the east shore near the channel entrance. A valid Idaho Invasive Species Sticker is required for all non-motorized and motorized watercraft.

---

## Description & Exploration Options

- **Upper Lake Loop:** Paddle the quiet northern shoreline of Upper Twin Lake, exploring timbered bays, wetland inlets, and mountain reflections beneath the Selkirk foothills.
- **The Narrows Channel:** Navigate south through the winding 0.5-mile channel connecting Upper and Lower Twin Lakes. The channel offers calm, sheltered water lined with lily pads, cattails, and excellent birdwatching for osprey, Great Blue Herons, and waterfowl.
- **Full Twin Lakes Traverse:** Combine both lakes via the channel for a 5- to 7-mile round-trip paddle covering over 900 total surface acres.

---

## Driving Directions

1. **From Coeur d'Alene / Post Falls, ID:** Travel north on **ID-41 N** toward Rathdrum for approximately 12 miles.
2. **Turn onto Twin Lakes Road:** From Rathdrum, head northwest on **Twin Lakes Road** toward Spirit Lake.
3. **Access Launch:** Turn left onto **Fish Hatchery Road** or **Twin Lakes Beach Road** to reach the IDFG public boat launch on the east shore.

---

## Nearby Attractions & Provisions

- **Connected Waterways:** Explore [Lower Twin Lakes Launch](lower-twin-lakes-launch.md) and [Twin Lakes Narrows](twin-lakes-narrows.md).
- **Nearby Lakes:** Spirit Lake, Hauser Lake, and Mt. Spokane State Park.
- **Rest & Provisions:** Gas, groceries, and dining are available 10 minutes south in Rathdrum, ID, or north in Spirit Lake, ID.
"""

with open("docs/paddle/idaho/twin-lakes/upper-twin-lakes-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized upper-twin-lakes-launch.md successfully")
