import os

md_content = """---
tags:
  - Peaks & Mountains
  - Moderate
  - Day Hiking
  - Scenic Overlook
stats:
  - label: Activity Type
    value: Day Hiking, Scenic Overlooks & Beach Access
  - label: Distance
    value: 6.2 Miles RT (Blacktail Overlook) / 4.0 Miles RT (Maiden Rock)
  - label: Elevation Gain
    value: 1,750 ft (Blacktail Overlook) / 1,200 ft (Maiden Rock Return)
  - label: Trail Difficulty
    value: Moderately Difficult
  - label: Designation
    value: Pend Oreille Lake Trail #117 & Maiden Rock Trail #321
  - label: Topo Maps
    value: IPNF / Sandpoint Ranger District / Cocolalla Lake Quad
  - label: Trailhead GPS
    value: '48°07''00"N 116°32''29"W'
  - label: Managing District
    value: Sandpoint Ranger District
notes:
  - label: Idaho Panhandle National Forests Alerts & Notices
    url: https://www.fs.usda.gov/alerts/ipnf/alerts-notices
  - label: USFS Sandpoint Ranger District
    url: https://www.fs.usda.gov/ipnf
---

# Blacktail Mountain Overlook & Maiden Rock Beach

![Panoramic 220-degree view of Lake Pend Oreille from Blacktail Mountain Overlook](../../../assets/images/61570003_orig.jpg)
_Panoramic 220-degree view of Lake Pend Oreille from Blacktail Mountain Overlook._

Rising above the western shoreline of Lake Pend Oreille near Cocolalla Lake, the **Butler Road Trailhead** serves as the launching point for two premier North Idaho hikes: **Pend Oreille Lake Trail #117** to the sweeping 220-degree Blacktail Mountain Overlook, and **Maiden Rock Trail #321** descending through cedar groves to a secluded beach.

---

## Overview & Trail Profile

!!! danger "Emergency Dispatch & Ranger Contact"

    In case of a backcountry emergency, injury, or water rescue, dial **911** or contact the Kootenai County Sheriff Dispatch at **[208-446-1300](tel:2084461300)**.

    - **USFS Managing Office:** Sandpoint Ranger District — **[208-769-3000](tel:2087693000)**.

!!! warning "Motorcycle Loose Rock & Poison Ivy Alert"

    - **Trail #117 Loose Rock:** Shared motorized dirt bike use on Trail #117 creates loose, rocky footing. Trekking poles are recommended.
    - **Maiden Rock Return Ascent:** Descending Trail #321 drops 1,200 vertical feet to the lake. The return hike is entirely uphill.
    - **Poison Ivy at Cliff Base:** Poison Ivy (*Toxicodendron radicans*) grows abundantly near the base of Maiden Rock cliffs. Identify three drooping leaves per stem and avoid contact.

---

## Route Options

### Option 1: Blacktail Mountain Overlook via Trail #117 (6.2 Miles RT)

From the Butler Road trailhead, follow **Pend Oreille Lake Trail #117** northeast as it climbs through mixed forest:

- **Distance & Elevation:** 3.1 miles one-way (6.2 miles round-trip) with 1,750 feet of elevation gain.
- **The Overlook Ridge:** At 2.5 miles, the trail skirts the western flank of Blacktail Mountain. A faint 0.5-mile spur path breaks east along an open ridge to two rocky outcroppings (the historic site of a former fire lookout).
- **Panoramic Vistas:** The second rocky outcropping delivers a breathtaking 220-degree panorama of Granite Point, the Green Monarch cliffs, Scotchman Peak, and the Cabinet Mountains Wilderness.

### Option 2: Maiden Rock Beach via Trail #321 (4.0 Miles RT)

Departing from the same trailhead, **Maiden Rock Trail #321** drops down toward the western shore of Lake Pend Oreille:

- **Distance & Elevation:** 2.0 miles one-way (4.0 miles round-trip) dropping 1,200 vertical feet down to the shoreline.
- **Cedar Forest & Beach:** The trail descends through a shaded canopy of young western red cedars to a pebble beach, picnic tables, pit toilet, and boat camp.
- **Deep Water & Swimming:** Water depths reach over 800 feet just 50 feet off Maiden Rock point, making it a popular spot for swimming, rock skipping, and sunbathing.

---

## Trailhead & Forest Road Directions

1. From **Coeur d'Alene, Idaho**, drive north on **US-95** past Careywood to the southern end of Cocolalla Lake.
2. At the first Blacktail Road turnoff on the right, continue 0.8 miles to the second **Blacktail Road** turnoff (a sharp right turn).
3. Follow Blacktail Road a short distance to where it turns left onto **Butler Road**.
4. Continue on Butler Road to the designated trailhead parking lot.

---

## Nearby Destinations & Attractions

- **Cocolalla Lake:** Scenic fishing and kayaking lake located just west of the trailhead.
- **Evans Landing & Talache Landing:** Historic lakefront access points on the west shore of Lake Pend Oreille.
- **North & South Chilco Mountains & Packsaddle Mountain:** Nearby high-elevation alpine ridge climbs.

---

## Hazards & Trail Safety

!!! warning "Trail Footing & Shoreline Hazards"

    - **Rocky Footing:** Loose scree and rock on Trail #117 require deliberate steps.
    - **Steep Lake Return:** Pace yourself on the 1,200-foot climb back up from Maiden Rock Beach, especially on hot summer afternoons.
    - **Poison Ivy:** Keep pets on leash near the Maiden Rock cliff base to avoid carrying poison ivy oils on fur.

---

## Refreshments & Nearby Dining

Popular dining spots in nearby Sandpoint, Athol, and Coeur d'Alene:

- **Moon Time:** Neighborhood pub in East Coeur d'Alene.
- **Franklin's Hoagies:** Sub sandwiches and hoagies.
- **Mexican Food Factory:** Regional Mexican restaurant.
- **Trails End Brewery:** Local craft brewery and pizzeria.

---

## Trip Planning & Weather

Check local weather forecasts before departing:

- **NOAA Weather Forecast:** [National Weather Service Cocolalla / Sandpoint Forecast](https://forecast.weather.gov)
- **Forest Alerts:** [Idaho Panhandle National Forests Alerts & Notices](https://www.fs.usda.gov/alerts/ipnf/alerts-notices)

---

## Photo Gallery

![The west shoreline of Lake Pend Oreille looking south from the ridge](../../../assets/images/p448.png)
_The west shoreline of Lake Pend Oreille looking south from the ridge._

---

![Granite rock formation overlooking the deep waters of Lake Pend Oreille](../../../assets/images/p449.png)
_Granite rock formation overlooking the deep waters of Lake Pend Oreille._

---

![Trail #321 descending down to Maiden Rock boat camp through a cool cedar forest](../../../assets/images/202159200.jpg)
_Trail #321 descending down to Maiden Rock boat camp through a cool cedar forest._

---

![Maiden Rock beach and 800-foot deep shoreline on Lake Pend Oreille](../../../assets/images/202159206.jpg)
_Maiden Rock beach and 800-foot deep shoreline on Lake Pend Oreille._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/blacktail-mountain-overlook.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized blacktail-mountain-overlook.md successfully")
