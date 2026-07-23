#!/usr/bin/env bash
set -euo pipefail

echo "Building static site..."
source .venv/bin/activate
zensical build -f mkdocs.yml
