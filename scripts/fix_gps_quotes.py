import os
import glob
import re

count = 0
files_changed = []

for filepath in glob.glob("docs/**/*.md", recursive=True):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()

    new_content = content

    # Regex matching GPS / coordinate lines in YAML frontmatter or stats
    # Replace quotes inside coordinate strings like 50°44'15"N or 47°01'03.71"N
    # Replace double quote after digits/primes before N/S/E/W or comma/space with double prime ″ or &quot;
    
    # 1. Match frontmatter stats value lines with coordinates
    def replace_coord_quotes(match):
        val = match.group(0)
        # Replace 15"N or 03.71"N with 15″N or 03.71″N
        val_fixed = re.sub(r'(\d+[\'\′\.]*\d*)"([NSEW\s,]|&|$)', r'\1″\2', val)
        val_fixed = re.sub(r'(\d+)""([NSEW\s,]|&|$)', r'\1″\2', val_fixed)
        return val_fixed

    # Match lines like 'value: ...' or 'GPS: ...'
    lines = new_content.splitlines()
    modified_lines = []
    line_changed = False

    for line in lines:
        if "label:" in line or "value:" in line or "GPS" in line or "gps" in line or "°" in line:
            # Replace quotes in degree/minute/second patterns
            fixed_line = re.sub(r'(\d+)[°\s]*(\d+)[\'\′\s]*([\d\.]+)"([NSEW\s,\)])', r'\1°\2′\3″\4', line)
            # Also catch remaining quote right after digits before N/S/E/W
            fixed_line = re.sub(r'(\d+)"([NSEW])', r'\1″\2', fixed_line)
            if fixed_line != line:
                line_changed = True
                line = fixed_line
        modified_lines.append(line)

    if line_changed:
        new_content = "\n".join(modified_lines) + "\n"
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        count += 1
        files_changed.append(filepath)

print(f"Fixed GPS quotes in {count} files:")
for f in files_changed:
    print(f" - {f}")
