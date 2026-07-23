#!/usr/bin/env bash
set -euo pipefail

# Run optional cleanup if files are passed
if [ "$#" -gt 0 ]; then
    source .venv/bin/activate
    python scripts/cleanup_markdown.py "$@"
fi

source .venv/bin/activate
echo "Linting markdown files..."
if [ "$#" -gt 0 ]; then
    pymarkdown --config .pymarkdownlnt.json scan "$@"
else
    pymarkdown --config .pymarkdownlnt.json scan "docs/blog/**/*.md"
fi
