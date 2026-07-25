#!/usr/bin/env python3
"""One-time migration: reorganize docs/ + mkdocs.yml nav to mirror the
Activity -> Region -> Sub-area -> Route structure of the old
inlandnwroutes.com (Weebly) site.

Not a recurring build-time generator (unlike scripts/generate_*_page.py) --
run by hand, once, per section:

    python scripts/migrate_to_activities_nav.py hike

Prints the new nav YAML block to stdout and performs the `git mv`s.
"""
import os
import re
import subprocess
import sys

DOCS = "docs"

# ---------------------------------------------------------------------------
# Old-site data: { region: { subregion_or_None: [(title, old_slug), ...] } }
# ---------------------------------------------------------------------------

HIKE = {
    "Canada": {None: [
        ("The Bugaboos", "the-bugaboos"), ("Fisher Peak", "fisher-peak"), ("Lake O'Hara", "lake-ohara"),
    ]},
    "Idaho": {
        "American Selkirks": [
            ("Bottleneck Lake & Peak", "bottleneck-lake--peak"), ("Beehive Lake 6457'", "beehive-lake-6457"),
            ("Burton Peak 6844' Trail #9", "burton-peak-6844-trail-9"),
            ("Cutoff Peak 6844' and Smith Peak's North Ridge", "cutoff-peak-6844-and-smith-peaks-north-ridge"),
            ("Fault Lake 5980' & Hunt Peak 7058' Trail #59", "fault-lake-5980--hunt-peak-7058-trail-59"),
            ("Fisher Peak Trail #27", "fisher-peak-trail-27"),
            ("Hunt Lake 5813' Gunsight Peak 7352'", "hunt-lake-5813-gunsight-peak-7352"),
            ("Harrison Lake & Peak 7292' Trail #217", "harrison-lake--peak-7292-trial--217"),
            ("Little Harrison Lake 6271' & Peak 7292'", "little-harrison-lake-6271--peak-7292"),
            ("Iron Mountain 6426' Trails #180 & 176", "iron-mountain-6426-trails-180--176"),
            ("Kootenai W.L.R.", "kootenai-wlr"), ("Long Canyon Trail #16", "long-canyon-trail-16"),
            ("Long Mountain 7265' and Lake", "long-mountain-7265-and-lake"),
            ("Lookout Lake & Mountain 7627'", "lookout-lake--mountain-7627"),
            ("Mollies & Phoebes Tip", "mollies--phoebes-tip"),
            ("Mount Roothaan 7326' and Chimney Rock 7124' Trail #256", "mount-roothaan-7326-and-chimney-rock-7124-trail-256"),
            ("Myrtle Lake 5950' & Myrtle Peak 7122' Trail #286", "myrtle-lake-5950--myrtle-peak-7122-trail-286"),
            ("Parker Peak 7670'", "parker-peak-7670"), ("Pyramid Peak 7355' Trail #13", "pyramid-peak-7355-trail-13"),
            ("Red Top Mountain 6266' Trail #102", "red-top-mountain-6266-trail-102"),
            ("Roman Nose Lakes & Peak, Idaho", "roman-nose-lakes--peak-idaho"),
            ("Russell Peak 6618' Trail #12 & Russell Ridge #92", "russell-peak-6618-trail-12--russell-ridge-92"),
            ("Pyramid and Ball Lakes Trail #43", "pyramid-and-ball-lakes-trail-43"),
            ("Selkirk Crest High Traverse", "selkirk-crest-high-traverse"),
            ("Shorty Peak Trail #95 6515' & Lone Tree Peak 6732'", "shorty-peak-trail-95-6515--lone-tree-peak-6732"),
            ("Snow Lake & Peak", "snow-l--p"),
            ("Trout 6352' & Big Fisher 6732' Lakes Trail #13 & 41", "trout-6352--big-fisher-6732-lakes-trail-13--41"),
            ("Two Mouth Lakes to the Wigwams High Traverse", "two-mouth-lakes-to-the-wigwams-high-traverse"),
            ("Two Mouth Lakes 5785'", "two-mouth-lakes-5785"), ("The Wigwams 7033'", "the-wigwams-7033"),
            ("West Fork Lake, Mountain 6416' & Lookout Tower Trail #347", "west-fork-lake-mountain-6416--lookout-tower-trail-347"),
        ],
        "North Idaho Hikes": [
            ("Lake Estelle", "lake-estelle"), ("Moose Mountain Loop Hike", "moose-mountain-loop-hike"),
            ("American Falls Trail #308", "american-falls-trail-308"), ("Bernard Peak Overlook", "bernard-peak-overlook"),
            ("Blacktail Mountain", "blacktail-mountain"), ("Blacktail Mountain Overlook", "blacktail-mountain-overlook"),
            ("Clifty Mountain to Katka Peak", "clifty-mountain-to-katka-peak"),
            ("North and South Chilco Peak", "north-and-south-chilco-peak"),
            ("Elk Creek Falls National Recreation Area", "elk-creek-falls-national-recreation-area"),
            ("Five Lakes Butte", "five-lakes-butte"), ("Giant Cedar Grove Trail", "giant-cedar-grove-trail"),
            ("Graham Mountain", "graham-mountain1"), ("The Green Monarchs", "the-green-monarchs"),
            ("Little Guard Peak & Lookout", "little-guard-peak--lookout"),
            ("Lunch Peak & Mount Pend Orielle", "lunch-peak--mount-pend-orielle"),
            ("Maiden Rock Trail", "maiden-rock-trail"), ("Marie Creek", "marie-creek"),
            ("Mickinnick Trail", "mickinnick-trail"), ("Mineral Ridge", "mineral-ridge"),
            ("Morris Creek Old Growth Cedar Grove", "morris-creek-old-growth-cedar-grove"),
            ("Mount CDA Trail #79 Caribou Ridge", "mount-cda-trail-79-caribou-ridge"),
            ("Mount CDA Trail #257", "mount-cda-trail-257"), ("Myrtle Peak Trail", "myrtle-peak-trail"),
            ("Navigation Trail #291", "navigation-trail-291"), ("Packsaddle Mountain", "packsaddle-mountain"),
            ("Shefoot Mountain", "shefoot-mountain1"),
            ("Short Peak 6515' and Lone Tree Peak 6732'", "short-peak-6515-and-lone-tree-peak-6732"),
            ("Snow Peak", "snow-peak"), ("Tubbs Hill", "tubbs-hill"), ("Q'emlin Park", "qemlin-park"),
        ],
        "Proposed Scotchman Peaks Wilderness": [
            ("Scotchman's Peak", "scotchmans-peak"), ("Star Peak", "star-peak"),
            ("Sawtooth Mountain", "sawtooth-mountain"), ("Ross Creek Cedars", "ross-creek-cedars"),
            ("Pillick Ridge 6167'", "pillick-ridge-6167"),
        ],
        "Silver Valley Area": [
            ("Bloom Peak", "bloom-peak"), ("CDA River Tr 20", "cda-river-tr-20"), ("Crystal Lake", "crystal-lake"),
            ("Elsie Lakes-Striped Peak-Trail 16", "elsie-lakes-striped-peak-trail-16"),
            ("Glidden Lakes Upper and Lower", "glidden-lakes-upper-and-lower"),
            ("Graham Mountain", "graham-mountain"), ("Trail 7 to Granite Peak", "trail-7-to-granite-peak"),
            ("Independence Creek", "independence-creek"), ("Latour-Frosty Peaks", "latour-frosty-peaks"),
            ("Little Guard Lookout", "little-guard-lookout"), ("Lone (& Long Lake) Lakes", "lone-long-lake-lakes"),
            ("Pulaski Tunnel Trail", "pulaski-tunnel-trail"), ("Revett Lake", "revett-lake1"),
            ("Settlers Grove of Ancient Cedars", "settlers-grove-of-ancient-cedars"),
            ("Shefoot Mountain", "shefoot-mountain"),
            ("Shoshone Medical Center Wellness Trail", "shoshone-medical-center-wellness-trail"),
            ("State Line Ridge Trail", "state-line-ridge-trail"),
            ("Upper and Lower Stevens Lake", "upper-and-lower-stevens-lake"),
            ("Stevens Peak via West Willow Ridge 6838'", "stevens-peak-via-west-willow-ridge-6838"),
            ("Stevens Peak SMI Mountain School", "stevens-peak-smi-mountain-school"),
            ("Upper & Lower St Regis Lakes", "upper--lower-st-regis-lakes"),
        ],
    },
    "Montana": {
        "Bitterroots": [
            ("Hub Lake", "hub-lake"), ("St Joe Lake 6472' Illinois Peak 7690'", "st-joe-lake-6472rsquo-illinois-peak-7690rsquo"),
            ("Ward Peak 7312' & Eagle Peak 7333' Trail #250", "ward-peak-7312--eagle-peak-7333-trail-250"),
            ("Cliff Lake & Eagle Cliff Peak", "cliff-lake--eagle-cliff-peak1"),
        ],
        "Proposed Scotchman Peaks Wilderness": [
            ("Scotchman's Peak", "scotchmans-peak"),
            ("Spar Peak, Little Spar Lake & Horseshoe Pond", "spar-peak-little-spar-lake--horseshoe-pond"),
            ("Star Peak", "star-peak1"), ("Sawtooth Mountain", "sawtooth-mountain1"),
            ("Ross Creek Cedars", "ross-creek-cedars1"), ("Pillick Ridge 6167'", "pillick-ridge-61671"),
        ],
        "Cabinet Mountains Wilderness": [
            ("A Peak 8,634'", "a-peak-8634"), ("Bear Lake", "bear-lake"), ("Baree Lake", "baree-lake"),
            ("Bramlet Lake", "bramlet-lake"), ("Cabinet Divide Trail #360", "cabinet-divide-trail-360"),
            ("Cedar Lake 5914'", "cedar-lake-5914"), ("Cliff/St P/Rock P", "cliffst-p-rock-p"),
            ("Chicago Peak", "chicago-peak"), ("Dome Mountain", "dome-mountain"),
            ("Engle Peak 7583' Trail #926", "engle-peak-7583-trail-926"), ("Geiger L/Lost Buck Pass", "geiger-llost-buck-pass"),
            ("Granite Lake 4629'", "granite-lake-4629"), ("Leigh Lake", "leigh-lake"),
            ("Little Ibex Lake", "little-ibex-lake"), ("Minor Lake", "minor-lake"), ("Rock Lake 4958'", "rock-lake-4958"),
            ("Scenery Mountain", "scenery-mountain"), ("Sky/Hanging Valley", "skyhanging-valley"),
            ("Snowshoe Peak 8738'", "snowshoe-peak-8738"), ("St Paul Lake", "st-paul-lake"),
            ("Taylor Peak", "taylor-peak"), ("William Grambauer", "william-grambauer"), ("Moran Basin", "moran-basin"),
            ("Parmenter Lake", "parmenter-lake"), ("Wanless Lake", "wanless-lake"),
            ("Wanless Lake via Trail #912", "wanless-lake-via-trail-912"),
            ("Wanless Lake via Trail #921", "wanless-lake-via-trail-921"),
            ("Wanless Lake via Trail's #656, #360, #912", "wanless-lake-via-trailrsquos-656-360-912"),
        ],
        "Lolo National Forest": [
            ("Blossom Lake", "blossom-lake"), ("Cliff Lake & Eagle Cliff Peak", "cliff-lake--eagle-cliff-peak"),
            ("Cube Iron Mt", "cube-iron-mt"), ("Heart Lake", "heart-lake"), ("Hub Lake & Dipper Falls", "hub-lake--dipper-falls"),
            ("Revett Lake", "revett-lake"), ("Siamese Lake Loop", "siamese-lake-loop"),
            ("St Regis Lakes Upper & Lower", "st-regis-lakes-upper--lower"), ("Terrace Lake", "terrace-lake"),
        ],
    },
    "Oregon": {None: [
        ("John Day Fossil Bed National Monument", "john-day-fossil-bed-national-monument"),
        ("Silver Falls S.P.", "silver-falls-sp"), ("Smith Rocks", "smith-rocks"),
        ("South Sister Mountain 10,358'", "south-sister-mountain-10358"),
    ]},
    "Washington": {
        "Colville National Forest": [("Hall Mountain 6233' Trail #588", "hall-mountain-6233-trail-588")],
        "Scablands": [
            ("Banks Lake North Trail", "banks-lake-north-trail"), ("Banks Lake", "banks-lake"),
            ("Breezy Hill, Ancient and Dusty Lakes", "breezy-hill-ancient-and-dusty-lakes"),
            ("Columbia National Wildlife Refuge", "columbia-national-wildlife-refuge"),
            ("Escure Ranch", "escure-ranch"), ("Fishtrap Lake", "fishtrap-lake"),
            ("Frenchman's Coulee", "frenchmans-coulee"), ("Ginkgo Petrified Forest", "ginkgo-petrified-forest"),
            ("Hawk Creek S P", "hawk-creek-s-p"), ("Hog Canyon & Falls", "hog-canyon--falls"),
            ("Juniper Dunes Wilderness", "juniper-dunes-wilderness"), ("Lake Lenore Caves & Mesa", "lake-lenore-caves--mesa"),
            ("Lakeview Ranch", "lakeview-ranch"), ("Lions Ferry to Palouse Falls", "lions-ferry-to-palouse-falls"),
            ("Northrup Canyon", "northrup-canyon"), ("Odessa Area", "odessa-area"),
            ("Palouse Falls State Park Heritage Site", "palouse-falls-state-park-heritage-site"),
            ("Quincy Lakes", "quincy-lakes"), ("Steamboat Rock", "steamboat-rock"),
            ("Sun Lakes S P Dry Falls Area", "sun-lakes-s-p-dry-falls-area"), ("Turnbull N.W.R.", "turnbull-nwr"),
            ("Twin Lakes", "twin-lakes1"),
        ],
        "Spokane County Parks": [
            ("Saltese Flats Wetland Trail", "saltese-flats-wetland-trail"),
            ("Spokane County Conservation Futures", "spokane-county-conservation-futures"),
        ],
        "Eastern Washington": [
            ("13 Mile Canyon Trail #23", "13-mile-canyon-trail-23"), ("Abercrombie Mountain", "abercrombie-mountain"),
            ("Crawford S.P., Gardner Cave", "crawford-sp-gardner-cave"), ("Gypsy Peak", "gypsy-peak"),
            ("Hoodoo Canyon", "hoodoo-canyon"), ("Hooknose Mountain", "hooknose-mountain"),
            ("Kalispell Rock", "kalispell-rock"), ("Roosevelt Grove of Ancient Cedars", "roosevelt-grove-of-ancient-cedars"),
            ("Sullivan Lake Shore Line", "sullivan-lake-shore-line"),
        ],
    },
    "Mexico": {None: [("Sayulita, Nayarit", "sayulita-nayarit")]},
    "South America": {None: [("Patagonia", "patagonia")]},
}

BIKE = {None: {None: [
    ("Saltese Highlands Summit Loop", "saltese-highlands-summit-loop"),
    ("Arrow Leaf", "arrow-leaf"), ("California Creek", "california-creek"),
]}}

# ---------------------------------------------------------------------------
# region overview pages that become the index.md of their new folder
# key: (activity_base_folder, region_display_name, subregion_display_name_or_None)
# value: current basename (searched via basename index, any directory)
# ---------------------------------------------------------------------------
INDEX_PAGES = {
    ("hike", None, None): "hike",
    ("hike", "Canada", None): "canada",
    ("hike", "Idaho", None): "idaho",
    ("hike", "Idaho", "American Selkirks"): "american-selkirks",
    ("hike", "Idaho", "North Idaho Hikes"): "north-idaho-hikes",
    ("hike", "Idaho", "Proposed Scotchman Peaks Wilderness"): "proposed-scotchman-peaks-wilderness",
    ("hike", "Idaho", "Silver Valley Area"): "silver-valley-area",
    ("hike", "Montana", None): "montana",
    ("hike", "Montana", "Bitterroots"): "bitterroots",
    ("hike", "Montana", "Cabinet Mountains Wilderness"): "cabinet-mountains-wilderness",
    ("hike", "Montana", "Lolo National Forest"): "lolo-national-forest",
    ("hike", "Oregon", None): "oregon",
    ("hike", "Washington", None): "washington",
    ("hike", "Washington", "Scablands"): "washington-scablands",
    ("hike", "Washington", "Colville National Forest"): "colville-national-forest",
    ("hike", "Mexico", None): "mexico",
    ("hike", "South America", None): "south-america",
}

# Slugs on the old site that don't match a current basename directly.
SLUG_OVERRIDES = {
    "st-joe-lake-6472rsquo-illinois-peak-7690rsquo": "st-joe-lake--illinois-peak",
    "wanless-lake-via-trailrsquos-656-360-912": "wanless-lake-via-trails-656-360-912",
    "graham-mountain1": "graham-mountain",       # old site had 2 URLs, only 1 file survived
    "shefoot-mountain1": "shefoot-mountain",
    "revett-lake1": "revett-lake",
    "cliff-lake--eagle-cliff-peak1": "cliff-lake--eagle-cliff-peak",
    "star-peak1": "star-peak",
    "sawtooth-mountain1": "sawtooth-mountain",
    "ross-creek-cedars1": "ross-creek-cedars",
    "pillick-ridge-61671": "pillick-ridge-6167",
}

ACTIVITIES = {
    "hike": HIKE,
    "bike": BIKE,
}


def slugify(name):
    s = name.lower()
    s = s.replace("&", "and").replace("'", "").replace(".", "").replace(",", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def build_basename_index():
    idx = {}
    for root, dirs, files in os.walk(DOCS):
        if "blog" in root.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), DOCS)
                idx.setdefault(f[:-3], []).append(rel)
    return idx


def resolve_basename(slug):
    return SLUG_OVERRIDES.get(slug, slug)


def git_mv(src, dst):
    dst_dir = os.path.dirname(dst)
    if dst_dir and not os.path.isdir(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)
    subprocess.run(["git", "mv", src, dst], check=True, cwd=os.path.dirname(DOCS) or ".")


def migrate(base_folder, data):
    idx = build_basename_index()
    moved = {}  # old rel path -> new rel path
    nav_regions = []  # [(region_name, [nav_items])]

    def move_index_page(idx_key, folder):
        if idx_key not in INDEX_PAGES:
            return None
        idx_basename = INDEX_PAGES[idx_key]
        cands = idx.get(idx_basename)
        if not cands:
            print(f"    !! no overview file found for '{idx_basename}'", file=sys.stderr)
            return None
        src_rel = cands[0]
        dst_rel = os.path.join(folder, "index.md").replace(os.sep, "/")
        if src_rel in moved:
            return moved[src_rel]
        if src_rel != dst_rel:
            print(f"git mv docs/{src_rel} docs/{dst_rel}")
            git_mv(os.path.join(DOCS, src_rel), os.path.join(DOCS, dst_rel))
        moved[src_rel] = dst_rel
        return dst_rel

    top_index_path = move_index_page((base_folder, None, None), base_folder)

    for region, subs in data.items():
        region_slug = slugify(region) if region else None
        region_items = []
        region_folder = os.path.join(base_folder, *((region_slug,) if region_slug else ()))
        # Region-level overview (e.g. idaho.md -> hike/idaho/index.md), independent
        # of whether this region has any None-keyed (flat) subregion entries.
        if region_slug:
            move_index_page((base_folder, region, None), region_folder)
        for subregion, items in subs.items():
            sub_slug = slugify(subregion) if subregion else None
            folder = os.path.join(base_folder, *(p for p in (region_slug, sub_slug) if p))
            target_items = []

            if subregion:
                move_index_page((base_folder, region, subregion), folder)

            for title, old_slug in items:
                basename = resolve_basename(old_slug)
                cands = idx.get(basename)
                if not cands:
                    print(f"    !! MISSING: {region}/{subregion}/{title} -> {basename}.md", file=sys.stderr)
                    continue
                src_rel = cands[0]
                if src_rel in moved:
                    dst_rel = moved[src_rel]
                else:
                    dst_rel = os.path.join(folder, os.path.basename(src_rel))
                    if src_rel != dst_rel:
                        print(f"git mv docs/{src_rel} docs/{dst_rel}")
                        git_mv(os.path.join(DOCS, src_rel), os.path.join(DOCS, dst_rel))
                    moved[src_rel] = dst_rel
                target_items.append((title, dst_rel.replace(os.sep, "/")))

            if subregion:
                region_items.append((subregion, target_items))
            else:
                region_items.extend(("__flat__", t) for t in target_items)
        nav_regions.append((region, region_items))

    return nav_regions, moved, top_index_path


def print_nav_yaml(section_title, nav_regions, top_index=None, indent=2):
    pad = " " * indent
    print(f"{pad}- {section_title}:")
    if top_index:
        print(f"{pad}  - {top_index}")
    for region, region_items in nav_regions:
        if region is None:
            for _, (title, path) in region_items:
                print(f"{pad}  - {title}: {path}")
            continue
        print(f"{pad}  - {region}:")
        for entry in region_items:
            if entry[0] == "__flat__":
                title, path = entry[1]
                print(f"{pad}    - {title}: {path}")
            else:
                subregion, items = entry
                print(f"{pad}    - {subregion}:")
                for title, path in items:
                    print(f"{pad}      - {title}: {path}")


# ---------------------------------------------------------------------------
# Fix relative markdown/image links broken by moving their target (or, for
# hand-authored hub pages like hike.md, moving the file that contains them).
# ---------------------------------------------------------------------------

LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")
HTML_LINK_RE = re.compile(r'((?:href|src)=")([^"]+)(")')


def fix_links(moved):
    """moved: {old_docs_rel_path: new_docs_rel_path}, forward-slash or os.sep."""
    moved = {k.replace(os.sep, "/"): v.replace(os.sep, "/") for k, v in moved.items()}
    new_to_old = {v: k for k, v in moved.items()}

    changed = []
    for root, dirs, files in os.walk(DOCS):
        # Blog posts never move here, but they DO link out to regular content
        # pages that might -- so still scan/fix their links, just via the
        # identity (old==new) path since the posts themselves are stationary.
        for f in files:
            if not f.endswith(".md"):
                continue
            new_rel = os.path.relpath(os.path.join(root, f), DOCS).replace(os.sep, "/")
            old_rel = new_to_old.get(new_rel, new_rel)  # unmoved files: old == new
            old_dir = os.path.dirname(old_rel)
            new_dir = os.path.dirname(new_rel)

            path = os.path.join(DOCS, new_rel)
            with open(path, encoding="utf-8") as fp:
                content = fp.read()

            def repl(m):
                prefix, target, suffix = m.group(1), m.group(2), m.group(3)
                if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                    return m.group(0)
                frag = ""
                clean_target = target
                if "#" in target:
                    clean_target, frag = target.split("#", 1)
                    frag = "#" + frag
                old_target_abs = os.path.normpath(os.path.join(old_dir, clean_target)).replace(os.sep, "/")
                new_target_abs = moved.get(old_target_abs, old_target_abs)
                new_link = os.path.relpath(new_target_abs, new_dir).replace(os.sep, "/")
                if new_link == clean_target:
                    return m.group(0)
                return f"{prefix}{new_link}{frag}{suffix}"

            new_content = LINK_RE.sub(repl, content)
            new_content = HTML_LINK_RE.sub(repl, new_content)
            if new_content != content:
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                changed.append(new_rel)
    return changed


def moved_from_git_status():
    """Rebuild the old->new rel-path map from `git status` rename detection,
    for re-running fix_links() after the migrate() process has already exited."""
    out = subprocess.run(["git", "status", "--porcelain", "--", "docs"],
                          check=True, capture_output=True, text=True).stdout
    moved = {}
    for line in out.splitlines():
        if line[0] in "RC" or line[1] in "RC":
            rest = line[3:]
            old, new = rest.split(" -> ")
            old = old.strip().removeprefix("docs/")
            new = new.strip().removeprefix("docs/")
            moved[old] = new
    return moved


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--relink":
        moved = moved_from_git_status()
        print(f"--- re-fixing links for {len(moved)} known-moved files ---")
        changed = fix_links(moved)
        for c in changed:
            print(f"  fixed links in docs/{c}")
        sys.exit(0)

    if len(sys.argv) != 2 or sys.argv[1] not in ACTIVITIES:
        print(f"usage: {sys.argv[0]} <{'|'.join(ACTIVITIES)}|--relink>", file=sys.stderr)
        sys.exit(1)
    name = sys.argv[1]
    nav, moved, top_index = migrate(name, ACTIVITIES[name])
    print(f"\n--- fixing links for {len(moved)} moved files ---")
    changed = fix_links(moved)
    for c in changed:
        print(f"  fixed links in docs/{c}")
    print("\n--- nav yaml ---")
    print_nav_yaml(name.capitalize(), nav, top_index)
