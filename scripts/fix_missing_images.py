import os
import re
import time
import requests
from pathlib import Path

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match: [*(Image missing)*](URL "TITLE") or without title
    # Example: [*(Image missing)*](https://www.inlandnwroutes.com/uploads/7/9/2/5/79257998/12192021825p_orig.jpeg "LAKE ESTELLE, IDAHO")
    # Using re.sub with a replacement function
    
    # regex pattern
    pattern = r'\[\*\s*\(Image missing\)\s*\*\]\((https?://[^)]+\.(?:jpg|jpeg|png|gif|webp))(?: "([^"]*)")?\)'
    
    # We will keep track if the file changed
    changed = False
    
    def replacer(match):
        nonlocal changed
        url = match.group(1)
        title = match.group(2) or "Image"
        
        filename = os.path.basename(url)
        # some urls might have query parameters, let's clean it up
        filename = filename.split('?')[0]
        
        # Where to save
        assets_dir = Path('docs/assets/images')
        assets_dir.mkdir(parents=True, exist_ok=True)
        
        save_path = assets_dir / filename
        
        # Download if it doesn't exist
        if not save_path.exists():
            print(f"Downloading {filename}...")
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    with open(save_path, 'wb') as img_f:
                        img_f.write(response.content)
                    time.sleep(0.5) # Be nice to the server
                else:
                    print(f"Failed to download {url}: {response.status_code}")
                    return match.group(0) # Keep original if failed
            except Exception as e:
                print(f"Error downloading {url}: {e}")
                return match.group(0)
        
        # Return new markdown image tag
        changed = True
        return f'![Image](/assets/images/{filename}){{: data-src="/assets/images/{filename}" data-title="{title}" }}'
    
    new_content = re.sub(pattern, replacer, content)
    
    # Also handle <!-- Missing Image: [*(Image missing)*](URL) -->
    # Sometimes it's wrapped in HTML comments. If so, strip the comment.
    comment_pattern = r'<!-- Missing Image:\s*(.*?)-->'
    def comment_replacer(match):
        inner = match.group(1).strip()
        if inner.startswith('![Image]'): # Already replaced by previous step!
            return inner
        elif inner.startswith('[*(Image missing)*]'):
            # It's an unreplaced one (failed download, etc.)
            return match.group(0)
        return inner # Return stripped just in case it was successfully processed
    
    new_content2 = re.sub(comment_pattern, comment_replacer, new_content)
    if new_content2 != new_content:
        changed = True
        new_content = new_content2

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

if __name__ == '__main__':
    import sys
    import glob
    
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        # Recursively find all md files in docs/
        files = []
        for path in Path('docs').rglob('*.md'):
            files.append(str(path))
            
    for f in files:
        process_file(f)
