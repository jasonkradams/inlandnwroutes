import os

content = """---
title: "Bonnie Lake Landing (Rock Creek Access)"
tags:
  - Lakes
  - Paddling
  - Washington Scablands
  - Rock Creek
  - Spokane County
stats:
  - label: Paddle Distance
    icon: map-marker-distance
    value: 5.4 miles round-trip (includes Rock Creek paddle)
  - label: Elevation
    icon: terrain
    value: 1,798'
  - label: Dimensions
    icon: vector-square
    value: 5.4 miles long, 327 acres
  - label: Launch GPS
    icon: crosshairs-gps
    value: 47°14'22" N 117°35'45" W
  - label: Maps
    icon: map
    value: Chapman Lake, Pine City, & Rock Lake USGS Topo Maps
notes:
  - label: "Spokane County Sheriff Emergency: 911 or (509) 477-2240"
    url: tel:5094772240
  - label: NOAA Weather Forecast for Bonnie Lake
    url: https://forecast.weather.gov/MapClick.php?lat=47.2394&lon=-117.5958
---

![Private Property Notice](../../../assets/images/20201024165655.jpg)
_Private Property Notice at Bonnie Lake Landing._

Bonnie Lake is a remote, narrow scabland lake enclosed by dramatic basalt walls rising 600 to 800 feet above the water. Reached via a scenic paddle up Rock Creek from the Belsby Road bridge, the lake features a single publicly accessible island campground halfway up its 5.4-mile length.

!!! warning "Strict Private Property & Access Boundaries"

    Except for the island campground and a 1-square-mile public parcel surrounding the island, **all shoreline around Bonnie Lake and along Rock Creek is privately owned**. Please respect local landowners by remaining on the water and staying strictly within public island boundaries. Do not trespass on private farmland or canyon walls.

---

## Description & Natural Attractions

- **Rock Creek Approach:** Launch at the Belsby Road bridge and paddle upstream along Rock Creek into Bonnie Lake. As you approach the lake entrance, look to your left to spot two unique lava caves formed when prehistoric basalt flows surrounded giant ancient trees.
- **Rock Arch & Basalt Palisades:** Near the creek mouth, look for a natural rock arch span. The lake itself is bounded by sheer 600- to 800-foot channelless scabland basalt cliffs.
- **Wildlife Observation:** Early morning paddlers frequently spot Turkey Vultures roosting on the high rock faces, catching morning thermals to soar gracefully over the canyon.
- **Island Camping:** The island situated 2/3 of the way up the lake offers the only public landing and primitive camping site on the water.

---

## Driving Directions & Launch Logistics

1. **From Cheney, WA:** Drive south out of Cheney on Cheney-Plaza Road for approximately 15 miles.
2. **Turn onto Rock Lake Road:** At the junction where Cheney-Plaza Road veers left, continue straight onto Rock Lake Road.
3. **Turn onto Belsby Road:** Turn left onto Belsby Road and continue for about 4 miles as the road winds down into the canyon bottom.
4. **Launch & Parking:** The launch site is located at the far right side of the Belsby Road bridge over Rock Creek.

!!! tip "Landowner Parking Courtesy"

    **Unload gear at the bridge, then park on the wide turnaround curve at the bottom of the hill before the bridge.** Local farmers maneuver heavy agricultural machinery out of field access gates near the bridge and will have vehicles towed if parked near the bridge abutments.

---

## Local Nearby Attractions & Provisions

- **Nearby Recreation:** Combine your trip with visits to Turnbull National Wildlife Refuge, Sprague Lake, or nearby scabland waterways.
- **Historic Sites:** Drive through downtown Sprague, WA, to check out Dave's Antique Truck Museum.
- **Rest & Provisions:** Stop in Cheney, WA, for pre-paddle meals or post-trip dining at Lenny's.

---

## Photo Gallery

![Lava Tree Caves near Bonnie Lake Entrance](../../../assets/images/11142021942p-jpeg.jpg)
_Two ancient lava caves formed by prehistoric basalt flows around gigantic trees near the lake entrance._
"""

with open("docs/paddle/washington/scablands/bonnie-lake-landing.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized bonnie-lake-landing.md successfully")
