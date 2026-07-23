import os
import glob
import re
import yaml
import textwrap

POSTS_DIR = 'docs/blog/posts'
posts = []

for path in glob.glob(os.path.join(POSTS_DIR, '*.md')):
    rel_path = os.path.relpath(path, 'docs/blog')
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    m_fm = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if m_fm:
        fm = yaml.safe_load(m_fm.group(1))
        title = fm.get('title', os.path.basename(path))
        date = str(fm.get('date', '2023-01-01'))
        cats = fm.get('categories', ['General News'])
    else:
        title = os.path.basename(path)
        date = '2023-01-01'
        cats = ['General News']
        
    posts.append({
        'title': title,
        'date': date,
        'category': cats[0] if cats else 'General News',
        'link': rel_path
    })

posts.sort(key=lambda x: x['date'], reverse=True)

cats_map = {}
for p in posts:
    c = p['category']
    if c not in cats_map:
        cats_map[c] = []
    cats_map[c].append(p)

intro = "Welcome to the Inland NW Routes blog! Explore trail updates, safety guides, forest closure alerts, and wilderness reports from around the Inland Northwest."
wrapped_intro = "\n".join(textwrap.wrap(intro, width=90))

md_content = f"""# Inland NW Routes Blog

{wrapped_intro}

---

## Recent Posts

| Date | Title |
| :--- | :--- |
"""

for p in posts[:15]:
    date_str = p['date']
    title_str = p['title']
    link_str = p['link']
    
    overhead = len(f"| **{date_str}** | []({link_str}) |")
    max_title = 115 - overhead
    if max_title < len(title_str):
        if max_title > 6:
            title_str = title_str[:max_title - 3] + '...'
        else:
            m_blog = re.match(r'^(Blog\s*#?\s*\d+)', title_str)
            if m_blog:
                title_str = m_blog.group(1)
            else:
                title_str = title_str[:max(3, max_title)]
                
    line_stub = f"| **{date_str}** | [{title_str}]({link_str}) |\n"
    md_content += line_stub

md_content += "\n---\n\n## Browse All Posts by Category\n\n"

for cat, cat_posts in sorted(cats_map.items()):
    md_content += f"### {cat}\n\n"
    for p in cat_posts:
        date_str = p['date']
        title_str = p['title']
        link_str = p['link']
        
        overhead = len(f"- **{date_str}**: []({link_str})")
        max_title = 115 - overhead
        if max_title < len(title_str):
            if max_title > 6:
                title_str = title_str[:max_title - 3] + '...'
            else:
                m_blog = re.match(r'^(Blog\s*#?\s*\d+)', title_str)
                if m_blog:
                    title_str = m_blog.group(1)
                else:
                    title_str = title_str[:max(3, max_title)]
                    
        line_stub = f"- **{date_str}**: [{title_str}]({link_str})\n"
        md_content += line_stub
    md_content += "\n"

with open("docs/blog/index.md", "w", encoding="utf-8") as fp:
    fp.write(md_content)

print(f"Generated Blog Index in docs/blog/index.md with {len(posts)} posts across {len(cats_map)} categories.")
