import os

md_content = """---
tags:
  - Lakes
  - Moderate
  - Day Hiking
  - Backpacking
  - Equestrian
  - Clearwater National Forest
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking & Alpine Exploration
  - label: Distance
    value: 6.4 Miles RT (Summit & Main Basin)
  - label: Elevation Gain
    value: 1,563 ft
  - label: Trail Difficulty
    value: Moderate to Advanced (Off-Trail Navigation)
  - label: Designation
    value: USFS Trail #233
  - label: Topo Maps
    value: Nez Perce-Clearwater NF / Bacon Peak & Chamberlain Mountain Quads
  - label: Trailhead GPS
    value: '46°56''06"N 115°14''44"W'
  - label: Managing District
    value: North Fork Ranger District (Clearwater NF)
notes:
  - label: Nez Perce-Clearwater National Forests Alerts
    url: https://www.fs.usda.gov/alerts/nezperceclearwater/alerts-notices
  - label: Lolo National Forest Alerts
    url: https://www.fs.usda.gov/alerts/lolo/alerts-notices
---

# Five Lakes Butte & Alpine Basin

Nestled within the rugged backcountry of the **Mallard-Larkins Pioneer Area** in the North Fork Clearwater River drainage, **Five Lakes Butte** is the scenic centerpiece of an extraordinary subalpine basin. Despite its name, the area actually encompasses **eight high-mountain alpine lakes**: Tin, Copper, Silver, Gold, Heather, Platinum, Seed, and Berry Lakes.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or search and rescue request, dial **911** or contact the Clearwater County Sheriff Dispatch at **[208-476-4521](tel:2084764521)**.

    - **USFS Managing Office:** North Fork Ranger District (Orofino, ID) — **[208-476-4541](tel:2084764541)**.

!!! warning "Off-Trail Scrambling & Cliff Hazards"

    - **Advanced Route Finding:** Established Trail #233 reaches Silver and Gold Lakes. Traversing north beyond Five Lakes Butte summit to Heather, Seed, and Berry Lakes requires off-trail alpine navigation skills.
    - **North Summit Cliffs:** Avoid the sheer cliff drop-offs on the north side of Five Lakes Butte summit by skirting to the right (east) during off-trail descents.

Following **USFS Trail #233** from Gospel Hill Road (Forest Road 715), the trail climbs a forested ridge between two mountain creeks. Passing Platinum Lake, the route leads past Tin, Copper, and Silver Lakes before ascending open granite ridges to the 360-degree panoramic summit of Five Lakes Butte.

---

## The Alpine Lakes Basin

### Primary Lakes (Tin, Copper, Silver, Gold, Heather)

- **Tin & Copper Lakes:** Lower basin lakes tucked along the initial ascent of Trail #233.
- **Silver Lake:** Features prime backcountry campsites along its northeast shore.
- **Gold Lake:** Nestled directly beneath the craggy, vertical south face of Five Lakes Butte. The still waters reflect the dramatic cliff face, and a popular campsite is located on the northeast shore.
- **Heather Lake:** High alpine tarn tucked north below the Butte summit.

### Secondary Basin Lakes (Platinum, Seed, Berry)

- **Platinum Lake:** Located near the lower entrance to the basin.
- **Seed & Berry Lakes:** Upper basin tarns accessible via off-trail scrambling north and west of Five Lakes Butte summit.

---

## Route Options & Off-Trail Loop

### Option 1: Trail #233 to Five Lakes Butte Summit (6.4 Miles RT)

- **Distance & Elevation:** 3.2 miles one-way (6.4 miles round-trip) with 1,563 feet of elevation gain.
- **The Ridge Ascent:** From Silver Lake, Trail #233 climbs west along the ridge above Gold Lake. Near the summit, the ridge splits; stay right up the open granite spur to reach the 360-degree summit.

### Option 2: Off-Trail Heather & Seed Lakes High Traverse

- **The Alpine Loop:** From the summit of Five Lakes Butte, head north, skirting right to avoid cliffs. Drop 1,100 vertical feet down to Heather and Seed Lakes. From Seed and Berry Lakes, traverse southwest across open alpine terrain above timberline back to Gold Lake. Follow a faint path southeast from Gold Lake to rejoin Trail #233 above Silver Lake for the return walk to the trailhead.

---

## Trailhead & Forest Road Directions

### From Superior, Montana (via Hoodoo Pass)

1. From **I-90 at Superior, MT**, head south on **Forest Road 257 (Diamond Road)** for 36 miles, crossing **Hoodoo Pass**.
2. Turn right onto **Forest Road 720**, crossing the North Fork of the Clearwater River near Cedar Grove Campground.
3. Drive 10.5 miles on F.R. 720 toward Fly Hill.
4. Turn right onto **Gospel Hill Road (Forest Road 715)** and drive 7.5 miles to the trailhead at Meadow Creek.

### From Lewiston / Pierce, Idaho (via French Mountain Road)

1. From **Lewiston, ID**, take **US-12 east** to Greer, then turn east on **SH-11** through Weippe toward Pierce.
2. Just before Pierce, turn right onto **French Mountain Road** (49 miles to Kelly Creek).
3. Turn left (east) onto **Forest Road 250** at Kelly Forks and follow it past Lake Creek.
4. Turn left over the North Fork Clearwater River toward Cedar Grove Campground, then turn right immediately across the bridge onto **Forest Road 720 (Fly Hill Road)**.
5. At 10 miles, turn right onto **Forest Road 715** and drive 18 miles to the trailhead parking area on the left.

---

## Nearby Destinations & Attractions

- **St. Joe Wild and Scenic River:** Crystal-clear trout fishing and rafting corridor to the north.
- **Mallard-Larkins Pioneer Area:** 70,000-acre primitive mountain wilderness.
- **Black Peak, Eagle Point Lookout & Snow Peak:** High-elevation peaks along the Clearwater-St. Joe divide.

---

## Hazards & Route Finding

!!! info "Navigation Advisory"

    - **Trailhead to Gold Lake:** Established, easy-to-follow singletrack.
    - **Beyond the Summit:** Off-trail alpine navigation across scree and boulder fields. Carry a topo map and GPS.

---

## Trip Planning & Weather

Check local mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Pierce / Clearwater Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Nez Perce-Clearwater National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/nezperceclearwater/alerts-notices)
"""

target_path = "docs/hike/idaho/north-idaho-hikes/five-lakes-butte.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized five-lakes-butte.md successfully")
