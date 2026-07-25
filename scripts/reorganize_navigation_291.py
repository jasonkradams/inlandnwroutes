import os

md_content = """---
tags:
  - Trails & Scrambles
  - Easy
  - Day Hiking
  - Backpacking
  - Priest Lake
stats:
  - label: Activity Type
    value: Day Hiking & Backpacking
  - label: Distance
    value: 6 Miles RT (Plowboy CG) / 12 Miles RT (Navigation CG)
  - label: Elevation Gain
    value: "< 1,000 ft Net Gain"
  - label: Trail Difficulty
    value: Easy (Gentle Lakeshore Profile)
  - label: Topo Maps
    value: IPNF / Priest Lake Ranger District / Upper Priest Lake Quad
  - label: Trailhead GPS
    value: '48°47''42"N 116°54''38"W'
  - label: Managing District
    value: Priest Lake Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Priest Lake Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Navigation Trail #291 to Upper Priest Lake

![Navigation Trail #291 along the scenic western shore of Upper Priest Lake](../../../assets/images/61720221257p_orig.jpeg)
_Navigation Trail #291 along the scenic western shore of Upper Priest Lake._

Stretching along the pristine western shoreline of Upper Priest Lake, **Navigation Trail #291** offers one of the most
scenic and accessible Wilderness-adjacent hikes in North Idaho. Departing from Beaver Creek Campground, this gently
rolling trail connects quiet sandy beaches, ancient forest groves, and backcountry campgrounds with panoramic views of
the Northern Selkirk Mountains.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or lost hiker, immediately dial **911** or contact the Boundary County
    Sheriff Dispatch at **[208-267-3151](tel:2082673151)**.

    - **USFS Managing Office:** Priest Lake Ranger District (Nordman, ID) — **[208-443-2512](tel:2084432512)**.

!!! tip "Ideal Family & Beginner Backpacking Destination"

    With minimal elevation gain (less than 1,000 feet net gain out and back), abundant lake views, and well-maintained
    backcountry campsites, Navigation Trail #291 is a premier choice for beginner backpackers, family trips, swimming,
    and lakefront relaxation.

The trail begins near Beaver Creek Campground at the northwest head of Lower Priest Lake. Traversing mostly level
terrain through dense conifer forest, the path stays close to the lakeshore, offering frequent glimpses of the
mirror-smooth water. Trail #291 continues north past Navigation Campground before terminating at Forest Road 1013,
approximately 3.5 miles northwest of Upper Priest Lake.

---

## Route Options & Extensions

### Option 1: Beaver Creek to Plowboy Campground (6 Miles RT)

The first major destination along the trail is **Plowboy Campground**, located at the southern tip of Upper Priest
Lake:

- **Distance:** 3.0 miles one-way (6.0 miles round-trip).
- **Features:** Designated tent sites, fire rings, and open views looking northeast across the Selkirk Range.

### Option 2: Beaver Creek to Navigation Campground (12 Miles RT)

Continuing north along the western shoreline brings hikers to **Navigation Campground**:

- **Distance:** 6.0 miles one-way (12.0 miles round-trip).
- **Features:** Expansive 360-degree panoramas of Upper Priest Lake, Snowy Top Peak, and Little Snowy Top.
- **Backcountry Note:** Bring personal sit pads, as campsite picnic tables may be weathered or damaged.

### Option 3: Full Through-Hike to Forest Road 1013 (12.1 Miles One-Way)

Beyond Navigation Campground, the trail heads northwest through dense old-growth timber, crossing two small mountain
streams before terminating at **Forest Road 1013** (12.1 miles one-way from Beaver Creek).

---

## Trailhead Directions

### Southern Access (Beaver Creek Trailhead)

1. From **Nordman, Idaho**, turn east onto **Reeder Bay Road**.
2. Follow the paved main road north for approximately 14 miles toward **Beaver Creek Campground**.
3. Turn right into the campground entrance, then take an immediate left uphill to the designated trailhead parking lot.
   *(Pull-through parking is available for horse trailers)*.

### Northern Access (Forest Road 1013)

1. From **Nordman**, drive north on **Highway 57**, which transitions into gravel **Forest Service Road 302** after 4 miles.
2. Follow F.R. 302 north for 14 miles to the Granite Pass junction, where it becomes **Forest Road 1013**.
3. Continue 5.5 miles on F.R. 1013 (1 mile past the Hughes Meadows turnoff) to the northern trailhead on the right.

---

## Nearby Destinations & Attractions

- **Roosevelt Grove of Ancient Cedars & Granite Falls:** Giant old-growth cedar grove and double waterfall complex.
- **Salmo-Priest Wilderness:** Rugged roadless wilderness area straddling the WA/ID border.
- **Snowy Top & Little Snowy Top:** Prominent alpine peaks dominating the northern skyline.
- **Trapper Creek Campground & Hughes Meadows:** Scenic backcountry meadows and wildlife viewing corridors.

---

## Trail Hazards & Safety Advice

!!! warning "Moist Trails & Spring Fungi Awareness"

    - **Slippery Footing:** Rain and lake mist can make boardwalks, bridge crossings, and exposed roots extremely slippery.
    - **Spring Mushroom Growth:** Damp microclimates along the trail support rich fungi displays in spring and early
      summer, including poisonous **False Morels** (*Gyromitra esculenta*) and vibrant **Spring Orange Peel Fungus**.
      Do not consume wild mushrooms.

---

## Refreshments & Local Services

Popular dining stops in nearby Nordman and Priest River include:

- **Ardy's Cafe:** Classic local breakfast and lunch cafe in Nordman.
- **Burger Express:** Popular burger drive-in in Priest River.

---

## Trip Planning & Weather

Check mountain weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Nordman / Priest Lake Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![Plowboy Campground along the peaceful shore of Upper Priest Lake](../../../assets/images/6182025226p.jpg)
_Plowboy Campground along the peaceful shore of Upper Priest Lake._

---

![Gerald Lindquist, trail leader, hiking Navigation Trail #291](../../../assets/images/6172022104p.jpg)
_Gerald Lindquist, trail leader, hiking Navigation Trail #291._

---

![Lush forest canopy and trail corridor along Navigation Trail #291](../../../assets/images/6172022105p.jpg)
_Lush forest canopy and trail corridor along Navigation Trail #291._

---

![Navigation Trail #291 winding along the upper lake shore](../../../assets/images/6172022108p.jpg)
_Navigation Trail #291 winding along the upper lake shore._

---

![Looking east across Upper Priest Lake from Navigation Campground](../../../assets/images/img-2727.jpg)
_Looking east across Upper Priest Lake from Navigation Campground._

---

![Spring Orange Peel Fungus (Caloscypha fulgens) blooming along the damp trail](../../../assets/images/6172022122p.jpg)
_Spring Orange Peel Fungus (Caloscypha fulgens) blooming along the damp trail._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/navigation-trail-291.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized navigation-trail-291.md successfully")
