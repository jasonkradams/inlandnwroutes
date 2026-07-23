import re
from pathlib import Path

def fix_captions(directory):
    # Matches ![alt](src "title"){: data-src="href" }
    # We want to extract the title and put it into data-title inside the attr_list
    # The title may contain newlines, so we use [\s\S] or re.DOTALL
    pattern = re.compile(r'!\[([^\]]*)\]\(([^)"]+)\s+"([^"]*)"\)\{: data-src="([^"]+)" \}', re.DOTALL)
    
    docs_dir = Path(directory)
    count = 0
    file_count = 0
    for md_file in docs_dir.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def repl(match):
            alt = match.group(1)
            src = match.group(2)
            title = match.group(3)
            href = match.group(4)
            
            # Escape quotes inside title if any, or just use single quotes for data-title if it contains double quotes?
            # Markdown attr_list usually accepts single or double quotes. If title has no double quotes (because it was extracted from double quotes), we are safe to use double quotes.
            # Convert newlines in title to HTML break or just leave them? 
            # Glightbox handles HTML in data-title. Let's just leave it, or replace newline with <br>.
            # Actually, let's keep the raw text, just strip extra whitespace.
            clean_title = title.strip().replace('\n', '<br>')
            
            return f'![{alt}]({src}){{: data-src="{href}" data-title="{clean_title}" }}'
            
        new_content, num_subs = pattern.subn(repl, content)
        
        if num_subs > 0:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {num_subs} captions in {md_file.relative_to(docs_dir)}")
            count += num_subs
            file_count += 1
            
    print(f"Total captions fixed: {count} in {file_count} files")

if __name__ == '__main__':
    fix_captions('docs')
