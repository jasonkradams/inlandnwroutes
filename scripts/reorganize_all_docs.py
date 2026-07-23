#!/usr/bin/env python3
import os
import glob
import re
import textwrap

DOCS_DIR = 'docs'
all_md_files = sorted(glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True))

def smart_wrap_paragraph(line, max_len=108):
    if len(line) <= max_len:
        return [line]
    # Do not wrap headings, table rows, horizontal rules, or admonition headers
    if line.startswith('#') or line.startswith('|') or line.startswith('---') or line.startswith('!!!'):
        return [line]
    if re.search(r'^\s*!\[.*\]\(.*\)\s*$', line):
        return [line]
    
    # Detect list prefix (bullet or number)
    match = re.match(r'^(\s*[\*\-\+]\s+|\s*\d+\.\s+)?(.*)$', line)
    if not match:
        return [line]
    
    prefix = match.group(1) or ''
    text = match.group(2)
    
    if not text.strip():
        return [line]
        
    sub_indent = ' ' * len(prefix) if prefix else ''
    available_width = max(30, max_len - len(prefix))
    
    wrapped = textwrap.wrap(
        text,
        width=available_width,
        break_long_words=False,
        break_on_hyphens=False,
        subsequent_indent=sub_indent
    )
    
    if not wrapped:
        return [line]
    wrapped[0] = prefix + wrapped[0]
    
    # Prevent wrapped lines from starting with numbers like '1903.' or '1991.' by shifting preceding word
    cleaned_wrapped = []
    for i, w in enumerate(wrapped):
        if i > 0 and re.match(r'^\s*\d+\.', w):
            if cleaned_wrapped:
                prev_words = cleaned_wrapped[-1].split(' ')
                if len(prev_words) > 1:
                    last_word = prev_words.pop()
                    cleaned_wrapped[-1] = ' '.join(prev_words)
                    w = last_word + ' ' + w.lstrip()
        cleaned_wrapped.append(w)
            
    return cleaned_wrapped

def process_body_lines(lines, max_len=108):
    in_code = False
    blocks = []
    curr_block = []
    curr_type = None  # 'para', 'list'

    def flush_block():
        nonlocal curr_block, curr_type
        if not curr_block:
            return
        if curr_type == 'para':
            joined = ' '.join(l.strip() for l in curr_block if l.strip())
            joined = re.sub(r'\s+', ' ', joined)
            wrapped = smart_wrap_paragraph(joined, max_len=max_len)
            blocks.extend(wrapped)
        elif curr_type == 'list':
            for item in curr_block:
                item = re.sub(r'^(\s*)\*\s+', r'\1- ', item)
                blocks.extend(smart_wrap_paragraph(item, max_len=max_len))
        else:
            blocks.extend(curr_block)
        curr_block = []
        curr_type = None

    for line in lines:
        if line.strip().startswith('```'):
            flush_block()
            in_code = not in_code
            blocks.append(line)
            continue
            
        if in_code:
            blocks.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            flush_block()
            blocks.append('')
            continue

        is_special = (stripped.startswith('#') or stripped.startswith('|') or 
                      stripped.startswith('---') or stripped.startswith('!!!') or
                      re.search(r'^\s*!\[.*\]\(.*\)\s*$', stripped))
        
        is_list = (stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s+', stripped))

        if is_special:
            flush_block()
            blocks.append(line.rstrip())
        elif is_list:
            if curr_type != 'list':
                flush_block()
                curr_type = 'list'
            curr_block.append(line.rstrip())
        else:
            if curr_type != 'para':
                flush_block()
                curr_type = 'para'
            curr_block.append(line.rstrip())

    flush_block()
    return blocks

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # 0. Separate frontmatter from body
    lines = content.splitlines()
    fm_lines = []
    body_lines = lines
    
    if len(lines) > 0 and lines[0].strip() == '---':
        end_fm = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end_fm = i
                break
        if end_fm > 1:
            clean_fm = [l for l in lines[1:end_fm] if l.strip() != '']
            fm_lines = ['---'] + clean_fm + ['---']
            body_lines = lines[end_fm + 1:]

    # Clean body content
    body_str = '\n'.join(body_lines)
    
    # 1. Clean zero-width spaces, non-breaking spaces, and un-spaced ellipses
    body_str = body_str.replace('\u200b', '').replace('\xa0', ' ')
    body_str = re.sub(r'(\w)…(\w)', r'\1… \2', body_str)
    body_str = re.sub(r'(\w)\.\.\.(\w)', r'\1... \2', body_str)
    
    # 2. Normalize image paths relative to filepath
    rel_dir = os.path.relpath(os.path.dirname(filepath), DOCS_DIR)
    if rel_dir == '.':
        correct_prefix = 'assets/images/'
    else:
        depth = len(rel_dir.replace('\\', '/').split('/'))
        correct_prefix = ('../' * depth) + 'assets/images/'
    
    # Fix absolute or malformed image paths
    body_str = re.sub(r'(/|\.|\w)*/?assets/images/', correct_prefix, body_str)
    
    # Extract title from {: data-src=... data-title="..."} and put into alt/caption
    def fix_image_attr(match):
        full_match = match.group(0)
        img_match = re.search(r'!\[[^\]]*\]\(([^)]+)\)', full_match)
        img_path = img_match.group(1) if img_match else ''
        title_match = re.search(r'data-title=[\"\']([^\"\']+)[\"\']', full_match)
        if title_match:
            title = title_match.group(1).strip()
            return f'![{title}]({img_path})\n_{title}_'
        return f'![Image]({img_path})'

    body_str = re.sub(r'!\[[^\]]*\]\([^)]+\)\{\:[^\}]*\}', fix_image_attr, body_str)
    
    # Remove orphaned trailing quote right after image tag
    body_str = re.sub(r'(!\[[^\]]*\]\([^\)]+\))\"', r'\1', body_str)
    
    # 3. Clean scraped web artifacts
    body_str = re.sub(r'##\s*\[[^\]]+\.html\]\(\)', '', body_str)
    body_str = re.sub(r'\[[^\]]+\.html\]\(\)', '', body_str)
    body_str = re.sub(r'\[<https://www\.inlandnwroutes\.com\]\(https://www\.inlandnwroutes\.com>/?\)', '', body_str)
    body_str = re.sub(r'https?://www\.inlandnwroutes\.com/uploads/\S+', '', body_str)
    body_str = re.sub(r'\[0\s*Comments\]', '', body_str, flags=re.IGNORECASE)
    body_str = re.sub(r'###\s*Leave a Reply\.?', '', body_str, flags=re.IGNORECASE)
    body_str = re.sub(r'\[\[email\s*protected\]\]\(/cdn-cgi/l/email-protection\)', 'info@inlandnwroutes.com', body_str)
    body_str = re.sub(r'/cdn-cgi/l/email-protection', '', body_str)
    body_str = re.sub(r'\[\"\]\(\"\)', '', body_str)
    body_str = re.sub(r'\[\"\]\(\)', '', body_str)
    
    # 4. Process body lines with block joining & smart wrapping
    raw_body = [l.rstrip() for l in body_str.splitlines()]
    new_body = process_body_lines(raw_body, max_len=108)
            
    # Combine frontmatter and body
    final_lines = []
    if fm_lines:
        final_lines.extend(fm_lines)
        final_lines.append('')  # Single blank line after frontmatter
        
    final_lines.extend(new_body)
    
    final_str = '\n'.join(final_lines)
    # Collapse 3+ consecutive blank lines to 2
    final_str = re.sub(r'\n{3,}', '\n\n', final_str)
    
    if not final_str.endswith('\n'):
        final_str += '\n'
        
    return final_str

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
