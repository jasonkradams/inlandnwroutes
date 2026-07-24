import os

md_content = """---
title: Hiking & Scrambling Guides
tags:
  - Trails & Scrambles
  - Hiking
  - Backpacking
  - Scrambling
---

# Hiking & Scrambling Regional Portal

Welcome to the Inland NW Routes Hiking & Scrambling portal! The Inland Northwest offers an unparalleled diversity of mountain terrain—from the rugged granite spires of the American Selkirks and the glaciated wilderness of the Cabinet Mountains to the historic ridge trails of the Bitterroots and the high alpine crests of the Canadian Rockies.

Explore the interactive regional map below or browse our primary guidebooks to discover trail statistics, directions, geology, and weather alerts for each region.

---

## Interactive Regional Hiking Map

Click any map marker to inspect regional highlights and open the corresponding hiking guide.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="hiking-regions-map" style="width: 100%; height: 520px; border-radius: 12px; margin-top: 1rem; margin-bottom: 2rem; border: 1px solid var(--md-default-foreground-color--lightest, #ccc); box-shadow: 0 4px 14px rgba(0,0,0,0.12); z-index: 1;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  if (typeof L === 'undefined') return;

  var map = L.map('hiking-regions-map').setView([48.2, -115.8], 7);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var regions = [
    { name: "American Selkirks", coords: [48.55, -116.65], link: "american-selkirks.md", desc: "Granite spires, Priest Lake & Harrison Peak" },
    { name: "Cabinet Mountains Wilderness", coords: [48.15, -115.65], link: "blog/posts/34-cabinet-mountain-wilderness.md", desc: "Glaciated wilderness peaks & alpine lakes" },
    { name: "Proposed Scotchman Peaks", coords: [48.20, -116.05], link: "blog/posts/blog-58-proposed-scotchman-peak-wilderness.md", desc: "Scotchman Peak (7,709') & steep vertical ridges" },
    { name: "Bitterroot Mountains", coords: [47.10, -115.35], link: "bitterroots.md", desc: "St. Joe River headwaters & Silver Valley crest" },
    { name: "Canadian Rockies & Bugaboos", coords: [50.50, -116.70], link: "canada.md", desc: "Fisher Peak, Creston Valley & Bugaboos" },
    { name: "Glacier National Park", coords: [48.65, -113.80], link: "glacier-np.md", desc: "Highline trail & Continental Divide passes" },
    { name: "Spokane Regional Trails", coords: [47.65, -117.40], link: "spokane-county-conservation-futures.md", desc: "Conservation Futures & Scabland trail networks" }
  ];

  regions.forEach(function(r) {
    var marker = L.marker(r.coords).addTo(map);
    marker.bindPopup('<div style="font-family: inherit; font-size: 0.9rem;"><strong><a href="' + r.link + '">' + r.name + '</a></strong><br><span style="font-size: 0.8rem; color: #555;">' + r.desc + '</span></div>');
  });
});
</script>

---

## Regional Hiking Guidebooks Overview

| Regional Range / Area | Geography & Key Highlights | Guide Link |
| :--- | :--- | :--- |
| **American Selkirks** | High granite spires, Priest Lake basin, Harrison & Chimney Rock | [American Selkirks Guide](american-selkirks.md) |
| **Cabinet Mountains Wilderness** | Deep glaciated valleys, Snowshoe Peak (8,736'), Leigh Lake | [Cabinet Wilderness Guide](blog/posts/34-cabinet-mountain-wilderness.md) |
| **Proposed Scotchman Peaks** | Steep terrain above Lake Pend Oreille, Scotchman Peak (7,709') | [Scotchman Peaks Guide](blog/posts/blog-58-proposed-scotchman-peak-wilderness.md) |
| **Bitterroot Mountains** | St. Joe River headwaters, Illinois Peak (7,690'), Stateline Trail | [Bitterroots Guide](bitterroots.md) |
| **Canadian Rockies** | Bugaboos, Fisher Peak (9,336'), Creston Valley | [Canadian Rockies Guide](canada.md) |
| **Glacier National Park** | Continental Divide passes, Highline Trail, alpine lakes | [Glacier N.P. Guide](glacier-np.md) |
| **Spokane & Scablands** | Spokane Conservation Futures, Washington Scabland coulees | [Spokane Regional Guide](spokane-county-conservation-futures.md) |

---

## Trip Planning & Wilderness Safety

!!! info "Essential Wilderness Preparation"

    - **Weather & Conditions:** Always check local weather and Forest Service trail alerts before heading into backcountry areas.
    - **14 Essentials:** Carry proper navigation (map & GPS), layers, sun protection, hydration, and emergency shelter.
    - **Bear & Wildlife Safety:** Carry bear spray in an accessible location and practice Leave No Trace principles across all trail networks.
"""

with open("docs/hike.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print("Generated interactive map docs/hike.md successfully")
