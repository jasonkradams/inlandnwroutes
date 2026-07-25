#!/usr/bin/env python3
import os
import sys
import glob
import re
import yaml
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tag_browser import render_tag_browser

DOCS_DIR = 'docs'
TAGS_FILE = os.path.join(DOCS_DIR, 'tags.md')

def generate_tags_content(docs_dir=DOCS_DIR):
    tag_map = collections.defaultdict(list)

    for filepath in sorted(glob.glob(os.path.join(docs_dir, '**/*.md'), recursive=True)):
        rel_path = os.path.relpath(filepath, docs_dir).replace('\\', '/')
        if rel_path == 'tags.md' or rel_path.startswith('blog/'):
            continue
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        lines = content.splitlines()
        if len(lines) > 0 and lines[0].strip() == '---':
            end_fm = -1
            for i in range(1, len(lines)):
                if lines[i].strip() == '---':
                    end_fm = i
                    break
            if end_fm > 1:
                try:
                    fm = yaml.safe_load('\n'.join(lines[1:end_fm]))
                    if fm and isinstance(fm, dict) and 'tags' in fm and fm['tags']:
                        title = None
                        for line in lines[end_fm + 1:]:
                            if line.startswith('# '):
                                title = line[2:].strip()
                                break
                        if not title:
                            title = rel_path.replace('.md', '').replace('-', ' ').title()

                        tags = [str(t).strip() for t in (fm['tags'] if isinstance(fm['tags'], list) else [fm['tags']]) if t and str(t).strip()]
                        for t in tags:
                            tag_map[t].append((title, rel_path))
                except Exception:
                    pass

    return render_tag_browser(
        heading="Browse by Tag",
        description="Every route, trail, launch, ski area, lake, and flora guide on Inland NW Routes is tagged by region, activity type, and difficulty. Search or select tags below to instantly filter matching guides.",
        tag_map=tag_map,
        noun="guide",
    )

def main():
    content = generate_tags_content()
    with open(TAGS_FILE, 'w', encoding='utf-8') as fp:
        fp.write(content)
    print(f'Successfully generated {TAGS_FILE} with {len(content.splitlines())} lines.')

if __name__ == '__main__':
    main()
