#!/usr/bin/env bash
set -e

# Root of the MIRRORNODE workspace (two levels up from this script)
ORG_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

OUT_DIR="$ORG_ROOT/canon/index"
OUT_FILE="$OUT_DIR/repos.json"

mkdir -p "$OUT_DIR"

echo "Indexing MIRRORNODE repositories..."

# Discover git repos directly under ORG_ROOT (exclude canon itself)
repos=$(
  find "$ORG_ROOT" -mindepth 2 -maxdepth 2 -type d -name ".git" \
    | while read gitdir; do
        repo_dir="$(dirname "$gitdir")"
        repo_name="$(basename "$repo_dir")"
        echo "$repo_name"
      done \
    | sort -u
)

# Convert repo list to JSON array
repos_json="$(printf '%s\n' "$repos" | jq -R . | jq -s .)"

# Write canonical index
jq -n \
  --arg ts "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --argjson repos "$repos_json" \
  '{
    schema: "canon.index.v1",
    generated_at: $ts,
    repo_count: ($repos | length),
    repos: $repos
  }' > "$OUT_FILE"

echo "✓ Indexed $(echo "$repos" | wc -l | tr -d ' ') repositories"
echo "→ $OUT_FILE"

