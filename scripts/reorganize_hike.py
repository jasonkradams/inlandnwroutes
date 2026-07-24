import os

content = """---
title: "St. Joe Lake & Illinois Peak"
tags:
  - Trails & Scrambles
  - Hiking
  - Backpacking
  - Scrambling
stats:
  - label: Activity Types
    value: "Hiking, Backpacking, Scrambling"
  - label: Distance
    value: "12.0 miles RT (Lake); 5.0 miles RT (Basin Circuit)"
  - label: St. Joe Lake Elevation
    value: "6,472 ft"
  - label: Surrounding Peak Elevations
    value: "Illinois Peak (7,690 ft), Gold Crown Peak (7,374 ft), Unnamed Peak (7,260 ft), Graves Peak (7,235 ft)"
  - label: Difficulty
    value: "Moderate (Lake & Illinois Peak) / Difficult (Basin Circuit & Unnamed Peak)"
  - label: Managing Agency
    value: "USFS - Idaho Panhandle National Forests (St. Joe Ranger District)"
  - label: Maps
    value: "IPNF - St. Joe N.F., Illinois Peak Quad (MT-ID)"
  - label: Trailhead GPS
    value: "47°01'03.71\"N, 115°04'51.49\"W"
notes:
  - label: St. Joe Ranger District Weather & Trail Alerts
    url: https://forecast.weather.gov
---

# St. Joe Lake & Illinois Peak

St. Joe Lake sits in a high glacial basin at 6,472 feet near the crest of the Bitterroot Mountains. Surrounded by dramatic summits—including Illinois Peak (7,690'), Gold Crown Peak (7,374'), Graves Peak (7,235'), and Unnamed Peak (7,260')—this area offers exceptional backcountry camping, day hiking along the Idaho-Montana Stateline Trail, and off-trail scrambling.

---

## Regional Mountain Ranges Overview

| Regional Destination | Description & Scope | Guide Link |
| :--- | :--- | :--- |
| **Canadian Rockies** | Glacier national parks & northern alpine summits | [Canadian Rockies Guide](canada.md) |
| **American Selkirks** | High granite peaks & lakes in Northern Idaho | [American Selkirks Guide](american-selkirks.md) |
| **Cabinet Mountains** | Glaciated wilderness peaks in Northwest Montana | [Cabinet Wilderness Guide](blog/posts/34-cabinet-mountain-wilderness.md) |
| **Scotchman Peaks** | Proposed wilderness above Lake Pend Oreille | [Scotchman Peaks Guide](blog/posts/blog-58-proposed-scotchman-peak-wilderness.md) |
| **Glacier National Park** | Montana alpine wilderness & continental divide | [Glacier N.P. Guide](glacier-np.md) |
| **Bitterroot Mountains** | High crest along the Idaho-Montana state line | [Bitterroots Guide](bitterroots.md) |

---

## Trail Description & Basin Landscape

The hike to St. Joe Lake begins on a gentle grade, following the headwaters of the St. Joe River through a flat forested valley for the first few miles. Two easy stream crossings occur within the first mile. As you approach the lake basin, the trail gains elevation rapidly.

Just before reaching the lake, the trail opens into a expansive subalpine meadow filled with seasonal wildflowers, offering sweeping views of Gold Crown Peak and Rambikur Waterfall cascading down the valley wall.

!!! info "Campground & Spring Water Options"

    - **Northwest Shore Camps:** Three large, well-established campsites are located along the northwest shore of St. Joe Lake.
    - **East Meadow Spring:** A high bench and meadow sit approximately 400 feet above the east side of the lake, featuring a reliable spring water source.
    - **Inlet Waterfall Camping:** Please restrict camping strictly to pre-existing, established sites. Do not create new fire rings or disturb unimpacted meadow soil near the inlet waterfall.

![St. Joe Lake nestled beneath alpine crests](assets/images/img-1826-1.jpg)
_St. Joe Lake nestled beneath alpine crests._

---

## Route Options & Itineraries

### Option #1: Overnight Lake Camp & Illinois Peak Day Hike

Set up basecamp at St. Joe Lake. On day two, follow a well-maintained trail to the summit of Illinois Peak (7,690'). From the summit ridge, panoramic views stretch east toward Glacier National Park and northeast into the Canadian Rockies.

Historic features near the summit include several old mine prospects, the stone foundation of an early USFS fire lookout tower, and two historic pet graves. Return to St. Joe Lake for an afternoon swim and trout fishing.

![Wildflowers blooming below Gold Crown Peak](assets/images/img-1845-1.jpg)
_Wildflowers blooming below Gold Crown Peak._

### Option #2: Four-Peak Basin Scramble Circuit

A 6-hour, 15-minute alpine circuit encircling the entire St. Joe Lake basin, bagging four distinct summits in a single day. Approximately half of the 5-mile loop requires off-trail cross-country navigation:

1. **Unnamed Peak (7,260'):** From the lake, ascend south to the lowest saddle and climb steep bear grass slopes along the south ridge to gain the summit in under an hour.
2. **Graves Peak (7,235'):** Descend to the saddle, follow the ridgeline east to join the Stateline Trail, and look for a decommissioned trail heading uphill southwest. Follow the ridge spine cross-country to Graves Peak summit.
3. **Illinois Peak (7,690'):** Rejoin the Stateline Trail and follow spur trails leading directly to the Illinois Peak summit ridge.
4. **Gold Crown Peak (7,374'):** Descend toward the lake until reaching the saddle below Gold Crown Peak. Scramble the ridge to a double peak offering dramatic views of the entire basin.
5. **Return:** Side-hill southeast through alpine meadows back to the main lake trail.

![Gold Crown Peak with Illinois Peak in the background](assets/images/img-6082-1-1.jpg)
_Gold Crown Peak with Illinois Peak in the background._

### Option #3: Stateline Point-to-Point Shuttle Hike

With two vehicles, park one car at the main trailhead. Drive the second vehicle 6 miles back to Cedar Creek Pass. Hike the Stateline National Recreation Trail along the ridge down to St. Joe Lake. On the final day, descend Trail #49 along the river back to your vehicle.

---

## Getting There & Trailhead Directions

1. Drive **I-90 East** to **Superior, Montana**.
2. Take the exit south and follow **Diamond Road** a short distance to **Cedar Creek Road (FS Road #320)**.
3. Drive **25 miles** up Cedar Creek Road to the pass, then continue **6 miles** down to the trailhead.
4. Total driving time on dirt roads is approximately 1.5 hours.

!!! tip "Road Conditions & Maintenance"

    The Montana approach via Cedar Creek Road is well-maintained gravel. Access from the Idaho side of the pass is rougher and requires higher vehicle clearance.

---

## Hazards & Local Amenities

!!! warning "Scrambling & Exposure Hazards"

    Scrambling the basin ridgelines involves steep terrain and sheer drop-offs. Stay well back from cliff edges and unstable cornices.

### Local Attractions & Points of Interest

- **Regional Destinations:** Red Ives Ranger Station, Avery, North Fork Clearwater River, Kelly Creek, Clark Fork River.
- **Refreshments & Pubs (R & P):**
  - **Radio Brewing Company** (Kellogg, ID)
  - **City Limits Pub & Grill** (Wallace, ID)

---

## Photo Gallery

![Saddle scramble route up Peak 7260](assets/images/img-1878-1-1.jpg)
_Saddle scramble route up Peak 7260._

![Golden Eagle soaring above the St. Joe Lake basin](assets/images/img-1865-1.jpg)
_Golden Eagle soaring above the St. Joe Lake basin._

![High ridge traverse above St. Joe Lake](assets/images/img-1878-2.jpg)
_High ridge traverse above St. Joe Lake._

![Overview of St. Joe Lake basin](assets/images/img-1826.jpg)
_Overview of St. Joe Lake basin._
"""

with open("docs/hike.md", "w", encoding="utf-8") as fp:
    fp.write(content)

print("Refactored docs/hike.md successfully")
