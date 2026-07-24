"""Generate the dynamic tag index for `docs/tags.md`."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.generate_tags_page import generate_tags_content


def on_page_markdown(markdown, page, config, files):
    if page.file.src_path.replace("\\", "/") == "tags.md":
        docs_dir = config.get("docs_dir", "docs")
        return generate_tags_content(docs_dir)
    return markdown
