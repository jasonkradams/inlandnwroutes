import os
import shutil

INDEX_MAP = {
    'Blog': ('blog-index.md', 'blog/index.md'),
    'Lakes': ('lakes.md', 'lakes/index.md'),
    'Paddling & Rivers': ('paddle.md', 'paddle/index.md'),
    'Peaks & Mountains': ('mountains.md', 'mountains/index.md'),
    'Trails & Scrambles': ('trails.md', 'trails/index.md'),
    'Waterfalls': ('waterfalls.md', 'waterfalls/index.md'),
    'Winter & Skiing': ('ski.md', 'ski/index.md'),
}

# Move files
for section_name, (old_file, new_file) in INDEX_MAP.items():
    old_path = os.path.join('docs', old_file)
    new_path = os.path.join('docs', new_file)
    
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Moved {old_path} to {new_path}")
    else:
        print(f"Not found: {old_path}")

# Rewrite mkdocs.yml
with open('mkdocs.yml', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    replaced = False
    
    if "- Blog Index: blog-index.md" in line:
        new_lines.append(line.replace("- Blog Index: blog-index.md", "- blog/index.md"))
        replaced = True
    elif "- Blog: blog-index.md" in line:
        new_lines.append(line.replace("- Blog: blog-index.md", "- blog/index.md"))
        replaced = True
    elif "- blog-index.md" in line:
        new_lines.append(line.replace("- blog-index.md", "- blog/index.md"))
        replaced = True
        
    elif "- Lakes: lakes.md" in line:
        new_lines.append(line.replace("- Lakes: lakes.md", "- lakes/index.md"))
        replaced = True
    
    elif "- Paddle: paddle.md" in line:
        new_lines.append(line.replace("- Paddle: paddle.md", "- paddle/index.md"))
        replaced = True
        
    elif "- Mountains: mountains.md" in line:
        new_lines.append(line.replace("- Mountains: mountains.md", "- mountains/index.md"))
        replaced = True
        
    elif "- Trails: trails.md" in line:
        new_lines.append(line.replace("- Trails: trails.md", "- trails/index.md"))
        replaced = True
        
    elif "- Waterfalls: waterfalls.md" in line:
        new_lines.append(line.replace("- Waterfalls: waterfalls.md", "- waterfalls/index.md"))
        replaced = True
        
    elif "- Ski: ski.md" in line:
        new_lines.append(line.replace("- Ski: ski.md", "- ski/index.md"))
        replaced = True
        
    if not replaced:
        new_lines.append(line)

with open('mkdocs.yml', 'w') as f:
    f.writelines(new_lines)

print("Updated mkdocs.yml")
