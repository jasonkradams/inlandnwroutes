#!/usr/bin/env python3
"""Generate the searchable "Browse by Category" page for `docs/blog/tags.md`.

Mirrors `generate_tags_page.py`, but scoped to blog posts and keyed off each
post's `categories:` front matter (the taxonomy the blog plugin already uses)
instead of the site-wide `tags:` front matter used by regular guide pages.
"""
import os
import sys
import glob
import re
import yaml
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tag_browser import render_tag_browser

DOCS_DIR = 'docs'
BLOG_TAGS_FILE = os.path.join(DOCS_DIR, 'blog', 'tags.md')


def generate_blog_tags_content(docs_dir=DOCS_DIR):
    posts_dir = os.path.join(docs_dir, 'blog', 'posts')
    tag_map = collections.defaultdict(list)

    for filepath in sorted(glob.glob(os.path.join(posts_dir, '*.md'))):
        rel_path = os.path.relpath(filepath, os.path.join(docs_dir, 'blog')).replace('\\', '/')
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()

        m_fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not m_fm:
            continue
        try:
            fm = yaml.safe_load(m_fm.group(1)) or {}
        except Exception:
            continue

        title = fm.get('title') or os.path.basename(filepath).replace('.md', '').replace('-', ' ').title()
        cats = fm.get('categories') or ['General News']
        categories = [str(c).strip() for c in (cats if isinstance(cats, list) else [cats]) if c and str(c).strip()]
        for category in categories:
            tag_map[category].append((title, rel_path))

    return render_tag_browser(
        heading="Browse by Category",
        description=(
            "Every post on the Inland NW Routes blog is tagged by category -- trail safety,\n"
            "wildfire & closures, winter sports, and more. Search or select a category\n"
            "below to instantly filter matching posts."
        ),
        tag_map=tag_map,
        noun="post",
        root_prefix="blog/",
    )


def main():
    content = generate_blog_tags_content()
    with open(BLOG_TAGS_FILE, 'w', encoding='utf-8') as fp:
        fp.write(content)
    print(f'Successfully generated {BLOG_TAGS_FILE} with {len(content.splitlines())} lines.')


if __name__ == '__main__':
    main()
