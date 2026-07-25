import os

md_content = """---
tags:
  - Peaks & Mountains
  - Moderate
  - Day Hiking
  - Backpacking
  - Equestrian
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking & Equestrian
  - label: Distance
    value: 9.6 Miles RT
  - label: Elevation Gain
    value: 2,660 ft
  - label: Summit Elevation
    value: 6,760 ft
  - label: Trail Difficulty
    value: Moderate (Final 1,240 ft Ridge Climb)
  - label: Designation
    value: Snow Peak Wildlife Management Area (32,292 Acres)
  - label: Topo Maps
    value: IPNF Avery R.D. / Bathtub Mountain & Montana Peak Quads
  - label: Trailhead GPS
    value: '47°04''40"N 115°34''41"W'
  - label: Managing District
    value: Avery Ranger District / IDFG
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: Idaho Fish & Game Snow Peak WMA Information
    url: https://idfg.idaho.gov/
---

# Snow Peak (6,760') — Wildlife Management Area Trail #55

![Unnamed alpine tarn nestled below the granite summit of Snow Peak](../../../assets/images/202139139-jpeg-1.jpg)
_Unnamed alpine tarn nestled below the granite summit of Snow Peak._

Located in high country of Shoshone County, Idaho, the **Snow Peak Wildlife Management Area (WMA)** encompasses
32,292 acres of roadless mountain terrain co-managed by the U.S. Forest Service and Idaho Department of Fish and Game.
Trail #55 leads hikers and horseback riders 4.8 miles through dense conifer forest and subalpine saddles to an active
fire lookout tower atop Snow Peak (6,760').

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or search and rescue request, dial **911** or contact the Shoshone County
    Sheriff Dispatch at **[208-556-1114](tel:2085561114)**.

    - **USFS Managing Office:** Avery Ranger District — **[208-245-4517](tel:2084434517)**.

!!! warning "Mountain Goat Sanctuary & Non-Motorized Rules"

    - **Mountain Goat Conservation:** Snow Peak is famous for resident herds of wild **Mountain Goats**. Do not approach,
      corner, or feed the goats. **Please leave dogs at home** to avoid provoking or stressing nursery herds.
    - **Non-Motorized Access Only:** All 50 miles of trails within Snow Peak WMA are strictly non-motorized (foot and
      equestrian traffic only).

Starting near Bathtub Mountain, Trail #55 travels through dense timber before bearing right at an early junction. At
3.6 miles, the trail breaks out onto an open saddle where **Spotted Louis Trail #104** branches right. Stay left on
Trail #55 for the final 0.8-mile climb, gaining 1,240 vertical feet to the active fire lookout atop Snow Peak.

Looking south from the summit, the wild ridges of the neighboring **Mallard-Larkins Pioneer Area** stretch out across
the horizon.

---

## Snow Peak Wildlife Management Area (WMA) History

Acquired in 1990 through a major land exchange between Idaho Fish and Game and the Plum Creek Timber Corporation, the
32,292-acre WMA was created primarily to protect critical roadless elk hunting habitat and winter range for deer, elk,
moose, mountain goats, and black bear.

In 2008, all surrounding Forest Service lands were designated as inventoried roadless under the Idaho Roadless Rule,
ensuring permanent non-motorized wilderness character across the entire sanctuary.

---

## Trailhead Directions

### Route 1: Via St. Regis, Montana (I-90)

1. From **I-90 Exit 33 at St. Regis, Montana**, turn north onto **Highway 200**.
2. Pass the gas station and turn left (NW) for 0.5 miles, then turn left (SW) onto **Little Joe Creek Road #282**.
3. Cross over the I-90 freeway bridge and follow F.R. 282 for 25 miles to the Idaho/Montana state line.
4. At the border, the road becomes **Forest Road 50**. Drive 5 miles and turn right onto **Forest Road 339**.
5. Rejoin **Forest Road 50** after 339, turn left for 2.5 miles, then turn right onto **Forest Road 509**.
6. Turn left onto **Forest Road 1258** toward Mammoth Springs Campground.
7. At Mammoth Springs, turn left onto **Forest Road 201** for 3.5 miles to the Pineapple Saddle trailhead.

### Route 2: Via Wallace, Avery & St. Joe River Road

1. From **Wallace, Idaho**, take Moon Pass Road #456 south past the Route of the Hiawatha tunnels to **Avery**.
2. Turn left (east) onto **Forest Road 50 (St. Joe River Road)** and drive past Nugget Creek Campground.
3. In 5.5 miles, turn right onto **Forest Road 509**.
4. Follow F.R. 509 to **Forest Road 1258**, pass Mammoth Springs Campground, and turn onto **Forest Road 201**.
5. Drive 3.5 miles on F.R. 201 to the Snow Peak Trailhead.

---

## Nearby Destinations & Attractions

- **Mallard-Larkins Pioneer Area:** Adjacent 70,000-acre primitive roadless area famous for alpine tarns and rugged peaks.
- **St. Joe Wild & Scenic River:** World-renowned cutthroat trout fishing and whitewater rafting river.
- **Red Ives Historical Ranger Station:** Historic 1930s Forest Service ranger station complex on the upper St. Joe River.
- **Ward Peak, Eagle Peak & Five Lakes Butte:** High-elevation Selkirk/St. Joe backcountry hiking destinations.

---

## Trip Planning & Weather

Check mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Avery / Snow Peak Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![Active USFS fire lookout tower atop Snow Peak (6,760')](../../../assets/images/202139150-jpeg-1.jpg)
_Active USFS fire lookout tower atop Snow Peak (6,760')._

---

![Spokane Mountaineers volunteers conducting trail maintenance on Trail #55](../../../assets/images/202139155-jpeg-1.jpg)
_Spokane Mountaineers volunteers conducting trail maintenance on Trail #55._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/snow-peak.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized snow-peak.md successfully")
