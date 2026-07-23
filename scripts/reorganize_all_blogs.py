#!/usr/bin/env python3
import os
import glob
import re

POSTS_DIR = 'docs/blog/posts'
all_posts = sorted(glob.glob(os.path.join(POSTS_DIR, '*.md')))

# 1. Build mapping for internal blog post links
slug_to_file = {}
for p in all_posts:
    basename = os.path.basename(p)
    slug = basename.replace('.md', '')
    slug_to_file[slug] = basename
    # Also map title-based slugs or variations
    clean_slug = re.sub(r'^blog-\d+-', '', slug)
    if clean_slug and clean_slug not in slug_to_file:
        slug_to_file[clean_slug] = basename

def clean_post_content(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        raw = fp.read()

    # Split frontmatter
    fm_match = re.match(r'^(---\s*\n.*?\n---\s*\n)(.*)$', raw, re.DOTALL)
    if not fm_match:
        return False
    
    frontmatter = fm_match.group(1)
    body = fm_match.group(2)

    # Clean web scraping artifacts from body
    body = re.sub(r'##\s*\[[^\]]+\.html\]\(\)', '', body)
    body = re.sub(r'\[[^\]]+\.html\]\(\)', '', body)
    body = re.sub(r'\[<https://www\.inlandnwroutes\.com\]\(https://www\.inlandnwroutes\.com>/?\)', '', body)
    body = re.sub(r'https?://www\.inlandnwroutes\.com/uploads/\S+', '', body)
    body = re.sub(r'\[0\s*Comments\]', '', body, flags=re.IGNORECASE)
    body = re.sub(r'###\s*Leave a Reply\.?', '', body, flags=re.IGNORECASE)
    body = re.sub(r'\[\[email\s*protected\]\]\(/cdn-cgi/l/email-protection\)', 'info@inlandnwroutes.com', body)
    body = re.sub(r'/cdn-cgi/l/email-protection', '', body)

    # Convert old site blog URLs to relative local Markdown links
    def replace_url(m):
        full = m.group(0)
        url_path = m.group(1).strip('/')
        parts = url_path.split('/')
        target_slug = parts[-1]
        if target_slug in slug_to_file:
            return slug_to_file[target_slug]
        # Try stripping leading blog-12- etc
        clean_target = re.sub(r'^blog-\d+-', '', target_slug)
        if clean_target in slug_to_file:
            return slug_to_file[clean_target]
        return full

    body = re.sub(r'https?://www\.inlandnwroutes\.com/blog/([a-zA-Z0-9_-]+)', replace_url, body)
    body = re.sub(r'/blog/([a-zA-Z0-9_-]+)', replace_url, body)

    # Clean up image paths to relative ../../assets/images/
    body = re.sub(r'(/|\.|\w)*/?assets/images/', '../../assets/images/', body)
    
    # Strip malformed data-src inside image titles
    body = re.sub(r'\"([^\"]*)\{\:\s*data-src=[^\}]*\}', r'"\1"', body)

    # Remove extra blank lines and normalize line endings
    lines = [line.rstrip() for line in body.splitlines()]

    # Ensure single excerpt marker <!-- more -->
    has_more = False
    cleaned_lines = []
    first_para_found = False

    for line in lines:
        if '<!-- more -->' in line:
            if not has_more:
                cleaned_lines.append('<!-- more -->')
                has_more = True
            continue
        cleaned_lines.append(line)

    # If no excerpt marker was present, insert after first non-empty paragraph
    if not has_more:
        final_lines = []
        in_fm_or_head = True
        para_lines = 0

        for line in cleaned_lines:
            final_lines.append(line)
            if line.strip() and not line.startswith('#') and not line.startswith('!') and not line.startswith('---'):
                para_lines += 1
            elif not line.strip() and para_lines > 0 and not has_more:
                final_lines.append('<!-- more -->')
                has_more = True
        
        if not has_more:
            final_lines.append('\n<!-- more -->')
        
        cleaned_lines = final_lines

    # Normalize headings spacing (blank line above and below every heading)
    post_body = '\n'.join(cleaned_lines)
    
    # Fix heading blank lines for MD022
    post_body = re.sub(r'([^\n])\n(#{1,6}\s+)', r'\1\n\n\2', post_body)
    post_body = re.sub(r'(#{1,6}\s+[^\n]+)\n([^\n#])', r'\1\n\n\2', post_body)
    
    # Fix list blank lines for MD032
    post_body = re.sub(r'([^\n])\n(\s*[\*\-\+]\s+)', r'\1\n\n\2', post_body)
    post_body = re.sub(r'(\s*[\*\-\+]\s+[^\n]+)\n([^\n\*\-\+\s])', r'\1\n\n\2', post_body)

    # Clean double spaces at EOL
    post_body = re.sub(r' +\n', '\n', post_body)
    post_body = re.sub(r'\n{3,}', '\n\n', post_body)

    new_full = frontmatter + '\n' + post_body.strip() + '\n'

    if new_full != raw:
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(new_full)
        return True
    return False

modified_count = 0
for path in all_posts:
    if clean_post_content(path):
        modified_count += 1

print(f'Reorganized and cleaned {modified_count} blog post files.')
