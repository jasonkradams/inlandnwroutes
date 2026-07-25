import os

content = """---
title: "Palouse River Paddle & Lyons Ferry Launch"
tags:
  - Paddling
  - Rivers
  - Washington Scablands
  - Palouse River
  - Lyons Ferry
  - Palouse Falls
stats:
  - label: Paddle Distance
    icon: map-marker-distance
    value: 14.0 miles round-trip
  - label: Elevation
    icon: terrain
    value: 543' at Lyons Ferry to 734' in upper canyon
  - label: Route Length
    icon: vector-square
    value: 7.0 miles one-way up Palouse River canyon
  - label: Launch GPS
    icon: crosshairs-gps
    value: Lyons Ferry 46°35'50" N 118°13'56" W | Palouse Canyon 46°39'04" N 118°13'27" W
  - label: Maps
    icon: map
    value: USGS Starbuck West Topo Map
notes:
  - label: "Franklin County Sheriff Emergency: 911 or (509) 545-3501"
    url: tel:5095453501
  - label: "Whitman County Sheriff Emergency: 911 or (509) 297-6266"
    url: tel:5092976266
  - label: NOAA Weather Forecast for Lyons Ferry / Palouse River
    url: https://forecast.weather.gov/MapClick.php?lat=46.5972&lon=-118.2322
---

The lower Palouse River paddle is one of the most spectacular canyon river journeys in the Inland Northwest. Launching from Lyons Ferry State Park at the confluence of the Snake and Palouse Rivers, paddlers navigate 7 miles upstream into a towering basalt gorge cut by Ice Age Floods toward the plunge pool below Palouse Falls.

!!! warning "River Currents, Whitewater & Wading Logistics"

    - **Rapids & Class Rating:** The lower river features Class I and II riffles, increasing to Class III in the upper canyon near Palouse Falls. Early summer high flows generate powerful currents over shallow rock bars.
    - **Lining & Wading:** In low water or shallow rapids, paddlers must wade or line boats upstream over gravel bars. Use your paddle extended as a guide to keep your boat off sharp basalt rocks.

---

## Route Description & Canyon Exploration

- **Lyons Ferry Confluence:** Launch at the WDFW / Lyons Ferry State Park boat ramp on the Snake River and turn north into the calm mouth of the Palouse River.
- **Palisade Canyon Walls:** As you progress upstream, sheer basalt cliffs rise hundreds of feet straight out of the water, creating a dramatic acoustics chamber for canyon wildlife.
- **Bat Colony at Mile 4.4:** A prime backcountry campsite sits on a grassy knoll 25 feet above the river at Mile 4.4. At dusk, tens of thousands of bats stream continuously out of high cliff fissures to forage over the river.
- **Fish & Wildlife:** Large native fish frequently breach in the quiet pools, while raptors and blue herons patrol the cliff ledges.

---

## Driving Directions

1. **From Spokane, WA:** Drive west on I-90 for approximately 60 miles to **Ritzville (Exit 221)**.
2. **South on WA-261:** Turn left (south) onto WA-261 South and drive past Washtucna for 6.4 miles.
3. **Continue on WA-261 S:** Stay on WA-261 South for another 13.8 miles down into the Snake River canyon.
4. **Arrival at Lyons Ferry:** Turn into **Lyons Ferry State Park** / WDFW boat launch area on the right before crossing the Snake River bridge.

---

## Local Nearby Attractions & Provisions

- **Palouse Falls State Park:** Visit the upper overlook to view Washington's official state waterfall plunging 198 feet into the basalt canyon.
- **Juniper Dunes Wilderness:** Explore the active sand dunes and old-growth juniper groves located southwest near Tri-Cities.
- **Provisions & Amenities:** Lyons Ferry KOA / Marina offers seasonal fuel, camp supplies, and food near the launch.
"""

with open("docs/paddle/washington/scablands/palouse-river-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized palouse-river-launch.md successfully")
