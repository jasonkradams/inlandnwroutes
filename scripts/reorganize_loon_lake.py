import os

content = """---
title: Loon Lake Launch
tags:
  - Paddling & Rivers
  - Stevens County
  - Lakes
stats:
  - label: Waterbody
    value: Loon Lake
  - label: Lake Area
    value: 1,100 Acres
  - label: Paddle Distance
    value: 8.5 Mile Perimeter Loop
  - label: Elevation
    value: 2,385'
  - label: Launch Type
    value: WDFW Concrete Boat Ramp & Dock
  - label: Launch Coordinates
    value: 48°03′20″N 117°38′17″W
notes:
  - label: WDFW Loon Lake Access Information
    url: https://wdfw.wa.gov/places-to-go/water-access-sites
  - label: Stevens County Sheriff Emergency Contact
    url: tel:5096845296
---

The WDFW Public Access Site provides water access to Loon Lake, an 1,100-acre lake in southern Stevens County adjacent to the community of Loon Lake. Covering 2.6 miles in length with an 8.5-mile shoreline perimeter, Loon Lake is a popular regional destination for paddling, trout and warm-water fishing, and water sports.

!!! info "Trip Planning & Boating Considerations"

    - **Motorized Boat Traffic:** Shorelines are heavily populated and powerboat traffic is active on summer weekends. Early morning or shoulder-season paddles offer the quietest water conditions.
    - **Permit Required:** A WDFW Vehicle Access Pass or Washington State Discover Pass is required for vehicle parking at WDFW access sites.
    - **Weather Forecast:** Check [NOAA Weather Conditions for Loon Lake](https://forecast.weather.gov/MapClick.php?lat=48.0556&lon=-117.6381) prior to launching.

---

## Paddle Route & Highlights

- **8.5-Mile Perimeter Circuit:** Paddling the 8.5-mile shoreline loop offers an engaging circuit past residential docks, timbered hillsides, and quiet coves.
- **Fishery & Wildlife:** Popular fishery for kokanee salmon, rainbow trout, tiger muskie, and largemouth bass. Waterfowl and bald eagles frequent the shoreline habitats.
- **Seasonal Paddling:** Spring migration and cool autumn days bring tranquil conditions and autumn foliage along the surrounding hills.

---

## Driving Directions

1. From Spokane, drive north on **US-395 N** for approximately 30 miles (about 5 miles north of Clayton, WA).
2. Turn left (west) onto **WA-292 W** toward the town of Loon Lake and proceed for less than 1 mile.
3. Turn left onto **Loon Lake–McVay Pit Road**, continuing onto **McVay Road**.
4. Follow McVay Road as it transitions into **Shore Acres Road**.
5. Turn left into the signed **WDFW Loon Lake Public Access** parking lot and boat ramp.

---

## Nearby Destinations

- Deer Lake Launch
- Diamond Lake Launch
- Spokane River Water Trail
"""

with open("docs/paddle/washington/eastern-washington/loon-lake-launch.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized loon-lake-launch.md successfully")
