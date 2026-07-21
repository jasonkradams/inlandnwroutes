#!/usr/bin/env bash
set -euo pipefail

echo "Starting local dev server..."
source .venv/bin/activate
zensical serve -f mkdocs.yml
