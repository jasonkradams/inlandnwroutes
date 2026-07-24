"""Shared renderer for the searchable tag-browser pages (site tags, blog categories).

Both `generate_tags_page.py` and `generate_blog_tags_page.py` collect a
{tag_name: [(title, url), ...]} mapping from their own source of front matter
and hand it to `render_tag_browser`, which emits the tag-cloud + static
fallback list markup that `docs/javascripts/extra.js` turns into an
interactive, searchable filter.
"""
import json


def _site_url(root_relative_path):
    """Convert a docs-root-relative `.md` path to a clean, site-absolute URL.

    The tag-data JSON is embedded once and read by client-side JS on whatever
    page it's rendered on, so its links can't rely on being relative to the
    tag-browser page's own (possibly nested) output directory -- they need to
    be absolute from the site root.
    """
    path = root_relative_path.replace("\\", "/")
    if path == "index.md":
        path = ""
    elif path.endswith("/index.md"):
        path = path[: -len("index.md")]
    elif path.endswith(".md"):
        path = path[: -len(".md")] + "/"
    return "/" + path


def render_tag_browser(heading, description, tag_map, noun="guide", root_prefix=""):
    articles = []
    for tag_name, pages in tag_map.items():
        for title, url in pages:
            site_url = _site_url(root_prefix + url)
            articles.append({"title": title, "url": site_url, "tags": [tag_name]})
    # Merge per-article tag lists (an article can carry more than one tag)
    merged = {}
    for art in articles:
        key = art["url"]
        if key not in merged:
            merged[key] = {"title": art["title"], "url": art["url"], "tags": []}
        merged[key]["tags"].extend(art["tags"])
    articles = list(merged.values())

    sorted_tags = sorted(tag_map.items(), key=lambda x: (-len(x[1]), x[0]))

    lines = [
        f"# {heading}",
        "",
        description,
        "",
        '<div class="tag-filter-controls">',
        '  <input type="text" id="tag-search-input" class="tag-search-input" placeholder="Search tags..." autocomplete="off" />',
        '  <div id="active-filters-bar" class="active-filters-bar" style="display: none;">',
        '    <span class="active-filters-label">Active Filters:</span>',
        '    <span id="active-tags-chips"></span>',
        '    <button id="clear-tags-btn" class="clear-tags-btn" type="button">Clear All</button>',
        '    <span id="filter-count-badge" class="filter-count-badge"></span>',
        "  </div>",
        '  <div id="tag-cloud-container" class="tag-cloud-container">',
    ]

    for tag_name, pages in sorted_tags:
        clean_tag = tag_name.replace('"', "&quot;")
        lines.append(
            f'    <button type="button" class="tag-pill-btn" data-tag="{clean_tag}">{tag_name} <span class="tag-count">({len(pages)})</span></button>'
        )

    lines.extend(
        [
            "  </div>",
            "</div>",
            "",
            "---",
            "",
            '<div id="tag-results-container" class="tag-results-container" markdown="1">',
        ]
    )

    plural = f"{noun}s" if noun[-1] != "s" else noun
    for tag_name, pages in sorted(tag_map.items()):
        pages_sorted = sorted(pages, key=lambda x: x[0])
        clean_tag = tag_name.replace('"', "&quot;")
        lines.append(f'<div class="static-tag-section" data-tag="{clean_tag}" markdown="1">')
        lines.append("")
        lines.append(f"## {tag_name}")
        lines.append("")
        label = noun if len(pages_sorted) == 1 else plural
        lines.append(f"Found **{len(pages_sorted)}** {label} tagged with **{tag_name}**:")
        lines.append("")
        for p_title, p_url in pages_sorted:
            lines.append(f"- [{p_title}]({p_url})")
        lines.append("")
        lines.append("</div>")

    lines.extend(
        [
            "</div>",
            "",
            f'<script id="tag-data" type="application/json">\n{json.dumps(articles, indent=2)}\n</script>',
        ]
    )

    return "\n".join(lines) + "\n"
