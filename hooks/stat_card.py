"""Render the `stats` / `notes` frontmatter into a stat-card table.

Pages set structured data in frontmatter instead of hand-writing markup:

    ---
    stats:
      - label: Distance
        icon: map-marker-distance
        value: 9 miles RT
    notes:
      - Idaho panhandle national forest/alerts <https://...>
    ---

This hook turns that into a real Markdown table (so the `tables` extension,
icon shortcodes, links, etc. all render normally) and inserts it right after
the page's H1, before the rest of the content is processed.
"""


def _build_card(stats):
    lines = ['<div class="stat-card" markdown="1">', "", "| | |", "|---|---|"]
    for item in stats:
        icon = item.get("icon") or "information-outline"
        label = item["label"]
        value = item.get("value", "")
        lines.append(f"| :material-{icon}: **{label}** | {value} |")
    lines += ["", "</div>"]
    return "\n".join(lines)


def _build_notes(notes):
    lines = ['<div class="stat-card-notes" markdown="1">', ""]
    lines += [f"- {note}" for note in notes]
    lines += ["", "</div>"]
    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    stats = page.meta.get("stats")
    if not stats:
        return markdown

    blocks = [_build_card(stats)]
    notes = page.meta.get("notes")
    if notes:
        blocks.append(_build_notes(notes))
    insertion = "\n\n".join(blocks)

    lines = markdown.split("\n")
    h1_idx = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if h1_idx is None:
        return markdown

    lines[h1_idx + 1 : h1_idx + 1] = ["", insertion]
    return "\n".join(lines)
