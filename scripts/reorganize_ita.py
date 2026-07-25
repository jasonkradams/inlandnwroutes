import os

md_content = """---
tags:
  - Resources
  - Conservation & Organizations
  - Trail Maintenance
stats:
  - label: Organization Name
    value: "Idaho Trails Association (ITA)"
  - label: Organization Type
    value: "501(c)(3) Non-Profit Backcountry Trail Stewardship Organization"
  - label: Region & Scope
    value: "Idaho Public Lands & Backcountry Wilderness Trails"
  - label: Official Website
    value: "[idahotrailsassociation.org](https://www.idahotrailsassociation.org)"
notes:
  - label: Idaho Trails Association (ITA Official Site)
    url: https://www.idahotrailsassociation.org
  - label: ITA Volunteer Trail Work Projects
    url: https://www.idahotrailsassociation.org/projects/
---

# Idaho Trails Association

![Idaho Trails Association](../../assets/images/italogo_orig.png)
_Idaho Trails Association._

As the primary non-profit voice for Idaho's hikers, the Idaho Trails Association (ITA) promotes the conservation,
enjoyment, and protection of Idaho's expansive backcountry trail network on foot.

---

## Mission & Backcountry Stewardship

ITA is dedicated to keeping Idaho's hiking trails open, accessible, and well-maintained. Operating as a 501(c)(3)
non-profit organization, ITA partners with volunteers, youth groups, local organizations, and federal land managers
to preserve non-motorized trail access throughout Idaho's national forests and wilderness areas.

---

## Volunteer Trail Maintenance & Wilderness Advocacy

Through hands-on volunteer work parties, public education, and wilderness advocacy, ITA preserves Idaho's remote
trail systems:

- **Volunteer Trail Projects:** Organizing multi-day backcountry work trips and weekend trail clearings using traditional
  crosscut saws, Pulaskis, and hand tools.
- **Agency Partnerships:** Working closely with the U.S. Forest Service, Bureau of Land Management, and Idaho Department
  of Parks and Recreation to clear downed timber and repair trail washouts.
- **Wilderness Education & Advocacy:** Educating the public on Leave No Trace ethics and advocating for wilderness
  trail maintenance funding.

To sign up for a volunteer trail project or support backcountry trail stewardship in Idaho, visit the
[Idaho Trails Association Website](https://www.idahotrailsassociation.org).
"""

with open("docs/resources/conservation-and-like-minded-organizations/idaho-trails-association.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized idaho-trails-association.md successfully")
