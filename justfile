# Justfile

# Serve the static site locally
serve:
	./scripts/serve.sh

# Lint the markdown files
lint:
	./scripts/lint.sh

# Normalize asset names
normalize:
	source .venv/bin/activate && python scripts/normalize_assets.py
