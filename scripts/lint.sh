#!/usr/bin/env bash
set -euo pipefail

echo "Running markdown cleanup heuristics..."
source .venv/bin/activate
python scripts/cleanup_markdown.py

echo "Linting markdown files..."
pymarkdown --config .pymarkdownlnt.json scan "docs/*.md"
