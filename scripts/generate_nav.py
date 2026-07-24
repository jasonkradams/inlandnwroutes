import os
import glob
import yaml

DOCS_DIR = "docs"

# Files that are already explicitly managed
EXCLUDED = {
    "index.md",
    "blog.md",
    "14-essentials.md",
    "about-us.md",
    "contact.md",
    "liability-release.md",
    "biography--chic.md",
    "biography--david.md",
}

def get_title(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    
    # Fallback to filename formatting
    basename = os.path.basename(filepath).replace(".md", "")
    return basename.replace("-", " ").title()

def categorize(filepath):
    filename = os.path.basename(filepath).lower()
    title = get_title(filepath).lower()

    # Blog posts must win regardless of what their title talks about (e.g. a
    # post titled "Stevens Lakes Peak Massive Avalanche" is still a blog post,
    # not a lake guide) -- check this before any topic keyword.
    if filepath.startswith(os.path.join(DOCS_DIR, "blog", "posts") + os.sep):
        return "Blog Archive"
    if any(k in filename or k in title for k in ["blog-", "newsletter"]):
        return "Blog Archive"

    # Search keywords
    if any(k in filename or k in title for k in ["lake", "pond", "reservoir"]):
        return "Lakes"
    if any(k in filename or k in title for k in ["peak", "mountain", "ridge", "crest", "summit", "dome"]):
        return "Peaks & Mountains"
    if any(k in filename or k in title for k in ["ski", "resort", "nordic", "snow"]):
        return "Winter & Skiing"
    if any(k in filename or k in title for k in ["fall"]):
        return "Waterfalls"
    if any(k in filename or k in title for k in ["paddle", "kayak", "canoe", "boat", "launch", "river", "bay"]):
        return "Paddling & Rivers"
    if filepath.startswith(os.path.join(DOCS_DIR, "store")):
        return "Store"
    if any(k in filename or k in title for k in ["wildflower", "flora", "plant", "lily", "moss", "tree"]):
        return "Flora & Wildlife"
    
    return "Trails & Scrambles"

def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    
    categories = {
        "Peaks & Mountains": [],
        "Lakes": [],
        "Waterfalls": [],
        "Paddling & Rivers": [],
        "Winter & Skiing": [],
        "Flora & Wildlife": [],
        "Trails & Scrambles": [],
        "Store": [],
        "Blog Archive": []
    }
    
    for filepath in md_files:
        rel_path = os.path.relpath(filepath, DOCS_DIR)
        
        # Skip excluded files
        if rel_path in EXCLUDED or rel_path == "blog-index.md":
            continue
            
        cat = categorize(filepath)
        title = get_title(filepath)
        categories[cat].append({title: rel_path})
        
    # Sort files within categories by title
    for cat in categories:
        categories[cat] = sorted(categories[cat], key=lambda x: list(x.keys())[0])

    # Build the nav dictionary to match MkDocs format
    nav_structure = []
    
    # Add explicit base nav items
    nav_structure.append({"Home": "index.md"})
    nav_structure.append({"Blog": "blog/index.md"})
    
    # Add generated categories (omit empty ones)
    for cat in sorted(categories.keys()):
        if categories[cat]:
            nav_structure.append({cat: categories[cat]})
            
    nav_structure.append({"14+ Essentials": "14-essentials.md"})
    nav_structure.append({"About": [
        {"Biography :: Chic": "biography--chic.md"},
        {"Biography :: David": "biography--david.md"},
        {"About Us": "about-us.md"},
        {"Contact": "contact.md"},
        {"Liability Release": "liability-release.md"},
    ]})

    # Output as YAML
    print("nav:")
    print(yaml.dump(nav_structure, sort_keys=False, indent=2, allow_unicode=True))

if __name__ == "__main__":
    main()
