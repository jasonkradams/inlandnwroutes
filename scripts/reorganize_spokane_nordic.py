import os

md_content = """---
tags:
  - Winter & Skiing
  - Resources
  - Conservation & Organizations
stats:
  - label: Organization Name
    value: "Spokane Nordic Ski Association (SNSA)"
  - label: Organization Type
    value: "501(c)(3) Non-Profit Nordic Ski Club"
  - label: Trail Area
    value: "Mt. Spokane State Park Nordic Ski Area"
  - label: Land Partners
    value: "Washington State Parks, Inland Empire Paper Co., Idaho Department of Lands"
  - label: Mailing Address
    value: "PO Box 501, Spokane, WA 99210"
  - label: Official Website
    value: "[spokanenordic.org](https://www.spokanenordic.org)"
notes:
  - label: Spokane Nordic Ski Association Official Website
    url: https://www.spokanenordic.org
  - label: Mt. Spokane Nordic Trail Conditions & Grooming Reports
    url: https://www.spokanenordic.org/grooming
---

# Spokane Nordic Ski Association

The Spokane Nordic Ski Association (SNSA) is a volunteer-driven 501(c)(3) non-profit organization dedicated to
promoting, maintaining, and advocating for cross-country skiing in the Inland Northwest. Operating primarily at
Mt. Spokane State Park, SNSA provides trail maintenance, grooming support, youth and adult ski education, and
community events.

---

## Overview & Organizational Mission

Spokane Nordic exists to foster a vibrant community celebrating health, fitness, family, and outdoor winter
recreation. Run entirely by a volunteer Board of Directors, SNSA works continuously to enhance Nordic skiing
opportunities for winter sports enthusiasts of all ages and skill levels throughout the region.

---

## Trail Network & Land Partnership

The expansive Nordic Ski Area at Mt. Spokane State Park is made possible through a unique cooperative partnership
between **Washington State Parks**, **Inland Empire Paper Company**, and the **Idaho Department of Lands**.

Through membership dues, grants, and private donations, Spokane Nordic directly funds and manages:

- **Trail Maintenance & Signage:** Installing trail maps, directional signs, and safety markers across the network.
- **Land Access & Leases:** Covering land lease fees to keep private and state-managed timberlands open for winter
  public recreation.
- **Facilities & Shelters:** Providing firewood, maintaining trail warming huts, and financing trailhead facility
  improvements.
- **Grooming Operations & Advocacy:** Coordinating grooming logistics with Washington State Parks and advocating for
  state trail development funding.

---

## Community Programs, Lessons & Events

Spokane Nordic offers comprehensive Nordic skiing instruction and community programming:

- **Youth & Adult Lessons:** Offering classic and skate ski instruction for all ages, from complete beginners to
  advanced technique clinics.
- **Junior Nordic Team:** Supporting youth cross-country ski development and competitive racing programs.
- **Winter Events & Races:** Hosting annual community ski races, full-moon night skis, and social gatherings.

---

## Membership & Volunteer Support

Spokane Nordic is member-funded and community-supported. Joining SNSA helps maintain the Mt. Spokane trail system
and provides members with:

- Regular grooming updates and trail conditions newsletters.
- Invitations to exclusive club ski clinics and social events.
- Opportunities to volunteer for work parties, trail clearing, and event support.

For more information, trail maps, or to become a member, visit the [Spokane Nordic Ski Association Website](https://www.spokanenordic.org).

---

## Photo Gallery

![Groomed Nordic ski trail at Mt. Spokane State Park](../../assets/images/202210021210.jpg)
_Groomed Nordic ski trail at Mt. Spokane State Park._

![Cross-country skiers enjoying classic and skate trails](../../assets/images/202210021211.jpg)
_Cross-country skiers enjoying classic and skate trails._

![Nordic ski chalet and staging area at Mt. Spokane](../../assets/images/202210021212.jpg)
_Nordic ski chalet and staging area at Mt. Spokane._

![Winter trail signage in the Mt. Spokane Nordic system](../../assets/images/202210021213.jpg)
_Winter trail signage in the Mt. Spokane Nordic system._

![Snow-covered evergreen forest along the Nordic trails](../../assets/images/202210021214.jpg)
_Snow-covered evergreen forest along the Nordic trails._

![Skate skiers on freshly groomed corduroy](../../assets/images/202210021215.jpg)
_Skate skiers on freshly groomed corduroy._

![Junior Nordic ski lesson program in action](../../assets/images/202210021216.jpg)
_Junior Nordic ski lesson program in action._

![Panoramic view of Mt. Spokane winter trail network](../../assets/images/202210021217.jpg)
_Panoramic view of Mt. Spokane winter trail network._
"""

with open("docs/resources/conservation-and-like-minded-organizations/spokane-nordic-ski-association.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized spokane-nordic-ski-association.md successfully")
