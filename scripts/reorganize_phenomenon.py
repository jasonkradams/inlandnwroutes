import os

content = """---
title: "Atmospheric Phenomena"
tags:
  - Gallery
  - Atmospheric Phenomena
  - Weather
  - Brocken Spectre
---

Certain atmospheric and meteorological phenomena produce awe-inspiring optical effects in the high mountains of the Inland Northwest and across the globe.

!!! tip "Weird Weather Reference"

    Explore more unusual weather phenomena at the [NOAA Weird Weather Guide](https://www.weather.gov/owlie/weird-weather).

---

## Brocken Spectre & Glory

![Brocken Spectre and Glory Image by Chris Herath](../../assets/images/122220211150a.jpg)
_Brocken Spectre and Glory photo captured by Chris Herath showing an enlarged shadow cast onto underlying mountain clouds surrounded by a rainbow halo._

### Optical Physics of the Glory

A **Glory** is an atmospheric optical effect that casts a brilliant rainbow halo around the head of an observer's shadow. The conditions required to witness a glory are best in high mountain environments, tall ridgelines, or aircraft when the observer stands above a cloud or fog layer with the sun directly behind them.

Glories appear when sunlight hits tiny, uniform water droplets that compose clouds or fog. The light refracts and diffraction scatters the colors into concentric circles around the observer's shadow, similar to a compact, circular rainbow.

### The Legend of the Brocken Spectre

When a glory surrounds an observer's shadow projected against underlying clouds, the resulting illusion is called a **Brocken Spectre** (named after the Brocken peak in the Harz Mountains of Germany).

Because the shadow is cast onto cloud droplets at varying distances, depth perception is distorted. The light exaggerates the shadow's scale, making the observer appear gigantic and long-limbed. As wind shifts the cloud droplets, the shadow appears to move independently, creating an eerie effect that fueled mountain folklore and alpine superstitions for centuries.
"""

with open("docs/gallery/categories/phenomenon.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized phenomenon.md successfully")
