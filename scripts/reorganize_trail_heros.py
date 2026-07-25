import os

md_content = """---
tags:
  - Trail Heroes
  - Stewardship & Conservation
  - Photo Gallery
---

# Trail Heroes

The images below showcase a few of the dedicated trail heroes working in and around Spokane and Coeur d'Alene. The next time you encounter these trail stewards on the route, offer them a warm thanks or a high five—most are active volunteers with the **Spokane Mountaineers** and the **Washington Trails Association (WTA)**.

!!! tip "Trail Stewardship & LNT Practices"

    As trail workers and volunteers, we ask for your help in keeping our regional trails clean and accessible:

    - **Litter Prevention:** Carry lightweight plastic grocery bags in your daypack to collect and pack out trail litter without directly touching debris.
    - **Campfire Safety:** Grocery bags weigh only 6 grams each and can double as water buckets to thoroughly extinguish campfires.

Click any image to enlarge and view high-resolution photo and caption.

## Photo Gallery

- ![Spokane Mountaineers After Building a New Trail at Newman Lake Conservation Futures Property](../../assets/images/12222021415p.jpg)
- ![Trail Champion Michael Pitner and a Regional Trail Angel](../../assets/images/12222021418p.jpg)
- ![Trail Hero Clearing Brush Away from the Work Route](../../assets/images/12222021419p.jpg)
- ![Volunteer Digging Trail Tread in the Dirt at Newman Lake](../../assets/images/12222021420p.jpg)
- ![Trail Heroes Posing with Pulaskis and Shovels at Newman Lake](../../assets/images/12222021421p.jpg)
- ![Trail Hero Taking a Well-Earned Break After Building Newman Lake Trail](../../assets/images/12222021422p.jpg)
- ![Volunteers Resting Mid-Day Along the Work Route](../../assets/images/12222021423p.jpg)
- ![Volunteer Inspecting Completed Trail Tread at Newman Lake](../../assets/images/12222021424p.jpg)
- ![Rich Landers — Regional Outdoor Advocate and Legendary Trail Hero](../../assets/images/12222021425p.jpg)
- ![Trail Super Hero Denise Preparing Trail Work Equipment](../../assets/images/122222021426p.jpg)
- ![Trail Heroes Posing at Lone Lake in the Stevens Peak Area](../../assets/images/12222202142_orig.jpeg)
- ![Volunteers Heading Back to Newman Lake Trailhead After a Day with Pulaskis](../../assets/images/122222021428p.jpg)
- ![Trail Maintenance Crew at Work in the Inland Northwest](../../assets/images/12222021429p.jpg)
- ![Denise Taking a Lunch Break During Trail Work](../../assets/images/12222021430p.jpg)
- ![Trail Heroes Digging Tread Between Red Route Flags at Newman Lake](../../assets/images/12222021432p.jpg)
- ![Volunteers Hopscotching Sections Every 30 Feet Along the New Trail](../../assets/images/12222021438p.jpg)
- ![Teamwork and Tool Safety During Trail Construction](../../assets/images/122222021438p.jpg)
- ![Lynn Smith — Spokane Mountaineers Trail Boss and North Idaho Super Hero](../../assets/images/12222021654p.jpg)
- ![Chic Burge Using Tree Rootballs to Fill in Trail Holes](../../assets/images/img-8882.jpg)
- ![Trail Crew Filling in Trail Tread After a Toppled Tree Event](../../assets/images/122220214337p.jpg)
- ![Trail Crew Enjoying a Lighthearted Moment on the Job](../../assets/images/12222021439p.jpg)
- ![Lone Lake Trail Crew Posing After a Successful Work Day](../../assets/images/12222021655p.jpg)
- ![Volunteers Clipping Back Overgrown Brush Along the Lone Lake Trail](../../assets/images/122220216561p.jpg)
- ![Volunteer Trail Crew Posing Along the Mountain Route](../../assets/images/12222021657p.jpg)
- ![On-the-Job Crosscut Saw Safety and Operation Training](../../assets/images/12222021658p.jpg)
- ![Volunteers Enjoying Trailhead Snacks After a Work Day in the Mountains](../../assets/images/122220216591p.jpg)
- ![Trail Crew Smiles Even During Inclement Weather](../../assets/images/12222021700p.jpg)
- ![Trail Angel Learning Crosscut Sawing Techniques](../../assets/images/20210619-114508.jpg)
- ![Resting at Stevens Lake After a Sawing Session](../../assets/images/20210619-141747.jpg)
- ![Trail Heroes Posing Above Crystal Lake on Rochat Divide](../../assets/images/11182021438p.jpg)
- ![Holly Weiler and Massive WTA Work Party at Fishtrap Lake](../../assets/images/123020211105a.jpg)
- ![Holly Weiler Checking Progress and Laying Out Fishtrap Lake Trail Route](../../assets/images/123020211106a.jpg)
- ![Trail Work Along the Shore of Fish Lake](../../assets/images/123020211107a.jpg)
- ![Volunteers Line Up at Fishtrap Lake Work Party](../../assets/images/123020211108a.jpg)
- ![Trail Building Hand Tools Lineup for Fishtrap Lake Project](../../assets/images/dsc-0162-copy.jpg)

---

## Regional Trail Super Heroes

Below are three key stewards whose decades of dedication have built, restored, and preserved the regional trail network across Eastern Washington and North Idaho:

### Rich Landers

![Rich Landers — Outdoor Editor Extraordinaire](../../assets/images/232022905p.jpg)
_Rich Landers — Outdoor Editor Extraordinaire._

Rich Landers is a regional trail hero extraordinaire. For decades as Outdoor Editor for the *Spokesman-Review*, Rich enriched the lives of outdoor enthusiasts across the Inland Northwest by showcasing mountain trails, advocating for public land conservation, and guiding readers to outdoor adventures.

### Holly Weiler

![Holly Weiler — Washington Trails Association & Spokane Mountaineers Lead](../../assets/images/122222021431p.jpg)
_Holly Weiler — Washington Trails Association & Spokane Mountaineers Lead._

Few individuals have contributed more to trail construction, maintenance, and advocacy in our region than Holly Weiler. Serving as Eastern Washington Regional Coordinator for the Washington Trails Association (WTA) and as a leader in the Spokane Mountaineers, Holly organizes dozens of volunteer work parties every season.

### Lynn Smith

![Lynn Smith — Lone Lake & Regional Trail Steward](../../assets/images/2320221000p.jpg)
_Lynn Smith — Lone Lake & Regional Trail Steward._

Super trail hero Lynn Smith, pictured at Lone Lake following a trail maintenance work day. Lynn's tireless work clearing blowdowns, rebuilding tread, and maintaining remote backcountry routes across North Idaho and Eastern Washington has earned him icon status among the Spokane Mountaineers, WTA, and all who hike regional trails.
"""

target_path = "docs/gallery/categories/trail-heros.md"
with open(target_path, "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Reorganized trail-heros.md successfully")
