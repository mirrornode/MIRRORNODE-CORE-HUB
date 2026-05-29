#!/bin/bash
# Sync main → origin/main. Refuses to run if not on main.
# Skips no-op pushes when already in sync.
set -e

cd "$(dirname "$0")/.."

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "✗ Not on main (currently on: $CURRENT_BRANCH)"
    echo "  Merge your branch to main first, then run this script."
    exit 1
fi

if git diff --quiet && git diff --cached --quiet; then
    if [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main 2>/dev/null)" ]; then
        echo "✓ Already up to date with origin/main. Nothing to push."
        exit 0
    fi
fi

echo "→ Syncing main to GitHub..."
git add -A
git diff --cached --quiet || git commit -m "chore: sync $(date '+%Y-%m-%d %H:%M')"
git push origin main
echo "✓ Done — main is up to date on origin."
