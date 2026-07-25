import os

content = """---
title: "First Street Launch (St. Maries)"
tags:
  - Rivers
  - Paddling
  - St. Joe River
  - St. Maries River
  - North Idaho
  - Benewah County
stats:
  - label: Activity
    icon: bicycle
    value: Motorized & Non-Motorized Boat Launch / River Paddling
  - label: Location
    icon: map-marker
    value: 1st Street Landing, St. Maries, Benewah County, ID
  - label: Elevation
    icon: terrain
    value: 2,129'
  - label: River Access
    icon: vector-square
    value: Lower St. Joe River & St. Maries River Confluence
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°19'10" N 116°34'15" W
  - label: Maps
    icon: map
    value: USGS St. Maries Topo Map & Benewah County Parks
notes:
  - label: "Benewah County Sheriff Emergency: 911 or (208) 245-2555"
    url: tel:2082452555
  - label: City of St. Maries Parks Department
    url: https://www.stmariesid.org
  - label: NOAA Weather Forecast for St. Maries
    url: https://forecast.weather.gov/MapClick.php?lat=47.3146&lon=-116.5707
---

The First Street Launch is a convenient municipal water access site located at the northern terminus of 1st Street in downtown St. Maries, Idaho. Positioned along the lower St. Joe River near its confluence with the St. Maries River, this launch provides easy access for powerboats, kayaks, canoes, and stand-up paddleboards.

!!! info "City Park Amenities & Docks"

    The launch facility features a paved concrete boat ramp, boarding docks, paved vehicle and trailer parking, picnic tables, and restroom facilities managed by the City of St. Maries Parks Department.

---

## Paddling Routes & Exploration Options

- **St. Maries River Confluence:** Paddle a short distance upstream or downstream to explore the quiet junction where the St. Maries River flows into the St. Joe River.
- **Upstream St. Joe Paddle:** Travel east (upstream) along the calm, deep waters of the St. Joe River toward [Aqua Park Launch](aqua-park-launch.md) and [Cherry Bend Park Launch](cherry-bend-park-launch.md).
- **Downstream Lake Coeur d'Alene Route:** Paddle west (downriver) through the winding St. Joe River channel toward Heyburn State Park and the southern mouth of Lake Coeur d'Alene.

---

## Driving Directions

1. **From Coeur d'Alene / Harrison, ID:** Travel south on **ID-3 S** into downtown St. Maries.
2. **Turn onto 1st Street:** From Main Avenue or College Avenue in downtown St. Maries, turn north onto **1st Street**.
3. **Arrive at Launch:** Continue north on 1st Street to the river bank where the road terminates at the city boat ramp and parking area.

---

## Nearby Attractions & Provisions

- **St. Joe River Access Sites:** Explore [Aqua Park Launch](aqua-park-launch.md), [Cherry Bend Park Launch](cherry-bend-park-launch.md), and [Silvertip Landing](silvertip-landing.md).
- **Regional Destinations:** Heyburn State Park, St. Joe National Forest, and the Route of the Hiawatha rail-trail.
- **Rest & Provisions:** Full groceries, restaurants, breweries, gas, and outfitters are located right in downtown St. Maries within walking distance of the launch.
"""

with open("docs/paddle/idaho/st-joe-and-st-maries-rivers/first-street-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized first-street-launch.md successfully")
