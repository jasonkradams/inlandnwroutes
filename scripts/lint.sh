#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
echo "Linting markdown files..."

if [ "$#" -gt 0 ]; then
    pymarkdown --config .pymarkdownlnt.json scan "$@"
else
    pymarkdown --config .pymarkdownlnt.json scan "docs/blog/**/*.md"
fi
