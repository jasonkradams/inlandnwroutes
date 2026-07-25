import os

content = """---
title: Long Lake Launch
tags:
  - Paddling & Rivers
  - Spokane County
  - Lake Spokane
stats:
  - label: Waterbody
    value: Long Lake (Spokane River)
  - label: Reservoir Area
    value: 5,000+ Acres
  - label: Elevation
    value: 1,539'
  - label: Launch Type
    value: Public Boat Launch
  - label: Launch Coordinates
    value: 47°48′51″N 117°46′56″W
notes:
  - label: Spokane County Parks Information
    url: https://www.spokanecounty.org/parks
  - label: Spokane County Sheriff Emergency Contact
    url: tel:5094772240
---

Long Lake Launch provides water access to the lower section of Lake Spokane, a 21-mile Spokane River reservoir formed above the Avista Long Lake Dam. Located in western Spokane County, this launch offers a peaceful entry point for exploring the scenic bluffs, sheltered bays, and protected shorelines of Fisk State Park and the McLellan Conservation Area.

!!! info "Trip Planning & Water Safety Alerts"

    - **Algae & Health Alerts:** During warm late-summer months, blue-green algae blooms may occur in shallow reservoir coves. Check local health postings prior to swimming or allowing pets in the water.
    - **Weather Forecasts:** Check [NOAA Weather Conditions for Long Lake](https://forecast.weather.gov/MapClick.php?lat=47.8142&lon=-117.7822) prior to launching.

---

## Paddle Route & Highlights

- **Fisk State Park & McLellan Conservation Area:** Paddling downstream from the launch provides direct water access to public shorelines at Fisk State Park and the McLellan Conservation Area.
- **Conservation History:** The 400-acre McLellan property was originally owned by a long-time Spokane Mountaineers member before being preserved for public recreation through Spokane County's Conservation Futures program.
- **Wildlife & Granite Bluffs:** Towering granite cliffs, ponderosa pine slopes, and osprey nesting sites line the reservoir banks.

---

## Driving Directions

1. From North Spokane, drive north on **N. Driscoll Boulevard**, which transitions into **WA-291 (Nine Mile Road)**.
2. Turn left (west) onto **W. 7 Mile Road**, which becomes **W. Four Mound Road**.
3. Turn north onto **N. Wood Road**, which transitions into **W. Charles Road** and then **W. Long Lake Road**.
4. Follow W. Long Lake Road under the high-voltage transmission lines.
5. Approximately 400 feet after passing the power lines, turn right (north) onto the unpaved access road leading down to the launch site.

---

## Nearby Attractions

- Avista Long Lake Dam & Hydroelectric Station
- Fisk State Park Shoreline Trails
- McLellan Conservation Area
- Nine Mile Recreation Area

---

## Photo Gallery

![Long Lake Launch Shoreline on Lake Spokane](../../../assets/images/5132025306p-2.jpg)
_Long Lake Launch Shoreline on Lake Spokane._
"""

with open("docs/paddle/washington/eastern-washington/long-lake-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized long-lake-launch.md successfully")
