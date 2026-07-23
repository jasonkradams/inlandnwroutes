import re
from pathlib import Path

def fix_glightbox(directory):
    # Matches [![alt](src)](href "title")
    pattern = re.compile(r'\[!\[(.*?)\]\((.*?)\)\]\((.*?)\)', re.DOTALL)
    
    docs_dir = Path(directory)
    count = 0
    file_count = 0
    for md_file in docs_dir.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def repl(match):
            alt = match.group(1)
            src = match.group(2)
            outer = match.group(3).strip()
            
            # Split outer link into href and optional title
            # Example: href="https://.../img.jpg" title="My Title"
            # In markdown: url "title"
            parts = outer.split(' "', 1)
            href = parts[0]
            title_part = ""
            if len(parts) > 1:
                title_part = ' "' + parts[1]
            # Handle newlines in the title_part by converting to <br> or just stripping?
            # Actually, we should just let the title have newlines, but we want the attr_list on one line ideally,
            # or we can replace newlines with a space in the title.
            clean_title_part = title_part.replace('\n', ' ')
            
            return f'![{alt}]({src}{clean_title_part}){{: data-src="{href}" }}'
            
        new_content, num_subs = pattern.subn(repl, content)
        
        if num_subs > 0:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {num_subs} glightbox image links in {md_file.relative_to(docs_dir)}")
            count += num_subs
            file_count += 1
            
    print(f"Total images fixed: {count} in {file_count} files")

if __name__ == '__main__':
    fix_glightbox('docs')
