import os

content = """---
title: Bead Lake Launch
tags:
  - Paddling & Rivers
  - Pend Oreille County
  - Colville National Forest
stats:
  - label: Lake Area
    value: 720 Acres
  - label: Shoreline Distance
    value: 9 Miles
  - label: Lake Elevation
    value: 2,833'
  - label: Launch Type
    value: USFS Concrete Boat Ramp & Dock
  - label: Launch Coordinates
    value: 48°17′53″N 117°07′25″W
notes:
  - label: Colville National Forest Recreation Alerts
    url: https://www.fs.usda.gov/alerts/colville/alerts-notices
  - label: Pend Oreille County Sheriff Emergency Contact
    url: tel:5094473151
---

Located in the Colville National Forest north of Newport, Washington, **Bead Lake** is the largest lake in Pend Oreille County at 720 acres. Nestled within forested hills, Bead Lake is famous for its crystal-clear water, kokanee salmon and cutthroat trout fishing, and scenic shoreline paddling.

!!! info "Trip Planning & Regulations"

    - **Weather & Wind:** Check [NOAA Weather Conditions for Bead Lake](https://forecast.weather.gov/MapClick.php?lat=48.2981&lon=-117.1236) before paddling. Mountain lakes are susceptible to sudden wind shifts.
    - **No-Wake Zone:** A strict **100-foot no-wake zone** is enforced along the entire shoreline to protect shorelines, paddlecraft, and swimmers.
    - **Clean, Drain, Dry:** Clean all watercraft prior to launching to prevent the introduction of aquatic invasive species.

---

## Paddle Route & Highlights

- **9-Mile Perimeter Tour:** Paddling the entire shoreline offers 9 miles of quiet-water exploration along timbered hillsides and rocky coves.
- **Dispersed Lakeshore Camping:** Four boat-in and hike-in primitive campsites are located along the eastern shore, accessible via watercraft or the Bead Lake Hiking Trail (#127).
- **Fishing:** Popular fishery for kokanee salmon, lake trout, and coastal cutthroat trout.

---

## Access & Driving Directions

- **From Newport, WA:** Head east on US-2 E for 0.5 miles.
- **Le Clerc Road:** Turn left onto Le Clerc Road and continue north for 2.7 miles.
- **Bead Lake Road:** Turn right onto Bead Lake Road (Forest Road 3215) and proceed 7.5 miles to the USFS boat launch entrance on the south shore.
- **Map:** View [Google Maps Driving Directions to Bead Lake Launch](https://goo.gl/maps/EechMppboixAYxaw8).

---

## Nearby Paddles & Destinations

- Marshall Lake Launch
- Pend Oreille River Water Trail
- Diamond Lake Launch

---

## Photo Gallery

![Bead Lake USFS Launch Ramp and Dock](../../../assets/images/20201012172607_orig.jpg)
_Bead Lake USFS Launch Ramp and Dock._
"""

with open("docs/paddle/washington/eastern-washington/bead-lake-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized bead-lake-launch.md successfully")
