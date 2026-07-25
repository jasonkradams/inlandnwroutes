import os

md_content = """---
tags:
  - Resources
  - Conservation & Organizations
  - Trail Maintenance
stats:
  - label: Organization Name
    value: "Washington Trails Association (WTA)"
  - label: Organization Type
    value: "501(c)(3) Non-Profit Trail Advocacy & Stewardship Organization"
  - label: Region & Scope
    value: "Washington State & Pacific Northwest Public Lands"
  - label: Annual Volunteer Effort
    value: "3,800+ Volunteers / 120,000+ Volunteer Trail Work Hours"
  - label: Official Website
    value: "[wta.org](https://www.wta.org)"
notes:
  - label: Washington Trails Association (WTA Official Site)
    url: https://www.wta.org
  - label: WTA Hiking Guide & Trip Reports
    url: https://www.wta.org/go-outside/hikes
  - label: WTA Volunteer Trail Work Parties
    url: https://www.wta.org/get-involved/volunteer
---

# Washington Trails Association

![Washington Trails Association](../../assets/images/wta-logo_orig.png)
_Washington Trails Association._

The Washington Trails Association (WTA) is the nation's largest state-based trail maintenance and hiking advocacy
organization. WTA mobilizes hikers and everyone who loves the outdoors to explore, steward, and champion trails and
public lands throughout Washington State.

---

## Mission, Advocacy & Volunteer Trail Stewardship

WTA protects trails through grassroots advocacy, public policy initiatives, and hands-on trail maintenance. By
partnering with federal, state, and local land managers, WTA works to ensure a safe, accessible, and sustainable
trail system across urban parks, state forests, and remote wilderness areas.

---

## Grassroots Advocacy & Public Land Protection

WTA advocates on crucial issues affecting hikers and outdoor recreationists across the Pacific Northwest:

- **Trail & Wilderness Funding:** Lobbying federal and state lawmakers for increased funding for public land managers
  and trail maintenance backlogs.
- **Access Preservation:** Protecting public access to trailheads, backcountry passes, and public recreation sites.
- **Wilderness Conservation:** Advocating for the protection of roadless areas, wild rivers, and fragile alpine
  ecosystems.

---

## Volunteer Trail Maintenance & Community Work Parties

WTA's advocacy voice is backed by the year-round dedication of thousands of volunteer trail stewards:

- **120,000+ Volunteer Hours:** More than 3,800 volunteers join WTA trail work parties annually, contributing over
  120,000 hours of volunteer trail labor each year.
- **Backcountry & Frontcountry Stewardship:** Volunteers build and repair trails ranging from local urban greenbelts
  to remote backcountry routes in the Cascades and Olympics.
- **Youth & Community Engagement:** WTA hosts youth trail crews, outdoor leadership training, and gear libraries to
  make outdoor recreation accessible to all communities.

To read crowd-sourced trip reports, find a hiking guide, or sign up for a volunteer trail work party, visit the
[Washington Trails Association Website](https://www.wta.org).
"""

with open("docs/resources/conservation-and-like-minded-organizations/washington-trails-association.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized washington-trails-association.md successfully")
