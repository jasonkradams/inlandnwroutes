import os

content = """---
title: "Silvertip Landing (St. Joe River Access)"
tags:
  - Rivers
  - Paddling
  - St. Joe River
  - North Idaho
  - Shoshone County
stats:
  - label: Activity
    icon: bicycle
    value: River Paddling, Floating & Fly Fishing
  - label: Location
    icon: map-marker
    value: St. Joe River Road (USFS Rd 50), St. Joe National Forest, ID
  - label: Elevation
    icon: terrain
    value: 2,500'
  - label: River Section
    icon: vector-square
    value: Upper St. Joe Wild & Scenic River Corridor
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°16'30" N 115°45'15" W
  - label: Maps
    icon: map
    value: USFS St. Joe River Corridor Map & USGS Topo Maps
notes:
  - label: "Shoshone County Sheriff Emergency: 911 or (208) 556-1114"
    url: tel:2085561114
  - label: "Benewah County Sheriff Emergency: 911 or (208) 245-2555"
    url: tel:2082452555
  - label: USFS St. Joe Ranger District Recreation Alerts
    url: https://www.fs.usda.gov/recmain/ipnf/recreation
  - label: NOAA Weather Forecast for St. Joe River Corridor
    url: https://forecast.weather.gov/MapClick.php?lat=47.2750&lon=-115.7542
---

Silvertip Landing is a scenic river access point and campground along the upper St. Joe River in the Idaho Panhandle National Forests. Located along the paved St. Joe River Road (USFS Road 50) east of St. Maries, Silvertip Landing serves as an ideal launch or take-out site for drift boats, rafts, kayaks, and inner tubes floating the crystal-clear waters of "The Shadowy St. Joe."

!!! info "Wild & Scenic River Corridor & Camping"

    The upper St. Joe River is designated as a National Wild and Scenic River, world-famous for its blue-ribbon Westslope Cutthroat Trout fishery. Silvertip Campground features primitive riverside campsites, vault toilets, and direct gravel river access.

---

## River Section & Floating Logistics

- **Upper Float Options:** Put in upstream at Avery or Hells Gulch for a scenic Class I–II float down to Silvertip Landing.
- **Lower Float Options:** Launch at Silvertip Landing and float downriver toward Calder or St. Maries.
- **Cold Water & Seasonal Flows:** Peak spring runoff (May–June) generates fast Class II–III water; summer and early autumn bring calm, crystal-clear pools ideal for inner-tubing, recreational kayaking, and wade-fishing.

---

## Driving Directions

1. **From St. Maries, ID:** Drive east on **St. Joe River Road (USFS Road 50)** for approximately 35 miles toward Avery.
2. **Arrival at Silvertip:** Look for signs for **Silvertip Campground & Boat Launch** on the right (river side) of the road.
3. **From Avery, ID:** Drive west (downriver) on St. Joe River Road (USFS Road 50) for about 10 miles.

---

## Nearby Attractions & Provisions

- **St. Joe River Launches:** Explore [Aqua Park Launch](aqua-park-launch.md), [Cherry Bend Park Launch](cherry-bend-park-launch.md), and [First Street Launch](first-street-launch.md).
- **Historic Sites:** Visit the historic town of Avery, ID, the Avery Fish Hatchery, and the Route of the Hiawatha rail-trail.
- **Provisions:** Supplies, gas, and dining are available upstream at the Avery Store or downstream in St. Maries, ID.
"""

with open("docs/paddle/idaho/st-joe-and-st-maries-rivers/silvertip-landing.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized silvertip-landing.md successfully")
