"""Recover "*Picture (Image missing)*" placeholders by re-fetching the live page.

Each doc under docs/ was scraped from https://www.inlandnwroutes.com/<slug>.html.
Where the local markdown shows a missing-image placeholder, the live page still has
the real <img> in the same position. Two ways to resolve it:

1. The file was actually downloaded already, just under a different name (Weebly
   download collisions got auto-suffixed with -1, -2, ...) - find it on disk.
2. It was never downloaded - fetch it from the live page and save it.

Alignment between a doc's image slots and the live page's <img> tags is positional:
slot i in the doc corresponds to the i-th <img> in #wsite-content. This only holds
when the counts match, so files where they don't are reported and left untouched.
"""

import argparse
import hashlib
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets" / "images"
BASE_URL = "https://www.inlandnwroutes.com"
COMMON_EXTS = [".jpg", ".jpeg", ".png", ".gif", ".webp"]

IMG_MD_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
MISSING_RE = re.compile(r"image missing", re.IGNORECASE)

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; inlandnwroutes-recovery-script)"}


@dataclass
class Slot:
    line_index: int
    kind: str  # "real" or "missing"


@dataclass
class FileResult:
    path: Path
    status: str  # ok, mismatch, no-container, fetch-error
    detail: str = ""
    resolved_local: int = 0
    resolved_download: int = 0
    ambiguous: int = 0
    replacements: dict = field(default_factory=dict)  # line_index -> new line text
    downloads: list = field(default_factory=list)  # (url, dest_path)


def doc_url(md_file: Path) -> str:
    rel = md_file.relative_to(DOCS_DIR)
    if rel.name == "index.md":
        slug = rel.parent.as_posix()
    else:
        slug = rel.with_suffix("").as_posix()
    if slug in ("", "index"):
        return BASE_URL + "/"
    return f"{BASE_URL}/{slug}.html"


def find_slots(lines: list[str]) -> list[Slot]:
    slots = []
    for i, line in enumerate(lines):
        if MISSING_RE.search(line):
            slots.append(Slot(i, "missing"))
        elif IMG_MD_RE.search(line):
            slots.append(Slot(i, "real"))
    return slots


def live_core(basename: str) -> str:
    stem = basename.rsplit(".", 1)[0]
    if stem.endswith("_orig"):
        stem = stem[: -len("_orig")]
    return stem


def find_local_match(core: str) -> list[Path]:
    matches = []
    for suffix in [""] + [f"-{n}" for n in range(1, 10)]:
        for ext in COMMON_EXTS:
            candidate = ASSETS_DIR / f"{core}{suffix}{ext}"
            if candidate.exists():
                matches.append(candidate)
    return matches


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def process_file(session: requests.Session, md_file: Path, delay: float) -> FileResult:
    text = md_file.read_text(encoding="utf-8")
    lines = text.split("\n")
    slots = find_slots(lines)
    missing_slots = [s for s in slots if s.kind == "missing"]
    if not missing_slots:
        return FileResult(md_file, "ok", "no missing slots")

    url = doc_url(md_file)
    try:
        resp = session.get(url, headers=HEADERS, timeout=15)
        time.sleep(delay)
    except requests.RequestException as e:
        return FileResult(md_file, "fetch-error", str(e))

    if resp.status_code != 200:
        return FileResult(md_file, "fetch-error", f"HTTP {resp.status_code} for {url}")

    soup = BeautifulSoup(resp.content, "html.parser")
    content = soup.find(id="wsite-content")
    if content is None:
        return FileResult(md_file, "no-container", f"no #wsite-content at {url}")

    live_imgs = [img for img in content.find_all("img") if img.get("src")]
    if len(live_imgs) != len(slots):
        return FileResult(
            md_file,
            "mismatch",
            f"local slots={len(slots)} live imgs={len(live_imgs)} ({url})",
        )

    result = FileResult(md_file, "ok")
    for slot, img in zip(slots, live_imgs):
        if slot.kind != "missing":
            continue
        src = img["src"]
        img_url = urljoin(url, src)
        basename = Path(urlparse(img_url).path).name
        core = live_core(basename)
        matches = find_local_match(core)
        distinct = sorted(set(matches))
        if len(distinct) > 1:
            # Multiple candidate filenames - if they're byte-identical duplicates,
            # it doesn't matter which name we point to; only flag genuine conflicts.
            hashes = {file_hash(p) for p in distinct}
            if len(hashes) == 1:
                distinct = distinct[:1]
        if len(distinct) == 1:
            rel_path = f"/assets/images/{distinct[0].name}"
            result.replacements[slot.line_index] = f"![Picture]({rel_path})"
            result.resolved_local += 1
        elif len(distinct) == 0:
            ext = Path(basename).suffix or ".jpg"
            dest_name = f"{core}{ext}"
            dest_path = ASSETS_DIR / dest_name
            result.replacements[slot.line_index] = f"![Picture](/assets/images/{dest_name})"
            result.downloads.append((img_url, dest_path))
            result.resolved_download += 1
        else:
            result.ambiguous += 1
            result.detail += f" ambiguous:{core}->{[p.name for p in distinct]};"
    return result


def apply_result(session: requests.Session, md_file: Path, result: FileResult, delay: float):
    if result.downloads:
        for img_url, dest_path in result.downloads:
            try:
                r = session.get(img_url, headers=HEADERS, timeout=20)
                time.sleep(delay)
                if r.status_code == 200:
                    dest_path.write_bytes(r.content)
                else:
                    print(f"  ! download failed ({r.status_code}): {img_url}")
                    return False
            except requests.RequestException as e:
                print(f"  ! download error: {img_url}: {e}")
                return False

    if not result.replacements:
        return True

    lines = md_file.read_text(encoding="utf-8").split("\n")
    for line_index, new_line in result.replacements.items():
        lines[line_index] = new_line
    md_file.write_text("\n".join(lines), encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write changes and download images (default: dry run)")
    parser.add_argument("--limit", type=int, default=None, help="only process the first N eligible files")
    parser.add_argument("--only", type=str, default=None, help="only process files whose path contains this substring")
    parser.add_argument("--delay", type=float, default=0.4, help="seconds to sleep between HTTP requests")
    args = parser.parse_args()

    candidates = [
        f for f in sorted(DOCS_DIR.rglob("*.md")) if MISSING_RE.search(f.read_text(encoding="utf-8"))
    ]
    if args.only:
        candidates = [f for f in candidates if args.only in str(f)]
    if args.limit:
        candidates = candidates[: args.limit]

    print(f"{len(candidates)} files with missing-image markers to process\n")

    session = requests.Session()
    tally = {"ok": 0, "mismatch": 0, "no-container": 0, "fetch-error": 0}
    total_local = total_download = total_ambiguous = 0

    for md_file in candidates:
        result = process_file(session, md_file, args.delay)
        tally[result.status] = tally.get(result.status, 0) + 1
        total_local += result.resolved_local
        total_download += result.resolved_download
        total_ambiguous += result.ambiguous

        rel = md_file.relative_to(DOCS_DIR)
        if result.status == "ok" and (result.resolved_local or result.resolved_download or result.ambiguous):
            print(
                f"{rel}: local={result.resolved_local} download={result.resolved_download} "
                f"ambiguous={result.ambiguous}{result.detail}"
            )
            if args.apply:
                ok = apply_result(session, md_file, result, args.delay)
                print(f"  {'applied' if ok else 'FAILED'}")
        elif result.status != "ok":
            print(f"{rel}: {result.status} - {result.detail}")

    print("\n--- summary ---")
    print(f"ok={tally.get('ok', 0)} mismatch={tally.get('mismatch', 0)} "
          f"no-container={tally.get('no-container', 0)} fetch-error={tally.get('fetch-error', 0)}")
    print(f"resolved via local disk match: {total_local}")
    print(f"resolved via fresh download:   {total_download}")
    print(f"ambiguous (needs manual look): {total_ambiguous}")
    if not args.apply:
        print("\n(dry run - pass --apply to write changes and download images)")


if __name__ == "__main__":
    main()
