import os

md_content = """---
tags:
  - Waterfalls
  - Day Hiking
  - Easy to Moderate
  - National Recreation Trails
  - Clearwater National Forest
stats:
  - label: Activity Type
    value: Day Hiking & Waterfall Exploration
  - label: Distance
    value: 2.5–3.0 Miles RT Loop
  - label: Elevation Gain
    value: ~652 ft Net Elevation Change
  - label: Trail Difficulty
    value: Easy to Moderate (Trail #740 / #742 / #740A)
  - label: Waterfall Drops
    value: Lower (50'), Middle (70'), Upper (20')
  - label: Topo Maps
    value: USFS Palouse Ranger District / Elk Creek Falls Recreation Area Brochure
  - label: Trailhead GPS
    value: '46°44''39"N 116°10''52"W'
  - label: Managing District
    value: Palouse Ranger District (Nez Perce-Clearwater NF)
notes:
  - label: Nez Perce-Clearwater National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/nezperceclearwater/alerts-notices
  - label: USFS Palouse Ranger District
    url: https://www.fs.usda.gov/detail/nezperceclearwater/about-forest/districts/?cid=stelprdb5341258
---

# Elk Creek Falls National Recreation Area

![Lower Elk Creek Falls plunging 50 feet through a basalt canyon wall](../../../assets/images/10242023432p.jpg)
_Lower Elk Creek Falls plunging 50 feet through a basalt canyon wall._

Tucked deep within the cedar and fir forests of the Nez Perce-Clearwater National Forests near Elk River, Idaho, the **Elk Creek Falls National Recreation Area** protects the highest cascading waterfall system in North Idaho. A well-maintained 2.5 to 3.0-mile loop trail system links three distinct waterfall overlooks: **Lower Elk Creek Falls (50')**, **Middle Elk Creek Falls (70')**, and **Upper Elk Creek Falls (20')**.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, cliff fall, or search and rescue request, dial **911** or contact the Clearwater County Sheriff Dispatch at **[208-476-4521](tel:2084764521)**.

    - **USFS Managing Office:** Palouse Ranger District (Potlatch, ID) — **[208-875-1131](tel:2088751131)**.

!!! warning "Viewpoint Safety & Wet Basalt Caution"

    - **Stay Behind Viewpoint Railings:** Always remain inside the constructed wooden viewpoint structures. Basalt cliff edges feature sheer 50 to 70-foot vertical drop-offs.
    - **Supervise Children & Pets:** Keep children close at all times and keep dogs leashed.
    - **Slippery Bedrock & Water Shoes:** Basalt rock along stream banks is extremely slick when wet. If wading or swimming below Upper Falls, wear sturdy water shoes or sandals.

The trailhead parking lot includes a vault toilet, informational kiosks, and picnic tables (no day-use fees). During winter, Forest Road 1452 is unplowed, turning the access into a popular 2.0-mile cross-country ski or snowshoe trek from State Highway 8 to the trailhead.

---

## Waterfall Exploration Loop

### Lower Elk Creek Falls (50' Drop)

From the main trailhead, follow **Trail #740** for 1.0 mile to a signed junction. Bear right at the "Y" and descend a semi-steep 1.25-mile trail to the Lower Falls viewpoint structure:

- **Highlights:** Lower Elk Creek Falls gushes around a massive basalt canyon wall before plunging 50 feet into the gorge below.

### Middle Elk Creek Falls (70' Drop)

Return uphill along Trail #740 to the junction with **Trail #742**:

- **Highlights:** Widely considered the most dramatic and photogenic of the three waterfalls, Middle Falls surges 70 feet down through a narrow, sheer basalt gorge.

### Upper Elk Creek Falls (20' Drop)

Continue along Trail #742 to a short spur trail leading to the Upper Falls viewpoint:

- **Highlights:** Upper Falls cascades 20 feet down over a wide, 30+ foot basalt ledge into a broad pool. On warm summer days, the pool below Upper Falls is a popular spot to wade and cool off.
- **Return Loop:** Reconnect with **Trail #740A** and follow it back to Trail #740 and the main parking area.

---

## Trailhead Directions

### From Spokane, WA

1. From **Spokane**, drive east on **I-90** over 4th of July Pass to **Exit 34 (Rose Lake / SH-3)**.
2. Drive south on **State Highway 3** through St. Maries to **Bovill, Idaho** (approx. 44 miles).
3. At Bovill, turn left (east) onto **State Highway 8** and drive 10 miles.
4. Turn right onto **Elk Creek Falls Road (Forest Road 1452)** and drive 2.0 miles to the trailhead parking area.

### From Moscow, ID

1. From **Moscow**, drive east on **State Highway 8** through Troy, Deary, and Bovill.
2. Continue 10 miles east of Bovill on SH-8.
3. Turn right onto **Elk Creek Falls Road (Forest Road 1452)** and drive 2.0 miles to the trailhead.

---

## Nearby Destinations & Attractions

- **Giant Western Red Cedar:** Located north of Elk River, home to one of the largest living western red cedars in North America.
- **Morris Creek Old Growth Cedar Grove:** Protected old-growth forest sanctuary with self-guided nature trails.
- **Hobo Cedar Grove Botanical Area:** Ancient cedar botanical reserve located south of Fernwood.
- **Dworshak Reservoir:** Expansive 54-mile reservoir offering boating, camping, and fishing.

---

## Refreshments & Nearby Dining

Popular dining stops in nearby Elk River, Bovill, and Deary:

- **Elk River Lodge & General Store:** Famous for huckleberry ice cream and regional gifts.
- **Tom's Tavern:** Classic local tavern in Bovill.

---

## Trip Planning & Weather

Check local weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Elk River / Bovill Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Nez Perce-Clearwater National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/nezperceclearwater/alerts-notices)

---

## Photo Gallery

![Lower Elk Creek Falls plunging 50 feet through a basalt canyon wall](../../../assets/images/10242023432p.jpg)
_Lower Elk Creek Falls plunging 50 feet through a basalt canyon wall._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/elk-creek-falls-national-recreation-area.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized elk-creek-falls-national-recreation-area.md successfully")
