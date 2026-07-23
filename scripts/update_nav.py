import os

with open("mkdocs.yml", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "nav:":
        break
    new_lines.append(line)

new_nav = """validation:
  nav:
    omit: warn

nav:
  - Home: index.md
  - Blog: blog.md
  - 14+ Essentials: 14-essentials.md
  - About:
      - 'Biography :: Chic': biography--chic.md
      - 'Biography :: David': biography--david.md
      - 'About Us': about-us.md
      - 'Contact': contact.md
      - 'Liability Release': liability-release.md
"""

new_lines.append(new_nav)

with open("mkdocs.yml", "w") as f:
    f.writelines(new_lines)
