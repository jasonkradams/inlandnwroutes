import os

content = """---
title: Chicken Mushroom Mashed Potato Soup
tags:
  - Recipes
  - Soups
  - Main Dishes
stats:
  - label: Author
    value: Chic Burge
  - label: Prep Time
    value: 15 mins
  - label: Cook Time
    value: 30 mins
  - label: Skill Level
    value: Quick & Easy
---

A quick, comforting, and hearty dish featuring seasoned chicken, sautéed mushrooms, and green onions in a rich homemade chicken gravy, served poured over smooth mashed potatoes.

!!! tip "Grandmother's Fail-Proof Gravy Technique"

    Chic's grandmother taught him this rule in the 1960s: **only add ice-cold water to flour in a shaker jar** when making gravy. Shake vigorously, then whisk into simmering broth. Only add seasonings, mushrooms, and chicken *after* the gravy thickens. It will never fail! For more details, see [Easy Quality Gravy](../brines-marinades-and-sauces/easy-quality-gravy.md).

---

## Ingredients

- **Chicken:** Baked chicken thighs and breasts (home-cooked or deli rotisserie; deboned with bones reserved)
- **Potatoes:** Organic potatoes
- **Mushrooms & Onions:** 4 button mushrooms (sliced), 2 sprigs of salad (green) onions (chopped), regular onion (optional)
- **Gravy Thickeners:** 1–2 inches of regular flour in a shaker jar + ice-cold water
- **Fats & Seasonings:** Butter or oleo (~1 oz for mashing + extra for frying veggies), salt, black pepper, garlic powder

---

## Instructions

### Step 1: Prepare the Broth & Chicken

1. **Debone Chicken:** Debone the chicken thighs and breasts. Reserve the meat for the final assembly.
2. **Boil Stock:** Place the chicken bones into a pot of water and boil to create a fresh chicken stock.
3. **Simmer Broth:** Remove all solid bones, strain the stock, and transfer 2–3 cups of broth into a large skillet or frying pan over medium heat.

### Step 2: Potatoes, Mushrooms & Onions

1. **Boil Potatoes:** Boil the organic potatoes until just tender *(do not over-boil to mush)*.
2. **Sauté Veggies:** In a separate pan, fry the sliced mushrooms and green onions in butter until soft.
3. **Mash Potatoes:** Drain the potatoes and mash with ~1 oz of butter (or oleo). **Do not add milk.**

!!! note "Breakfast Leftovers Tip"

    Always make extra mashed potatoes! In the morning, fry the leftover mashed potatoes in a skillet until crisp and top with a fried egg.

### Step 3: Make the Fail-Proof Gravy

1. **Flour Shaker Jar:** In a 6–8 oz jar with a tight-fitting lid, add 1–2 inches of regular flour.
2. **Ice-Cold Water:** Add ice-cold water to the jar, cap tightly, and shake thoroughly until smooth.
3. **Whisk & Thicken:** Slowly pour the cold flour-water mixture into the simmering chicken broth while whisking continuously with a fork until the gravy thickens.

### Step 4: Assemble & Serve

1. **Season & Combine:** Once the gravy sets up, add salt, black pepper, garlic powder, the fried mushrooms and onions, and the chopped chicken meat.
2. **Serve:** Divide warm mashed potatoes into medium glass bowls, ladle the rich chicken mushroom gravy generously over the top, and serve immediately!
"""

with open("docs/recipes/soups/chicken-mushroom-mashed-potato-soup.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized chicken-mushroom-mashed-potato-soup.md successfully")
