import os

md_content = """---
tags:
  - Peaks & Mountains
  - Easy to Moderate
  - Day Hiking
  - Mountain Biking
  - State Parks
stats:
  - label: Activity Type
    value: Day Hiking & Mountain Biking
  - label: Distance
    value: 3.0 Miles RT (Overlook) / 9.6 Miles RT (Summit)
  - label: Elevation Gain
    value: ~1,400 ft
  - label: Trail Difficulty
    value: Easy to Moderate (Trail #37)
  - label: Topo Maps
    value: Farragut State Park Brochure Map / Athol Quad
  - label: Trailhead GPS
    value: '47°57''05"N 116°36''09"W'
  - label: Managing Agency
    value: Idaho Dept of Parks & Rec / USFS
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: Farragut State Park Official Website
    url: https://parksandrecreation.idaho.gov/parks/farragut/
---

# Bernard Peak Overlook & High Point Trail #37

Perched high above the southern tip of Lake Pend Oreille within **Farragut State Park**, the **Bernard Peak Overlook** trail delivers quiet forest solitude and dramatic views over Idlewilde Bay, Beaver Bay, and Buttonhook Bay. Accessible via **High Point Trail #37**, hikers and mountain bikers can choose between a gentle 3.0-mile round-trip walk to the primary overlook or a 9.6-mile round-trip push to the true Bernard Peak summit.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Park Contact"

    In case of a park emergency, injury, or search and rescue request, dial **911** or contact the Kootenai County Sheriff Dispatch at **[208-446-1300](tel:2084461300)**.

    - **Farragut State Park Office:** **[208-683-2425](tel:2086832425)**.
    - **USFS Managing Office:** Coeur d'Alene River Ranger District — **[208-769-3000](tel:2087693000)**.

!!! info "Quiet Solitude Above Lake Pend Oreille"

    While Bernard Peak is heavily forested at the true summit, the lower overlook offers sweeping vistas looking east across Lake Pend Oreille toward Bayview. The deep forest canopy along High Point Trail #37 provides remarkable quiet and shade on warm summer days.

The trail is exceptionally well-signed for the first 2.5 miles from the Farragut Visitor Center. The route ascends through mature conifer timber before reaching a historic forest management area. Beyond the harvest zone, the singletrack trail is beautifully maintained as it climbs toward the overlook and upper Bernard Peak ridge.

---

## Route Options

### Option 1: Bernard Peak Overlook (3.0 Miles RT)

The most popular option follows Trail #37 to the primary scenic viewpoint:

- **Distance & Difficulty:** 1.5 miles one-way (3.0 miles round-trip), easy to moderate incline.
- **Highlights:** Shaded forest walking, scenic lake vistas, and family-friendly trail width.

### Option 2: Full Summit Push to Bernard Peak (9.6 Miles RT)

For mountain bikers and long-distance hikers seeking a full-day adventure:

- **Distance & Difficulty:** 4.8 miles one-way (9.6 miles round-trip) with approximately 1,400 feet of elevation gain.
- **Highlights:** Quiet backcountry singletrack traversing deep forest along the southern rim of Lake Pend Oreille.

---

## Trailhead Directions

1. From **US-95 at Athol, Idaho**, turn east onto **State Highway 54 (SH-54)**.
2. Drive 4 miles east into **Farragut State Park**.
3. Follow park signs to the **Farragut Visitor Center** parking area.
4. The signed trailhead for **Trail #37 (High Point / Bernard Peak Trail)** is located adjacent to the Visitor Center lot.

---

## Nearby Destinations & Attractions

- **Farragut State Park:** 4,000-acre state park featuring disc golf courses, swimming beaches, and historic WWII naval training center exhibits.
- **Beaver Bay & Buttonhook Bay:** Protected coves on Lake Pend Oreille popular for kayaking and paddleboarding.
- **Bayview, Idaho:** Scenic lakefront town offering boat launches and float-home dining.

---

## Trail Hazards & Wayfinding Advice

!!! warning "Timber Harvest Zone Navigation"

    - **Wayfinding near Cut Area:** In the timber harvest area near mile 2.5, trail flagging can be sparse. Continue eastbound along the southern periphery of the logged opening to re-enter the main singletrack. **Do not take any of the southbound logging roads.**

---

## Refreshments & Nearby Dining

Popular dining stops in nearby Bayview and Athol:

- **Bayview Waterfront Grill:** Lakefront dining overlooking scenic float homes in Bayview.
- **The Country Boy Cafe:** Classic local breakfast and lunch spot in Athol.

---

## Trip Planning & Weather

Check local weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Athol / Bayview Forecast](https://forecast.weather.gov)
- **State Park Info:** [Farragut State Park Official Portal](https://parksandrecreation.idaho.gov/parks/farragut/)
"""

target_path = "docs/hike/idaho/north-idaho-hikes/bernard-peak-overlook.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized bernard-peak-overlook.md successfully")
