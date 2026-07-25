import os

content = """---
title: "Arrowleaf Trail (Antoine Peak)"
tags:
  - Mountain Biking
  - Antoine Peak
  - Spokane Valley
  - Conservation Area
  - Singletrack
stats:
  - label: Activity
    icon: bicycle
    value: Mountain Biking & Trail Running
  - label: Location
    icon: map-marker
    value: Antoine Peak Conservation Area (Trentwood Trailhead), Otis Orchards, WA
  - label: Trail Access
    icon: sign-direction
    value: Trentwood Trailhead (South Side)
  - label: Difficulty
    icon: speedometer
    value: Moderate Singletrack
  - label: Maps
    icon: map
    value: Spokane County Parks / Trailforks
notes:
  - label: Arrowleaf Trail Route on Trailforks
    url: https://www.trailforks.com/trails/arrowleaf-245711/
---

![Arrowleaf Trail](../assets/images/889206359.jpg)
_Arrowleaf Trail at Antoine Peak Conservation Area._

The Arrowleaf Trail is a scenic singletrack route traversing the south face of Antoine Peak Conservation Area near Otis Orchards. Accessed directly from the Trentwood Trailhead, the trail winds through open ponderosa pine forests and hillside meadows filled with bright yellow Arrowleaf Balsamroot (*Balsamorhiza sagittata*) wildflowers in spring.

!!! tip "Trentwood Trailhead Access"

    The Trentwood Trailhead on the south side of Antoine Peak provides direct access to the lower singletrack network, offering scenic vistas across the Spokane Valley toward the Saltese Uplands and Mica Peak.

---

## Route & Trail Features

- **South Slope Exposure:** The south-facing singletrack melts out early in spring, making it one of the first dry dirt mountain bike rides in eastern Spokane County.
- **Spring Wildflower Displays:** In May, the open hillsides erupt with brilliant yellow arrowleaf balsamroot and purple lupine blooms.
- **Climb & Flow:** Features a smooth, steady grade suitable for intermediate mountain bikers, trail runners, and hikers alike.

---

## Photo Gallery

![Spring view along the Arrowleaf Trail](../assets/images/202204170144.jpg)
_Spring view along the Arrowleaf Trail on the south slope of Antoine Peak._

![Singletrack traversing open ponderosa slopes](../assets/images/202204170143.jpg)
_Singletrack traversing open ponderosa pine slopes toward the Trentwood Trailhead._

![Overlooking Spokane Valley from Arrowleaf Trail](../assets/images/202204170142.jpg)
_Overlooking Spokane Valley and southern foothills from the Arrowleaf Trail._

![Arrowleaf balsamroot blooms along Antoine Peak](../assets/images/202204170141-1.jpg)
_Arrowleaf balsamroot blooms along the lower Antoine Peak singletrack network._
"""

with open("docs/bike/arrow-leaf.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized arrow-leaf.md successfully")
