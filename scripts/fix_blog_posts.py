import os
import glob

def fix_blog_posts():
    blog_dir = "docs"
    md_files = glob.glob(os.path.join(blog_dir, "**", "*.md"), recursive=True)
    
    # Filter out directories and files that don't look like they have the text
    md_files = [f for f in md_files if os.path.isfile(f)]
    
    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        modified = False
        new_lines = []
        
        for i, line in enumerate(lines):
            # Fix main title
            if i < 5 and line.startswith("## ["):
                new_lines.append(line.replace("## [", "# [", 1))
                modified = True
            # Fix huge body text trapped in H2
            elif line.startswith("## ") and len(line) > 100:
                # Strip the `## ` prefix
                new_lines.append(line[3:])
                modified = True
            # Fix Leave a reply
            elif line.startswith("## Leave a Reply"):
                new_lines.append(line.replace("## ", "### ", 1))
                modified = True
            else:
                new_lines.append(line)
                
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

if __name__ == "__main__":
    fix_blog_posts()
