import json
from collections import defaultdict

with open("scratch/malformed_frontmatter_report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

by_category = defaultdict(list)

for item in data["malformed_files"]:
    path = item["file"]
    err = item["error"]
    
    if path.startswith("docs/hike/"):
        category = "Hike Guides"
    elif path.startswith("docs/paddle/"):
        category = "Paddle Guides"
    elif path.startswith("docs/waterfalls/"):
        category = "Waterfalls Guides"
    elif path.startswith("docs/wildflowers/"):
        category = "Wildflowers & Flora Guides"
    elif path.startswith("docs/ski/"):
        category = "Ski & Snowshoe Guides"
    else:
        category = "General / Index Pages"
        
    by_category[category].append((path, err))

print(f"=== SUMMARY OF MALFORMED FRONTMATTER ({data['total_malformed']} / {data['total_scanned']} files) ===\n")

for cat, items in sorted(by_category.items()):
    print(f"### {cat} ({len(items)} files)")
    for path, err in items:
        print(f"- [`{path}`]({path}): {err}")
    print()
