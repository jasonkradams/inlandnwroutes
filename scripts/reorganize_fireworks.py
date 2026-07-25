import os

md_content = """---
tags:
  - Photography
  - Coeur d'Alene
  - Photo Gallery
---

# Fireworks Photography

Capturing fireworks displays over Lake Coeur d'Alene and the surrounding Inland Northwest requires long-exposure techniques, careful planning, and a sturdy tripod.

!!! warning "Photography Purpose & Public Land Regulations"

    - **Photography Only:** These locations are recommended strictly for photography and viewing. Do **NOT** set off personal fireworks at any of these sites—personal fireworks are strictly illegal on public lands, state parks, and city properties in Coeur d'Alene and Kootenai County.
    - **No Trespassing:** Respect private property lines and stay on designated public roads and trails.
    - **Fire Prevention:** Areas like Tubbs Hill and Canfield Butte are extremely dry during summer. Fire danger is high.

---

## Long Exposure Camera Guide

To capture sharp fireworks trails against a dark sky, follow these essential camera settings:

- **Tripod & Remote Shutter:** Mount your camera on a sturdy tripod and use a cable release, Bluetooth trigger, or remote shutter to eliminate camera shake during multi-second exposures.
- **Manual Focus:** Turn off autofocus. Manually focus your lens on a distant light source before the show starts. Use live-view magnification to verify focus.
- **Low ISO (100 or lower):** Keep ISO at 100 or lower. Fireworks emit bright bursts of light; higher ISO settings create overexposed highlights and digital noise.
- **Turn Off Flash:** Disable built-in or pop-up flashes, which are ineffective beyond 20 feet and ruin exposure calculations.
- **Manual Exposure & Bulb Mode:** Set your mode dial to **Manual (M)** and shutter speed to **Bulb**. Set your aperture to **f/8 – f/11** for standard bursts, and tighten to **f/11 – f/16** during the intense Grand Finale.
- **Timing the Exposure:** Watch for the ascent trail of a rocket. Open the shutter as the shell rises (5 to 10 seconds total) and close the shutter just as the burst begins to dissipate.
- **White Balance:** Experiment with Daylight, Tungsten, or Kelvin white balance settings to achieve vivid color saturation.

---

## Recommended Vantage Points

| Vantage Point | Location & Access Details | Viewing Notes |
| :--- | :--- | :--- |
| **Highway 97** | 0.2 miles south of Arrow Point Resort | Pull-offs available along Hwy 97 shoulder. |
| **Highway 95 / Cougar Bay** | 1.6 miles south of Spokane River bridge | Parking on Hwy 95 is illegal; park safely NW and walk to water's edge. |
| **Cougar Bay Nature Reserve** | Trail access to vantage point or paddle approach | Best viewed by paddling to the beach near pilings; stay off private land. |
| **Canfield Butte** | Hike to West Summit | Requires a steep night hike; bring extra headlamp batteries. |
| **East Lake Coeur d'Alene Drive** | 1.2 miles SE of Silver Beach Marina | Pull off into designated parking near Lake Steamer Marker; displays visible above ridge. |
| **Signal Point** | Signal Point Road | Walk 1.5 miles past gate to viewpoint; stay strictly on public road. |
| **Mica Peak (WA)** | Via Belmont Road (9–10 mi RT, 2,500' gain) | High elevation view; stay clear of FAA radar dome property. |
| **Mineral Ridge (Silver Tip Overlook)** | 3.3-mile loop trail | Launch site obscured, but sky bursts remain fully visible across Wolf Lodge Bay. |
| **NIC Parkway (Dyke Road)** | North Idaho College waterfront | Popular viewing area; park only in designated spaces. |
| **Coeur d'Alene City Beach** | Downtown Coeur d'Alene waterfront | High-density crowd viewing directly across from resort launch barges. |
| **Tubbs Hill** | 0.2 to 1.1 miles along main loop trail | Great vantage points; extreme fire hazard—fireworks strictly prohibited. |

---

Click any image to enlarge and view high-resolution photo and caption.

## Photo Gallery

- ![Coeur d'Alene 4th of July Fireworks Display Over Lake CDA](../../assets/images/11242022341p.jpg)
- ![Coeur d'Alene 4th of July Fireworks Bursts](../../assets/images/11242022343p.jpg)
- ![Independence Day Fireworks Reflection Over Lake Coeur d'Alene](../../assets/images/11242022345p.jpg)
- ![Coeur d'Alene Resort Fireworks Over the Boardwalk](../../assets/images/11242022352p.jpg)
- ![Coeur d'Alene Resort Fireworks Bursting Over Water](../../assets/images/11242022353p.jpg)
- ![Multi-Color Fireworks Display at Coeur d'Alene Resort](../../assets/images/11242022355p.jpg)
- ![Long Exposure Fireworks Trails Above Lake Coeur d'Alene](../../assets/images/11242022356p.jpg)
- ![Golden Palm Fireworks Bursts Over Coeur d'Alene Resort](../../assets/images/11242022357p.jpg)
- ![Red and Blue Fireworks Explosions Over Coeur d'Alene Bay](../../assets/images/11242022359p.jpg)
- ![Coeur d'Alene Resort Fireworks Reflections](../../assets/images/11242022400p.jpg)
- ![Chrysanthemum Fireworks Bursts Above Coeur d'Alene Resort](../../assets/images/11242022404p.jpg)
- ![Vivid Fireworks Finale Over Lake Coeur d'Alene](../../assets/images/11242022405p.jpg)
- ![Coeur d'Alene Resort Grand Finale Fireworks](../../assets/images/11242022406p.jpg)
- ![Long Exposure Aerial Shell Explosions Over Water](../../assets/images/11242022408p.jpg)
- ![Silver Willow Fireworks Display Over Coeur d'Alene Resort](../../assets/images/11242022409p.jpg)
- ![Sparkling Fireworks Over Coeur d'Alene Resort Waterfront](../../assets/images/11242022410p.jpg)
- ![Multi-Shell Fireworks Burst Over Coeur d'Alene Lake](../../assets/images/11242022412p.jpg)
- ![Coeur d'Alene 4th of July Fireworks Celebration](../../assets/images/11212021106a.jpg)
- ![Grand Finale Fireworks Sky Bursts Over Coeur d'Alene Resort](../../assets/images/11242022416p.jpg)
"""

target_path = "docs/gallery/categories/fireworks.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized fireworks.md successfully")
