import os

content = """---
title: "Fishtrap Lake Paddle Guide"
tags:
  - Lakes
  - Paddling
  - Washington Scablands
  - BLM Recreation Area
  - Spokane County
stats:
  - label: Paddle Distance
    icon: map-marker-distance
    value: 6.6 miles round-trip
  - label: Elevation
    icon: terrain
    value: 1,978'
  - label: Dimensions
    icon: vector-square
    value: 2.0 miles long & 190 acres
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°21'17" N 117°49'25" W
  - label: Maps
    icon: map
    value: USGS Fishtrap Lake Topo & BLM Fishtrap-Miller Ranch Recreation Map
notes:
  - label: "Spokane County Sheriff Emergency: 911 or (509) 447-2240"
    url: tel:5094472240
  - label: NOAA Weather Forecast for Fishtrap Lake
    url: https://forecast.weather.gov/MapClick.php?lat=47.3547&lon=-117.8236
---

![Fishtrap Lake Scabland Shoreline](../../../assets/images/img-0618.jpg)
_Fishtrap Lake Scabland Shoreline._

Fishtrap Lake is a tranquil 190-acre scabland lake surrounded by Bureau of Land Management (BLM) public lands, basalt rimrock, and historic homestead sites in southwestern Spokane County. Spring is the prime season to paddle Fishtrap Lake when temperatures are comfortable, the basalt hillsides turn vibrant green, wildflowers bloom, and migratory waterfowl appear in full breeding plumage.

!!! info "BLM Public Land Access"

    Most of the shoreline along Fishtrap Lake and the northern slopes toward Hog Canyon are managed by the Bureau of Land Management (BLM), offering public access for paddling, fishing, hiking, mountain biking, and primitive camping.

---

## Paddling Instructions & Points of Interest

- **Wildlife Viewing:** Spring paddling offers exceptional birdwatching, including American White Pelicans, nesting waterfowl, and Western Painted Turtles basking on logs along the quiet inlets.
- **Folsom Farm Interpretive Site:** Located along the access road, the historic Folsom Farm showcases how early 20th-century homesteaders converted the rugged scablands into family farms.
- **Historic World War I Dance Hall:** Near the lake's inlet stands an iconic wooden dance hall built over the water dating back to World War I.
- **BLM Trail Network:** The BLM Fishtrap Recreation Area trailhead provides hiking and mountain biking trails extending north and south through the scabland terrain.

---

## Driving Directions & Safety Hazards

1. **From Spokane, WA:** Take I-90 West for approximately 25 miles to **Fishtrap Exit 254**.
2. **South on Old State Highway:** Head south on Old State Highway for 2 miles to Scroggie Road.
3. **East on Scroggie Road:** Turn left (east) onto Scroggie Road and continue 1.5 miles to the WDFW Public Fishing access sign and boat launch.

!!! warning "Cold Water & Field Etiquette"

    - **Cold Spring Water:** Early spring water temperatures remain very cold. Always wear a PFD and dress appropriately for cold-water immersion.
    - **Field Etiquette:** Watch out for grazing cattle and cow patties along public access paths.

---

## Rest, Dining & Nearby Provisions

- **On-Lake Amenities:** Fishtrap Lake Resort offers seasonal boat rentals, tackle, snacks, and cabin rentals.
- **Regional Dining:** Head east into Cheney, WA, for post-paddle dining at Lenny's.

---

## Photo Gallery

Click any photo to view in high resolution with full captions.

![American White Pelican on Fishtrap Lake](../../../assets/images/20200525140507.jpg)
_American White Pelican resting on the open waters of Fishtrap Lake._

![Looking Northeast Up Fishtrap Lake](../../../assets/images/20200525140458.jpg)
_Looking northeast up the calm waters of Fishtrap Lake toward basalt rimrock._

![Western Painted Turtles Basking on Log](../../../assets/images/20200525140601.jpg)
_Western Painted Turtles basking in the spring sun on a submerged log._

![Lake Inlet and Historic Dance Hall](../../../assets/images/20200525140448.jpg)
_Inlet area near the historic World War I dance hall at the head of the lake._
"""

with open("docs/paddle/washington/scablands/fishtrap-lake-wa.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized fishtrap-lake-wa.md with full-width photo gallery successfully")
