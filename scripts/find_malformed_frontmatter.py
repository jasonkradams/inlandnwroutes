import os
import glob
import yaml
import json

def check_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if not content.startswith("---"):
        return "No frontmatter start marker (--- at line 1)"

    parts = content.split("---", 2)
    if len(parts) < 3:
        return "Unclosed frontmatter (missing closing ---)"

    frontmatter_raw = parts[1]

    # Check for squished markdown headers or broken keys inside YAML frontmatter
    lines = frontmatter_raw.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("##") or stripped.startswith("#"):
            return f"Squished Markdown heading inside YAML frontmatter: '{stripped}'"

    try:
        parsed = yaml.safe_load(frontmatter_raw)
        if not isinstance(parsed, dict) and parsed is not None:
            return f"Frontmatter parsed as {type(parsed).__name__} instead of dict"
        
        if parsed is not None:
            # Check stats structure if present
            if "stats" in parsed:
                stats = parsed["stats"]
                if not isinstance(stats, list):
                    return f"'stats' is not a list (got {type(stats).__name__})"
                for item in stats:
                    if not isinstance(item, dict):
                        return f"Item in 'stats' is not a dict: {item}"
                    if "label" not in item or "value" not in item:
                        return f"Item in 'stats' missing label/value: {item}"
            
            # Check notes structure if present
            if "notes" in parsed:
                notes = parsed["notes"]
                if not isinstance(notes, list):
                    return f"'notes' is not a list (got {type(notes).__name__})"
                for item in notes:
                    if isinstance(item, dict):
                        # If label is present but url is missing (and not a pure note)
                        if "label" in item and "url" not in item:
                            # Check if label is a note without link or incomplete dict
                            pass
                    elif isinstance(item, str):
                        # Some notes are simple strings or markdown links, check if split or malformed
                        if item.startswith("- "):
                            return f"Malformed note array item: '{item}'"

    except yaml.YAMLError as e:
        return f"YAML syntax error: {e}"

    return None

def main():
    docs_files = glob.glob("docs/**/*.md", recursive=True)
    malformed = []

    for path in sorted(docs_files):
        err = check_frontmatter(path)
        if err:
            malformed.append({"file": path, "error": err})

    out_file = "scratch/malformed_frontmatter_report.json"
    os.makedirs("scratch", exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"total_scanned": len(docs_files), "total_malformed": len(malformed), "malformed_files": malformed}, f, indent=2)

    print(f"Total markdown files scanned: {len(docs_files)}")
    print(f"Total files with malformed frontmatter: {len(malformed)}")
    print(f"Report saved to {out_file}")

if __name__ == "__main__":
    main()
