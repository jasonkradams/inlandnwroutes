#!/usr/bin/env python3
"""Rewrite the informal ``---`` delimited stat blocks at the top of docs
pages (EVENT TYPE / DISTANCE / GPS / ...) into real YAML frontmatter:

  - tags: derived from nav section, activity type, and difficulty
  - stats: a list of {label, icon, value} rows
  - notes: any leftover unlabeled lines from the old block
The `hooks/stat_card.py` mkdocs hook renders `stats`/`notes` into a themed
table at build time - the page body itself stays clean prose, with no
generated markup written into it.

Values are preserved verbatim; only field *labels* are cleaned up (typo
fixes, consistent Title Case) and cosmetic whitespace/encoding issues are
normalized. Nothing that looks like free-form prose is rewritten.

Run with --dry-run first (default) to get a report; pass --apply to write.
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path

import yaml

DOCS = Path(__file__).resolve().parent.parent / "docs"
MKDOCS_YML = DOCS.parent / "mkdocs.yml"

ZERO_WIDTH = "​"

# ---------------------------------------------------------------------------
# Nav section lookup
# ---------------------------------------------------------------------------

def load_nav_sections() -> dict[str, str]:
    text = MKDOCS_YML.read_text(encoding="utf-8")
    m = re.search(r"^nav:\n(.*)", text, re.S | re.M)
    nav = yaml.safe_load(m.group(0))["nav"]

    section_map: dict[str, str] = {}

    def walk(node, section):
        if isinstance(node, list):
            for item in node:
                walk(item, section)
        elif isinstance(node, dict):
            for k, v in node.items():
                walk(v, k if section is None else section)
        elif isinstance(node, str):
            section_map[node] = section

    walk(nav, None)
    return section_map


# ---------------------------------------------------------------------------
# Label (key) normalization
# ---------------------------------------------------------------------------

TYPO_FIXES = [
    (r"\bSGERIFF\b", "SHERIFF"),
    (r"\bSHERRIF\b", "SHERIFF"),
    (r"\bCOINTY\b", "COUNTY"),
    (r"\bCOUNT SHERIFF\b", "COUNTY SHERIFF"),
    (r"\bEANGER\b", "RANGER"),
    (r"\bRANGER NDISTRICT\b", "RANGER DISTRICT"),
    (r"\bDISTYRICT\b", "DISTRICT"),
    (r"\bAFENCY\b", "AGENCY"),
    (r"\bAGHENCY\b", "AGENCY"),
    (r"\bAMANGING\b", "MANAGING"),
    (r"\bDISTRBUTION\b", "DISTRIBUTION"),
    (r"\bELEWVATION\b", "ELEVATION"),
    (r"\bAACRES\b", "ACRES"),
    (r"\bGHRANT\b", "GRANT"),
    (r"\bCVOUNTY\b", "COUNTY"),
    (r"^[A-Z]{1,2}EVENT TYPE$", "EVENT TYPE"),
]

EXACT_KEY_RENAMES = {
    "DIFFICULTY GAIN": "DIFFICULTY",
    "OF LIFTS": "LIFTS",
    "OF NAMED RUNS": "NAMED RUNS",
    "LENGTH & ACREAGE": "LENGTH AND ACREAGE",
    "LEAVE": "LEAVES",
}

# Only these (post typo-fix/rename) labels - or a name ending in one of the
# generic suffixes below - are trusted to mark the start/continuation of a
# stat block. This is deliberately narrow: a page full of prose can easily
# contain an incidental "Some Sentence: rest of sentence" line, and treating
# that as a metadata field would swallow real content into bogus stats/notes.
KNOWN_LABELS = {
    "EVENT TYPE", "TYPE", "DISTANCE", "PADDLE DISTANCE",
    "DISTANCE CAR TO FALLS", "DISTANCE FROM SPOKANE", "MILES FROM SPOKANE",
    "ELEVATION", "ELEVATION GAIN", "ELEVATION LOSS", "ELEVATION VARIES",
    "LAKE ELEVATION", "RIVER ELEVATION", "SUMMIT ELEVATION", "BASE ELEVATION",
    "DIFFICULTY", "MAPS", "GPS", "LAUNCH GPS", "RANGER DISTRICT",
    "MANAGING AGENCY", "ACRES", "ACREAGE", "PHONE", "WEBSITE", "EMAIL", "HOURS",
    "VERTS", "AVERAGE SNOW FALL", "LIFTS", "NAMED RUNS", "RUNS",
    "AMENITIES", "OTHER AMENITIES", "RESORT NAME", "TYPE OF BUSINESS",
    "ADDRESS", "LENGTH AND ACREAGE", "PARTS USED",
    "GENESIS NAME", "DISTRIBUTION", "SEASON", "MEDICAL USE", "MEDICINAL USE",
    "POISONOUS", "POISONS", "POISONOUS PARTS", "EDIBILITY", "EDIBLE",
    "FEATURES", "LEAVES", "LEAF", "FRUITS", "FRUIT", "SUITABLE FOR", "FODDER",
    "WATERFALL", "WATERFALL TYPE", "DROP", "POOLS", "STREAM OR RIVER",
}
KNOWN_LABEL_SUFFIXES = (
    " COUNTY SHERIFF", " SHERIFF", " RANGER DISTRICT", " COUNTY PARKS",
)


def is_known_label(key: str) -> bool:
    if key in KNOWN_LABELS:
        return True
    return any(key.endswith(suf) for suf in KNOWN_LABEL_SUFFIXES)

SMALL_WORDS = {"and", "or", "of", "the", "to", "from", "at", "in", "for", "a", "an", "&"}

ACRONYM_FIXES = [
    (r"\bCda\b", "CdA"),
    (r"\bGps\b", "GPS"),
    (r"\bUsfs\b", "USFS"),
    (r"\bUsgs\b", "USGS"),
    (r"\bIpnf\b", "IPNF"),
]


def normalize_key(raw: str) -> str:
    key = raw.replace(ZERO_WIDTH, "").replace("\xa0", " ")
    key = key.lstrip("#-* ").strip()
    key = re.sub(r"\s+", " ", key).upper()
    for pat, repl in TYPO_FIXES:
        key = re.sub(pat, repl, key)
    key = EXACT_KEY_RENAMES.get(key, key)
    return key


def title_case_label(key: str) -> str:
    words = key.split(" ")
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if 0 < i < len(words) - 1 and lw in SMALL_WORDS:
            out.append(lw)
        else:
            out.append(w.capitalize())
    label = " ".join(out)
    for pat, repl in ACRONYM_FIXES:
        label = re.sub(pat, repl, label)
    return label


def clean_value(raw: str) -> str:
    v = raw.replace(ZERO_WIDTH, "").replace("\xa0", " ")
    v = re.sub(r"^\s*:\s*", "", v)
    v = re.sub(r"\bFIRSTor\b", "FIRST or", v)
    v = re.sub(
        r"\[\s*<(https?://[^>]+)>\s*\]\((https?://[^)]+)\)",
        lambda m: f"[{m.group(2)}]({m.group(2)})",
        v,
    )
    v = re.sub(r"[ \t]{2,}", " ", v).strip()
    return v


# ---------------------------------------------------------------------------
# Icon selection
# ---------------------------------------------------------------------------

def pick_icon(label: str, section: str | None) -> str:
    l = label.lower()
    if "type" in l or l == "event":
        return {
            "Winter & Skiing": "ski",
            "Paddling & Rivers": "kayaking",
            "Waterfalls": "waterfall",
            "Flora & Wildlife": "flower",
        }.get(section, "hiking")
    if "sheriff" in l:
        return "shield-account"
    if "ranger district" in l:
        return "pine-tree"
    if "difficulty" in l:
        return "speedometer"
    if "paddle distance" in l or "distance" in l and "sherif" not in l:
        return "map-marker-distance"
    if "elevation" in l and "gain" in l:
        return "elevation-rise"
    if "elevation" in l and "loss" in l:
        return "arrow-down-bold"
    if "elevation" in l:
        return "terrain"
    if "gps" in l:
        return "crosshairs-gps"
    if "map" in l:
        return "map"
    if "phone" in l:
        return "phone"
    if "website" in l or "email" in l:
        return "web"
    if "acre" in l:
        return "vector-square"
    if "snow" in l:
        return "weather-snowy-heavy"
    if "vert" in l:
        return "arrow-expand-vertical"
    if "named runs" in l or l == "runs":
        return "ski"
    if "lift" in l:
        return "gondola"
    if "miles from" in l or "distance from" in l:
        return "map-marker-path"
    if "amenit" in l:
        return "star-outline"
    if "agency" in l or "managing" in l:
        return "domain"
    if "waterfall" in l:
        return "waterfall"
    if "drop" in l:
        return "arrow-collapse-down"
    if "pool" in l:
        return "water"
    if "genesis" in l:
        return "book-open-variant"
    if "distribution" in l:
        return "earth"
    if "medical" in l:
        return "medical-bag"
    if "edib" in l:
        return "food-apple"
    if "poison" in l:
        return "skull-crossbones"
    if "leaves" in l or l == "leaf":
        return "leaf"
    if "fruit" in l or "seed" in l:
        return "fruit-cherries"
    if "season" in l:
        return "calendar"
    if "address" in l:
        return "map-marker"
    if "hour" in l:
        return "clock-outline"
    if "resort" in l or "business" in l:
        return "domain"
    return "information-outline"


# ---------------------------------------------------------------------------
# Per-file parsing
# ---------------------------------------------------------------------------

KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9 &/.'’]*?)\s*:\s*(.*)$")


class Skip(Exception):
    pass


PREAMBLE_CAP = 40


def _looks_like_key_line(line: str) -> bool:
    cleaned = line.replace(ZERO_WIDTH, "").replace("\xa0", " ").strip()
    m = KEY_RE.match(cleaned.lstrip("#").strip())
    if not m:
        return False
    return is_known_label(normalize_key(m.group(1)))


def find_h1(lines: list[str]) -> tuple[int, str]:
    h1_idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1_idx is None:
        raise Skip("no H1 found")
    return h1_idx, lines[h1_idx][2:].strip()


def collect_preamble(lines: list[str], after: int) -> tuple[list[tuple[str, str]], int]:
    """Collect H2/prose lines between the H1 and the stat block, stopping at
    the first line that looks like the block itself (a "---" or a key line).
    """
    items: list[tuple[str, str]] = []
    j = after
    while j < len(lines) and (j - after) <= PREAMBLE_CAP:
        line = lines[j]
        if line.strip() == "":
            j += 1
            continue
        if line.strip() == "---" or _looks_like_key_line(line):
            return items, j
        if line.startswith("## "):
            items.append(("h2", line[3:].strip()))
        else:
            items.append(("prose", line.strip()))
        j += 1
    raise Skip("no --- block found near top")


def find_block(lines: list[str], after: int) -> tuple[int, int, int]:
    """Returns (start, content_end, rest_start):
    block content is lines[start + 1 : content_end]; the untouched remainder
    of the document is lines[rest_start :].
    """
    j = after
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    if j >= len(lines):
        raise Skip("no --- block found near top")

    window_end = min(len(lines), j + 150)

    if lines[j].strip() == "---":
        # Classic pattern: opening "---", then content, then a terminator -
        # either a closing "---" or (if that was dropped) the next heading.
        for i in range(j + 1, window_end):
            s = lines[i].strip()
            if s == "---":
                return j, i, i + 1
            if s.startswith("## "):
                return j, i, i
        raise Skip("no --- block found near top")

    if _looks_like_key_line(lines[j]):
        # No opening "---" - content starts immediately; find the terminator.
        for i in range(j, window_end):
            s = lines[i].strip()
            if s == "---":
                return after - 1, i, i + 1
            if s.startswith("## "):
                return after - 1, i, i
        raise Skip("no --- block found near top")

    raise Skip("no --- block found near top")


def parse_block(block_lines: list[str]) -> tuple[list[tuple[str, str]], list[str]]:
    rows: list[tuple[str, str]] = []
    loose: list[str] = []
    for raw in block_lines:
        line = raw.replace(ZERO_WIDTH, "").replace("\xa0", " ").strip()
        if not line:
            continue
        stripped_for_match = line.lstrip("#").strip()
        m = KEY_RE.match(stripped_for_match)
        if m:
            key = normalize_key(m.group(1))
            label = title_case_label(key)
            value = clean_value(m.group(2))
            if value:
                rows.append((label, value))
            continue
        cleaned = clean_value(line)
        if cleaned:
            loose.append(cleaned)
    return rows, loose


def subtitle_extra(h1_text: str, h2_text: str) -> str | None:
    h1_tokens = set(re.findall(r"[a-z0-9]+", h1_text.lower()))
    h2_tokens = set(re.findall(r"[a-z0-9]+", h2_text.lower()))
    extra = h2_tokens - h1_tokens
    if extra:
        return h2_text
    return None


ACTIVITY_SPLIT_RE = re.compile(r",| and | & |/")


def derive_tags(rows: list[tuple[str, str]], section: str | None) -> list[str]:
    tags: list[str] = []
    if section:
        tags.append(section)

    type_value = None
    difficulty_value = None
    for label, value in rows:
        if label == "Event Type" and type_value is None:
            type_value = value
        if label == "Difficulty" and difficulty_value is None:
            difficulty_value = value

    if difficulty_value and len(difficulty_value.split()) <= 4:
        tags.append(title_case_label(difficulty_value.upper()))

    if type_value:
        seen = {t.lower() for t in tags}
        count = 0
        for token in ACTIVITY_SPLIT_RE.split(type_value):
            token = token.strip(" .")
            if not token:
                continue
            words = token.split()
            if not (1 <= len(words) <= 3):
                continue
            label = title_case_label(token.upper())
            if label.lower() in seen:
                continue
            seen.add(label.lower())
            tags.append(label)
            count += 1
            if count >= 6:
                break

    return tags


def build_stats(rows: list[tuple[str, str]], section: str | None) -> list[dict]:
    return [
        {"label": label, "icon": pick_icon(label, section), "value": value}
        for label, value in rows
    ]


def build_notice(prose_lines: list[str]) -> str | None:
    if not prose_lines:
        return None
    lines = ['!!! warning "Before you go"', ""]
    for item in prose_lines:
        lines.append(f"    {item}")
    return "\n".join(lines)


def already_migrated(raw: str) -> bool:
    if not raw.startswith("---\n"):
        return False
    end = raw.find("\n---", 4)
    if end == -1:
        return False
    return "stats:" in raw[4:end]

def process_file(path: Path, section_map: dict[str, str]) -> tuple[str, dict]:
    raw = path.read_text(encoding="utf-8")
    if already_migrated(raw):
        raise Skip("already migrated")

    lines = raw.split("\n")
    h1_idx, h1_text = find_h1(lines)
    preamble, search_from = collect_preamble(lines, h1_idx + 1)
    start, content_end, rest_start = find_block(lines, search_from)

    rows, loose = parse_block(lines[start + 1 : content_end])
    if not rows:
        raise Skip("block had no parseable key/value rows")

    relpath = str(path.relative_to(DOCS))
    section = section_map.get(relpath)

    tags = derive_tags(rows, section)

    # The last H2 in the preamble (if any) is the old subtitle; anything
    # else (earlier H2 notices, prose warnings) is preserved verbatim.
    subtitle = None
    had_h2 = any(kind == "h2" for kind, _ in preamble)
    notice_items = list(preamble)
    for i in range(len(notice_items) - 1, -1, -1):
        kind, text = notice_items[i]
        if kind == "h2":
            del notice_items[i]
            subtitle = subtitle_extra(h1_text, text)
            break

    notice_lines = [text for _, text in notice_items]

    stats = build_stats(rows, section)
    notice = build_notice(notice_lines)

    frontmatter: dict = {}
    if tags:
        frontmatter["tags"] = tags
    frontmatter["stats"] = stats
    if loose:
        frontmatter["notes"] = loose

    fm_text = yaml.safe_dump(
        frontmatter, allow_unicode=True, sort_keys=False, default_flow_style=False
    )

    out_parts = [f"---\n{fm_text}---"]
    out_parts.append(f"# {h1_text}")
    if notice:
        out_parts.append(notice)
    if subtitle:
        out_parts.append(f"*{subtitle}*")

    rest = lines[rest_start:]
    while rest and rest[0].strip() == "":
        rest.pop(0)
    out_parts.append("\n".join(rest))

    new_text = "\n\n".join(out_parts).rstrip("\n") + "\n"

    info = {
        "section": section,
        "rows": len(rows),
        "loose": len(loose),
        "tags": tags,
        "dropped_h2": bool(had_h2 and not subtitle),
        "kept_h2": bool(subtitle),
        "notice_lines": len(notice_lines),
    }
    return new_text, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default is dry-run)")
    ap.add_argument("--only", help="glob to restrict which files are processed")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    section_map = load_nav_sections()
    pattern = str(DOCS / (args.only or "*.md"))
    files = sorted(Path(p) for p in glob.glob(pattern))

    processed = 0
    skipped: dict[str, int] = {}
    skip_files: dict[str, list[str]] = {}

    for path in files:
        try:
            new_text, info = process_file(path, section_map)
        except Skip as e:
            reason = str(e)
            skipped[reason] = skipped.get(reason, 0) + 1
            skip_files.setdefault(reason, []).append(path.name)
            continue

        processed += 1
        if args.verbose:
            print(f"--- {path.relative_to(DOCS)} ---")
            print(f"  section={info['section']!r} rows={info['rows']} loose={info['loose']} "
                  f"tags={info['tags']} kept_h2={info['kept_h2']}")

        if args.apply:
            path.write_text(new_text, encoding="utf-8")

    print(f"\nProcessed: {processed}")
    print(f"Skipped: {sum(skipped.values())}")
    for reason, count in sorted(skipped.items(), key=lambda x: -x[1]):
        print(f"  {count:4d}  {reason}")
        if args.verbose:
            for fn in skip_files[reason][:10]:
                print(f"        - {fn}")

    if not args.apply:
        print("\n(dry run — pass --apply to write changes)")


if __name__ == "__main__":
    main()
