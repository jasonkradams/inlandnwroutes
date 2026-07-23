import os
import re
from pathlib import Path

def fix_asset_paths(directory):
    # Matches 'assets/images/' that is not preceded by a '/' or a word character
    pattern = re.compile(r'(?<![/a-zA-Z0-9])assets/images/')
    
    docs_dir = Path(directory)
    count = 0
    for md_file in docs_dir.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, num_subs = pattern.subn('/assets/images/', content)
        
        if num_subs > 0:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {num_subs} paths in {md_file.relative_to(docs_dir)}")
            count += 1
            
    print(f"Total files fixed: {count}")

if __name__ == '__main__':
    fix_asset_paths('docs')
