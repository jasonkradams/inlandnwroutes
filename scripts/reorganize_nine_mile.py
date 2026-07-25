import os

launch_content = """---
title: Nine Mile Recreation Area Launch
tags:
  - Paddling & Rivers
  - Spokane County
  - Washington State Parks
stats:
  - label: Waterbody
    value: Lake Spokane (Spokane River)
  - label: Launch Type
    value: Concrete Boat Ramp & Dock
  - label: Elevation
    value: 1,540'
  - label: Discover Pass Required
    value: "Yes"
  - label: Launch Coordinates
    value: 47°47′27″N 117°34′02″W
notes:
  - label: Riverside State Park Alerts & Permits
    url: https://parks.wa.gov/find-parks/state-parks/riverside-state-park
  - label: Spokane County Sheriff Emergency Contact
    url: tel:5094772240
---

Nine Mile Recreation Area is a popular water access site situated on Lake Spokane (the 21-mile reservoir formed along the Spokane River between Nine Mile Falls Dam and Long Lake Dam). Located within Riverside State Park, this site features paved boat ramps, docks, parking, picnicking, and swimming areas ideal for kayaks, canoes, paddleboards, and motorboats.

!!! info "Trip Planning & Regulations"

    - **Discover Pass:** A Washington State Discover Pass is required for vehicle parking at Riverside State Park sites.
    - **Current Conditions:** Check [NOAA Weather Conditions for Nine Mile Falls](https://forecast.weather.gov/MapClick.php?lat=47.7816&lon=-117.5456) before paddling.

---

## Paddle Route & Highlights

- **21-Mile Reservoir:** The Spokane River reservoir stretches 21 miles downstream to Long Lake Dam, providing calm, open-water paddling throughout summer with minimal linear current.
- **Scenic Granite Bluffs:** Paddle past granite rock formations, ponderosa pine forests, and quiet coves near Suncrest and Tumtum.
- **Wildlife Viewing:** Osprey, bald eagles, great blue herons, and waterfowl frequent the shoreline habitats along the river corridor.

---

## Access & Driving Directions

- From Spokane, follow WA-291 (Nine Mile Road) north past Nine Mile Falls Dam.
- Turn off WA-291 into the Nine Mile Recreation Area entrance within Riverside State Park to reach the boat launch and parking loop.

---

## Nearby Attractions

- Nine Mile Falls Dam & Powerhouse
- McLellan Conservation Area
- Fisk State Park
- Lake Spokane Campground
- Riverside State Park Trail System

---

## Photo Gallery

![Nine Mile Recreation Area Launch on Lake Spokane](../../../assets/images/5132025306p-2.jpg)
_Nine Mile Recreation Area Launch on Lake Spokane._
"""

rec_content = """---
title: Nine Mile Recreation Area
tags:
  - Paddling & Rivers
  - Spokane County
  - Washington State Parks
stats:
  - label: Waterbody
    value: Lake Spokane (Spokane River)
  - label: Reservoir Length
    value: 21 Miles
  - label: Elevation
    value: 1,540'
  - label: Discover Pass Required
    value: "Yes"
  - label: Launch Coordinates
    value: 47°47′27″N 117°34′02″W
notes:
  - label: Riverside State Park Information
    url: https://parks.wa.gov/find-parks/state-parks/riverside-state-park
  - label: Spokane County Sheriff Emergency Contact
    url: tel:5094772240
---

The Nine Mile Recreation Area provides water access and outdoor recreation along Lake Spokane, a 21-mile reservoir formed by Nine Mile Falls Dam and Long Lake Dam on the Spokane River. Managed as part of Riverside State Park, the area offers paddling, boating, fishing, rock scrambling, and trail exploration.

!!! info "Trip Planning & Regulations"

    - **Discover Pass:** A Washington State Discover Pass is required for all vehicle parking.
    - **Weather Forecast:** Check [NOAA Weather Conditions for Nine Mile Falls](https://forecast.weather.gov/MapClick.php?lat=47.7816&lon=-117.5456) prior to launching.

---

## Paddle Route & Highlights

- **Spokane River Reservoir:** The 21-mile stretch between Nine Mile Falls Dam and Long Lake Dam features smooth, quiet water ideal for touring kayaks and paddleboards.
- **Tumtum Rock Scrambling:** Granite bluffs and climbing/scrambling outcrops line the reservoir shorelines near Tumtum and Lake Spokane Campground.
- **Wildlife & Ecology:** Home to nesting osprey, bald eagles, and aquatic wildlife along ponderosa pine shorelines.

---

## Access & Directions

From Spokane, travel north on WA-291 (Nine Mile Road) past Nine Mile Falls Dam through Suncrest toward Tumtum to access Nine Mile Recreation Area entrance turnoffs.

---

## Nearby Points of Interest

- Nine Mile Falls Dam
- McLellan Conservation Area
- Fisk State Park
- Lake Spokane Campground

---

## Photo Gallery

![Nine Mile Recreation Area Shoreline](../../../assets/images/5132025306p-2.jpg)
_Nine Mile Recreation Area Shoreline._
"""

with open("docs/paddle/washington/eastern-washington/9-mile-recreation-area-launch.md", "w", encoding="utf-8") as f:
    f.write(launch_content)

with open("docs/paddle/washington/eastern-washington/nine-mile-recreation-area.md", "w", encoding="utf-8") as f:
    f.write(rec_content)

print("Reorganized both Nine Mile files successfully")
