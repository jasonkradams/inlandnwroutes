#!/usr/bin/env python3
import os
import glob
import re
import yaml
import json
import collections

DOCS_DIR = 'docs'
TAGS_FILE = os.path.join(DOCS_DIR, 'tags.md')

def generate_tags_content(docs_dir=DOCS_DIR):
    articles = []
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
                        if tags:
                            articles.append({'title': title, 'url': rel_path, 'tags': tags})
                            for t in tags:
                                tag_map[t].append((title, rel_path))
                except Exception:
                    pass

    sorted_tags = sorted(tag_map.items(), key=lambda x: (-len(x[1]), x[0]))

    lines = [
        '# Browse by Tag',
        '',
        'Every route, trail, launch, ski area, lake, and flora guide on Inland NW Routes is tagged by region, activity type, and difficulty. Search or select tags below to instantly filter matching guides.',
        '',
        '<div class="tag-filter-controls">',
        '  <input type="text" id="tag-search-input" class="tag-search-input" placeholder="Search tags (e.g. Backpacking, Lakes, Moderate)..." autocomplete="off" />',
        '  <div id="active-filters-bar" class="active-filters-bar" style="display: none;">',
        '    <span class="active-filters-label">Active Filters:</span>',
        '    <span id="active-tags-chips"></span>',
        '    <button id="clear-tags-btn" class="clear-tags-btn" type="button">Clear All</button>',
        '    <span id="filter-count-badge" class="filter-count-badge"></span>',
        '  </div>',
        '  <div id="tag-cloud-container" class="tag-cloud-container">',
    ]

    for tag_name, pages in sorted_tags:
        clean_tag = tag_name.replace('"', '&quot;')
        lines.append(f'    <button type="button" class="tag-pill-btn" data-tag="{clean_tag}">{tag_name} <span class="tag-count">({len(pages)})</span></button>')

    lines.extend([
        '  </div>',
        '</div>',
        '',
        '---',
        '',
        '<div id="tag-results-container" class="tag-results-container">',
    ])

    # Static fallback list grouped by tag for accessibility and non-JS rendering
    for tag_name, pages in sorted(tag_map.items()):
        pages_sorted = sorted(pages, key=lambda x: x[0])
        clean_tag = tag_name.replace('"', '&quot;')
        lines.append(f'<div class="static-tag-section" data-tag="{clean_tag}">')
        lines.append(f'## {tag_name}')
        lines.append('')
        lines.append(f'Found **{len(pages_sorted)}** guide{"s" if len(pages_sorted) != 1 else ""} tagged with **{tag_name}**:')
        lines.append('')
        for p_title, p_url in pages_sorted:
            lines.append(f'- [{p_title}]({p_url})')
        lines.append('')
        lines.append('</div>')

    lines.extend([
        '</div>',
        '',
        f'<script id="tag-data" type="application/json">{json.dumps(articles)}</script>',
        ''
    ])

    return '\n'.join(lines) + '\n'

def main():
    content = generate_tags_content()
    with open(TAGS_FILE, 'w', encoding='utf-8') as fp:
        fp.write(content)
    print(f'Successfully generated {TAGS_FILE} with {len(content.splitlines())} lines.')

if __name__ == '__main__':
    main()
