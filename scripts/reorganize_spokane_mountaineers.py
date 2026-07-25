import os

md_content = """---
tags:
  - Resources
  - Conservation & Organizations
  - Mountaineering & Education
stats:
  - label: Organization Name
    value: "Spokane Mountaineers"
  - label: Founded
    value: "1915 (Over 100 Years of Heritage)"
  - label: Organization Type
    value: "501(c)(3) Non-Profit Outdoor & Mountaineering Club"
  - label: Leadership Structure
    value: "100% Volunteer-Led (Elected Board & Volunteer Instructors)"
  - label: Educational Offerings
    value: "15+ Schools, Clinics & Seminars (Climbing, Backpacking, Skiing, MTB, WFA)"
  - label: Official Website
    value: "[spokanemountaineers.org](https://www.spokanemountaineers.org)"
notes:
  - label: Spokane Mountaineers Official Website
    url: https://www.spokanemountaineers.org
  - label: Spokane Mountaineers Schools & Clinics Directory
    url: https://www.spokanemountaineers.org/s/schools-and-clinics
  - label: Member Benefits & Join the Club
    url: https://www.spokanemountaineers.org/s/member-benefits
---

# Spokane Mountaineers

![Spokane Mountaineers Logo](../../assets/images/spokane-mountaineers-logo-orig.png)
_Spokane Mountaineers Logo._

The Spokane Mountaineers is an all-volunteer 501(c)(3) non-profit outdoor organization dedicated to mountain
climbing, backpacking, backcountry skiing, mountain biking, conservation, and outdoor safety in the Inland
Northwest.

---

## Overview & Organizational Mission

The mission of the Spokane Mountaineers is to encourage good fellowship among outdoor enthusiasts, maintain a
vibrant schedule of volunteer-led mountaineering and backcountry trips, promote environmental conservation, and
teach safe, self-reliant outdoor skills.

Operating continuously for over a century, the club provides comprehensive outdoor education taught by experienced,
passionate volunteer instructors who have progressed through the club's own curriculum.

---

## Over 100 Years of Heritage

Founded in **1915** by a group of Spokane Public Library staff members (originally established as the *Spokane
Walking Club*), the organization celebrated its **Centennial Anniversary in 2015**.

- **Historical Legacy:** Over 100 years of leading climbs, trail explorations, and conservation initiatives across the
  Selkirks, Cabinets, Cascades, and Canadian Rockies.
- **Centennial Publication:** Commemorated its 100-year milestone with the publication of *Peaks and Valleys: The
  Mountaineers First 100 Years*.
- **75+ Years of Mountain School:** The club's flagship Mountain School has been training Inland Northwest climbers
  in glacier travel, crevasse rescue, and alpine climbing since the mid-20th century.

---

## Educational Schools, Clinics & Seminars

The Spokane Mountaineers offer a comprehensive suite of hands-on educational courses designed to build self-reliance
and safety in the backcountry. All schools are open exclusively to club members and taught by volunteer leaders.

### Mountaineering & Climbing Schools

- **Mountain School:** Cornerstone 75+ year course covering snow/glacier travel, crevasse rescue, rock climbing,
  navigation, weather, and trip planning. *(Prerequisite: Backpacking foundation)*.
- **Rock School:** Top-rope rock climbing fundamentals, tying in, belaying, rappelling, and anchor building for gym-to-crag
  transitions. *(Prerequisite: None; beginner friendly)*.
- **Sport Lead School:** Bolt-protected lead climbing, lead belaying (ATC & GRIGRI), clipping, cleaning quickdraws,
  and fall safety. *(Prerequisite: Rock School or top-rope experience)*.
- **Trad Lead School:** Placing and removing traditional gear protection, multi-pitch efficiency, and trad anchor
  construction. *(Prerequisite: Sport lead experience & Rock/Mountain School)*.
- **Multipitch Sport School:** Multi-pitch sport climbing techniques, rope management, and belay station efficiency.
- **Alpine Climbing School:** 12-month capstone mentorship program applying multi-pitch efficiency to technical alpine
  peak objectives. *(Prerequisite: Mountain School, Trad Lead, Ice Seminar)*.
- **Ice Climbing Seminar:** Top-rope and lead ice climbing movement and tool placement, typically held in Hyalite
  Canyon, Montana.
- **Aid Climbing Seminar:** Big-wall aid placement techniques, jumaring, and haul system management.
- **Crack Climbing Seminar:** Specialized technique instruction for finger, hand, fist, and off-width crack climbing.
- **High Angle Rescue Seminar:** Self-rescue and partner rescue systems, hauling, and escaping the belay on vertical
  terrain.

### Backpacking & Non-Technical Scrambling

- **Backpack School:** A popular foundational course featuring indoor gear lectures, clothing layering advice,
  training hikes, and a weekend overnight campout designed for novice backpackers.
- **Scramble School:** Teaches non-technical peak bagging and off-trail travel across steep, rocky, and brushy terrain.
  Focuses on safe movement, handholds, scree navigation, and off-trail map/compass orientation.

### Backcountry Skiing & Mountain Biking

- **Backcountry Skiing 101 & Backcountry Ski School:** Teaches intermediate and advanced skiers how to safely transition
  from resort lifts to sidecountry and backcountry powder, covering touring gear, track-setting, and terrain selection.
- **Mountain Bike Fundamentals:** A 1-day skills clinic focused on body positioning, effective braking, cornering,
  and navigating technical trail obstacles.
- **Mountain Bike Intermediate:** Advanced singletrack maneuvering, drops, rock gardens, and technical trail riding.

### Wilderness Medicine & Leadership Development

- **Wilderness First Aid (WFA):** A 16-hour certification course (offered in partnership with Longleaf Wilderness
  Medicine) covering wilderness medical emergencies, patient assessment, and trauma management when help is hours away.
- **Wilderness First Responder (WFR):** Comprehensive 80-hour medical training for backcountry leaders and trip guides.
- **Leadership Development:** Internal training program for trip leaders, safety officers, and committee chairs.

---

## Member Benefits & Community Activities

Membership in the Spokane Mountaineers opens doors to a supportive, active outdoor community:

- **Year-Round Activities:** Access to hundreds of volunteer-led trips annually, including day hikes, backpack trips,
  alpine climbs, ski tours, and mountain bike rides.
- **Educational Priority:** Priority registration and discounted tuition for all club schools, clinics, and seminars.
- **Local Business Discounts:** Exclusive member discounts at participating Inland Northwest outdoor outfitters and
  retail partners.
- **Social Community:** Monthly club meetings, guest speaker presentations, slide shows, and social gatherings.

---

## Volunteer Leadership & Governance

The Spokane Mountaineers is governed 100% by volunteer members.

- **Board of Directors:** An elected volunteer Board of Directors manages club governance, conservation advocacy,
  and financial stewardship.
- **Volunteer Instructors:** All schools, clinics, and trips are led by experienced volunteer members who donate hundreds
  of hours annually to pass along backcountry skills to the next generation.

To learn more, view course schedules, or become a member, visit the [Spokane Mountaineers Official Website](https://www.spokanemountaineers.org).
"""

with open("docs/resources/conservation-and-like-minded-organizations/spokane-mountaineers.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Updated docs/resources/conservation-and-like-minded-organizations/spokane-mountaineers.md with high-fidelity logo image")
