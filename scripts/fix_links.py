import os
import glob
import re

DOCS_DIR = "docs"

def fix_links():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    
    # Regex to match markdown links: [text](/page.html) or [text](/page.html#anchor)
    md_link_pattern = re.compile(r'\]\(/([^)]+)\.html(#?[^)]*)\)')
    
    # Regex to match absolute links to root: [text](/ )
    md_root_link = re.compile(r'\]\((/)(#?[^)]*)\)')

    count = 0
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Replace ](/page.html) with ](page.md)
        content = md_link_pattern.sub(r'](\1.md\2)', content)
        
        # Replace ](/) with ](index.md)
        content = md_root_link.sub(r'](index.md\2)', content)
        
        # Some links might be plain href="/page.html" inside HTML tags
        content = re.sub(r'href="/([^"]+)\.html"', r'href="\1.md"', content)
        content = re.sub(r'href="/"', r'href="index.md"', content)
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
    print(f"Fixed links in {count} files.")

if __name__ == "__main__":
    fix_links()
