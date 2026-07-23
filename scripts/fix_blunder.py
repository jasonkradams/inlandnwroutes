import os
import glob

DOCS_DIR = "docs"

def fix_blunder():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    
    count = 0
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Revert the href="/" and `](/` blunders
        content = content.replace('index.mdcdn-cgi', '/cdn-cgi')
        content = content.replace('index.md/www.inlandnwroutes.com', '//www.inlandnwroutes.com')
        content = content.replace('index.mdblog/previous', '/blog/previous')

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            
    print(f"Fixed blunder in {count} files.")

if __name__ == "__main__":
    fix_blunder()
