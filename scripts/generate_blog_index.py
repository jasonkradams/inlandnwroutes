import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hooks.blog_index import _build_blog_markdown

def main():
    content = _build_blog_markdown("docs")
    with open("docs/blog/index.md", "w", encoding="utf-8") as fp:
        fp.write(content)
    print("Generated Blog Index in docs/blog/index.md")

if __name__ == "__main__":
    main()
