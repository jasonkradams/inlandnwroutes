from bs4 import BeautifulSoup
import urllib.parse
import json

with open("scratch/home.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

nav = soup.find('ul', class_='wsite-menu-default')

def parse_menu(ul):
    items = []
    if not ul:
        return items
        
    for li in ul.find_all('li', recursive=False):
        a = li.find('a', recursive=False)
        if not a:
            continue
            
        title = a.get_text(strip=True)
        href = a.get('href')
        
        if not href:
            continue
            
        if href == "/":
            filename = "index.md"
        else:
            path = urllib.parse.urlparse(href).path.strip("/")
            filename = path.replace(".html", ".md") if path else "index.md"
            if not filename.endswith(".md"):
                filename += ".md"
        
        sub_ul = li.find('ul', class_='wsite-menu', recursive=False)
        if not sub_ul:
            wrap = li.find('div', class_='wsite-menu-wrap')
            if wrap:
                sub_ul = wrap.find('ul', class_='wsite-menu')
                
        if sub_ul:
            children = parse_menu(sub_ul)
            items.append({title: children})
        else:
            items.append({title: filename})
            
    return items

menu = parse_menu(nav)
with open("scratch/nav.json", "w") as f:
    json.dump(menu, f, indent=2)

print(f"Extracted {len(menu)} top-level items.")
