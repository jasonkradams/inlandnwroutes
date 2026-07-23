#!/usr/bin/env bash
set -euo pipefail

echo "Building static site..."
source .venv/bin/activate
python scripts/generate_tags_page.py
zensical build -f mkdocs.yml
