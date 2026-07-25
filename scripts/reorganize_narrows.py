import os

content = """---
title: "Twin Lakes Narrows Channel Guide"
tags:
  - Lakes
  - Paddling
  - Channels
  - North Idaho
  - Twin Lakes
  - Kootenai County
stats:
  - label: Activity
    icon: bicycle
    value: Non-Motorized Paddling & Wildlife Viewing
  - label: Location
    icon: map-marker
    value: The Narrows (Connecting Upper & Lower Twin Lakes), Kootenai County, ID
  - label: Elevation
    icon: terrain
    value: 2,313'
  - label: Dimensions
    icon: vector-square
    value: 0.5 miles long, 30–100' wide
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°53'15" N 116°54'45" W
  - label: Maps
    icon: map
    value: USGS Spirit Lake & Rathdrum Topo Maps
notes:
  - label: "Kootenai County Sheriff Emergency: 911 or (208) 446-1300"
    url: tel:2084461300
  - label: IDFG Access & Boating Rules
    url: https://idfg.idaho.gov/access/twin-lakes
  - label: NOAA Weather Forecast for Twin Lakes
    url: https://forecast.weather.gov/MapClick.php?lat=47.8856&lon=-116.8978
---

"The Narrows" is a tranquil 0.5-mile serpentine waterway connecting Upper Twin Lake (525 acres) and Lower Twin Lake (390 acres) in Kootenai County, Idaho. Flanked by lush cattail marshes, water lilies, and timbered banks, this sheltered channel is one of the premier non-motorized paddling corridors in North Idaho.

!!! warning "Strict No-Wake Zone & Waterway Rules"

    The entire Narrows channel is a designated **5 MPH No-Wake Zone** enforced by Kootenai County Sheriff Marine Patrol to prevent shoreline erosion, protect wetland bird habitat, and ensure paddler safety.

---

## Description & Channel Highlights

- **Sheltered Water:** The channel remains calm and protected even when mountain winds whip up chop on the open lakes, making it perfect for stand-up paddleboards, canoes, and beginner kayakers.
- **Abundant Wildlife:** The marshy shoreline provides critical nesting habitat for osprey, bald eagles, Great Blue Herons, red-winged blackbirds, turtles, and beaver.
- **Inter-Lake Navigation:** Paddlers can launch from either lake and use The Narrows to complete a full 900-acre Twin Lakes circuit.

---

## Driving Directions & Access Points

1. **From Coeur d'Alene / Post Falls, ID:** Drive north on **ID-41 N** for 12 miles to Rathdrum.
2. **Twin Lakes Road:** Turn northwest onto **Twin Lakes Road** toward Spirit Lake and proceed 5 miles.
3. **Channel Access:** The Narrows bridge crosses the channel between the lakes. Public boat ramps are located nearby at [Upper Twin Lakes Launch](upper-twin-lakes-launch.md) (north) and [Lower Twin Lakes Launch](lower-twin-lakes-launch.md) (south).

---

## Nearby Attractions & Provisions

- **Connected Waterways:** Explore [Upper Twin Lakes Launch](upper-twin-lakes-launch.md) and [Lower Twin Lakes Launch](lower-twin-lakes-launch.md).
- **Regional Destinations:** Spirit Lake, Hauser Lake, and Mt. Spokane State Park.
- **Rest & Provisions:** Gas, groceries, and dining are available 10 minutes south in Rathdrum, ID, or north in Spirit Lake, ID.
"""

with open("docs/paddle/idaho/twin-lakes/twin-lakes-narrows.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized twin-lakes-narrows.md successfully")
