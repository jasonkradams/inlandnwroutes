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

PADDLE = {
    "Washington": {
        "Scablands": [
            ("Amber Lake Launch", "amber-lake-launch"), ("Badger Lake Launch", "badger-lake-launch"),
            ("Banks Lake Kayak and Hike", "banks-lake-kayak-and-hike"), ("Bonnie Lake Landing", "bonnie-lake-landing"),
            ("Clear Lake Launch", "clear-lake-launch"), ("Fishtrap Lake, WA", "fishtrap-lake-wa"),
            ("Marshall Lake Launch", "marshall-lake-launch"), ("Medical Lake Launch", "medical-lake-launch"),
            ("West Medical Lake", "west-medical-lake"), ("Palouse River Launch", "palouse-river-launch"),
            ("Potholes Reservoir", "potholes-reservoir"),
        ],
        "Eastern Washington": [
            ("9 Mile Recreation Area Launch", "9-mile-recreation-area-launch"), ("Bead Lake Launch", "bead-lake-launch"),
            ("Bear Lake Launch", "bear-lake-launch"), ("Davis Lake Launch", "davis-lake-launch"),
            ("Eloika Lake Launch", "eloika-lake-launch"), ("3rd Street Launch", "3rd-street-launch"),
            ("Liberty Lake Regional Park", "liberty-lake-regional-park"), ("Long Lake Launch", "long-lake-launch1"),
            ("Loon Lake Launch", "loon-lake-launch"), ("Newman Lake Road", "newman-lake-road"),
            ("Pewee Falls, Pend Orielle River", "pewee-falls-pend-orielle-river"), ("Boulder Bay Landing", "boulder-bay-landing"),
            ("Gateway Regional Park", "gateway-regional-park"), ("Nine Mile Recreation Area", "nine-mile-recreation-area"),
            ("Long Lake Launch (North)", "long-lake-launch"),
        ],
    },
    "Idaho": {
        "North Idaho Launch Sites - CDA Lake": [
            ("Blackwell Island Launch", "blackwell-island-launch"), ("Blue Bay Landing", "blue-bay-landing"),
            ("Booth Park Launch", "booth-park-launch"), ("Carlin Bay Launch", "carlin-bay-launch"),
            ("Cougar Bay Landing", "cougar-bay-landing"), ("Gould's Launch", "goulds-launch"),
            ("Harrison, Idaho Launch", "harrison-idaho-launch"), ("Harrison Slough", "harrison-slough"),
            ("Hawley's Landing", "hawleys-landing"), ("Heyburn S.P./Lake Chatcolet Launch", "heyburn-splakechatcolet-launch"),
            ("Higgins Point Launch", "higgins-point-launc"), ("Kidd Island Bay Launch", "kidd-island-bay-launch"),
            ("Loffs Bay Launch", "loffs-bay-launch"), ("Mica Bay Launch", "mica-bay-launch"),
            ("Mineral Ridge Launch", "mineral-ridge-launch"), ("Neachen Bay Launch", "neachen-bay-launch"),
            ("N.I.C. Dike Road Landing", "nic-dike-road-landing"), ("Old Mission Launch", "old-mission-launch1"),
            ("Rockford Bay Launch", "rockford-bay-launch"), ("Sanders Beach Landing", "sanders-beach-landing"),
            ("Spokane Point Launch", "spokane-point-launch"), ("Sun Up Bay Launch", "sun-up-bay-launch"),
            ("Windy Bay Launch", "windy-bay-launch"),
        ],
        "CDA River Chain Lakes": [
            ("Anderson Lake/Thompson Lake Launch", "anderson-lakethompson-lake-launch"), ("Black Lake Launch", "black-lake-launch"),
            ("Killarney Lake Launch", "killarney-lake-launch"), ("Medimont Lake Launch", "medimont-lake-launch"),
            ("Old Mission Launch", "old-mission-launch"), ("Rainy Hill Launch", "rainy-hill-launch"),
            ("Rose Lake Launch", "rose-lake-launch"),
        ],
        "Additional Launches": [
            ("Upper CDA River Landing", "upper-cda-river-landing"), ("Cocolalla Access Launch", "cocolalla-access-launch"),
            ("Fernan Lake Park West", "fernan-lake-park-west"), ("Fernan Lake Launch East", "fernan-lake-launch-east"),
            ("Honeysuckle Launch", "honeysuckle-launch"), ("Sportsman Access Launch", "sportsman-access-launch"),
            ("Hauser Lake Park Launch", "hauser-lake-park-launch"),
        ],
        "Pend Orielle Lake": [
            ("Echo Bay Lake Pend Orielle", "echo-bay-lake-pend-orielle"), ("Bayview City Launch", "bayview-city-launch"),
            ("Denton Slough", "denton-slough"), ("Farrugut State Park Launch", "farrugut-state-park-launch"),
            ("Garfield Bay Launch", "garfield-bay-launch"), ("Granite Creek Landing", "granite-creek-landing"),
            ("Hope Launch", "hope-launch"), ("Johnson Creek Launch", "johnson-creek-launch"),
            ("Lakeview Launch", "lakeview-launch"), ("Pack River and Hwy-95 Launch", "pack-river-and-hwy-95-launch"),
            ("Pringle Park Launch", "pringle-park-launch"), ("Sam Owen Camp Ground Launch", "sam-owen-camp-ground-launch"),
            ("Sandpoint City Beach Launch", "sandpoint-city-beach-launch"), ("Sunnyside Park Launch", "sunnyside-park-launch"),
            ("Talache Landing", "talache-landing"), ("Trestle Creek Recreation Area Launch", "trestle-creek-recreation-area-launch"),
            ("Whiskey Rock Camp Ground Landing", "whiskey-rock-camp-ground-landing"),
        ],
        "Pend Orielle River": [
            ("Albeni Cove Launch", "albeni-cove-launch"), ("Cary Launch", "cary-launch"), ("Laclede Launch", "laclede-launch"),
            ("Memorial Field Launch", "memorial-field-launch"), ("Metaline Launch", "metaline-launch"),
            ("Morton Slough", "morton-slough"), ("Priest River City Park Launch", "priest-river-city-park-launch"),
            ("Priest River Recreation Area Launch", "priest-river-recreation-area-launch"), ("Rieley Creek Launch", "rieley-creek-launch"),
            ("Springy Point Camp Ground Launch", "springy-point-camp-ground-launch"),
        ],
        "Lower Priest Lake": [
            ("Blue Diamond Marina", "blue-diamond-marina"), ("Bishop's Marina", "bishops-marina"),
            ("Cavanaugh Bay Launch", "cavanaugh-bay-launch"), ("Coolin Bay Docks and Ramp", "coolin-bay-docks-and-ramp"),
            ("Indian Creek Camp Ground Launch", "indian-creek-camp-ground-launch"), ("Kalispell Bay Launch", "kalispell-bay-launch"),
            ("Tule Bay/Beaver Creek Landing", "tule-baybeaver-creek-landing"),
        ],
        "Spokane River": [
            ("Bronze Bay Launch", "bronze-bay-launch"), ("Q'emiln Park Launch", "qemiln-park-launch"),
            ("East Riverview Landing/Launch", "east-riverview-landinglaunch"),
        ],
        "Spirit Lake": [
            ("Bronze Bay Launch (Spirit)", "bronze-bay-launch1"), ("Maiden Rock Launch", "maiden-rock-launch"),
            ("Spirit Lake Boat Launch", "spirit-lake-boat-launch"),
        ],
        "St. Joe and St. Maries Rivers": [
            ("Aqua Park Launch", "aqua-park-launch"), ("Cherry Bend Park Launch", "cherry-bend-park-launch"),
            ("First Street Launch", "first-street-launch"), ("Silvertip Landing", "silvertip-landing"),
        ],
        "Twin Lakes": [
            ("Lower Twin Lakes Launch", "lower-twin-lakes-launch"), ("Twin Lakes Narrows", "twin-lakes-narrows"),
            ("Upper Twin Lakes Launch", "upper-twin-lakes-launch"),
        ],
    },
    "Montana": {
        "Bull Lake": [("Bad Medicine Launch and CG", "bad-medicine-launch-and-cg"), ("Dorr Skeels Camp Ground", "dorr-skeels-camp-ground")],
        "Bull River": [("Bull River North", "bull-river-north"), ("Bull River Middle", "bull-river-middle"), ("Bull River South", "bull-river-south")],
        "Clark Fork River": [
            ("Big Eddy Camp Ground and Launch", "big-eddy-camp-ground-and-launch"), ("Grass Widow", "grass-widow"),
            ("Noxon Ramp", "noxon-ramp"), ("Thompson Falls State Park", "thompson-falls-state-park"),
        ],
        "Glacier National Park": [("Kintla Lake", "kintla-lake")],
        None: [("Sanders County", "sanders-county")],
    },
    "Oregon": {None: [("Clear Lake", "clear-lake")]},
    "Canada": {None: [("Whiteswan Provintial Park", "whiteswan-provintial-park")]},
}

SKI = {
    "Backcountry": {None: [
        ("Backcountry Ski Friends", "backcountry-ski-friends"), ("Deer Creek Nordic Sno-Park", "deer-creek-nordic-sno-park"),
        ("Mount Spokane Snowshoe/Nordic Ski/BC Ski", "mount-spokane-snowshoenordic-skibc-ski"),
    ]},
    "USA": {
        "Washington": [
            ("Bluewood", "bluewood"), ("49°N Ski Area", "49degn-ski-area"), ("Loup Loup Ski Bowl", "loup-loup-ski-bowl"),
            ("Mission Ridge Ski & Board Resort", "mission-ridge-ski--board-resort"),
            ("Mount Spokane Ski & Snowboard Park", "mount-spokane-ski--snowboard-park"),
        ],
        "Idaho": [
            ("Bogus Basin Ski Resort", "bogus-basin-ski-resort"), ("Brundage Mountain Resort", "brundage-mountain-resort"),
            ("Lookout Pass Ski & Rec.", "lookout-pass-ski--rec"), ("Schweitzer Mountain Resort", "schweitzer-mountain-resort"),
            ("Silver Mountain Resort", "silver-mountain-resort"),
        ],
        "Montana": [
            ("Big Sky Resort", "big-sky-resort"), ("Blacktail Mountain Ski Area", "blacktail-mountain-ski-area"),
            ("Bridger Bowl", "bridger-bowl"), ("Discovery Ski Area", "discovery-ski-area"),
            ("Red Lodge Mountain", "red-lodge-mountain"), ("Teton Pass Resort", "teton-pass-resort"),
            ("Tamarack Resort", "tamarack-resort"), ("Turner Mountain Ski Area", "turner-mountain-ski-area"),
            ("Whitefish Mountain Resort", "whitefish-mountain-resort"),
        ],
        "Oregon": [
            ("Mount Bachelor Ski Resort", "mount-bachelor-ski-resort"), ("Anthony Lakes Mt. Resort", "anthony-lakes-mt-resort"),
            ("Mount Hood Meadows", "mount-hood-meadows"), ("Mount Hood Ski Bowl", "mount-hood-ski-bowl"),
            ("Timberline Lodge Ski Area", "timberline-lodge-ski-area"),
        ],
        "Utah": [
            ("Alta Ski Area", "alta-ski-area"), ("Brighton Resort", "brighton-resort"), ("Deer Valley Resort", "deer-valley-resort"),
            ("Park City Ski Area", "park-city-ski-area"), ("Powder Mountain Resort", "powder-mountain-resort"),
            ("Snow Basin Resort", "snow-basin-resort"), ("Snowbird Ski Area", "snowbird-ski-area"),
            ("Solitude Mountain", "solitude-mountain"), ("Sundance Ski Resort", "sundance-ski-resort"),
        ],
        "Wyoming": [
            ("Grand Targhee Ski Resort", "grand-targhee-sku-resort"), ("Jackson Hole Ski Resort", "jackson-hole-ski-resort"),
            ("Snowking Ski Resort", "snowking-ski-resort"),
        ],
    },
    "Canada": {
        "British Columbia": [
            ("Apex Mountain Resort", "apex-mountain-resort"), ("Mount Baldy Ski Resort", "mount-baldy-ski-resort"),
            ("Fernie Alpine Resort", "fernie-alpine-resort"), ("Kicking Horse Mt. Resort", "kicking-horse-mt-resort"),
            ("Kimberrly Alpine Resort", "kimberrly-alpine-resort"), ("Panorama Mountain Resort", "panorama-mountain-resort"),
            ("Red Mountain Resort", "red-mountain-resort"), ("Revelstoke Mt. Resort", "revelstoke-mt-resort"),
            ("Salmo Ski Area", "salmo-ski-area"), ("Silver Star Mountain Resort", "silver-star-mountain-resort"),
            ("Sun Peaks Resort", "sun-peaks-resort"), ("Whistler Blackcomb", "whistler-blackcomb"),
            ("Whitewater Ski Resort", "whitewater-ski-resort"),
        ],
        "Alberta": [
            ("Lake Louise Ski Resort", "lake-louise-ski-resort"), ("Marmot Basin", "marmot-basin"),
            ("Mount Norquay", "mount-norquay"), ("Sunshine Ski Resort", "sunshine-ski-resort"),
        ],
    },
}

WATERFALLS = {
    "Washington": {None: [
        ("Crystal Falls", "crystal-falls"), ("Douglas Falls Grange Parkb", "douglas-falls-grange-parkb"),
        ("Dry Falls, Sun Lakes S.P.", "dry-falls-sun-lakes-sp"), ("Finch Arboretum", "finch-arboretum"),
        ("Granite Falls & La Sota Fallsb", "granite-falls--la-sota-fallsb"), ("Hawk Creek Falls S.P.", "hawk-creek-falls-sp"),
        ("Liberty Creek Falls", "liberty-creek-falls"), ("Palisades Creek Falls", "palisades-creek-falls"),
        ("U. & L. Palouse Falls", "u--l-palouse-falls"), ("Boundrary Dam", "boundary-dam"),
        ("Pewee Falls", "pewee-falls"), ("Sweet Creek Falls", "sweet-creek-falls"), ("Towell Falls", "towell-falls"),
    ]},
    "Idaho": {None: [
        ("American Falls", "american-falls"), ("Copper Falls", "copper-falls"),
        ("Elk Creek Falls Recreation Area", "elk-creek-falls-recreation-area"),
        ("Falls Creek Falls, Idaho", "falls-creek-falls-idaho"),
        ("Fern, Shadow & Centennial Falls", "fern-shadow--centennial-falls"),
        ("Hunt Creek Falls", "hunt-creek-falls"), ("Moyie Falls", "moyie-falls"),
        ("Little Harrison Lake Falls", "little-harrison-lake-falls"), ("Myrtle Creek Falls", "myrtle-creek-falls"),
        ("Post Falls, Falls", "post-falls-falls"), ("Revett Falls", "revett-falls"),
        ("U. & L. Snow Creek Falls", "u--l-snow-creek-falls"), ("Torrelle Falls", "torrelle-falls"),
        ("Wellington Falls", "wellington-falls"), ("Willow Creek Falls East", "willow-creek-falls-east"),
        ("Willow Creek West Cascades", "willow-creek-west-cascades"),
    ]},
    "Montana": {None: [
        ("Cascade Falls", "cascade-falls"), ("Dipper Falls", "dipper-falls"), ("Granite Falls", "granite-falls"),
        ("Graves Creek Falls", "graves-creek-falls"), ("Kootenai Falls", "kootenai-falls"),
        ("Leigh Lake Falls Upper", "leigh-lake-falls-upper"), ("Leigh Lake Falls Lower", "leigh-lake-falls-lower"),
        ("Rock Creek Falls", "rock-creek-falls"), ("St. Paul Lake Falls", "st-paul-lake-falls"),
        ("Vermillion Falls", "vermillion-falls"), ("Upper Yaak Falls", "upper-yaak-falls"), ("Lower Yaak Falls", "lower-yaak-falls"),
    ]},
    "Oregon": {None: [("Silver Falls State Park", "silver-falls-state-park")]},
}

WILDFLOWERS = {
    "Red and Pink": {None: [
        ("Alpine Laurel", "alpine-laurel"), ("Bitterroot", "bitterroot"), ("Grass Widow", "grass-widow1"),
        ("Kinnikinnick", "kinnikinnick"), ("Mountain Spiraea", "mountain-spiraea"), ("Red Dead Nettle", "red-dead-nettle"),
        ("Red Indian Paint Brush", "red-indian-paint-brush"), ("Red Twinberry", "red-twinberry"),
        ("Scarlet Beebalm", "scarlet-beebalm"), ("Scarlet Gilia", "scarlet-gilia"), ("Showy Phlox", "showy-phlox"),
        ("Spreading Dogbane", "spreading-dogbane"), ("Sticky Geranium", "sticky-geranium"),
        ("Western Moss Heather", "western-moss-heather"),
    ]},
    "Orange": {None: [
        ("Orange Day-Lily", "orange-day-lily"), ("Merten's Coralroot", "mertens-coralroot"), ("Wild Honeysuckle", "wild-honeysuckle"),
    ]},
    "Yellow": {None: [
        ("Balkan Toadflax", "balkan-toadflax"), ("Bird'sfoot Trefoil", "birdsfoot-trefoil"),
        ("Dwarf Yellow Fleabane", "dwarf-yellow-fleabane"), ("False Hellebore", "false-hellebore"),
        ("Glacier Lilies", "glacier-lilies"), ("Hop Goodena", "hop-goodena"), ("Large Hop Clover", "large-hop-clover"),
        ("Saint John's Wort", "saint-johns-wort"), ("Shrubby Cinquefoil", "shrubby-cinquefoil"),
        ("Stream Violet", "stream-violet"), ("Tansy", "tansy"), ("Yellow Columbine", "yellow-columbine"),
        ("Cliff Penstemon", "cliff-penstemon"),
    ]},
    "Blue": {None: [
        ("Camas", "camas"), ("Gentian", "gentian"), ("Mountain Kittentail", "mountain-kittentail"),
        ("Nuttall's Larkspur", "nuttalls-larkspur"), ("Lupine", "lupine"),
    ]},
    "Purple": {None: [
        ("Ballhead Waterleaf", "ballhead-waterleaf"), ("Broad-Leaf Sweet Pea", "broad-leaf-sweet-pea"),
        ("Alpine Sweet-Vetch", "alpine-sweet-vetch"), ("Elephant's Head", "elephants-head"), ("Fireweed", "fireweed"),
        ("Devil's Club", "devils-club"), ("Woodland Pinedrop", "woodland-pinedrop"),
        ("Dark Throated Shooting Star", "dark-throated-shooting-star"), ("Large-Flower Clarkia", "large-flower-clarkia"),
        ("Large-Flowered Triteleia", "large-flowered-triteleia"), ("Lewis' Monkey Flower", "lewis-monkey-flower"),
        ("Sagebrush Mariposa", "sagebrush-mariposa"), ("Bellflower", "bellflower"), ("Threadleaf Phacilia", "threadleaf-phacilia"),
    ]},
    "White": {None: [
        ("Baker's Mariposa Lily", "bakers-mariposa-lily"), ("Baneberry", "baneberry"), ("Bear Grass", "bear-grass"),
        ("Bride's Bonnet", "brides-bonnet"), ("0xeye Daisy", "0xeye-daisy"), ("Polemonium", "polemonium"),
        ("Service Berry Saskatoon", "service-berry-saskatoon"), ("Sitka Valerian", "sitka-valerian"),
        ("Snowbrush Ceanothus", "snowbrush-ceanothus"), ("Spring Beauties", "spring-beauties"),
        ("Star Flowered Lily of the Valley", "star-flowered-lily-of-the-valley"), ("Thimbelberry", "thimbelberry"),
        ("Threeleaf Foamflower", "threeleaf-foamflower"), ("Meadowsweet", "meadowsweet"), ("Trillium", "trillium"),
        ("Woodland Star", "woodland-star"), ("Mountain Deathcamas", "mountain-deathcamas"), ("Sego Lily", "sego-lily"),
    ]},
}

RESOURCES = {
    "Conservation and Like-Minded Organizations": {None: [
        ("Washington Trails Association", "washington-trails-association"),
        ("Idaho Trails Association", "idaho-trails-association"),
        ("Spokane Mountaineers", "spokane-mountaineers"),
        ("Spokane Canoe and Kayak Club", "spokane-canoe-and-kayak-club"),
        ("Spokane Nordic Ski Association", "spokane-nordic-ski-association"),
    ]},
    "General": {None: [
        ("Managing Agencies", "managing-agencies"),
        ("Idaho: A Climbing Guide", "idaho-a-climbing-guide"),
        ("Hiking Boise", "hiking-boise"),
        ("Evans Outdoor Adventures", "evans-outdoor-adventures"),
        ("Camera Corral", "camera-corral"),
        ("Hiking From Here", "hiking-from-here"),
        ("Inland NW Hikers", "inland-nw-hikers"),
        ("Silverlight", "silverlight"),
        ("Silverstreak Zipline Tours", "silverstreak-zipline-tours"),
        ("Trails End Brewery", "trails-end-brewery"),
        ("Medical Information", "medical-information"),
        ("Weather, Thunderstorms and Lightning", "weather-thunderstorms-and-lightning"),
        ("Trail Etiquette and Skills", "trail-etiquette-and-skills"),
        ("Gear :: David", "gear-david"),
        ("Gear :: Chic", "gear-chic"),
        ("Photography", "photography"),
        ("Wildlife", "wildlife"),
        ("Hints", "hints"),
        ("Restaurants and Pubs", "restaurants-and-pubs"),
    ]},
}

GALLERY = {
    "Contributors": {None: [
        ("Amy Voeller", "amy-voeller"),
        ("Chris Herath", "chris-herath"),
        ("David Crafton", "david-crafton"),
        ("Tony Kozlowski", "tony-kozlowski"),
        ("Vanette Leighty", "vanette-leighty"),
    ]},
    "Categories": {None: [
        ("Panorama", "panorama"),
        ("Streams to Rivers", "streams-to-rivers"),
        ("Wildlife", "wildlife"),
        ("Deserts & Scablands", "deserts--scablands"),
        ("Atmosphere", "atmosphere"),
        ("Trails", "trails"),
        ("Rocks", "rocks"),
        ("Trees", "trees"),
        ("Trail Heros", "trail-heros"),
        ("Outhouses", "outhouses"),
        ("Faces", "faces"),
        ("Winter", "winter"),
        ("Fungi - Rooms", "fungi---rooms"),
        ("Phenomenon", "phenomenon"),
        ("Fireworks", "fireworks"),
    ]},
}

WRITINGS = {None: {None: [
    ("Adages", "adages"),
    ("Essays", "essays"),
    ("Notes", "notes"),
    ("Poems", "poems"),
    ("Quotes", "quotes"),
    ("Stories", "stories"),
]}}

RECIPES = {
    "Soups": {None: [
        ("Chicken and Rice Soup", "chicken-and-rice-soup"),
        ("Moma Moreno's Chicken Green Chili Soup", "moma-morenos-chicken-green-chili-soup"),
        ("Chicken Mushroom Mashed Potato Soup", "chicken-mushroom-mashed-potato-soup"),
        ("Uncle Chuck's Manhatten Style Clam Chowder", "uncle-chucks-manhatten-style-clam-chowder"),
        ("Soup for Lunch in the Mountains", "soup-for-lunch-in-the-mountains"),
    ]},
    "Desserts": {None: [
        ("Uncle Chuck's World Famous Blondies", "uncle-chucks-world-famous-blondies"),
        ("Instant Birthday Cake", "instant-birthday-cake"),
    ]},
    "Brines, Marinades and Sauces": {None: [
        ("Easy Quality Gravy", "easy-quality-gravy"),
    ]},
    "Main Dishes": {None: [
        ("Basil Shrimp Poscuitto Ham Wraps", "basil-shrimp-poscuitto-ham-wraps"),
        ("Clammy Cabbage Over Pasta", "clammy-cabbage-over-pasta"),
        ("Tcda Curried Rice", "tcda-curried-rice"),
        ("Lunch in the Mountains", "lunch-in-the-mountains"),
    ]},
}

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
    "long-lake-launch1": "long-lake-launch",     # same old-site duplicate-URL pattern as above
    "old-mission-launch1": "old-mission-launch",
    "bronze-bay-launch1": "bronze-bay-launch",
    "farrugut-state-park-launch": "farragut-state-park-launch",  # old-site typo
    "tule-baybeaver-creek-landing": "tule-bay-beaver-creek-landing",  # old-site typo
    "49degn-ski-area": "49-degrees-north-ski-area",
    "grand-targhee-sku-resort": "grand-targhee-ski-resort",  # old-site typo ("sku")
}

ACTIVITIES = {
    "hike": HIKE,
    "bike": BIKE,
    "paddle": PADDLE,
    "ski": SKI,
    "waterfalls": WATERFALLS,
    "wildflowers": WILDFLOWERS,
    "resources": RESOURCES,
    "gallery": GALLERY,
    "writings": WRITINGS,
    "recipes": RECIPES,
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


def _yaml_key(title):
    # A bare "Title: Rest" breaks unquoted YAML `key: value` mapping syntax
    # (the second colon looks like another mapping separator).
    if ":" in title or title.startswith(("'", '"')):
        return "'" + title.replace("'", "''") + "'"
    return title


def print_nav_yaml(section_title, nav_regions, top_index=None, indent=2):
    pad = " " * indent
    print(f"{pad}- {section_title}:")
    if top_index:
        print(f"{pad}  - {top_index}")
    for region, region_items in nav_regions:
        if region is None:
            for _, (title, path) in region_items:
                print(f"{pad}  - {_yaml_key(title)}: {path}")
            continue
        print(f"{pad}  - {_yaml_key(region)}:")
        for entry in region_items:
            if entry[0] == "__flat__":
                title, path = entry[1]
                print(f"{pad}    - {_yaml_key(title)}: {path}")
            else:
                subregion, items = entry
                print(f"{pad}    - {_yaml_key(subregion)}:")
                for title, path in items:
                    print(f"{pad}      - {_yaml_key(title)}: {path}")


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
