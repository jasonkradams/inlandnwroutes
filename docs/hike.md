---
title: Hiking & Scrambling Guides
tags:
  - Trails & Scrambles
  - Hiking
  - Backpacking
  - Scrambling
---

# Hiking & Scrambling Regional Portal

Welcome to the Inland NW Routes Hiking & Scrambling portal! The Inland Northwest offers an extraordinary range of alpine landscapes—from the granite spires of the American Selkirks and glaciated cirques of the Cabinet Mountains Wilderness to the high ridge passes of the Bitterroots and the dramatic summits of the Canadian Rockies.

Explore the interactive map below with highlighted regional boundaries, or select a mountain range from the guide table to view detailed trail statistics, directions, geology, and weather alerts.

---

## Interactive Regional Map with Highlighted Hiking Areas

Click any highlighted region or map marker to inspect local mountain highlights and open the regional guidebook.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="hiking-regions-map" style="width: 100%; height: 550px; border-radius: 12px; margin-top: 1rem; margin-bottom: 2rem; border: 1px solid var(--md-default-foreground-color--lightest, #ccc); box-shadow: 0 4px 14px rgba(0,0,0,0.12); z-index: 1;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  if (typeof L === 'undefined') return;

  var map = L.map('hiking-regions-map').setView([48.3, -115.8], 7);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var regions = [
    {
      name: "American Selkirks",
      link: "american-selkirks.md",
      desc: "Granite spires, Priest Lake basin & Harrison Peak",
      color: "#00BCD4",
      center: [48.55, -116.65],
      bounds: [[48.30, -116.95], [48.95, -116.95], [48.95, -116.25], [48.30, -116.25]]
    },
    {
      name: "Cabinet Mountains Wilderness",
      link: "blog/posts/34-cabinet-mountain-wilderness.md",
      desc: "Glaciated wilderness peaks & alpine lakes",
      color: "#10B981",
      center: [48.15, -115.65],
      bounds: [[47.90, -115.95], [48.45, -115.95], [48.45, -115.35], [47.90, -115.35]]
    },
    {
      name: "Proposed Scotchman Peaks",
      link: "blog/posts/blog-58-proposed-scotchman-peak-wilderness.md",
      desc: "Scotchman Peak (7,709') & steep vertical ridges",
      color: "#F59E0B",
      center: [48.20, -116.05],
      bounds: [[48.08, -116.22], [48.32, -116.22], [48.32, -115.92], [48.08, -115.92]]
    },
    {
      name: "Bitterroot Mountains",
      link: "bitterroots.md",
      desc: "St. Joe River headwaters & Silver Valley crest",
      color: "#6366F1",
      center: [47.10, -115.35],
      bounds: [[46.80, -115.75], [47.48, -115.75], [47.48, -114.95], [46.80, -114.95]]
    },
    {
      name: "Canadian Rockies & Bugaboos",
      link: "canada.md",
      desc: "Fisher Peak, Creston Valley & Bugaboos",
      color: "#8B5CF6",
      center: [50.50, -116.70],
      bounds: [[49.40, -117.30], [51.10, -117.30], [51.10, -115.60], [49.40, -115.60]]
    },
    {
      name: "Glacier National Park",
      link: "glacier-np.md",
      desc: "Highline trail & Continental Divide passes",
      color: "#06B6D4",
      center: [48.65, -113.80],
      bounds: [[48.35, -114.25], [49.00, -114.25], [49.00, -113.35], [48.35, -113.35]]
    },
    {
      name: "Spokane Regional Trails",
      link: "spokane-county-conservation-futures.md",
      desc: "Conservation Futures & Scabland trail networks",
      color: "#F43F5E",
      center: [47.65, -117.40],
      bounds: [[47.40, -117.65], [47.85, -117.65], [47.85, -117.15], [47.40, -117.15]]
    }
  ];

  regions.forEach(function(r) {
    // Highlighted region polygon
    var poly = L.polygon(r.bounds, {
      color: r.color,
      weight: 2,
      fillColor: r.color,
      fillOpacity: 0.22
    }).addTo(map);

    var popupHtml = '<div style="font-family: inherit; font-size: 0.9rem;"><strong><a href="' + r.link + '">' + r.name + '</a></strong><br><span style="font-size: 0.8rem; color: #555;">' + r.desc + '</span></div>';

    poly.bindPopup(popupHtml);

    // Marker pin at center
    var marker = L.marker(r.center).addTo(map);
    marker.bindPopup(popupHtml);
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
