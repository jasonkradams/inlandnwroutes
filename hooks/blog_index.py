"""Generate the dynamic blog index for `docs/blog/index.md`."""
import os
import glob
import re
import yaml
import collections


def _build_blog_markdown(docs_dir="docs"):
    posts_dir = os.path.join(docs_dir, "blog", "posts")
    posts = []

    for filepath in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
        rel_path = os.path.relpath(filepath, os.path.join(docs_dir, "blog")).replace("\\", "/")
        with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()

        m_fm = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
        if m_fm:
            try:
                fm = yaml.safe_load(m_fm.group(1)) or {}
                title = fm.get("title", os.path.basename(filepath))
                date = str(fm.get("date", "2023-01-01"))
                cats = fm.get("categories", ["General News"])
            except Exception:
                title = os.path.basename(filepath)
                date = "2023-01-01"
                cats = ["General News"]
        else:
            title = os.path.basename(filepath)
            date = "2023-01-01"
            cats = ["General News"]

        posts.append({
            "title": title,
            "date": date,
            "category": cats[0] if (isinstance(cats, list) and cats) else "General News",
            "link": rel_path
        })

    # Sort posts newest first
    posts.sort(key=lambda x: x["date"], reverse=True)

    cats_map = collections.defaultdict(list)
    for p in posts:
        cats_map[p["category"]].append(p)

    lines = [
        "---",
        "tags:",
        "---",
        "",
        "# Inland NW Routes Blog",
        "",
        "Welcome to the Inland NW Routes blog! Explore trail updates, safety guides, forest closure alerts, and wilderness reports from around the Inland Northwest.",
        "",
        "---",
        "",
        "## Recent Posts",
        "",
        "| Date | Title |",
        "| :--- | :--- |",
    ]

    for p in posts[:15]:
        date_str = p["date"]
        title_str = p["title"]
        link_str = p["link"]

        overhead = len(f"| **{date_str}** | []({link_str}) |")
        max_title = 110 - overhead
        if len(title_str) > max_title:
            if max_title > 6:
                title_str = title_str[: max_title - 3] + "..."
            else:
                m_blog = re.match(r"^(Blog\s*#?\s*\d+)", title_str)
                title_str = m_blog.group(1) if m_blog else title_str[: max(3, max_title)]

        lines.append(f"| **{date_str}** | [{title_str}]({link_str}) |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Browse All Posts by Category")
    lines.append("")

    cat_keys = sorted(cats_map.keys())
    for idx, cat_name in enumerate(cat_keys):
        cat_posts = cats_map[cat_name]
        lines.append(f"### {cat_name}")
        lines.append("")
        for p in cat_posts:
            date_str = p["date"]
            title_str = p["title"]
            link_str = p["link"]

            overhead = len(f"- **{date_str}**: []({link_str})")
            max_title = 110 - overhead
            if len(title_str) > max_title:
                if max_title > 6:
                    title_str = title_str[: max_title - 3] + "..."
                else:
                    m_blog = re.match(r"^(Blog\s*#?\s*\d+)", title_str)
                    title_str = m_blog.group(1) if m_blog else title_str[: max(3, max_title)]

            lines.append(f"- **{date_str}**: [{title_str}]({link_str})")
        
        if idx < len(cat_keys) - 1:
            lines.append("")

    return "\n".join(lines) + "\n"


def on_page_markdown(markdown, page, config, files):
    if page.file.src_path.replace("\\", "/") == "blog/index.md":
        docs_dir = config.get("docs_dir", "docs")
        return _build_blog_markdown(docs_dir)
    return markdown
