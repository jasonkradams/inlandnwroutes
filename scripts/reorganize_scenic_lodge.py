import os

md_content = """---
tags:
  - Peaks & Mountains
  - Day Hiking
  - History & Speakeasy
stats:
  - label: Activity Type
    value: Day Hike
  - label: Distance
    value: 6.4 Miles RT
  - label: Elevation Gain
    value: 1,150 ft
  - label: Summit Elevation
    value: 3,658 ft
  - label: Trail Difficulty
    value: Strenuous (13% Average Grade)
  - label: Land Permit
    value: Inland Empire Paper Co. Permit Required
  - label: Topo Maps
    value: GaiaGPS / USFS 2016
  - label: Trailhead GPS
    value: '47°50''25.4"N 116°57''32.3"W'
notes:
  - label: Inland Empire Paper Co. Permit Portal
    url: https://www.ieprecreation.com/
  - label: City of Rathdrum Official Website
    url: https://www.rathdrum.org/
---

# Scenic Lodge on Rathdrum Mountain (3,658')

![Concrete entrance steps leading into the historical Scenic Lodge speakeasy foundation](../../../assets/images/202311180703.jpg)
_Concrete entrance steps leading into the historical Scenic Lodge speakeasy foundation._

Perched high on the south ridge of Rathdrum Mountain (3,658') in North Idaho, the ruins of the **Scenic Lodge** offer
a fascinating historical hike. Built during the Prohibition era and Great Depression, this remote structure once
operated as a mountainside dancehall and speakeasy. Today, hikers can explore the surviving stone basement walls,
concrete front entrance steps, and towering planted cottonwoods overlooking the Spokane Valley.

---

## Historical Discovery & Background

Over twenty years ago, local hikers exploring near the summit of Rathdrum Mountain stumbled across a flat mountain
bench featuring a massive stone foundation, concrete front steps, and a row of large deciduous trees that stood out in
stark contrast to the surrounding conifer forest. Given the craftsmanship, remote location, and commanding panorama, it
was long rumored to be an old Prohibition-era speakeasy.

Recent archival research and historic photographs shared by the *Old School North Idaho* historical group confirmed the
identity of the site as the **Scenic Lodge**. Historical USGS and USFS topographic maps pinpoint the structure on the
upper ridge, making it an ideal destination for a historical day hike.

!!! info "Prohibition-Era Mountainside Speakeasy"

    During the 1920s and 1930s, the Scenic Lodge served as a secluded retreat where visitors gathered for music,
    dancing, and social gatherings during the Great Depression. Resting on the stone foundation today offers panoramic
    views of both Mica Peak summits across the East Spokane Valley.

---

## Trail Description & Hike Profile

The hike to the Scenic Lodge foundation is a rigorous physical workout following an active timber management and fire
access road:

- **Distance & Elevation:** 6.4 miles round-trip with 1,150 feet of net elevation gain.
- **Steep Fire Road Grade:** The route ascends an Inland Empire Paper Company access road averaging a **13% incline**,
  with several pitch sections exceeding 18% along steep, cambered switchbacks.
- **Off-Road & Hunting Activity:** While the access road is gated to standard public motor vehicles, off-road vehicles
  (ORVs) and administrative timber trucks occasionally utilize the corridor. During autumn hunting seasons, hikers
  will encounter licensed hunters along the road.

---

## Trailhead Directions & Permit Requirements

!!! warning "Inland Empire Paper Company Permit Required"

    The access route traverses private industrial timberlands managed by the Inland Empire Paper Company (IEP).
    **An active IEP recreational permit is mandatory** prior to parking or entering the property. Permits can be
    purchased online at [IEP Recreation](https://www.ieprecreation.com/) or at authorized retail vendors in Rathdrum.

### Driving Directions

1. From **Rathdrum, Idaho**, head north on Highway 41 towards Spirit Lake.
2. Turn left (west) onto **Hidden Valley Road**.
3. Follow Hidden Valley Road to its terminus at the base of Rathdrum Mountain.
4. Park at the designated roadside pull-outs just before the gated Inland Empire Paper Company fire road on the right.

---

## Weather & Trip Planning

Check mountain weather forecasts before embarking, as the exposed fire road can be icy during late autumn and winter.

- **NOAA Weather Forecast:** [National Weather Service Spokane / Rathdrum Forecast](https://forecast.weather.gov)
- **Trail Network:** [Trailforks Rathdrum Mountain Trail Directory](https://www.trailforks.com/)

---

## Photo Gallery

![Parking pull-out at the end of Hidden Valley Road near the gated fire road access](../../../assets/images/202311180631.jpg)
_Parking pull-out at the end of Hidden Valley Road near the gated fire road access._

---

![Inland Empire Paper Company property boundary and permit notice sign](../../../assets/images/202311180648.jpg)
_Inland Empire Paper Company property boundary and permit notice sign._

---

![Hiking the steep Inland Empire Paper fire road toward Rathdrum Mountain](../../../assets/images/202311180657.jpg)
_Hiking the steep Inland Empire Paper fire road toward Rathdrum Mountain._

---

![Large cottonwood trees standing in front of the Scenic Lodge speakeasy site](../../../assets/images/202311180659.jpg)
_Large cottonwood trees standing in front of the Scenic Lodge speakeasy site._

---

![Concrete entrance steps leading into the historical Scenic Lodge speakeasy foundation](../../../assets/images/202311180703.jpg)
_Concrete entrance steps leading into the historical Scenic Lodge speakeasy foundation._
"""

target_path = "docs/hike/idaho/north-idaho-hikes/scenic-lodge-rathdrum-mountain.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Updated image paths in scenic-lodge-rathdrum-mountain.md successfully")
