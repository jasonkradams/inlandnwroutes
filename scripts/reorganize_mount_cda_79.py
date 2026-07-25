import os

md_content = """---
tags:
  - Peaks & Mountains
  - Difficult
  - Day Hiking
  - Backpacking
  - Mountain Biking
  - Equestrian
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking, Mountain Biking & Equestrian
  - label: Distance
    value: 10.6 Miles RT (Out & Back) / 14 Miles (Loop)
  - label: Elevation Gain
    value: 2,112 ft
  - label: Trail Difficulty
    value: Difficult (15 Technical Switchbacks)
  - label: Designation
    value: National Recreation Trail (NRT #79)
  - label: Topo Maps
    value: IPNF / CDA River Ranger District / Mount CDA Quad
  - label: Trailhead GPS
    value: '47°36''27"N 116°40''08"W'
  - label: Managing District
    value: Coeur d'Alene River Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Coeur d'Alene River Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Caribou Ridge National Recreation Trail #79

![Hikers ascending Caribou Ridge National Recreation Trail #79 above Beauty Bay](../../../assets/images/1202022743p_orig.jpg)
_Hikers ascending Caribou Ridge National Recreation Trail #79 above Beauty Bay._

Designated as a **National Recreation Trail (NRT #79)**, the Caribou Ridge Trail is a premier ridge climb along the
eastern rim of Lake Coeur d'Alene. Rising 2,112 feet above Beauty Bay, the trail tackles 15 steep switchbacks through
mixed conifer forest and wildflower meadows, culminating at the Mount Coeur d'Alene Overlook.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or lost hiker, immediately dial **911** or contact the Kootenai County
    Sheriff Dispatch at **[208-446-1300](tel:2084461300)**.

    - **USFS Managing Office:** Coeur d'Alene River Ranger District — **[208-769-3000](tel:2087693000)**.

!!! warning "Steep & Technical Switchbacks"

    Caribou Ridge Trail #79 ascends 2,112 feet over 15 steep, exposed switchbacks above Beauty Bay. The tight turns are
    physically demanding for hikers and highly technical for downhill mountain bikers. Exercise extreme caution on loose
    gravel and blind corners.

Starting from the Beauty Creek Campground parking area, the trail heads due south across Beauty Creek before beginning
its relentless ascent. After navigating 15 tight switchbacks over 5.3 miles, Trail #79 connects with Forest Road 439
near the Mount Coeur d'Alene Overlook and Campground.

---

## Route Extensions & Loop Options

### Option 1: Mount CDA Summit Extension via Trail #227

From the Mount Coeur d'Alene Overlook and Campground, hikers can extend their trip by following **Trail #227** for
another 2 miles along the upper ridge to the summit of Mount Coeur d'Alene.

### Option 2: Extended Loop via Trail #257 & Forest Road 439 (14 Miles)

Mountain bikers and long-distance day hikers frequently combine **Trail #257**, **Forest Road 439**, and **Trail #79**
into a popular **14-mile loop**:

1. Ascend Mount Coeur d'Alene via **Trail #257** from Beauty Creek.
2. Follow **Forest Road 439** north for 3 miles to the Mount CDA Overlook.
3. Descend technical singletrack down **Caribou Ridge Trail #79** to Beauty Bay.

---

## Trailhead Directions

1. From **Coeur d'Alene, Idaho**, take **I-90 East** to **Exit 22** (Harrison / Highway 97).
2. Drive south on Highway 97 past the Mineral Ridge parking area for 0.2 miles.
3. Turn left (east) onto **Beauty Creek Road** (Forest Road 438).
4. Drive 0.6 miles to the **Beauty Creek Campground** parking area on the right to access the signed trailhead.

---

## Nearby Destinations & Attractions

- **Mount Coeur d'Alene Trail #257:** Neighboring climbing route starting from Beauty Creek Road.
- **Mineral Ridge Trail:** Famous 3.3-mile BLM scenic trail overlooking Wolf Lodge Bay.
- **Beauty Creek & Wolf Lodge Bay:** Scenic kayaking, paddleboarding, and eagle-watching bays.

---

## Refreshments & Nearby Dining

Popular local dining spots in nearby Coeur d'Alene and Post Falls:

- **Moon Time:** Neighborhood pub in East Coeur d'Alene.
- **Franklin's Hoagies:** Sub sandwiches and hoagies.
- **Mexican Food Factory:** Regional Mexican restaurant.
- **Trails End Brewery:** Local craft brewery and pizzeria.

---

## Trip Planning & Weather

Check local weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Coeur d'Alene / Beauty Bay Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![Inland Northwest spring wildflowers blooming along Caribou Ridge Trail #79](../../../assets/images/6182025214p.jpg)
_Inland Northwest spring wildflowers blooming along Caribou Ridge Trail #79._

---

![Spokane Mountaineers group hiking Trail #79 led by trip leader Chris B.](../../../assets/images/1202022749p.jpg)
_Spokane Mountaineers group hiking Trail #79 led by trip leader Chris B._

---

![One-sided Mitrewort (Orthilia secunda) blooming along Trail #79 in May](../../../assets/images/1202022753p.jpg)
_One-sided Mitrewort (Orthilia secunda) blooming along Trail #79 in May._

---

![Alpine stars wildflowers blooming along Caribou Ridge Trail #79](../../../assets/images/1202022758p.jpg)
_Alpine stars wildflowers blooming along Caribou Ridge Trail #79._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/mount-cda-trail-79-caribou-ridge.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized mount-cda-trail-79-caribou-ridge.md successfully")
