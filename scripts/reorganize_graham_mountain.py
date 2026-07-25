import os

md_content = """---
tags:
  - Peaks & Mountains
  - Moderate
  - Day Hiking
  - Backpacking
  - Equestrian
  - Skiing & Snowshoeing
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking & Snowshoeing
  - label: Distance
    value: 11.0 Miles RT
  - label: Elevation Gain
    value: 3,445 ft
  - label: Summit Elevation
    value: 5,727 ft
  - label: Trail Difficulty
    value: Moderately Difficult (Relentless Climb)
  - label: Designation
    value: Coal Creek Trail #41 & Graham Ridge Trail #18
  - label: Topo Maps
    value: IPNF / Coeur d'Alene River Ranger District / Kellogg Quad
  - label: Trailhead GPS
    value: '47°38''54"N 116°07''13"W'
  - label: Managing District
    value: Coeur d'Alene River Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Coeur d'Alene River Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Graham Mountain (5,727') — Coal Creek Trail #41

Ascending out of the Coeur d'Alene River Valley near Kingston, Idaho, **Graham Mountain (5,727')** offers a challenging 11.0-mile round-trip climb along **Coal Creek Trail #41**. Gaining 3,445 vertical feet through old-growth western red cedars and historic mining sites, the trail leads up to **Graham Ridge Trail #18** for a sweeping 360-degree panorama of Silver Mountain, Kellogg Peak, and the Coeur d'Alene River watershed.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or search and rescue request, dial **911** or contact the Shoshone County Sheriff Dispatch at **[208-556-1114](tel:2085561114)**.

    - **USFS Managing Office:** Coeur d'Alene River Ranger District — **[208-769-3000](tel:2087693000)**.

!!! warning "Relentless Grade & Spring Creek Crossings"

    - **Relentless Climb:** Trail #41 climbs steadily up Coal Creek canyon for 5.5 miles with few switchbacks. Good stamina and pacing are essential.
    - **Spring High-Water Crossings:** Trail #41 skirts Coal Creek and crosses it. During spring snowmelt, creek crossings can be swift and deep.

---

## Route Description & Summit Trail

### Section 1: Coal Creek Canyon & Old-Growth Cedars (5.5 Miles)

Starting from the Coal Creek Trailhead off Coeur d'Alene River Road (Hwy 9), Trail #41 heads south through a dense forest canopy:

- **Distance & Elevation:** 5.5 miles one-way to the ridge junction.
- **Mining History & Cedar Forest:** The trail skirts Coal Creek through a towering grove of old-growth western red cedars, passing several historic 19th-century mining shafts and tailing piles.

### Section 2: Graham Ridge Junction to Summit (1.0 Mile)

- **The Ridge Junction:** At 5.5 miles, Trail #41 intersects **Graham Ridge Trail #18** (also designated Trail #33).
- **The Summit Ridge:** Turn right (southwest) onto Trail #18 and follow the open ridge for 1.0 mile to the **5,727-foot summit of Graham Mountain**.
- **Panoramic Vistas:** The summit provides unobstructed 360-degree views looking south toward Silver Mountain Resort (Kellogg Peak), north over the winding Coeur d'Alene River, and east into the Silver Valley.

---

## Trailhead & Access Directions

1. From **I-90 at Exit 43 (Kingston, Idaho)**, cross over the freeway and head north onto **Coeur d'Alene River Road (State Highway 9)**.
2. Drive north along the river for **12.5 miles** to the marked Coal Creek turnoff.
3. Turn right (south) up the short dirt access road to the designated **Coal Creek Trailhead** parking lot.

---

## Nearby Destinations & Attractions

- **Historic Snake Pit (Enaville):** Landmark 1880s log structure and dining institution located north of Kingston.
- **Fern & Shadow Falls:** Scenic waterfall hikes located nearby along North Fork Coeur d'Alene River tributaries.
- **Little Guard Lookout:** Historic rental fire lookout perched high above the river valley.
- **Coeur d'Alene River National Recreation Trail #20:** Paved/gravel riverfront trail system following the lower river corridor.
- **Bumblebee Campground:** Popular USFS riverside campground along the Coeur d'Alene River.

---

## Trail Hazards & Safety Considerations

!!! warning "Aspect & Water Supply"

    - **Continuous Aspect:** The trail maintains a continuous, direct upward pitch. Carry ample drinking water, as water sources become scarce once you climb out of Coal Creek onto Graham Ridge.

---

## Refreshments & Nearby Dining

Popular local dining stops in Kingston, Kellogg, Wallace, and Coeur d'Alene:

- **The Historic Snake Pit:** Famous 1880s tavern and restaurant north of Kingston.
- **Radio Brewing Company:** Local craft brewery in Kellogg.
- **Wallace Dining:** Pizza Factory, 1313 Club, Brooks Hotel & Restaurant, City Limits Brew Pub, The Fainting Goat, Smoke House BBQ & Saloon, Wallace Brewing Co., and Muchacho's Tacos.
- **Coeur d'Alene Pubs:** Moon Time & Mexican Food Factory.

---

## Trip Planning & Weather

Check local mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Kingston / Kellogg Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

_Photo contributions for Graham Mountain are welcome. To submit photography, contact the editorial team._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/graham-mountain.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized graham-mountain.md successfully")
