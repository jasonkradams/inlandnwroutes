import os

content = """---
title: "Lower Twin Lakes Launch"
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
    value: Lower Twin Lake, Rathdrum / Spirit Lake, ID
  - label: Elevation
    icon: terrain
    value: 2,313'
  - label: Dimensions
    icon: vector-square
    value: 390 acres (connected to Upper Twin Lake via 0.5-mile channel)
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°52'30" N 116°53'45" W
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

Lower Twin Lake (390 acres) forms the southern basin of the Twin Lakes system in Kootenai County, Idaho. Surrounded by timbered slopes and summer lake homes, Lower Twin Lake features clear water and a sheltered shoreline ideal for recreational paddling, fishing, and kayaking.

!!! info "IDFG Boat Ramp & Watercraft Regulations"

    Public access is provided via an Idaho Department of Fish and Game (IDFG) boat ramp on the southeast shore. An Idaho Invasive Species Sticker is required for all watercraft launched on the lake.

---

## Description & Lake Highlights

- **Recreational Paddling:** Lower Twin Lake offers calm early-morning water popular for canoes, kayaks, and stand-up paddleboards.
- **Warm-Water Fishery:** Highly regarded for bass (largemouth and smallmouth), yellow perch, black crappie, and stocked rainbow trout along weed lines.
- **Channel Access to Upper Lake:** Paddlers can travel north up the lake into [Twin Lakes Narrows](twin-lakes-narrows.md), a 0.5-mile marshy channel leading directly into [Upper Twin Lakes Launch](upper-twin-lakes-launch.md) (525 acres).

---

## Driving Directions

1. **From Coeur d'Alene / Post Falls, ID:** Head north on **ID-41 N** for approximately 12 miles to Rathdrum.
2. **Twin Lakes Road:** Turn northwest onto **Twin Lakes Road** toward Spirit Lake.
3. **Access Launch:** Turn left onto **Lower Twin Lakes Road** to reach the IDFG public boat ramp parking area on the southeast shoreline.

---

## Nearby Attractions & Provisions

- **Connected Waterways:** Explore [Twin Lakes Narrows](twin-lakes-narrows.md) and [Upper Twin Lakes Launch](upper-twin-lakes-launch.md).
- **Regional Lakes:** Spirit Lake, Hauser Lake, and Mt. Spokane State Park.
- **Rest & Provisions:** Full groceries, gas, and local dining are available 10 minutes south in Rathdrum, ID, or north in Spirit Lake, ID.
"""

with open("docs/paddle/idaho/twin-lakes/lower-twin-lakes-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized lower-twin-lakes-launch.md successfully")
