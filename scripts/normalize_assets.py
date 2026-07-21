#!/usr/bin/env python3
import os
import re
import urllib.parse

DOCS_DIR = "docs"
ASSETS_DIR = os.path.join(DOCS_DIR, "assets", "images")

def normalize_name(filename):
    """
    Normalizes asset filenames:
    - Removes URL parameters if they got saved (e.g. ?1669956683)
    - Lowercase
    - Removes '_orig'
    - Replaces spaces and dashes with underscores (or vice versa, let's use dashes for web)
    """
    # Remove query string if somehow saved
    name = filename.split('?')[0]
    
    # Split ext
    base, ext = os.path.splitext(name)
    
    # Normalize base
    base = base.lower()
    base = base.replace("_orig", "")
    base = base.replace("_", "-")
    base = re.sub(r'[^a-z0-9\-]', '', base) # remove special chars
    
    # Deduplicate dashes
    base = re.sub(r'\-+', '-', base).strip('-')
    
    if not base:
        base = "image"
        
    ext = ext.lower()
    if ext == '.jpeg':
        ext = '.jpg'
        
    return base + ext

def main():
    if not os.path.exists(ASSETS_DIR):
        print(f"{ASSETS_DIR} does not exist. Nothing to normalize.")
        return

    # Map old name to new name
    rename_map = {}
    
    for filename in os.listdir(ASSETS_DIR):
        if filename.startswith('.'):
            continue
            
        old_path = os.path.join(ASSETS_DIR, filename)
        if not os.path.isfile(old_path):
            continue
            
        new_filename = normalize_name(filename)
        
        # Handle collisions
        base, ext = os.path.splitext(new_filename)
        counter = 1
        final_new_filename = new_filename
        while final_new_filename in rename_map.values() and filename not in rename_map:
            final_new_filename = f"{base}-{counter}{ext}"
            counter += 1
            
        if filename != final_new_filename:
            new_path = os.path.join(ASSETS_DIR, final_new_filename)
            os.rename(old_path, new_path)
            # URL decoding for matching in markdown (scraper might have URL encoded names or unencoded)
            rename_map[filename] = final_new_filename
            print(f"Renamed: {filename} -> {final_new_filename}")

    if not rename_map:
        print("No files needed renaming.")
        return

    # Now update markdown files
    md_files = [f for f in os.listdir(DOCS_DIR) if f.endswith('.md')]
    for md_file in md_files:
        md_path = os.path.join(DOCS_DIR, md_file)
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        changed = False
        for old_name, new_name in rename_map.items():
            # Match paths exactly to avoid partial replacements
            # e.g. /assets/images/old_name
            # Need to be careful with URL encoding
            old_name_encoded = urllib.parse.quote(old_name)
            
            # Replace unencoded
            if f"/assets/images/{old_name}" in content:
                content = content.replace(f"/assets/images/{old_name}", f"assets/images/{new_name}")
                changed = True
            
            # Replace encoded
            if f"/assets/images/{old_name_encoded}" in content:
                content = content.replace(f"/assets/images/{old_name_encoded}", f"assets/images/{new_name}")
                changed = True
                
            # Also fix the outer link hrefs pointing to weebly uploads if they match the old name
            # e.g. ](/uploads/7/9/2/5/79257998/dsc0595_orig.jpg "Title")
            # We will just blindly replace any /uploads/.../old_name with the new relative path
            # This uses a simple regex.
            weebly_pattern = r'\]\(/uploads/[^\s)]+/' + re.escape(old_name)
            if re.search(weebly_pattern, content):
                content = re.sub(weebly_pattern, f"](assets/images/{new_name}", content)
                changed = True

        # Ensure no absolute paths are left for local markdown previews
        if "/assets/images/" in content:
            content = content.replace("/assets/images/", "assets/images/")
            changed = True

        if changed:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated references in {md_file}")

if __name__ == "__main__":
    main()
