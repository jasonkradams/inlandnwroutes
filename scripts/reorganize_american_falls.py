import os

md_content = """---
tags:
  - Waterfalls
  - Easy
  - Day Hiking
  - Backpacking
  - Mountain Biking
  - Swimming
  - Priest Lake
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking, Mountain Biking & Swimming
  - label: Distance
    value: 16.2 Miles RT (Full Trail) / 2.5 Miles RT (Shortcut) / 14.0 Miles (MTB Shuttle)
  - label: Elevation Gain
    value: 640 ft (River Trail) / 1,040 ft (Continental Trail #28 Descent)
  - label: Trail Difficulty
    value: Easy (Gentle River Gradient with Wooden Boardwalks)
  - label: Designation
    value: Upper Priest River Trail #308 & Continental Trail #28
  - label: Topo Maps
    value: IPNF / Kaniksu NF / Continental Mountain Quad
  - label: Trailhead GPS
    value: '48°53''45"N 116°57''51"W'
  - label: Managing District
    value: Priest Lake Ranger District (Nordman, ID)
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Priest Lake Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Upper Priest River Trail #308 to American Falls

![American Falls (Upper Priest River Falls) cascading over granite ledges](../../../assets/images/20201115093034_orig.jpg)
_American Falls (Upper Priest River Falls) cascading over granite ledges._

The **Upper Priest River Trail #308** to **American Falls** (also known as *Upper Priest River Falls*) is one of the most magnificent ancient forest hikes in the Pacific Northwest. Flanking the pristine Upper Priest River near the Canadian border, Trail #308 wanders through one of the largest intact old-growth cedar and hemlock groves in North America, where giant trees measure up to 10 feet in diameter.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or search and rescue request, dial **911** or contact the Boundary County Sheriff Dispatch at **[208-267-3151](tel:2082673151)**.

    - **USFS Managing Office:** Priest Lake Ranger District (Nordman, ID) — **[208-443-2512](tel:2084432512)**.

!!! warning "Grizzly Bear & Moose Active Habitat"

    This remote northern wilderness corridor near the Canadian border is active grizzly bear and moose habitat. Make noise while hiking or mountain biking, carry EPA-approved bear spray in an easily accessible holster, and maintain a safe distance from all wildlife.

!!! quote "Reflections on Wilderness"

    "There are two things I like about life... living it, and living in nature. The solitude is deafening." — *Chic Burge (January 1, 2023)*

The trail follows a gentle gradient along the riverbank, enhanced by extensive wooden boardwalks built to protect fragile mossy soils. Near the falls, keep an eye out for bright orange peel fungus growing along ancient fallen logs.

---

## Route Options

### Option 1: Full Upper Priest River Trail #308 (16.2 Miles RT)

Hike the full length of Trail #308 along the Upper Priest River from the main lower trailhead to American Falls and back:

- **Distance & Difficulty:** 8.1 miles one-way (16.2 miles round-trip) with 640 feet of gentle elevation gain.
- **Highlights:** Ancient old-growth cedar and hemlock groves, quiet river solitude, and extensive wooden boardwalks.

### Option 2: Shortcut via Continental Trail #28 (2.5 Miles RT)

For a shorter day hike to American Falls:

- **Distance & Elevation:** Drive past the main trailhead on Forest Road 1388 to the Continental Trailhead. Hike 1.5 miles down Continental Trail #28 (descending 1,040 vertical feet) to intersect Trail #308, then continue 1.0 mile north to American Falls (2.5 miles round-trip).

### Option 3: Mountain Bike Point-to-Point Shuttle (14.0 Miles)

- **Shuttle Route:** Leave a shuttle car at the main Trail #308 trailhead, drive up Forest Road 1388 past Continental Creek to the Trail #28 trailhead, and ride 14 miles descending 1,040 feet back down to the lower trailhead.

---

## Trailhead & Forest Road Directions

1. From **Priest River, Idaho**, drive north on **Highway 57** for 37 miles to Nordman.
2. Continue 14 miles north on **Forest Road 302** to Granite Creek and Stagger Inn Campground (home to the Roosevelt Grove of Ancient Cedars and Granite Falls).
3. Drive 1.6 miles to the **Forest Road 1013** junction.
4. Take the middle fork onto F.R. 1013 for nearly 12 miles to the signed **Trail #308** parking area on the left.

---

## Nearby Destinations & Attractions

- **Roosevelt Grove of Ancient Cedars & Granite Falls:** 2,000-year-old giant cedars and cascading waterfalls.
- **Hughes Meadows & Hughes Ridge:** Scenic high-country meadows and wildlife viewing areas.
- **Little Snowy Top & Snowy Top Mountain:** Historic fire lookout site along the Canadian border ridge.

---

## Safety & Wildlife Considerations

- **Bear Safety:** Always store food in bear-resistant containers or hang food bags properly when overnight backpacking.
- **Boardwalk Footing:** Wooden boardwalks can become slick when wet; exercise care with footing.

---

## Refreshments & Nearby Dining

Popular dining spots in nearby Nordman and Priest River:

- **Stagger Inn:** Backcountry roadhouse near Nordman.
- **Burger Express:** Classic diner in Priest River.

---

## Trip Planning & Weather

Check local mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Nordman / Priest Lake Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![A section of Upper Priest River Trail #308 through old-growth cedar and hemlock](../../../assets/images/p380.png)
_A section of Upper Priest River Trail #308 through old-growth cedar and hemlock._

---

![Upper Priest River Falls, also known as American Falls](../../../assets/images/p168.png)
_Upper Priest River Falls, also known as American Falls._

---

![Long exposure view of American Falls cascading over granite ledges](../../../assets/images/10232023120p.jpg)
_Long exposure view of American Falls cascading over granite ledges._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/american-falls-trail-308.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized american-falls-trail-308.md successfully")
