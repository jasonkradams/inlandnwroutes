#!/usr/bin/env python3
import os
import glob
import re

DOCS_DIR = 'docs'
all_md_files = sorted(glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True))

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # 1. Clean zero-width spaces and non-breaking spaces
    content = content.replace('\u200b', '').replace('\xa0', ' ')
    
    # 2. Normalize image paths relative to filepath
    rel_dir = os.path.relpath(os.path.dirname(filepath), DOCS_DIR)
    if rel_dir == '.':
        correct_prefix = 'assets/images/'
    else:
        depth = len(rel_dir.replace('\\', '/').split('/'))
        correct_prefix = ('../' * depth) + 'assets/images/'
    
    # Fix absolute or malformed image paths
    content = re.sub(r'(/|\.|\w)*/?assets/images/', correct_prefix, content)
    
    # Clean malformed data-src attributes inside image title quotes
    content = re.sub(r'\"([^\"]*)\{\:\s*data-src=[^\}]*\}', r'"\1"', content)
    
    # 3. Clean scraped web artifacts
    content = re.sub(r'##\s*\[[^\]]+\.html\]\(\)', '', content)
    content = re.sub(r'\[[^\]]+\.html\]\(\)', '', content)
    content = re.sub(r'\[<https://www\.inlandnwroutes\.com\]\(https://www\.inlandnwroutes\.com>/?\)', '', content)
    content = re.sub(r'https?://www\.inlandnwroutes\.com/uploads/\S+', '', content)
    content = re.sub(r'\[0\s*Comments\]', '', content, flags=re.IGNORECASE)
    content = re.sub(r'###\s*Leave a Reply\.?', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\[\[email\s*protected\]\]\(/cdn-cgi/l/email-protection\)', 'info@inlandnwroutes.com', content)
    content = re.sub(r'/cdn-cgi/l/email-protection', '', content)
    
    # 4. Clean trailing spaces (MD009)
    lines = [l.rstrip() for l in content.splitlines()]
    content = '\n'.join(lines)
    
    # 5. Heading blank line spacing (MD022)
    content = re.sub(r'([^\n])\n(#{1,6}\s+)', r'\1\n\n\2', content)
    content = re.sub(r'(#{1,6}\s+[^\n]+)\n([^\n#])', r'\1\n\n\2', content)
    
    # 6. List blank line spacing (MD032)
    content = re.sub(r'([^\n])\n(\s*[\*\-\+]\s+)', r'\1\n\n\2', content)
    content = re.sub(r'(\s*[\*\-\+]\s+[^\n]+)\n([^\n\*\-\+\s])', r'\1\n\n\2', content)
    
    # 7. Collapse multiple blank lines to max 2
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Ensure newline at EOF
    if not content.endswith('\n'):
        content += '\n'
        
    return content

modified = 0
for filepath in all_md_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
        orig = fp.read()
    new_c = process_file(filepath)
    if new_c != orig:
        modified += 1
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(new_c)

print(f'Processed and reorganized {len(all_md_files)} files; modified {modified} files.')
