#!/usr/bin/env python3
import os
import glob
import re
import yaml
import collections

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

                        tags = fm['tags'] if isinstance(fm['tags'], list) else [fm['tags']]
                        for t in tags:
                            if t and str(t).strip():
                                tag_map[str(t).strip()].append((title, rel_path))
                except Exception:
                    pass

    lines = [
        '# Browse by Tag',
        '',
        'Every route, trail, launch, ski area, lake, and flora guide on Inland NW Routes is tagged by region, activity type, and difficulty. Select a tag below to explore all matching guides.',
        '',
        '## Quick Navigation',
        '',
    ]

    # Build tag pill badges at top sorted by count
    sorted_tags_by_count = sorted(tag_map.items(), key=lambda x: (-len(x[1]), x[0]))
    badge_items = []
    for tag_name, pages in sorted_tags_by_count:
        anchor = tag_name.lower().replace(' ', '-').replace('&', '').replace('+', '').replace('.', '').replace(',', '')
        anchor = re.sub(r'-+', '-', anchor).strip('-')
        badge_items.append(f'[{tag_name} ({len(pages)})](#{anchor})')

    lines.append(' • '.join(badge_items))
    lines.append('')
    lines.append('---')
    lines.append('')

    # Group by tag alphabetically
    for tag_name, pages in sorted(tag_map.items()):
        pages_sorted = sorted(pages, key=lambda x: x[0])
        lines.append(f'## {tag_name}')
        lines.append('')
        lines.append(f'Found **{len(pages_sorted)}** guide{"s" if len(pages_sorted) != 1 else ""} tagged with **{tag_name}**:')
        lines.append('')
        for p_title, p_url in pages_sorted:
            lines.append(f'- [{p_title}]({p_url})')
        lines.append('')

    return '\n'.join(lines) + '\n'

def main():
    content = generate_tags_content()
    with open(TAGS_FILE, 'w', encoding='utf-8') as fp:
        fp.write(content)
    print(f'Successfully generated {TAGS_FILE} with {len(content.splitlines())} lines.')

if __name__ == '__main__':
    main()
