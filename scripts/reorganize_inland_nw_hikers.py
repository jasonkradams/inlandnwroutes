import os

content = """---
title: "Inland NW Hikers"
tags:
  - Resources
  - Hiking Clubs
  - Community
  - Inland NW Hikers
notes:
  - label: Inland NW Hikers Meetup Group
    url: https://www.meetup.com/Inland-Northwest-Hikers/
---

**Inland NW Hikers** is a passionate community of local outdoor enthusiasts dedicated to exploring the trails of the Inland Northwest and sharing memorable experiences in nature.

!!! info "Group Mission & Community"

    "Our goal is to foster an atmosphere where people have an opportunity to enjoy getting out in a relaxed and social environment. Several of our organizers hold leadership positions in local non-profits devoted to preserving and protecting wild land and water across the Inland Northwest."

---

## Overview & Activities

From casual park walks to challenging mountain ascents, Inland NW Hikers leads year-round events designed for hikers of all experience levels.

- **Primary Focus:** Day hikes and snowshoe outings across Washington, Idaho, and Montana.
- **Multi-Sport Outings:** Kayaking, canoeing, bicycling, and human-powered recreation.
- **Educational Workshops:** Leadership-led backcountry safety, conservation awareness, and trail skills.
- **Proven Track Record:** Over **1,000 hikes led** across 9+ years of community adventure.
- **Membership & Dog Policy:** Open to anyone ages 18+. Dogs are welcome on most hikes at individual event organizers' discretion.

---

## Event Difficulty Rating System

Every outing posted by Inland NW Hikers includes a streamlined rating code:

- **Rating Format:** The **number** represents total mileage, while the **letter** represents elevation gain.
- **Event Descriptions:** Always read the organizer's full write-up for trail conditions, technical difficulty, expected weather, and required gear.

---

## Frequent Hiking Destinations

| Region | Primary Destinations & Parks |
| :--- | :--- |
| **Spokane County & Nearby Parks** | Mt. Spokane State Park, Riverside State Park, Antoine Peak Conservation Area, Beacon Hill, Dishman Hills, South Hill Bluffs, Glenrose Unit, Rocks of Sharon, Little Spokane River, Mica Peak, Liberty Lake Regional Park |
| **Regional Backcountry** | Central Washington, Northern Washington, North Idaho Panhandle, and Western Montana |

---

## Get Involved

Join upcoming hikes, connect with local outdoor companions, and explore upcoming events on the official Meetup page:

- **Official Meetup Group:** [Inland NW Hikers on Meetup](https://www.meetup.com/Inland-Northwest-Hikers/)
"""

with open("docs/resources/general/inland-nw-hikers.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized inland-nw-hikers.md successfully")
