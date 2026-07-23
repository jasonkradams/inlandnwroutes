import sys
import re

def gridify(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # First, strip out any existing grid card divs so we can do a clean rebuild
    content = content.replace('<div class="grid cards" markdown>\n\n', '')
    content = content.replace('<div class="grid cards" markdown>\n', '')
    content = content.replace('</div>\n\n', '')
    content = content.replace('</div>\n', '')

    lines = content.split('\n')
    new_lines = []
    in_grid = False

    for i, line in enumerate(lines):
        # Check if the line contains an image (whether it has a bullet or not)
        if line.strip().startswith('![') or line.strip().startswith('- !['):
            # Clean up the line to just be the image
            clean_line = line.strip()
            if clean_line.startswith('- '):
                clean_line = clean_line[2:]
                
            if not in_grid:
                new_lines.append('<div class="grid cards" markdown>')
                new_lines.append('')
                in_grid = True
                
            new_lines.append(f'- {clean_line}')
        else:
            if in_grid and line.strip() != '':
                # The grid ended (we hit non-empty text that is not an image)
                new_lines.append('')
                new_lines.append('</div>')
                new_lines.append('')
                in_grid = False
                
            if line.strip() != '' or not in_grid:
                new_lines.append(line)
            elif in_grid and line.strip() == '':
                # Inside a grid, we don't need multiple empty lines between items
                pass

    if in_grid:
        new_lines.append('')
        new_lines.append('</div>')
        new_lines.append('')

    content = '\n'.join(new_lines)
    # Remove excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath} to use grid layout.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            gridify(arg)
    else:
        print("Usage: python make_grid.py <file1.md> <file2.md> ...")
