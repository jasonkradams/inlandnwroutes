import os

content = """---
title: Boulder Beach Landing
tags:
  - Paddling & Rivers
  - Spokane County
  - Spokane River
stats:
  - label: Waterbody
    value: Spokane River
  - label: Access Type
    value: Hand Launch & Landing Beach
  - label: Elevation
    value: 1,915'
  - label: Parking
    value: Paved Parking Lot
  - label: Launch Coordinates
    value: 47°41′40″N 117°18′29″W
notes:
  - label: Spokane County Parks & Trails Info
    url: https://www.spokanecounty.org/parks
  - label: Spokane County Sheriff Emergency Contact
    url: tel:5094772240
---

**Boulder Beach Landing** (also referred to as Boulder Bay Landing) is a designated non-motorized hand-launch and landing site located along the Spokane River on East Upriver Drive. Positioned adjacent to the Spokane River Centennial Trail and directly west of Camp Sekani Park, Boulder Beach provides easy access for kayaks, canoes, and stand-up paddleboards exploring the smooth water stretch above Upriver Dam.

![Aerial Satellite Map of Boulder Beach Landing on the Spokane River](../../../assets/images/2021527321-jpeg-1_orig.jpeg)
_Aerial Satellite Map of Boulder Beach Landing on the Spokane River._

!!! info "Trip Planning & Hand Launch Regulations"

    - **Non-Motorized Hand Launch Only:** Boulder Beach is exclusively a hand-launch site for non-motorized paddlecraft. Motorized powerboats and jet skis cannot be launched here.
    - **Short Path Carry:** A short, gentle foot path leads from the parking lot down to the sandy riverbank.
    - **Weather & Flow Forecasts:** Check [NOAA Weather Conditions for Spokane River](https://forecast.weather.gov/MapClick.php?lat=47.6944&lon=-117.3081) before paddling.

---

## Paddle Route & Highlights

- **Spokane River Paddling:** Enjoy wide, calm-water paddling upstream toward Millwood or downstream toward Minnehaha Rocks.
- **Centennial Trail Access:** Located directly along the paved Spokane River Centennial Trail, making it an excellent multi-sport destination for paddling, cycling, and running.
- **Nearby Parks & Climbing:** Situated between the Camp Sekani Park mountain bike trail network to the east and the Minnehaha Rocks climbing area to the west.

---

## Driving Directions

- **From East (Millwood / Argonne Rd):** Drive north on **N. Argonne Road** to **E. Upriver Drive**. Turn left (west) onto E. Upriver Drive and proceed for approximately 1 mile to the signed Boulder Beach parking entrance on the river side.
- **From West (Spokane / Minnehaha):** Follow **E. Upriver Drive** east past the Minnehaha Climbing Area for approximately 1.5 miles to the Boulder Beach parking lot.

---

## Nearby Destinations

- Spokane River Centennial Trail
- Camp Sekani Park Mountain Bike Trails
- Minnehaha Rocks Climbing Area
- Upriver Dam & Reservoir

---

## Photo Gallery

- ![Aerial Satellite Map of Boulder Beach Landing on the Spokane River](../../../assets/images/2021527321-jpeg-1_orig.jpeg)
- ![Spokane River Water Health Alert Notice](../../../assets/images/5132025306p-2.jpg)
"""

with open("docs/paddle/washington/eastern-washington/boulder-bay-landing.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized boulder-bay-landing.md successfully")
