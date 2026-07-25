import os

md_content = """---
tags:
  - Peaks & Mountains
  - Moderate
  - Day Hiking
  - Backpacking
  - Equestrian
  - Mountain Biking
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking, Mountain Biking & Equestrian
  - label: Distance
    value: 2.0 Miles RT
  - label: Elevation Gain
    value: 1,838 ft
  - label: Trail Difficulty
    value: Moderate (Loose Summit Scree)
  - label: Topo Maps
    value: IPNF / Sandpoint Ranger District / Packsaddle Mountain Quad
  - label: Trailhead GPS
    value: '48°00''58"N 116°20''43"W'
  - label: Summit GPS
    value: '48°05''51"N 116°21''22"W'
  - label: Managing District
    value: Sandpoint Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Sandpoint Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Packsaddle Mountain (Trail #76)

![Granite boulder scree and high subalpine ridges from the summit of Packsaddle Mountain](../../../assets/images/1202022825p_orig.jpg)
_Granite boulder scree and high subalpine ridges from the summit of Packsaddle Mountain._

Rising prominently southeast of Lake Pend Oreille, **Packsaddle Mountain** is the highest peak in the immediate
surrounding range. Access via Trail #76 provides a rewarding 2.0-mile round-trip hike through subalpine forest to a
dramatic rock summit block offering 360-degree views across Idaho, Washington, Montana, and British Columbia.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or lost hiker, immediately dial **911** or contact the Bonner County
    Sheriff Dispatch at **[208-263-8417](tel:2082638417)**.

    - **USFS Managing Office:** Sandpoint Ranger District — **[208-263-5111](tel:2082635111)**.

!!! info "Panoramic Four-State & International Views"

    Because Packsaddle Mountain towers above neighboring ridges, the summit block delivers spectacular vistas spanning
    Lake Pend Oreille to the west, the Selkirk Range to the north, the Cabinet Mountains in Montana to the east, and the
    Canadian Rockies across the northern border.

Trail #76 begins southeast of the summit, meandering through a high-country forest of subalpine fir and lodgepole pine.
Two backcountry mountain springs are located along the route (though seasonal flow should not be relied upon). Near the
top, the trail emerges from the timber onto the massive rock summit block. A short scrambling path leads over loose scree
to the highest point.

---

## Trailhead & Forest Road Directions

1. From **Coeur d'Alene, Idaho**, drive north on **US-95** toward Sandpoint.
2. At the Bunco Road turnoff (opposite Silverwood Theme Park), turn right (east) onto **Bunco Road**.
3. In 2.2 miles, turn left (north) for 1.0 mile, then turn right (east) past Bunco Corners to the ORV parking area.
4. Continue east along **Forest Road 332** for approximately 25 miles.
5. Pass the junction for Powder Mountain Trail #452. Continue 2.0 miles past Trail #452 and turn onto spur
   **Forest Road 1073**.
6. Follow F.R. 1073 to the trailhead near North Gold Creek.

---

## Nearby Destinations & Attractions

- **Chilco Mountains & Chilco Peaks:** Nearby twin alpine peaks with scenic ridge trails.
- **Lake Pend Oreille:** Idaho's largest and deepest lake, located just west of the mountain.
- **Farragut State Park:** Major state park offering hiking, disc golf, and shoreline camping at Bayview.
- **The Green Monarchs:** Precipitous granite cliffs rising directly from Lake Pend Oreille's eastern shore.

---

## Hazards & Trail Safety

!!! warning "Forest Road & Summit Scree Caution"

    - **Forest Road 332 Drive:** F.R. 332 is a long, narrow, and dusty 25-mile gravel road. Drive carefully and watch
      for logging trucks and off-road vehicles.
    - **Loose Summit Scree:** The final scramble onto the summit block traverses steep, loose scree. Exercise caution with
      footing near ledge drop-offs.

---

## Refreshments & Nearby Dining

Popular dining stops in nearby Athol, Coeur d'Alene, and Sandpoint:

- **Moon Time:** Neighborhood pub in East Coeur d'Alene.
- **Franklin's Hoagies:** Sub sandwiches and hoagies.
- **Mexican Food Factory:** Regional Mexican restaurant.
- **Trails End Brewery:** Local craft brewery and pizzeria.

---

## Trip Planning & Weather

Check local mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Sandpoint / Packsaddle Mountain Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![The rocky summit ridge of Packsaddle Mountain peeking out above the forest canopy](../../../assets/images/1202022827p.jpg)
_The rocky summit ridge of Packsaddle Mountain peeking out above the forest canopy._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/packsaddle-mountain.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Updated image alt and caption text in packsaddle-mountain.md")
