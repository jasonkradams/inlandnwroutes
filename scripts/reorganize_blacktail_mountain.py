import os

md_content = """---
tags:
  - Peaks & Mountains
  - Moderate
  - Day Hiking
  - Backpacking
  - Equestrian
  - Priest Lake
stats:
  - label: Activity Type
    value: Day Hiking, Backpacking & Equestrian
  - label: Distance
    value: 3.6 Miles RT
  - label: Elevation Gain
    value: 1,295 ft
  - label: Summit Elevation
    value: 5,495 ft
  - label: Trail Difficulty
    value: Moderately Difficult (Semi-Steep & Rocky Summit)
  - label: Designation
    value: USFS Trail #292
  - label: Topo Maps
    value: IPNF / Priest Lake Ranger District / Upper Priest Lake Quad
  - label: Trailhead GPS
    value: '48°42''43"N 116°55''05"W'
  - label: Managing District
    value: Priest Lake Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Priest Lake Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Blacktail Mountain (5,495') — Trail #292

![Panoramic view of Priest Lake from the summit of Blacktail Mountain](../../../assets/images/20201116053958_orig.jpg)
_Panoramic view of Priest Lake from the summit of Blacktail Mountain._

Rising high above the eastern shore of Upper Priest Lake, **Blacktail Mountain (5,495')** offers a rewarding 3.6-mile round-trip hike along **Trail #292**. Climbing 1,295 vertical feet through huckleberry slopes and open wildflower meadows, the summit delivers sweeping vistas of Priest Lake, Bartoo Island, Fourmile Island, and the entire crest of the Selkirk Mountains.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or search and rescue request, dial **911** or contact the Bonner County Sheriff Dispatch at **[208-263-8417](tel:2082638417)**.

    - **USFS Managing Office:** Priest Lake Ranger District (Nordman, ID) — **[208-443-2512](tel:2084432512)**.

!!! info "Historic Alidade & Fire Lookout Artifacts"

    Built in 1932, the original gabled-roof L-4 lookout tower atop Blacktail Mountain was destroyed in 1941. Today, the rotating metal **alidade** (fire-finder map platter) still stands firmly anchored to the summit bedrock alongside a photogenic leaning outhouse located just northeast of the peak.

Trail #292 begins 0.1 miles west of the Tango Creek Road saddle parking area, marked by a memorial sign on an uphill tree. The trail starts moderately steep through dense timber, equipped with rest benches on the lower climbs. As elevation increases, the forest opens into meadows where wild huckleberries flank the trail in late summer. The final 15 minutes involve light rock hopping across the summit crest.

---

## Route Options

### Option 1: Standard Shaded USFS Trail #292

The main USFS trail stays inside the cool forest canopy for the majority of the climb, making it the preferred route on hot, sunny summer days.

### Option 2: Upper Burned Ridge Route (1.6 Mile Junction)

At mile 1.6, hikers can choose to branch right onto an open ridge that burned in a historical wildfire. This open ridge path offers earlier views and warmer sun on cool autumn mornings before rejoining Trail #292 near the summit.

---

## Fire Lookout History & Summit Features

- **1932 L-4 Lookout Tower:** A 10-foot wood tower and L-4 cab built in 1932 served as a primary fire detection post for Upper Priest Lake until its removal in 1941.
- **The Standing Alidade:** The historic metal fire-finder platter remains on the summit bedrock. Fire spotters rotated the platter like a compass to sight Smoke columns and cross-reference bearing angles with neighboring towers.
- **Historic Outhouse:** A weathered, leaning wooden outhouse remains standing northeast of the summit, framed by expansive views of the American Selkirks.

---

## Trailhead & Forest Road Directions

1. From **Priest River, Idaho**, drive north on **Highway 57** for approximately 37 miles past Nordman.
2. Highway 57 transitions into gravel **Forest Road 302**. Follow F.R. 302 for 3 miles until pavement ends.
3. Turn right (north) onto **Tango Creek Road (Forest Road 638)**.
4. At 1.0 mile, bear left at the "Y" junction to stay on F.R. 638.
5. Follow F.R. 638 uphill for 4.2 miles to the saddle parking area on the right.
6. The trailhead for **Trail #292** is located 0.1 miles west (downhill) along the road from the saddle lot.

---

## Nearby Destinations & Attractions

- **Upper Priest Lake & Lower Priest Lake:** Pristine lakes connected by the scenic Thoroughfare.
- **Granite Falls & Roosevelt Grove of Ancient Cedars:** 2,000-year-old giant cedars and roaring waterfalls.
- **Salmo-Priest Wilderness:** 41,000-acre roadless wilderness area straddling the Washington border.

---

## Hazards & Trail Safety

!!! warning "Rough Forest Road & Rocky Summit Caution"

    - **Rough Road Access:** The final mile of Forest Road 638 is rocky and rough; high-clearance vehicles are recommended.
    - **Summit Scree & Rock Hopping:** The final approach to the summit involves brief rock hopping over granite scree. Exercise care with footing.

---

## Refreshments & Nearby Dining

Popular local dining stops in nearby Nordman and Priest River:

- **Stagger Inn:** Famous backcountry roadhouse near Nordman.
- **Burger Express:** Classic drive-in diner in Priest River.

---

## Trip Planning & Weather

Check local mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Nordman / Priest Lake Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![Telephoto view of Mount Roothaan and Chimney Rock from Blacktail Mountain (Photo by Chris Herath)](../../../assets/images/11072021317p.jpg)
_Telephoto view of Mount Roothaan and Chimney Rock from Blacktail Mountain (Photo by Chris Herath)._

---

![The American Selkirk Range stretching across the eastern horizon from the summit](../../../assets/images/2021115329-jpeg-1.jpg)
_The American Selkirk Range stretching across the eastern horizon from the summit._

---

![Historic leaning outhouse perched on the ridge near Blacktail Mountain summit](../../../assets/images/p399.png)
_Historic leaning outhouse perched on the ridge near Blacktail Mountain summit._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/blacktail-mountain.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized blacktail-mountain.md successfully")
