import os

content = """---
title: Outdoor Poems & Verses
tags:
  - Writings
  - Poems
  - Silver Mountain
---

A collection of outdoor poems, ski verses, and creative trail-name wordplay compiled by Chic Burge and contributors to InlandNWroutes.

!!! info "Submissions Welcome"

    We encourage readers, skiers, and trail wanderers to share their own poems and writings on human-powered sports. Please keep submissions clean and concise.

---

## Trail & Mountain Verses

!!! quote "Out on the Trail"

    Out on the trail as miles go by,
    The hills and valleys touch the azure sky.
    The creeks run cold and clear all through the year,
    Beautiful lakes dot the terrain and are fed by an occasional rain.
    Above the sparkling lakes on magnificent ridge lines,
    Is where we can be found looking for a place to dine.

    — **Chic Burge** *(November 25, 2011)*

!!! quote "Spice"

    The plural of mouse is mice,
    So the plural of spouse should be spice,
    And that’s all I’m discussing about this.

    — **@wordesse**

!!! quote "Clear as a Whistle"

    There's something special about a day as clear as a whistle.
    The cold kept the snow so skiable it was unbelievable.
    The rush of the shush turns our knees to mush,
    But we can't stop until we are on top.
    Our addiction runs deep when we are in the steep.
    As the day comes to an end, I hope my knees can still bend.
    But nonetheless, there will be another day—or else.

    — **Chic Burge** *(February 5, 2017)*

---

## Silver Mountain Ski Epics

!!! quote "Silver Mountain: A Skiing Epic"

    Riding the Gondola gives us rise and opens up our eyes.
    As it speeds along its string, the snow-covered trees sparkle and sing.
    The Mountain Haus sits high, up above in the sky,
    But the snow calls my name—after all, it's why I came.

    Soon South of the Border was in order,
    Crankin' down through the ancient trees does everything but tease.
    The powder is deep, and the runs are steep;
    The challenge of South of the Border is the traverse we all call a son of a B.

    Secret Trees, of course, are next, with trees and cold smoke making it the best.
    As we shush down Sunrise, the Road to Heaven catches our eyes;
    A drop down through the fluff is just the right stuff.

    Around Skyway Ridge to Chair 4 we go, looking for just the right snow.
    We find it along the Wardner Traverse, where 16 to 1 is our course.
    The float down through the pow causes lots of yahoos and a wow!
    Gold completes the run—it's all great fun.

    Marsha's Edge awaits, so up we go, we can't wait!
    Up and down we go on Chair 4, looking for pow and so much more.
    Chair 3 shines in the sun and offers so much fun,
    But it is time for lunch, because we are a hungry bunch.

    Paymaster Trees stand out afar and call us to raise the bar.
    Screamin' down Centennial gets us to the right trail;
    Collateral, under Chair 3, has a face that's the place to ski.
    But the high dry terrain calls, so up Chair 2 we haul our gear.

    Rock Garden directs us to SOB's Prow which is untouched—the way we love it so much.
    Once on top, Quicksilver leads us to Why Not, so why not?
    Silverbelt takes us to the North Star trees, and they are sure to please.
    As we ski past Steep and Deep, it draws us down through the deep and steep fluffy down.

    With the need to be high, crankin' down through Heaven gets high in the sky.
    And as the day draws to a close, I follow my nose:
    Shady Lady with its untracked snow is definitely the way to go.
    As we ride the Gondola down, there is not a face with a frown.
    We sit quietly, exhausted, admiring the mountain as we plan our next trip to Silver Mountain.

    *(Secret Trees and Marsha's Edge are local designations for favorite unnamed runs.)*

    — **Chic Burge** *(January 26, 2017)*

!!! quote "Skiing in Heaven at Silver Mountain"

    A day of skiing at Silver is like skiing in **Heaven**.
    You don't need **Collateral** to ski the **Steep and Deep**.
    Just the **North Star** to guide you.
    You will experience **Sheer Bliss** as you shush the **Solitude** of **Wardner Peak**.

    You won't get the **Shaft** from a **Shady Lady**, a **Bootlegger**, or any other **Jackass**.
    Eureka! There's **Gold** in them thar hills!
    But you will not find a **Claim Jumper** unless you look closely.
    However, you may find a **Corkscrew** or two in **Moguls** bar.

    **16 to 1** you will find **Heaven**, and you don't need **Collateral** or a **Silverbelt** to enjoy a **Sunrise** or a **Sunset**.
    You won't find **Terrible Edith** in the **Meadows**, or a **Fast Eddy** like **Tall Paul** on the **Ridge**.
    But you will find, if you look closely, **Northern Lights**, a **Happy Jack**, and a **Silver Basin** filled with pow.

    So **Why Not** **Rendezvous** with a **Gem**, and don't just go **Home James**—go to **Silver Mountain**!
    And don't forget the **Snow Tubing Hill** or the **Magic Carpet** beginners hill.
    You don't need a **Paymaster** to ski at Silver, nor do you need **Gold**.
    All you need to **Get There** is your addiction to powder.

    After you have worn yourself out, **Silver Rapids Waterpark** can soothe those sore muscles before you retire to your **Village** condo.
    So load up that old **Saddleback** car of yours and set your **T2D2** navigation system east to **Silver Mountain**!

    — **Chic Burge** *(January 26, 2017)*
"""

with open("docs/writings/poems.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Reorganized poems.md as series of quote admonitions successfully")
