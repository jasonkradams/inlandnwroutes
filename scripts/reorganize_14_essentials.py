import os

content = """---
title: "The 14+ Essentials Checklist"
tags:
  - Backcountry Safety
  - 14 Essentials
  - Wilderness Preparedness
  - Survival
notes:
  - label: MRA Backcountry Safety Guide
    url: https://mra.org/wp-content/uploads/2016/05/backcountrysafety.pdf
  - label: Life Flight Network Emergency Membership
    url: https://lifeflight.org
---

![The 14+ Essentials Checklist](assets/images/1664054130.jpeg)
_The 14+ Essentials Checklist._

Every backcountry traveler—whether hiking solo, in a group, or as a couple—must carry their own complete 14 Essentials pouch. Never rely on others for basic survival gear. Know your equipment inside and out before venturing into the mountains.

!!! quote "Core Philosophy"

    "As you read this section, please understand that it is designed to inform you. But more importantly, all these topics are things you should do your own research on to further your knowledge. The most important thing you can take with you on your outing is... **Knowledge**."
    — **Chic Burge**

---

## The 14+ Essentials Breakdown

1. **Fire Starters:** Waterproof matches, lighters, commercial fire paste, beard lichen, dryer lint tubes packed in ziplock bags, and **1500°F road flares** for winter conditions.
2. **Plastic Grocery Bags:** Carry 6–12 heavy plastic grocery bags. They weigh only 6 grams each, hold up to 1.5 gallons of water to douse smoldering campfires, and serve as waterproof trash liners.
3. **Rain Gear, Umbrella & Emergency Poncho:** Lightweight umbrellas prevent overheating while hiking in rain or snow. Keep a heavy lawn trash bag with folded paper towels as an emergency poncho.
4. **Map & Compass (plus GPS):** GPS units fail when batteries die. Always carry physical USGS Topo and USFS Forest maps in ziplock bags, along with a baseplate compass.
   - *Paperclip Compass:* Magnetize a paperclip against a steel tool and float it on a leaf in still water to indicate the North-South axis.
   - *Analog Watch Method:* Point the hour hand at the Sun; halfway between the hour hand and 12 o'clock points South.
   - *Stick & Shadow Line:* Place a rock at the shadow tip of a stick; wait 15 minutes and mark the new tip. A line from the first rock to the second runs West to East.
   - *North Star (Polaris):* Extend a line through the outer cup stars of the Big Dipper to locate Polaris.
5. **Extra High-Protein Food:** Energy bars where protein grams exceed carbohydrate grams (such as MET-Rx bars with 32g of protein).
6. **Extra Water & Purification:** Carry a minimum of 2 quarts plus a filter (Sawyer Squeeze Mini). Drop water bottles along out-and-back routes to lighten your pack for the climb.
7. **Extra Clothing:** Spare wool/fleece socks, microfiber towel, polar fleece jacket/pants, wool gloves, stocking cap, and face mask.
8. **Paper Towels & Trowel:** Carry paper towels in ziplock bags instead of fragile toilet paper. Dig cat-holes 6+ inches deep and at least 200 feet from any water source.
9. **Emergency Shelter:** Space blanket, plastic sheeting with parachute cord, or a lightweight bivy tent.
10. **Headlight & Extra Batteries:** Modern COB (Circuit On Board) headlights flood the trail with wide lumens, improving depth perception over narrow LED spot beams. Date your batteries upon installation.
11. **Knives:** Carry a small pocket knife for food prep and a 6-inch fixed blade (Bowie style) for splitting kindling.
12. **First Aid Kit:** Sterile gauze, athletic tape, Coban wraps, pain relievers, **Spenco 2nd Skin Burn Pads** for blister relief, and feminine hygiene pads for heavy bleeding.
13. **Signaling Devices:** High-decibel whistle (3 blasts indicate SOS), canned air horn, or signaling mirror.
14. **Sun Protection:** SPF 50+ sunscreen, wide-brimmed sun hat (Sunday Afternoons), and 100% UVA/UVB sunglasses with side/nose shades for snow reflection.

---

## Wilderness Emergency Protocols & STOP

!!! danger "S.T.O.P. Protocol (Stop, Think, Observe, Plan)"

    - **S — STOP:** Sit down, calm your breath, stop moving, and whistle 3 long blasts.
    - **T — THINK:** Assess your situation with a clear, rational mind.
    - **O — OBSERVE:** Scan terrain for familiar peaks, ridges, or trail junctions.
    - **P — PLAN:** Prepare your night shelter early before darkness and cold set in.

### Chic's Extended Field Checklist

- **Life Flight Network Membership:** Medical helicopter evacuations can cost tens of thousands of dollars. An annual membership covering your household is essential for backcountry travelers ([(800) 982-9299](tel:8009829299) or [lifeflight.org](https://lifeflight.org)).
- **Mobile Search Apps:** Install *AirFlare* ($4.99/year) to assist search and rescue teams in locating your cell signal.
- **Personal Locator Beacons (PLB):** Carry a satellite communicator (Garmin inReach or PLB) for remote wilderness traverses.
- **Trail Marking:** Carry surveyor's tape to mark obscure trail junctions (retrieve tape on the return leg).
- **Communication:** Carry walkie-talkies for large, strung-out hiking groups.

---

## Conservation & Trail Partner Organizations

We work closely with regional trail advocacy and volunteer maintenance organizations to keep Inland Northwest trails open, accessible, and well-preserved.

### Washington Trails Association (WTA)

![WTA Logo](assets/images/wta-logo_orig.png)
_WTA Logo_

![WTA Volunteer Trail Crew](assets/images/img-4638-2.jpg)
_WTA Volunteer Trail Crew_

Washington Trails Association mobilizes hikers to explore, steward, and champion public lands. WTA protects trails through grassroots advocacy and organizes over 120,000 hours of volunteer trail maintenance annually across Washington State.

- **Learn More:** Read our full [Washington Trails Association Guide](resources/conservation-and-like-minded-organizations/washington-trails-association.md) or visit [wta.org](https://www.wta.org).

---

### Idaho Trails Association (ITA)

![Idaho Trails Association Logo](assets/images/italogo_orig.png)
_Idaho Trails Association Logo_

![ITA Beehive Lake Trail Work](assets/images/beehive-2016-3-1.jpg)
_ITA Beehive Lake Trail Work_

Idaho Trails Association is dedicated to keeping Idaho's hiking trails open for all. ITA mobilizes volunteers for single-day and weeklong backcountry trail clearing projects, promoting Leave No Trace principles and traditional tool stewardship across Idaho's wilderness areas.

- **Learn More:** Read our full [Idaho Trails Association Guide](resources/conservation-and-like-minded-organizations/idaho-trails-association.md) or visit [idahotrailsassociation.org](https://www.idahotrailsassociation.org).

---

### Spokane Mountaineers

![Spokane Mountaineers Logo](assets/images/img-0805.png)
_Spokane Mountaineers Logo_

Founded in 1915, the Spokane Mountaineers is an outdoor club devoted to mountain conservation, education, and recreation. The club hosts year-round hiking, climbing, skiing, and paddling outings alongside annual backcountry safety clinics.

- **Learn More:** Read our full [Spokane Mountaineers Guide](resources/conservation-and-like-minded-organizations/spokane-mountaineers.md) or visit [spokanemountaineers.org](https://www.spokanemountaineers.org).
"""

with open("docs/14-essentials.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized 14-essentials.md successfully")
