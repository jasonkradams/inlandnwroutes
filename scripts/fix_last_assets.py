import os
import glob
import re

DOCS_DIR = "docs"

def fix_last():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**", "*.md"), recursive=True)
    
    # Catch any cdn-cgi link
    email_pattern = re.compile(r'\[[^\]]*\]\]?\(/cdn-cgi/l/email-protection[^\)]*\)')
    email_pattern2 = re.compile(r'\[[^\]]*\]\(/cdn-cgi/l/email-protection[^\)]*\)')
    
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        content = re.sub(email_pattern, "[Email Protected]", content)
        content = re.sub(email_pattern2, "[Email Protected]", content)
        
        # Missing images
        content = content.replace("assets/images/21540034.jpg", "missing-image.jpg")
        content = content.replace("assets/images/112026418p.jpg", "missing-image.jpg")
        content = content.replace("assets/images/112026415p.jpg", "missing-image.jpg")
        content = content.replace("assets/images/2112021859.jpg", "missing-image.jpg")
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                
    print("Fixed last assets.")

if __name__ == "__main__":
    fix_last()
