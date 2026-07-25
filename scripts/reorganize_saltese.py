import os

content = """---
title: "Saltese Highlands Summit Loop"
tags:
  - Mountain Biking
  - Spokane Valley
  - Saltese Uplands
  - Conservation Area
  - Trail Riding
stats:
  - label: Activity
    icon: bicycle
    value: Mountain Biking & Trail Running
  - label: Location
    icon: map-marker
    value: Saltese Uplands Conservation Area, Greenacres, WA
  - label: Season
    icon: calendar
    value: Spring & Fall (Exposed West-Facing Slope)
  - label: Elevation
    icon: terrain
    value: ~650' Elevation Gain
  - label: Maps
    icon: map
    value: Spokane County Parks / Trailforks
notes:
  - label: Saltese Uplands Loop to Summit Route on Trailforks
    url: https://www.trailforks.com/route/saltese-uplands-loop-to-summit-loop/
---

![Saltese Highlands Summit Loop](../assets/images/375476475.jpg)
_Saltese Highlands Summit Loop._

The Saltese Uplands Conservation Area offers open, rolling singletrack through grassland hills overlooking the Saltese Flats and Spokane Valley. Because the slopes face west into the afternoon sun, this trail network is an absolute favorite for spring and fall riding.

!!! tip "Seasonal Riding Advice"

    The open grasslands provide zero shade during mid-summer, making afternoon rides uncomfortably hot. Plan your rides for crisp spring mornings, autumn afternoons, or early summer sunsets to catch the best lighting over the valley.

---

## Route Description & Riding Strategy

This loop route ascends to the summit via the gradual, less steep leg of the trail before descending the steeper section back toward Turtle Gulch. The moderate loop distance makes it ideal for a quick workout or combining multiple laps for endurance training.

- **Ascent:** Follow the main Uplands Loop trail as it climbs gently along the open southern contour.
- **Summit Loop:** Turn onto the Summit Loop junction for sweeping 360-degree views of Mica Peak, the Saltese Wetlands restoration area, and the Spokane Valley.
- **Descent:** Enjoy the fast singletrack descent returning down through Turtle Gulch to the main trailhead parking lot.

---

## Photo Gallery

![Overlooking the Saltese Wetland Area](../assets/images/202204171030-turtle-gulch.jpg)
_Overlooking the Saltese Wetland Area from the Turtle Gulch and Uplands Loop junction._

![Uplands Loop and Summit Loop Junction](../assets/images/202204171035-uplands-summit-junction.jpg)
_Uplands Loop and Summit Loop junction amidst open hillside grasslands._
"""

with open("docs/bike/saltese-highlands-summit-loop.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized saltese-highlands-summit-loop.md successfully")
