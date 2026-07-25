import os

# Create directory docs/resources/trail-etiquette-and-skills
os.makedirs("docs/resources/trail-etiquette-and-skills", exist_ok=True)

# 1. index.md
index_content = """---
title: Trail Etiquette & Backcountry Skills
tags:
  - Resources
  - Trail Etiquette
  - Wilderness Skills
  - Safety
notes:
  - label: MRA Backcountry Safety Guide
    url: https://mra.org/wp-content/uploads/2016/05/backcountrysafety.pdf
---

![Trail Etiquette and Backcountry Preparedness](../../assets/images/1664054130.jpeg)
_Trail Etiquette and Backcountry Preparedness._

Welcome to the **Trail Etiquette & Backcountry Skills** guide. Whether you are a novice hiker or an experienced backcountry explorer, carrying knowledge, proper etiquette, and sound judgment into the mountains is essential for your safety and the preservation of public lands.

!!! quote "Knowledge Priority"

    "As you read this section, please understand that it is designed to inform you. But more importantly, all these topics are things you should do your own research on to further your knowledge. The most important thing you can take with you on your outing is... knowledge."
    — **Chic Burge**

---

## Guide Modules

Explore each dedicated skill module below for in-depth protocols and field advice:

| Module | Core Topics & Focus Areas | Guide Link |
| :--- | :--- | :--- |
| **Route Finding & Navigation** | Maps (USGS & USFS), Compass, Google Earth 3D relief, Surveyor's tape, PLBs | [Route Finding Guide](route-finding.md) |
| **Wildlife & Trail Hazards** | Poison Ivy, Bear Safety (US & Canada), Tick removal & prevention, Rattlesnakes | [Wildlife Hazards Guide](wildlife-hazards.md) |
| **Trail Etiquette & Leave No Trace** | Right-of-way rules, LNT principles, Campfires, Trail maintenance, Dog etiquette | [Trail Etiquette Guide](trail-etiquette.md) |
| **Camp Etiquette & Logistics** | Noise control, Backcountry sanitation, $3 spare key solution, SAR notifications | [Camp & Logistics Guide](camp-etiquette-and-logistics.md) |
| **Hiking Techniques & Hydration** | Pressure breathing, Steep downhill knee-saving techniques, Phone navigation | [Hiking Techniques Guide](hiking-techniques.md) |

---

## The 14 Essentials Checklist

Every outdoor participant must carry their own individual 14 Essentials kit. If group members become separated, each hiker must have the gear needed to survive independently.

1. **Navigation:** USGS Topo map, USFS Forest map, and a reliable magnetic compass.
2. **Illumination:** Headlamp or flashlight (with extra batteries; red light mode for camp).
3. **Sun Protection:** SPF 30+ sunscreen, UV sunglasses, and a brimmed hat.
4. **First Aid:** Complete first aid kit, blister treatment, antiseptic wipes, and medications.
5. **Knife & Repair Kit:** Multi-tool or pocket knife, duct tape, and cordage.
6. **Fire Starter:** Waterproof matches, lighter, and tinder (such as beard lichen or cotton dryer lint).
7. **Emergency Shelter:** Lightweight space blanket, bivouac sack, or small tarp.
8. **Nutrition:** Extra day's supply of high-calorie, non-perishable food.
9. **Hydration:** Minimum 2 liters of water plus a lightweight water filter (Sawyer Mini).
10. **Extra Clothing:** Insulation layer, rain jacket, gloves, and warm hat.
11. **Signaling:** High-decibel emergency whistle and signal mirror.
12. **Personal Locator Beacon (PLB):** GPS satellite communicator or emergency PLB.
13. **Notebook & Pen:** Pocket notebook for logging accident vitals, times, and SAR notes.
14. **Surveyor's Tape:** Bright 15" tape strips for marking escape routes in an emergency *(always retrieve when done)*.
"""

with open("docs/resources/trail-etiquette-and-skills/index.md", "w", encoding="utf-8") as f:
    f.write(index_content)


# 2. route-finding.md
route_content = """---
title: Route Finding & Navigation Skills
tags:
  - Resources
  - Route Finding
  - Navigation
  - Compass
  - Maps
notes:
  - label: USGS Topographical Maps
    url: https://www.usgs.gov/core-science-systems/ngp/topographic-maps
  - label: USFS Forest Maps
    url: https://www.fs.usda.gov
---

Developing strong navigation and route-finding skills takes years of practice. Relying solely on electronic devices or following others blindly can leave you vulnerable in the backcountry.

!!! tip "Navigation Philosophy"

    Route finding is an acquired skill. As you hike with experienced trip leaders, observe their route choices, ask questions, and speak up if you ever feel uncomfortable with a route choice or terrain risk.

---

## Essential Navigation Tools

### Magnetic Compass

A traditional magnetic compass is the single most reliable navigation tool you can carry. It never runs out of battery power and functions in freezing temperatures.

- **Classroom & Field Practice:** Take a map and compass orientation class, then practice triangulation in the field.
- **Waterproof Instructions:** Keep a ziplock bag with quick-reference compass and gear instructions in your pack. When cold, tired, or disoriented, simple written instructions prevent costly navigation errors.

### USGS Topographical & USFS Forest Maps

- **USGS Topo Maps:** Provide fine-scale contour lines, elevation profiles, and detailed terrain features. Use your compass and topo map to plot precise bearings and track off-trail progress.
- **USFS Forest Maps:** Provide broad regional coverage showing forest service roads, trailheads, and major mountain ranges. Ideal for landmark triangulation across large areas.

### Google Earth 3D Relief Previews

Before leaving home, study your intended route using Google Earth:

1. Capture vertical (overhead) and horizontal relief screenshots of your route.
2. In Google Earth, use two fingers to tilt the perspective to eye level, revealing ridge contours, avalanche chutes, and cliff bands.
3. Save these images on your phone for offline reference during the hike.

---

## Personal Locator Beacons (PLBs) & GPS Units

- **Subscription Communicators (Garmin inReach, ZOLEO):** Allow two-way satellite texting, tracking, and SOS signaling.
- **Standard PLBs (ACR ResQLink):** Broadcast an emergency 406 MHz signal directly to Search & Rescue authorities without monthly subscription fees.
- **Responsible Use Warning:** Activating an SOS for non-life-threatening inconveniences (such as tiredness or minor rain) can result in massive search charges and potential criminal penalties.

---

## Field Marking with Surveyor's Tape

When marking an uncertain trail or off-trail route:

1. **Fold-Loop Tying Method:** Fold a 15" strip of surveyor's tape in half, loop it over a tree branch, and pass the loose ends back through the loop. This secures the tape tightly against wind without damaging bark.
2. **Mandatory Retrieval Rule:** **Always retrieve your tape on the return hike.** Leaving surveyor's tape behind litters the wilderness and misleads future hikers.

---

## Off-Trail & Mountain Route Strategy

!!! warning "Backtracking & Group Safety"

    If an off-trail route becomes excessively steep, impassable, or dangerous, **stop immediately**. Backtrack to your last known secure location and discuss safer alternative routes with your hiking partners.

- **Junction Photo Logs:** Take photos of key trail junctions, rock cairns, or stream crossings from the perspective of your return hike.
- **Communication:** Discuss route decisions openly with all group members. Never force anyone to continue if they feel unsafe or ill-equipped for the terrain.
- **Benjamin Franklin Maxim:** *"If you fail to plan, you are planning to fail."*
"""

with open("docs/resources/trail-etiquette-and-skills/route-finding.md", "w", encoding="utf-8") as f:
    f.write(route_content)


# 3. wildlife-hazards.md
wildlife_content = """---
title: Wildlife & Trail Hazards
tags:
  - Resources
  - Wildlife Hazards
  - Poison Ivy
  - Bears
  - Ticks
  - Rattlesnakes
notes:
  - label: Offtrack Travel Bear Safety Guide
    url: https://offtracktravel.ca/bear-safety-canada/
  - label: BearSmart Species Quiz
    url: http://www.bearsmart.com/about-bears/know-the-difference/test-your-bear-smarts/
  - label: Mayo Clinic Poison Ivy Information
    url: https://www.mayoclinic.org
  - label: Tick Images & Identification
    url: https://identify.us.com/idmybug/ticks/tick-images/index.html
---

Exploring the backcountry requires respect for native wildlife and plant hazards. Understanding animal behavior and plant identification ensures safe, positive encounters.

---

## Poison Ivy Identification & First Aid

![Poison Ivy Drooping Three-Leaf Cluster](../../assets/images/12272021744p.png)
_Poison Ivy Drooping Three-Leaf Cluster._

Poison ivy grows frequently along the base of cliffs, rocky slopes, and shaded trail margins across the Inland Northwest.

### Identification & Urushiol Exposure

- **Leaf Structure:** Stems grow 12–16 inches tall with **three distinct drooping leaves**.
- **Oil Transfer (Urushiol):** The plant's potent oil sticks to skin, clothing, boots, and pet fur.
- **Symptoms:** Redness, intense itching, swelling, and blisters develop 12 to 48 hours after exposure and last 2 to 3 weeks.
- **Critical Rule:** If you suspect contact with poison ivy, **do not touch your face or body**. Wash thoroughly with Technu or soap and cool water.
- **Emergency Medical Warning:** If you inhale smoke from burning poison ivy and experience breathing difficulty, seek emergency medical care immediately.

---

## Bear Safety in the Inland Northwest & Canada

Both Black Bears (*Ursus americanus*) and Grizzly Bears (*Ursus arctos*) inhabit forests across Idaho, Washington, Montana, and Western Canada.

### Black Bear vs. Grizzly Bear Identification

| Feature | Black Bear | Grizzly Bear |
| :--- | :--- | :--- |
| **Preferred Habitat** | Dense forests, coastal woods, brush | Open alpine meadows, mountain slopes, river valleys |
| **Facial Profile** | Straight, flat profile; prominent ears | Dish-shaped concave snout; short rounded ears |
| **Shoulder Hump** | No distinct shoulder hump | Prominent muscular shoulder hump |
| **Claws** | Short (1–2"), dark, curved for climbing | Long (2–4"), light-colored, straight for digging |
| **Defensive Style** | Usually retreats or climbs trees | More likely to stand ground and defend space/cubs |

### Proactive Avoidance & Trail Noise

Bears prefer to avoid human contact. Preventing surprise encounters is your best defense:

- **Make Noise:** Call out, sing, or talk loudly—especially near rushing streams, windy ridges, or dense brush.
- **Leash Pets:** Loose dogs frequently provoke defensive attacks by chasing bears and running back to their owners.
- **Travel in Groups:** Larger hiking groups (3+ people) drastically reduce bear attack risks.
- **Chic's "OIYA OSO" Noise Call:** Chic calls out *"HEY BEAR"* or *"OIYA OSO"* (Spanish for "hey bear") and clacks hiking poles together.
- **Chic's Custom Wood Noise Instrument:** Carve a 12–15" split wood blade (2" wide, ¼" thick), drill a hole in the handle, lace with an 8-foot cord, and twist. Swinging it overhead creates a loud whirring sound audible to bears miles away.

### Bear Spray Guidelines

!!! tip "Bear Spray Deployment"

    Bear spray is a high-volume chili pepper aerosol designed for close-range defense (under 30 feet / 10 meters). A standard 225g canister discharges in 7 to 9 seconds.

- **Accessibility:** Wear bear spray in a hip or chest holster—never pack it inside your backpack.
- **Expiration:** Check expiration dates (typically 2 to 2.5 years from manufacture).

### Responding to Bear Encounters

- **Defensive Reactions (Surprised Bear, Cubs, Food Source):**
  - *Signs:* Swatting ground, snorting, blowing, jaw popping.
  - *Action:* Speak in a calm, low voice. Back away slowly. Do NOT run or drop your pack.
  - *If Attacked:* Drop face down, interlock fingers behind your neck, and play dead. Keep your pack on to protect your back.
- **Non-Defensive / Curious Reactions:**
  - *Signs:* Standing on hind legs (sniffing/looking), persistent approach, head up.
  - *Action:* Shout firmly, make yourself look large, stamp feet, prepare bear spray, and fight back aggressively if approached.

### Camping & Food Storage Rules

- **Frontcountry ("Bare" Campsite):** Keep sites empty when away. Store food, coolers, trash, and toiletries inside hard-sided vehicles.
- **Backcountry Camping:** Cook and eat at least 100 meters downwind of your tent. Hang food 12+ feet high and 4+ feet out on a bear branch (using 50 ft of nylon cord and a carabiner), or use an Ursack or bear canister.

---

## Ticks & Tick-Borne Disease Prevention

![Wood Tick Anatomy and Movement Pattern](../../assets/images/12272021724p.png)
_Wood Tick Anatomy and Movement Pattern._

![Proper Tick Extraction Technique with Tweezers](../../assets/images/332025817p.png)
_Proper Tick Extraction Technique with Tweezers._

![Tick Size Comparison and Microbe Risks](../../assets/images/332025843p.jpg)
_Tick Size Comparison and Microbe Risks._

![Target-Shaped Rash Sign of Infection](../../assets/images/12272021722p.jpg)
_Target-Shaped Rash Sign of Infection._

Ticks are slow-moving 8-legged arachnids that crawl up low vegetation waiting to cling to passing animals or clothing.

### Tick Prevention & Clothing

- Wear light-colored long pants tucked into your socks so ticks are easily spotted.
- Apply Permethrin spray to hiking boots and pants.
- Perform routine tick checks throughout the day.
- Post-hike: Change clothes at the vehicle, shower promptly, and submerge hiking clothes in a tub or basin (ticks float to the surface).

### 5-Step Tick Removal Protocol

1. Clean the skin around the tick with an alcohol wipe.
2. Grasp the tick with fine-tipped tweezers as close to the skin surface as possible.
3. Pull straight upward with steady, even pressure. **Do not twist or jerk.**
4. If mouthparts remain under the skin, scrape gently with a sterile needle to remove.
5. Disinfect the bite site and save the tick in a ziplock bag in your freezer. If a target-shaped bullseye rash or fever develops over the next 3 weeks, bring the tick to your doctor for analysis.

---

## Rattlesnakes in the Washington Scablands

Western Rattlesnakes (*Crotalus oreganus*) inhabit rocky canyons and basalt scablands across Eastern Washington and Idaho.

- **Behavior:** Non-aggressive unless provoked or stepped on. They rattle their tails as a clear warning to back away.
- **Sun-Warming Locations:** Cold-blooded snakes warm themselves on south-facing rocks, logs, and sunny trail edges. Look before stepping over obstacles.
- **Snake Gaiters:** If hiking off-trail in high-density scabland terrain, wear protective plastic snake gaiters below the knee.
"""

with open("docs/resources/trail-etiquette-and-skills/wildlife-hazards.md", "w", encoding="utf-8") as f:
    f.write(wildlife_content)


# 4. trail-etiquette.md
etiquette_content = """---
title: Trail Etiquette & Leave No Trace
tags:
  - Resources
  - Trail Etiquette
  - Leave No Trace
  - Campfires
  - Trail Maintenance
notes:
  - label: Washington Trails Association
    url: https://www.wta.org
  - label: Idaho Trails Association
    url: https://www.idahotrailsassociation.org
  - label: Spokane Mountaineers
    url: https://www.spokanemountaineers.org
---

Practicing good trail etiquette ensures that public trails remain clean, safe, and enjoyable for all outdoor enthusiasts.

---

## Leave No Trace & Pack It In, Pack It Out

The Leave No Trace (LNT) philosophy ensures wilderness areas remain pristine for future generations.

!!! info "Golden LNT Adage"

    *"If you can carry it in full, you can carry it out empty."*

- **Non-Burnables:** Tin cans, aluminum foil, glass, and plastic **do not burn** in campfires. Always pack out all food wrappers, foil, and trash.
- **Clean Up After Others:** Carrying out discarded trash left by less courteous visitors leaves the trail better than you found it.

---

## Trail Right-of-Way Rules

Understanding who yields on the trail prevents confusion and trail erosion:

| User Encounter | Right-of-Way Protocol |
| :--- | :--- |
| **Uphill Hikers vs. Downhill Hikers** | **Uphill hikers have the right-of-way.** Downhill hikers should step aside to preserve the uphill momentum. |
| **Hikers vs. Mountain Bikers** | Bikers should yield to hikers, but because bikes move fast, hikers should step off the trail safely when a biker approaches. |
| **Hikers vs. Equestrians (Horses)** | **Hikers must always yield to pack stock and horses.** Step off the trail on the downhill side, stand quietly, and speak softly to the rider so horses recognize you as human. |
| **Hikers vs. Trail Runners** | Hikers should step aside to allow trail runners to pass safely. |

---

## Trail Courtesy & Stewardship

- **Clear Trail Hazards:** Use your boot to flick loose sticks, pinecones, and rolling rocks off the trail to prevent ankle sprains for hikers behind you.
- **Aid Injured Hikers:** Coming to the aid of injured trail users takes precedence over reaching a summit or destination.
- **Noise Control:** Keep voices low. Never use external speakers to play music on the trail.
- **Trail Breaks:** Step completely off the treadway when stopping to rest or check maps so you do not block the path.
- **Protect Cairns:** Official rock cairns are built by land managers to mark obscure routes. **Do not build unauthorized cairns**, as custom rock piles confuse hikers and cause trail braiding.
- **Leash Dogs:** Keep dogs leashed at all times to prevent wildlife harassment and avoid startling fellow hikers. Pack out dog waste in sealed bags.

---

## Campfire Safety & Fire Conservation

!!! warning "Campfire Safety"

    Never leave a campfire unattended. Ensure campfires are 100% cold to the touch before leaving camp.

- **Down Wood Only:** Never chop down live trees or break standing dead branches. Scavenge only small downed wood.
- **Dousing Campfires:** Transport gallons of water to the fire ring (grocery plastic bags work in a pinch) and douse coals while stirring with a stick until cool.
- **Saving a Fire Overnight:** To keep embers alive overnight safely, place a 1-foot strip of cotton fabric into coals until charred, then cover completely with dirt. The charred cotton smolders safely. In the morning, uncover and use the charred cotton with dry beard lichen tinder to restart your fire.

---

## Volunteer Trail Maintenance

Maintain our public trails by joining local non-profit trail organizations:

- **[Spokane Mountaineers](https://www.spokanemountaineers.org):** Trail work parties, climbing schools, and conservation trips.
- **[Washington Trails Association (WTA)](https://www.wta.org):** Volunteer trail maintenance work parties across Washington state.
- **[Idaho Trails Association (ITA)](https://www.idahotrailsassociation.org):** Wilderness trail clearing and maintenance across Idaho.
"""

with open("docs/resources/trail-etiquette-and-skills/trail-etiquette.md", "w", encoding="utf-8") as f:
    f.write(etiquette_content)


# 5. camp-etiquette-and-logistics.md
camp_content = """---
title: Camp Etiquette, Group Logistics & Car Safety
tags:
  - Resources
  - Camp Etiquette
  - Logistics
  - Carpool
  - Emergency Preparedness
notes:
  - label: Spokane Regional Health District
    url: https://srhd.org
---

Proper camp management, sanitation, carpool logistics, and emergency contacts prevent backcountry issues and ensure smooth group outings.

---

## Camp Etiquette & Noise Control

- **Quiet Hours:** Keep camp noise to a low whisper during evening and early morning hours. Never play loud music or host loud gatherings in backcountry campsites.
- **Managing Snorers:** If you snore, pitch your tent well away from main group camp areas to avoid disturbing fellow campers.
- **Headlight Etiquette:** Use red light mode on headlamps around camp. Never shine white light directly into the eyes of fellow campers, as white light destroys night vision.

---

## Backcountry Sanitation & Hygiene

- **Human Waste Disposal:** Relieve yourself at least **200 feet** (70 adult paces) away from all trails, campsites, lakes, and streams. Dig a cat-hole **6 to 8 inches deep**, cover with soil, and place a large rock on top.
- **Blue Bags:** In designated high-alpine or national park areas, pack out all human waste using blue bags.
- **Dishwashing:** Never wash dishes directly in lakes or streams. Boil water, clean cookware at camp, and strain wastewater into a cat-hole 200 feet from water sources.

---

## Chic's Hardware Store Spare Door Key Solution

!!! tip "The $3 Door-Only Key Solution"

    Modern electronic chip keys are expensive to replace and risky to lose on the trail. Chic recommends having a **non-chip, mechanical door key** made at a local hardware store (around $3).

- **Carpool Convenience:** Provide a mechanical door key to carpool partners. If faster hikers reach the vehicle ahead of the driver, they can unlock the doors to dump heavy gear, change into dry clothes, or shelter from rain without risk of starting or stealing the vehicle.
- **Selkirks Case Study:** After spending 6 hours searching for lost van keys under the North Twin in the Selkirks, Chic keeps spare mechanical door keys in his wallet and vehicle for peace of mind.

---

## Emergency Responsible Person Notification

Always leave a detailed trip plan with a trusted contact before entering the backcountry:

1. **Trip Itinerary:** Specific trailhead name, planned route, vehicle description, license plate, and expected return time.
2. **Emergency Contacts:** Include the local County Sheriff's office phone number for the specific hike area.
3. **Overdue Protocol:** Instruct your contact on the exact time to call the Sheriff if you are overdue.
4. **Immediate Check-in:** Call or text your responsible contact immediately upon returning to cell service to cancel any pending SAR response.
5. **Trailhead Notes:** If you change your hiking route out of cell range, leave a clear note on your vehicle dashboard detailing your revised path.
"""

with open("docs/resources/trail-etiquette-and-skills/camp-etiquette-and-logistics.md", "w", encoding="utf-8") as f:
    f.write(camp_content)


# 6. hiking-techniques.md
tech_content = """---
title: Hiking Techniques, Hydration & Phone Navigation
tags:
  - Resources
  - Hiking Techniques
  - Pressure Breathing
  - Downhill Hiking
  - Hydration
notes:
  - label: NOAA National Weather Service
    url: https://www.weather.gov
---

![NOAA Hourly Weather Forecast Graph Sample](../../assets/images/plotter-php.png)
_NOAA Hourly Weather Forecast Graph Sample._

Optimizing your breathing rhythm, downhill biomechanics, and hydration habits maximizes endurance and protects your joints on demanding mountain routes.

---

## Uphill Pressure Breathing Technique

When ascending steep mountain trails or snow slopes, adopt the **Pressure Breathing** technique used by high-altitude mountaineers and cross-country skiers:

1. **Deep Inhalation:** Inhale deeply through your nose, filling your lungs completely from the diaphragm up.
2. **Pursed-Lip Exhalation:** Exhale forcefully through pursed lips (like blowing out a birthday candle).
3. **Physiological Benefit:** Pursed-lip exhalation increases back-pressure in the lungs, forcing more oxygen across pulmonary capillaries into your bloodstream.
4. **Result:** Noticeably reduces leg fatigue and increases core warmth within 5 to 10 minutes of steep climbing.

---

## Steep Downhill Knee-Saving Technique

Downhill hiking exerts immense impact force on knee joints. Spokane Mountaineer Miles Breneman advocates this proven biomechanical approach:

- **Posture:** Stand upright before initiating downhill steps.
- **Flexed Knees:** Unlock your knees and maintain a **slight flex** on every step.
- **Full Boot Sole Placement:** Avoid striking heel-first. Place your full boot sole flat on the ground so maximum lug surface area grips the trail, absorbing impact through muscles rather than knee joint bones.

---

## Continuous Hydration Management

- **Prevent Thirst:** Drink small sips of water continuously. Feeling thirsty indicates that systemic dehydration has already set in.
- **Accessible Water Holders:** Store water bottles in shoulder-strap holsters rather than buried inside your pack, encouraging frequent hydration throughout the day.

---

## Phone Navigation & Visual Photo Logging

1. **Junction Photo Proof:** Take photos of obscure trail Y-junctions, cairns, and landmarks on your way in from the reverse angle. Reviewing these photos on your return leg prevents wrong turns.
2. **Scabland Mesa Tracking:** In feature-repetitive scabland canyons, photograph high mesas, rock columns, and creek bends to verify your position on the return route.
3. **Pre-Hike Weather Verification:** Study NOAA's **Hourly Weather Forecast** graph prior to departure to anticipate hourly wind, temperature, and precipitation trends.
"""

with open("docs/resources/trail-etiquette-and-skills/hiking-techniques.md", "w", encoding="utf-8") as f:
    f.write(tech_content)


# 7. Remove old monolith file if it exists
old_file = "docs/resources/trail-etiquette-and-skills.md"
if os.path.exists(old_file):
    os.remove(old_file)
    print(f"Removed legacy monolith file: {old_file}")

print("Created 6 breakout markdown documents under docs/resources/trail-etiquette-and-skills/")
