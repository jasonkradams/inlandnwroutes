import os

content = """---
title: Chicken & Rice Soup
tags:
  - Recipes
  - Soups
  - Trail Meals
stats:
  - "Author": "Chic Burge"
  - "Prep Time": "30 mins"
  - "Cook Time": "4-12 hrs (Broth) + 30 mins"
  - "Yield": "1-2 Gallons (Canning friendly)"
---

A hearty, flavorful homemade chicken and rice soup featuring slow-simmered chicken stock, broiled sweet peppers, okra, and served alongside broiled garlic French bread. Perfect for canning or packing on cold mountain hikes!

!!! tip "Homemade Stock Is Key"

    Do **not** use store-bought chicken broths. The rich flavor comes entirely from slow-boiling the rotisserie chicken bones for several hours (or overnight).

!!! info "Grandmother's Dishwashing Tradition"

    As Chic's grandmother used to say: *"The person who gets the bay leaf does all the dishes!"* Since this recipe includes three bay leaves, you might just have some help in the kitchen.

---

## Ingredients

### Main Soup Ingredients

- **Rotisserie Chicken:** 1 large chicken (deboned; meat reserved)
- **Rice:** Basmati rice (cooked separately to your preference)
- **Sweet Peppers:** 5–6 sweet peppers
- **Onions:** 1 white onion, 1 red onion, and 3 sprigs of salad (green) onions
- **Celery:** 6 stalks
- **Okra:** ½ bag frozen cut okra (or 1 full bag for okra lovers)
- **Aromatics:** 3 bay leaves, plus additional herbs/spices as desired
- **Water:** Ample water for long broth simmering

### Garlic Butter French Bread

- **French Bread:** 1 fresh loaf (sliced French style)
- **Garlic Butter:** Butter or oleo, salt, black pepper, and garlic powder
- **Cheese:** Optional addition for serving on the trail

---

## Instructions

### Step 1: Prepare the Rich Chicken Stock

1. **Debone Chicken:** Debone the rotisserie chicken. Place the meat in a storage bag and refrigerate for later assembly.
2. **Slow Boil Bones:** Place all remaining chicken parts and bones into a large pot of boiling water.
3. **Simmer:** Bring to a hard boil, then reduce heat to a slow boil for 4 hours up to overnight. The longer you slow-boil the bones, the richer the broth.
4. **Maintain Water Level:** Stir occasionally and add water as needed to ensure it does not boil off.
5. **Strain:** After boiling, remove solid bones and strain the broth through cheesecloth to remove any semi-solids.

### Step 2: Prepare & Broil the Sweet Peppers

1. **Slice Peppers:** Cut the sweet peppers into thirds lengthwise. Remove seeds and white veins *(keep the veins if you prefer a spicier soup)*.
2. **Season & Broil:** Brush pepper pieces with olive oil and sprinkle with salt, black pepper, and garlic powder.
3. **Char Skins:** Broil inside-first until skins are lightly charred *(take care not to burn the flesh; omit broiling if making a spicier soup)*.
4. **Peel & Chop:** Let cool, peel off the charred skins, and slice into ½" x 2" pieces.

### Step 3: Cook the Soup

1. **Prep Veggies:** Cut the white onion, red onion, green onions, and celery into ½" x 2" pieces.
2. **Combine Ingredients:** Add the chopped vegetables, cut sweet peppers, frozen okra, bay leaves, and reserved chicken meat into the strained stock.
3. **Simmer to Preference:**
   - *For crispier vegetables:* Simmer for a short duration.
   - *For tender/softer vegetables:* Simmer for ~1 hour.
   - *Note on Seasoning:* Taste test as you cook. Chic recommends adding salt and pepper at the table rather than in the pot to avoid over-salting.
4. **Add Cooked Rice:** Cook the Basmati rice separately to near-done, then add the rice to the soup pot during the final 30+ minutes of cooking.

### Step 4: Garlic Butter French Bread

1. **Make Garlic Butter:** In a bowl, blend butter (or oleo) with salt, black pepper, and garlic powder using a fork. Chill in the refrigerator.
2. **Spread & Broil:** Coat slices of fresh French bread generously with the garlic butter. Broil butter-side up until lightly golden brown just before serving.
3. **Keep Warm:** Serve immediately in a bread bowl lined with a clean kitchen towel to retain heat.

---

## Canning & Trail Tips

!!! note "Canning for Future Meals"

    - Yields 1 to 2 gallons. Pour hot soup into clean, wide-mouth canning jars.
    - Leave jars on the counter until you hear the vacuum seal lids "snap" down.
    - Check seals by pressing down in the center of the lid. If firm and down, store in the refrigerator.
    - **Safety:** Allow jars to cool before refrigerating to prevent thermal shock and breakage. Properly sealed jars keep in the refrigerator for over a month.

!!! note "On the Trail"

    On cool hiking days, pack the soup in a jar and bring a camp stove. Reheat the soup on the trail, fry the garlic bread butter-side down in a pan, and top with optional cheese for an incredible mountain meal!
"""

with open("docs/recipes/soups/chicken-and-rice-soup.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized chicken-and-rice-soup.md successfully")
