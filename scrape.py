import os
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md

SITEMAP_URL = "https://www.inlandnwroutes.com/sitemap.xml"
BASE_URL = "https://www.inlandnwroutes.com"
DOCS_DIR = "docs"
ASSETS_DIR = os.path.join(DOCS_DIR, "assets", "images")

os.makedirs(ASSETS_DIR, exist_ok=True)

def normalize_text(text):
    """Normalize ALL CAPS text to sentence case."""
    stripped = text.strip()
    if len(stripped) > 3 and stripped.isupper():
        # Only capitalize if it's strictly all caps
        return text.capitalize()
    return text

def process_node(node):
    """Recursively process DOM nodes to fix ALL CAPS and convert bold paragraphs to headers."""
    if isinstance(node, NavigableString):
        new_text = normalize_text(node.string)
        if new_text != node.string:
            node.replace_with(new_text)
    elif node.name is not None:
        if node.name in ['p', 'div'] and ('paragraph' in node.get('class', []) or node.name == 'p'):
            text_content = node.get_text(strip=True)
            strong_content = ''.join([s.get_text(strip=True) for s in node.find_all(['strong', 'b'])])
            
            if text_content and text_content == strong_content and len(text_content) < 100:
                node.name = 'h3'
        
        for child in list(node.children):
            process_node(child)

def scrape():
    print("Fetching sitemap...")
    resp = requests.get(SITEMAP_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, "xml")
    
    urls = [loc.text for loc in soup.find_all("loc")]
    print(f"Found {len(urls)} URLs.")
    
    nav_items = []
    
    for url in urls:
        print(f"Processing: {url}")
        parsed_url = urllib.parse.urlparse(url)
        path = parsed_url.path.strip("/")
        if not path or path == "index.html" or path == "":
            filename = "index.md"
            title = "Home"
        else:
            filename = path.replace(".html", ".md")
            title = path.replace(".html", "").replace("-", " ").title()
            
        filepath = os.path.join(DOCS_DIR, filename)
        
        page_resp = requests.get(url)
        if page_resp.status_code != 200:
            print(f"Failed to fetch {url}")
            continue
            
        page_soup = BeautifulSoup(page_resp.content, "html.parser")
        
        content_div = page_soup.find(id="wsite-content")
        if not content_div:
            print(f"No wsite-content found in {url}")
            continue
            
        for img in content_div.find_all("img"):
            src = img.get("src")
            if not src:
                continue
                
            img_url = urllib.parse.urljoin(url, src)
            
            img_filename = os.path.basename(urllib.parse.urlparse(img_url).path)
            if not img_filename:
                continue
                
            img_filename = urllib.parse.unquote(img_filename)
            local_img_path = os.path.join(ASSETS_DIR, img_filename)
            
            if not os.path.exists(local_img_path):
                print(f"  Downloading image: {img_url}")
                try:
                    img_resp = requests.get(img_url, stream=True)
                    if img_resp.status_code == 200:
                        with open(local_img_path, 'wb') as f:
                            for chunk in img_resp.iter_content(1024):
                                f.write(chunk)
                except Exception as e:
                    print(f"  Failed to download {img_url}: {e}")
                    
            img['src'] = f"/assets/images/{img_filename}"
            
        process_node(content_div)
        
        md_content = md(str(content_div), heading_style="ATX")
        
        if not md_content.strip().startswith("#"):
            md_content = f"# {title}\n\n" + md_content
            
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        nav_items.append({title: filename})
        
    print("Generating mkdocs.yml...")
    
    home_item = next((item for item in nav_items if list(item.values())[0] == "index.md"), None)
    if home_item:
        nav_items.remove(home_item)
        nav_items.insert(0, {"Home": "index.md"})
        
    mkdocs_yml = f"""
site_name: INLAND NW ROUTES
site_description: A comprehensive guide to hiking and scrambling in the American Selkirks, Cabinet Mountain Wilderness, the Bitterroots and more.
theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: amber
      accent: amber
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: amber
      accent: amber
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  font:
    text: Inter
    code: Roboto Mono
  features:
    - navigation.tabs
    - navigation.top
    - search.suggest
    - search.highlight
    - navigation.indexes
    - content.code.copy
    - content.action.edit

extra_css:
  - stylesheets/extra.css

nav:
"""
    for item in nav_items:
        for k, v in item.items():
            mkdocs_yml += f"  - '{k}': {v}\n"
            
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        f.write(mkdocs_yml)

    os.makedirs(os.path.join(DOCS_DIR, "stylesheets"), exist_ok=True)
    with open(os.path.join(DOCS_DIR, "stylesheets", "extra.css"), "w") as f:
        f.write("""
/* Matching the Weebly Look & Feel */
:root {
  --md-primary-fg-color: #dab844;
  --md-typeset-color: #d5d5d5;
}

[data-md-color-scheme="slate"] {
  --md-typeset-color: #d5d5d5;
  --md-typeset-a-color: #dab844;
  --md-typeset-h1-color: #ffffff;
  --md-typeset-h2-color: #ffffff;
  --md-typeset-h3-color: #ffffff;
}
""")

if __name__ == "__main__":
    scrape()
