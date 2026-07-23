import os
import glob
import re
import urllib.parse

DOCS_DIR = "docs"

def fix_assets():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    
    # Regex to match any markdown links: [text](url) or ![alt](url)
    link_pattern = re.compile(r'!?\[([^\]]*)\]\(([^)]+)\)')
    
    # Regex to match cdn-cgi email links (including those with spaces/titles if any)
    email_pattern = re.compile(r'!?\[([^\]]*)\]\(/cdn-cgi/l/email-protection[^)]+\)')
    abs_email_pattern = re.compile(r'href="/cdn-cgi/l/email-protection[^"]+"')
    
    fixed_imgs = 0
    fixed_emails = 0
    
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Check links
        def link_repl(match):
            nonlocal fixed_imgs
            url_with_title = match.group(2)
            
            # Split off title if present (e.g. `assets/image.jpg "My Title"`)
            url = url_with_title.split()[0]
            
            # We only care about links pointing to image files
            if not any(url.lower().split("?")[0].endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]):
                return match.group(0)
                
            if url.startswith("http://") or url.startswith("https://") or url.startswith("data:"):
                return match.group(0)
                
            clean_url = url.split("?")[0].split("#")[0]
            
            if clean_url.startswith("/"):
                asset_path = os.path.join(DOCS_DIR, clean_url.lstrip("/"))
            else:
                file_dir = os.path.dirname(filepath)
                asset_path = os.path.join(file_dir, clean_url)
                
            asset_path = urllib.parse.unquote(asset_path)
            
            if not os.path.exists(asset_path):
                fixed_imgs += 1
                return f"<!-- Missing Image: {match.group(0)} -->"
            
            return match.group(0)
            
        content = link_pattern.sub(link_repl, content)

        # Fix Emails
        def email_repl(match):
            nonlocal fixed_emails
            fixed_emails += 1
            return "[Email Protected]"
            
        def html_email_repl(match):
            nonlocal fixed_emails
            fixed_emails += 1
            return 'href="mailto:protected@example.com"'

        content = email_pattern.sub(email_repl, content)
        content = abs_email_pattern.sub(html_email_repl, content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                
    print(f"Fixed {fixed_imgs} missing images.")
    print(f"Fixed {fixed_emails} email protection links.")

if __name__ == "__main__":
    fix_assets()
