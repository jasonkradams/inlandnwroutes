import re
import textwrap
import argparse
import sys

def clean_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace non-breaking spaces
    content = content.replace('\xa0', ' ')
    
    lines = content.split('\n')
    cleaned_lines = []
    
    for i, line in enumerate(lines):
        sline = line.strip()
        
        # Collapse multiple spaces into a single space (except at the start of a line, but we strip anyway for the logic)
        line = re.sub(r' {2,}', ' ', line)
        
        # Check if line looks like a year marker
        is_list_item = False
        if re.match(r'^[\-\*]?\s*(c\.?\s*)?\d{3,4}(bc|BC|ad|AD)?[\:\—\-\s]*[A-Z]', sline):
            is_list_item = True
        elif sline.startswith('- ') or sline.startswith('* '):
            is_list_item = True
            
        # Add a newline before list items if the previous line wasn't empty
        if is_list_item and i > 0 and cleaned_lines[-1].strip() != '':
            cleaned_lines.append('')
            
        # Handle standalone dates (like "1875" on its own line)
        if re.match(r'^\s*\d{3,4}(bc|BC|ad|AD)?[\.\s]*$', sline):
            line = f"\n### {sline.upper()}\n"
            
        cleaned_lines.append(line.strip())
        
    text = '\n'.join(cleaned_lines)
    
    # Clean up weird gaps (e.g., more than 2 newlines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Wrap text properly
    paragraphs = text.split('\n\n')
    formatted_paragraphs = []
    
    for p in paragraphs:
        if not p.strip():
            continue
            
        p_strip = p.strip()
        
        # Do not wrap headers, tables, or images
        if p_strip.startswith('#') or p_strip.startswith('|') or p_strip.startswith('!['):
            formatted_paragraphs.append(p_strip)
        elif p_strip.startswith('- ') or p_strip.startswith('* '):
            # List item
            lines_in_p = p_strip.split('\n')
            wrapped = textwrap.fill(' '.join([x.strip() for x in lines_in_p]), width=100)
            formatted_paragraphs.append(wrapped)
        else:
            # Check if this paragraph is a timeline entry (e.g. "1964—Billy Kidd...")
            if re.match(r'^[\-\*]?\s*(c\.?\s*)?\d{3,4}', p_strip):
                cleaned_p = ' '.join(x.strip() for x in p_strip.split('\n'))
                wrapped = textwrap.fill(cleaned_p, width=100)
                formatted_paragraphs.append(wrapped)
            else:
                # Normal text
                cleaned_p = ' '.join(x.strip() for x in p_strip.split('\n'))
                wrapped = textwrap.fill(cleaned_p, width=100)
                formatted_paragraphs.append(wrapped)

    final_text = '\n\n'.join(formatted_paragraphs)
    
    # --- SKI INDEX SPECIFIC LOGIC ---
    if 'docs/ski/index.md' in filepath:
        # Fix Headers
        final_text = final_text.replace("## Included below are three articles on the history of skiing. enjoy", "Included below are three articles on the history of skiing. Enjoy!")
        final_text = final_text.replace("## Fis timeline. a ski history", "## FIS Timeline: A Ski History")
        final_text = final_text.replace("## Local ski history ski history", "## Local Ski History")
        final_text = final_text.replace("## Mount spokane ski history", "## Mount Spokane Ski History")
        final_text = final_text.replace("## Avalanche awareness", "## Avalanche Awareness")
        
        # Fix duplicate "Brief History of Mt. Spokane State Park"
        final_text = final_text.replace("Brief History of Mt. Spokane State Park", "### Brief History of Mt. Spokane State Park")
        final_text = final_text.replace("The Rich History of Rope Tows, Tramways and Ski Lifts on Mt. Spokane", "### The Rich History of Rope Tows, Tramways and Ski Lifts on Mt. Spokane")
        
        # Ensure there's only one main H1
        if not final_text.startswith("# Ski"):
            final_text = "# Ski\n\n" + final_text.replace("# Ski", "")
            
        toc = """## Table of Contents
- [FIS Timeline: A Ski History](#fis-timeline-a-ski-history)
- [Local Ski History](#local-ski-history)
- [Mount Spokane Ski History](#mount-spokane-ski-history)
- [Avalanche Awareness](#avalanche-awareness)
"""
        final_text = final_text.replace("Included below are three articles on the history of skiing. Enjoy!", "Included below are three articles on the history of skiing. Enjoy!\n\n" + toc)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_text)
        
    print(f"Successfully cleaned up {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean up markdown formatting.")
    parser.add_argument('files', nargs='+', help="Markdown files to clean up")
    args = parser.parse_args()
    
    for filepath in args.files:
        clean_markdown(filepath)
