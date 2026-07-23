#!/usr/bin/env python3
import os
import glob
import re
import yaml
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
    
    # Detect leading indent (e.g. 4 spaces for admonitions)
    indent_match = re.match(r'^(\s*)', line)
    base_indent = indent_match.group(1) if indent_match else ''
    line_unindented = line[len(base_indent):]

    # Detect list prefix (bullet or number)
    match = re.match(r'^(\s*[\*\-\+]\s+|\s*\d+\.\s+)?(.*)$', line_unindented)
    if not match:
        return [line]
    
    prefix = match.group(1) or ''
    text = match.group(2)
    
    if not text.strip():
        return [line]
        
    sub_indent = base_indent + (' ' * len(prefix) if prefix else '')
    available_width = max(30, max_len - len(base_indent) - len(prefix))
    
    # Protect Markdown links [anchor](url) with exact-length dummy tokens so textwrap calculates length accurately
    links = []
    def link_replacer(m):
        link_str = m.group(0)
        idx = len(links)
        links.append(link_str)
        token = f"LINK{idx:03d}" + "X" * max(0, len(link_str) - 7)
        return token

    protected_text = re.sub(r'\[[^\]]+\]\([^\)]+\)', link_replacer, text)
    
    wrapped = textwrap.wrap(
        protected_text,
        width=available_width,
        break_long_words=False,
        break_on_hyphens=False,
        subsequent_indent=sub_indent
    )
    
    if not wrapped:
        return [line]
    
    # Restore protected links
    restored_wrapped = []
    for w in wrapped:
        for idx, l_str in enumerate(links):
            token = f"LINK{idx:03d}" + "X" * max(0, len(l_str) - 7)
            w = w.replace(token, l_str)
        restored_wrapped.append(w)

    restored_wrapped[0] = base_indent + prefix + restored_wrapped[0]
    
    # Prevent wrapped lines from starting with numbers like '1903.' to avoid MD029 false positives
    cleaned_wrapped = []
    for i, w in enumerate(restored_wrapped):
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
    in_admonition = False
    blocks = []
    curr_block = []
    curr_type = None  # 'para', 'list'
    curr_indent = ''
    seen_headings = {}
    last_h_level = 0

    def flush_block():
        nonlocal curr_block, curr_type, curr_indent
        if not curr_block:
            return
        if curr_type == 'para':
            joined = ' '.join(l.strip() for l in curr_block if l.strip())
            joined = re.sub(r'\s+', ' ', joined)
            wrapped = smart_wrap_paragraph(curr_indent + joined, max_len=max_len)
            blocks.extend(wrapped)
        elif curr_type == 'list':
            if blocks and blocks[-1] != '':
                blocks.append('')
            list_items = []
            curr_item = []
            for l in curr_block:
                stripped = l.strip()
                if stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s+', stripped):
                    if curr_item:
                        list_items.append(' '.join(curr_item))
                    curr_item = [stripped]
                else:
                    curr_item.append(stripped)
            if curr_item:
                list_items.append(' '.join(curr_item))

            for item in list_items:
                item = re.sub(r'^\*\s+', r'- ', item)
                item = re.sub(r'\s+', ' ', item)
                wrapped = smart_wrap_paragraph(curr_indent + item, max_len=max_len)
                blocks.extend(wrapped)
            blocks.append('')
        else:
            blocks.extend(curr_block)
        curr_block = []
        curr_type = None
        curr_indent = ''

    for idx, line in enumerate(lines):
        if line.strip().startswith('```'):
            flush_block()
            in_code = not in_code
            blocks.append(line)
            continue
            
        if in_code:
            blocks.append(line)
            continue

        stripped = line.strip()

        # Escape starting numbers (e.g. 1912.) to avoid MD029 ordered list mismatch
        if re.match(r'^\d+\.\s+', stripped):
            m_num = re.match(r'^(\d+)\.', stripped)
            if m_num and int(m_num.group(1)) > 50:
                stripped = re.sub(r'^(\d+)\.', r'\1\\.', stripped)

        # Handle heading space formatting (MD018), multiple H1s (MD025), trailing punct (MD026), and duplicates (MD024)
        if stripped.startswith('#'):
            flush_block()
            in_admonition = False
            heading_line = re.sub(r'^(#+)([^#\s])', r'\1 \2', stripped)
            
            # Convert secondary # into ## (MD025)
            if heading_line.startswith('# '):
                if last_h_level > 0:
                    heading_line = '#' + heading_line
                else:
                    last_h_level = 1
                    
            # Remove trailing punctuation (MD026)
            heading_line = re.sub(r'^(#+\s+.*?)[.:;!]+\s*$', r'\1', heading_line)
            
            h_match = re.match(r'^(#+)\s+(.*)$', heading_line)
            if h_match:
                hashes = h_match.group(1)
                h_text = h_match.group(2).strip()
                h_level_num = len(hashes)
                
                # Check for MD001 (heading level increment skipping)
                if last_h_level > 0 and h_level_num > last_h_level + 1:
                    h_level_num = last_h_level + 1
                    hashes = '#' * h_level_num
                
                last_h_level = h_level_num
                
                base_h = h_text.lower()
                if base_h in seen_headings:
                    seen_headings[base_h] += 1
                    count = seen_headings[base_h]
                    heading_line = f"{hashes} {h_text} ({count})"
                else:
                    seen_headings[base_h] = 1
                    heading_line = f"{hashes} {h_text}"

            if blocks and blocks[-1] != '':
                blocks.append('')
            blocks.append(heading_line)
            blocks.append('')  # Ensure blank line below heading (MD022)
            continue

        # Handle admonition blocks (!!! info "Title")
        if line.startswith('!!!'):
            flush_block()
            in_admonition = True
            blocks.append(line.rstrip())
            continue

        if in_admonition:
            if not stripped:
                flush_block()
                blocks.append('')
                continue
            elif stripped.startswith('#') or stripped.startswith('!!!'):
                flush_block()
                in_admonition = False
                indent = ''
            elif stripped.startswith('—') or stripped.startswith('- ') or stripped.startswith('>') or stripped.startswith('* '):
                flush_block()
                blocks.append('    ' + stripped)
                continue
            else:
                indent = '    '
        else:
            indent = ''

        if not stripped:
            flush_block()
            blocks.append('')
            continue

        # Check if line is an italic caption directly under an image tag
        prev_line_is_img = False
        if idx > 0:
            prev_stripped = lines[idx - 1].strip()
            if re.search(r'^\s*!\[.*\]\(.*\)\s*$', prev_stripped):
                prev_line_is_img = True

        # Convert standalone emphasis lines into proper headings (MD036) unless it's a caption under an image
        if not prev_line_is_img and re.match(r'^\s*[\*_]{1,2}[^*_]+[\*_]{1,2}\.?\s*$', stripped):
            if not stripped.startswith('**Elevation') and not stripped.startswith('**Distance'):
                flush_block()
                text = stripped.strip('*_').rstrip('.')
                h_level_num = 2 if last_h_level == 1 else max(2, min(4, last_h_level + 1))
                hashes = '#' * h_level_num
                heading_line = f"{hashes} {text}"
                h_lower = text.lower()
                if h_lower in seen_headings:
                    seen_headings[h_lower] += 1
                    heading_line = f"{hashes} {text} ({seen_headings[h_lower]})"
                else:
                    seen_headings[h_lower] = 1
                if blocks and blocks[-1] != '':
                    blocks.append('')
                blocks.append(heading_line)
                blocks.append('')  # Ensure blank line below heading (MD022)
                last_h_level = h_level_num
                continue

        is_special = (stripped.startswith('#') or stripped.startswith('|') or 
                      stripped.startswith('---') or stripped.startswith('!!!') or
                      re.search(r'^\s*!\[.*\]\(.*\)\s*$', stripped))
        
        is_list = (stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.\s+', stripped))

        if is_special:
            if curr_type == 'list' or curr_type == 'para':
                flush_block()
                if blocks and blocks[-1] != '':
                    blocks.append('')
            else:
                flush_block()
            blocks.append(line.rstrip())
        elif is_list or curr_type == 'list':
            if is_list and curr_type != 'list':
                flush_block()
                curr_type = 'list'
                curr_indent = indent
            curr_block.append(line.rstrip())
        else:
            if curr_type != 'para':
                flush_block()
                curr_type = 'para'
                curr_indent = indent
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
            s_line = lines[i].strip()
            if s_line == '---' or s_line.endswith('---'):
                if s_line.endswith('---') and s_line != '---':
                    lines[i] = s_line[:-3].rstrip()
                    lines.insert(i + 1, '---')
                end_fm = i
                break
        if end_fm > 1:
            try:
                fm_raw = '\n'.join(lines[1:end_fm])
                fm = yaml.safe_load(fm_raw)
                if isinstance(fm, dict) and 'notes' in fm and fm['notes']:
                    new_notes = []
                    notes_list = fm['notes'] if isinstance(fm['notes'], list) else [fm['notes']]
                    for n in notes_list:
                        if isinstance(n, dict):
                            new_notes.append(n)
                        elif isinstance(n, str):
                            s = n.strip()
                            m_link = re.match(r'^\[([^\]]+)\]\(([^)]+)\)$', s)
                            m_angle = re.match(r'^<(https?://[^>]+)>$', s)
                            m_url = re.match(r'^(https?://\S+)$', s)
                            if m_link:
                                new_notes.append({'label': m_link.group(1), 'url': m_link.group(2)})
                            elif m_angle:
                                new_notes.append({'label': 'Forest Service Alerts', 'url': m_angle.group(1)})
                            elif m_url:
                                new_notes.append({'label': 'Forest Service Alerts', 'url': m_url.group(1)})
                            else:
                                new_notes.append(s)
                    fm['notes'] = new_notes
                    fm_yaml = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip().splitlines()
                    fm_lines = ['---'] + fm_yaml + ['---']
                    body_lines = lines[end_fm + 1:]
            except Exception:
                clean_fm = [l for l in lines[1:end_fm] if l.strip() != '']
                fm_lines = ['---'] + clean_fm + ['---']
                body_lines = lines[end_fm + 1:]

    # Convert Setext headings (Line\n--- or Line\n===) to ATX headings (## Line)
    cleaned_body = []
    i = 0
    while i < len(body_lines):
        line = body_lines[i]
        nxt = body_lines[i+1] if i + 1 < len(body_lines) else ''
        if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('|') and not line.strip().startswith('!!!'):
            if nxt.strip() == '---' or nxt.strip() == '===':
                cleaned_body.append(f"## {line.strip()}")
                i += 2
                continue
        cleaned_body.append(line)
        i += 1
        
    body_lines = cleaned_body

    # Clean body content
    body_str = '\n'.join(body_lines)
    
    # 1. Clean zero-width spaces, non-breaking spaces, and un-spaced ellipses
    body_str = body_str.replace('\u200b', '').replace('\xa0', ' ')
    body_str = re.sub(r'(\w)…(\w)', r'\1… \2', body_str)
    body_str = re.sub(r'(\w)\.\.\.(\w)', r'\1... \2', body_str)

    # Clean link spaces (MD039)
    body_str = re.sub(r'\[\s+([^\]]+?)\s*\]\(', r'[\1](', body_str)
    body_str = re.sub(r'\[\s*([^\]]+?)\s+\]\(', r'[\1](', body_str)
    
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
    
    # Ensure H1 top-level heading exists (MD041), except for blog posts
    is_blog_post = filepath.replace('\\', '/').startswith('docs/blog/posts/')
    has_h1 = any(l.strip().startswith('# ') for l in raw_body)
    if not has_h1 and not is_blog_post:
        base_title = os.path.splitext(os.path.basename(filepath))[0].replace('-', ' ').title()
        raw_body = [f"# {base_title}", ""] + raw_body
        
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
