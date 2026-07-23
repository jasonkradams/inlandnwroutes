import os
import glob

DOCS_DIR = "docs"

def fix_fucked_links():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    
    count = 0
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # 1. Fix the index.mdassets issue caused by fix_links.py replacing /assets
        content = content.replace('index.mdassets/', '/assets/')
        
        # 2. Fix the missing https: protocol for links to inlandnwroutes.com
        content = content.replace('href="//www.inlandnwroutes.com', 'href="https://www.inlandnwroutes.com')
        content = content.replace('](//www.inlandnwroutes.com', '](https://www.inlandnwroutes.com')
        
        # 3. Check for any other index.md prefix blunders and fix them
        # Sometimes fix_links might have changed `](/something)` to `](index.mdsomething)`
        # But wait, it did `index.md\2` where \2 was `#anchor` or `path`.
        # For `/assets` it became `index.mdassets`. For `/blog` it became `index.mdblog`.
        content = content.replace('index.mdblog/', '/blog/')
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
    print(f"Fixed {count} files that got messed up.")

if __name__ == "__main__":
    fix_fucked_links()
