import os

content = """---
title: "Cherry Bend Park Launch (St. Joe River Access)"
tags:
  - Rivers
  - Paddling
  - St. Joe River
  - North Idaho
  - Benewah County
stats:
  - label: Activity
    icon: bicycle
    value: River Paddling, Powerboating & Floating
  - label: Location
    icon: map-marker
    value: St. Joe River Road (USFS Rd 50), St. Maries, Benewah County, ID
  - label: Elevation
    icon: terrain
    value: 2,135'
  - label: River Access
    icon: vector-square
    value: Lower St. Joe River Channel
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°19'05" N 116°30'20" W
  - label: Maps
    icon: map
    value: USGS St. Maries Topo Map & Benewah County Parks
notes:
  - label: "Benewah County Sheriff Emergency: 911 or (208) 245-2555"
    url: tel:2082452555
  - label: Benewah County Parks & Recreation
    url: https://www.idaho.gov
  - label: NOAA Weather Forecast for St. Maries / St. Joe River
    url: https://forecast.weather.gov/MapClick.php?lat=47.3146&lon=-116.5055
---

Cherry Bend Boat Park is a popular riverfront park and public boat launch situated along a scenic meander of the lower St. Joe River, just 4 miles east of St. Maries, Idaho. Surrounded by mature shade trees and green lawns, Cherry Bend is a favorite access point for powerboating, river floating, kayaking, and fishing.

!!! info "Park Amenities & Facility Info"

    Managed by Benewah County, the park features a paved concrete boat ramp, boarding dock, spacious vehicle and trailer parking, picnic tables, shade ramadas, and vault restrooms.

---

## River Floating & Navigation Options

- **Downstream Float to St. Maries:** Launch at Cherry Bend and float 4 miles downriver along the gentle, meandering St. Joe River channel to [First Street Launch](first-street-launch.md) in downtown St. Maries.
- **Upstream Take-Out Point:** Serve as a convenient take-out location for paddle trips originating upstream at [Silvertip Landing](silvertip-landing.md) or Calder.
- **Powerboating to Lake Coeur d'Alene:** Boaters can head downstream through the St. Joe River channel past St. Maries and Heyburn State Park to reach the southern end of Lake Coeur d'Alene.

---

## Driving Directions

1. **From St. Maries, ID:** Drive east on **St. Joe River Road (USFS Road 50)** for approximately 4 miles.
2. **Arrive at Launch:** Turn right into the **Cherry Bend Boat Park** entrance on the south (river) side of the highway.

---

## Nearby Attractions & Provisions

- **St. Joe River Access Sites:** Explore [First Street Launch](first-street-launch.md), [Aqua Park Launch](aqua-park-launch.md), and [Silvertip Landing](silvertip-landing.md).
- **Regional Destinations:** Heyburn State Park, St. Joe National Forest, and the Route of the Hiawatha rail-trail.
- **Rest & Provisions:** Groceries, restaurants, gas, and outfitters are located 10 minutes west in downtown St. Maries, ID.
"""

with open("docs/paddle/idaho/st-joe-and-st-maries-rivers/cherry-bend-park-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized cherry-bend-park-launch.md successfully")
