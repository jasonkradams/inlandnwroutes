import os
import re

def clean_and_link_phones(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Step 1: Strip out any existing nested markdown tel links like [([208) 123-4567](tel:2081234567))](tel:...)
    # First revert any crazy nested markdown tel links back to simple numbers:
    text = re.sub(r'\[\(*(\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4})\)*\]\(tel:\d+\)', r'\1', text)
    text = re.sub(r'\[\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})\]\(tel:\d+\)', r'(\1) \2-\3', text)

    # Step 2: Now cleanly format all unlinked phone numbers as [(XXX) XXX-XXXX](tel:XXXXXXXXXX)
    def replacer(match):
        area, prefix, line = match.group(1), match.group(2), match.group(3)
        digits = f"{area}{prefix}{line}"
        formatted = f"({area}) {prefix}-{line}"
        return f"[{formatted}](tel:{digits})"

    # Match 10-digit phone numbers in various formats: (509) 245-3552, 509-245-3552, 509.245.3552, 208.667.2331
    # Ensure they are NOT already preceded by [ or tel:
    pattern = re.compile(r'(?<!tel:)(?<!\[)\b\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})\b')
    
    lines = text.split('\n')
    new_lines = []
    for l in lines:
        if '![' in l or 'assets/images' in l:
            new_lines.append(l)
            continue
        new_l = pattern.sub(replacer, l)
        new_lines.append(new_l)

    result = '\n'.join(new_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result)

for root, dirs, files in os.walk("docs/resources"):
    for file in files:
        if file.endswith(".md"):
            clean_and_link_phones(os.path.join(root, file))

print("Cleanly formatted all phone numbers in docs/resources/")
