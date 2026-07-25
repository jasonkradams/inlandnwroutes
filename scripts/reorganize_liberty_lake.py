import os

third_content = """---
title: Liberty Lake 3rd Street Launch
tags:
  - Paddling & Rivers
  - Spokane County
  - Liberty Lake
stats:
  - label: Waterbody
    value: Liberty Lake
  - label: Lake Area
    value: 708 Acres
  - label: Paddle Distance
    value: 4.7 Mile Perimeter Loop
  - label: Elevation
    value: 2,047'
  - label: Launch Coordinates
    value: 47°39′14″N 117°05′02″W
notes:
  - label: Spokane County Parks Information
    url: https://www.spokanecounty.org/parks
  - label: Spokane County Sheriff Emergency Contact
    url: tel:5094772240
---

The 3rd Street Launch provides public boat access on the north shore of Liberty Lake, a 708-acre body of water situated just south of Interstate 90 between Spokane and the Idaho state line. Framed by the forested ridges of Mica Peak to the south, Liberty Lake offers an enjoyable 4.7-mile perimeter paddle close to the Spokane metropolitan area.

!!! info "Trip Planning & Access Notes"

    - **Parking & Congestion:** Paved launch access is located in a residential neighborhood along E. 3rd Avenue. Parking can be tight during peak summer weekends.
    - **Weather Forecast:** Check [NOAA Weather Conditions for Liberty Lake](https://forecast.weather.gov/MapClick.php?lat=47.6539&lon=-117.0839) before paddling.
    - **Clean, Drain, Dry:** Clean all watercraft prior to launching to prevent the spread of aquatic invasive species.

---

## Paddle Route & Highlights

- **4.7-Mile Perimeter Loop:** A complete circuit of Liberty Lake covers 4.7 miles of shoreline paddling past residential north shore docks, quiet reed beds, and timbered southern slopes.
- **Wildlife & Birding:** Bald eagles, osprey, waterfowl, and songbirds nest in the wetlands and forest canopy around the lake.
- **South End Recreation:** Paddle 1.7 miles south across the open lake to Liberty Lake Regional Park for swimming beaches, picnic shelters, and trail access.

---

## Driving Directions

1. From Interstate 90, take **Exit 296** (Liberty Lake / Otis Orchards).
2. Drive south on **N. Liberty Lake Road** to **E. Sprague Avenue**.
3. Turn left (east) onto E. Sprague Avenue and continue to **S. Molter Road**.
4. Turn right (south) onto S. Molter Road and proceed to **E. 3rd Avenue**.
5. Turn left (east) onto E. 3rd Avenue to reach the launch at the end of the street.

---

## Nearby Destinations

- Liberty Lake Regional Park (South Shore Launch & Trailhead)
- Mica Peak Conservation Area
- Saltese Flats Conservation Area
- Spokane River Water Trail
"""

park_content = """---
title: Liberty Lake Regional Park
tags:
  - Paddling & Rivers
  - Spokane County
  - Liberty Lake
stats:
  - label: Waterbody
    value: Liberty Lake
  - label: Park Area
    value: 3,591 Acres
  - label: Paddle Distance
    value: 4.7 Mile Perimeter Loop
  - label: Elevation
    value: 2,048'
  - label: Launch Coordinates
    value: 47°38′15″N 117°03′48″W
notes:
  - label: Liberty Lake Regional Park Trail Map & Fees
    url: https://www.spokanecounty.org/parks
  - label: Spokane County Sheriff Emergency Contact
    url: tel:5094772240
---

Liberty Lake Regional Park encompasses 3,591 acres on the southern shore of Liberty Lake. Featuring a sandy swimming beach, hand-launch watercraft access, designated picnic areas, campsites, and an extensive hiking trail system through ancient cedar groves and along Liberty Creek, it serves as the primary outdoor recreation destination on the lake.

!!! info "Trip Planning & Park Rules"

    - **Day-Use Fees:** Spokane County Parks charges a seasonal day-use entry fee during summer months.
    - **Weather & Conditions:** Check [NOAA Weather Conditions for Liberty Lake](https://forecast.weather.gov/MapClick.php?lat=47.6375&lon=-117.0633) before paddling.
    - **Trail System:** The 8.3-mile Liberty Lake Loop Trail leads past Split Creek and the Cedar Grove into the hills above the park.

---

## Paddle Route & Highlights

- **South Shore Paddling:** Launch from the park's sandy shore to explore quiet marshlands and reed beds along the inlet of Liberty Creek.
- **Lake Circuit:** Paddle 4.7 miles around the perimeter of Liberty Lake, taking in views of Mica Peak and the forested hillsides.
- **Water Recreation:** Ideal for kayaks, canoes, stand-up paddleboards, swimming, and warm-water fishing for bass and trout.

---

## Access & Driving Directions

1. From Interstate 90, take **Exit 296** (Liberty Lake / Otis Orchards).
2. Drive south on **N. Liberty Lake Road** for 1.7 miles.
3. Turn left (east) onto **E. Sprague Avenue** for 0.7 miles.
4. Turn right (south) onto **S. Molter Road** for 0.8 miles.
5. Turn left (east) onto **E. Valleyway Avenue**, which curves into **S. Zephyr Road** and **S. Idaho Road** heading south to the park entrance.

---

## Nearby Destinations

- Liberty Lake 3rd Street Launch (North Shore)
- Liberty Lake Loop Trail & Ancient Cedar Grove
- Mica Peak Conservation Area
- Saltese Flats Conservation Area
"""

with open("docs/paddle/washington/eastern-washington/3rd-street-launch.md", "w", encoding="utf-8") as f:
    f.write(third_content)

with open("docs/paddle/washington/eastern-washington/liberty-lake-regional-park.md", "w", encoding="utf-8") as f:
    f.write(park_content)

print("Reorganized 3rd-street-launch.md and liberty-lake-regional-park.md successfully")
