import os

md_content = """---
tags:
  - Peaks & Mountains
  - Difficult
  - Day Hiking
  - Backpacking
  - Mountain Biking
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking & Mountain Biking
  - label: Distance
    value: 9.6 Miles RT (Standard Ridge Route)
  - label: Elevation Gain
    value: 3,321 ft
  - label: Summit Elevation
    value: 6,349 ft (Big Dick Point 5,419 ft)
  - label: Trail Difficulty
    value: Difficult / Strenuous (Unrelenting Incline)
  - label: Topo Maps
    value: IPNF / St. Joe River Ranger District / Shefoot Mt. Quad
  - label: Trailhead GPS
    value: '47°20''00"N 115°46''16"W'
  - label: Managing District
    value: Coeur d'Alene River / St. Joe River Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Coeur d'Alene River Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Shefoot Mountain (6,349') & Big Dick Point (5,419')

![Shefoot Mountain and high-country ridge in the St. Joe region](../../../assets/images/img-0081_93.jpg)
_Shefoot Mountain and high-country ridge in the St. Joe region._

Rising high above the St. Joe River drainage and Moon Pass corridor, **Shefoot Mountain (6,349')** and its lower spur,
**Big Dick Point (5,419')**, offer one of the most challenging and rewarding ridge climbs in Shoshone County. Featuring an
unrelenting 3,321-foot vertical climb along Trail #189, the route rewards hikers with sweeping vistas of the Silver
Valley and vibrant early-summer wildflower displays.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or lost hiker, immediately dial **911** or contact the Shoshone County
    Sheriff Dispatch at **[208-556-1114](tel:2085561114)**.

    - **USFS Managing Office:** Coeur d'Alene River Ranger District — **[208-752-1221](tel:2087521221)** /
      **[208-769-3000](tel:2087693000)**.

!!! tip "Early-Summer Wildflowers & Dry Ridge Advice"

    - **Wildflower Season:** In June and early July, the upper slopes and alpine meadows around Shefoot Mountain are
      blanketed in blooming Beargrass and mountain wildflowers.
    - **No Water on Ridge:** There are no reliable water sources along the 4.8-mile singletrack ridge.
      **Carry all necessary water.**

Trail #189 climbs steadily and steeply for 2.4 miles from Moon Pass Road up a sharp ridge to **Big Dick Point (5,419')**.
From this viewpoint, the trail drops approximately 300 feet to a junction with Trail #501 before climbing steeply once
again to the summit of Shefoot Mountain.

---

## Route Options

### Option 1: Standard Ridge Climb via Trail #189 (9.6 Miles RT)

The primary hiking route ascends Trail #189 directly from the Moon Pass Road trailhead:

- **Distance:** 4.8 miles one-way (9.6 miles round-trip) with 3,321 feet of net elevation gain.
- **Highlights:** Uninterrupted panoramic viewpoints along the crest of Big Dick Point and the Shefoot summit block.

### Option 2: Long Liz Trail #190 Loop

For a varied loop hike or mountain bike ride, combine Trail #189 with **Long Liz Trail #190**:

- **Recommended Direction:** Ascend via **Long Liz Trail #190** and descend via **Trail #189 (Big Dick Point)**. Because
  the Big Dick Point trail is significantly steeper, descending it provides a cleaner climb up Long Liz.

### Option 3: Upper Access & Off-Trail Loop from Turkey Point

For hikers seeking shorter mileage or expansive ridge views without the full 3,300-foot climb:

- **High-Drive Access:** Follow Moon Pass Road #456 south past the Route of the Hiawatha tunnels to the upper forest
  roads near **Turkey Point**.
- **Off-Trail Ridge Loop:** Park near Turkey Point and explore a 4.0-mile off-trail loop traversing the high ridge
  surrounding Shefoot Mountain.

---

## Trailhead Directions

1. From **Wallace, Idaho**, take the first I-90 exit and turn left onto **Front Street**.
2. Proceed several blocks and turn right onto **2nd Street**.
3. Turn right onto **Bank Street**, then left onto **King Street**, which leads directly to **Placer Street**.
4. Follow Placer Street as it transitions into **Moon Pass Road #456**.
5. Drive south on F.R. 456 past the **Pearson Trailhead** (southern terminus of the Route of the Hiawatha).
6. Drive 1.35 miles past the Pearson turn-off to arrive at the signed **Big Dick Point Trailhead (Trail #189)**.

---

## Nearby Destinations & Attractions

- **Route of the Hiawatha:** World-famous 15-mile rail-trail featuring the 1.6-mile Taft Tunnel and steel trestles.
- **Pearson Trailhead & Avery:** Historic railroad towns along the St. Joe River.
- **Pulaski Tunnel Trail:** Historic 2.0-mile trail in Wallace commemorating Edward Pulaski and the 1910 Great Fire.
- **Hobo Cedar Grove Botanical Area:** 240-acre old-growth cedar grove with accessible boardwalk trails.

---

## Trail Hazards & Safety Considerations

!!! warning "Steep Terrain & Off-Road Motorized Use"

    - **Steep Pitch:** Trail #189 features continuous steep pitches with loose soil and rock. Trekking poles are highly
      recommended for the descent.
    - **Motorized Trail Use:** Trail #189 and connecting ridge trails are popular among experienced off-road
      motorcyclists. Listen carefully for approaching bikes and step off the trail on steep drop-offs.

---

## Refreshments & Nearby Dining

After hiking, explore local dining options in Wallace and Kellogg:

- **1313 Club:** Historic saloon and grill in downtown Wallace.
- **Pizza Factory:** Family dining in Wallace.
- **Radio Brewing Company:** Craft brewery and gastropub in Kellogg.

---

## Trip Planning & Weather

Check local weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Wallace / Moon Pass Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)
"""

target_path = "docs/hike/idaho/north-idaho-hikes/shefoot-mountain.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Updated line wrapping in shefoot-mountain.md")
