#!/usr/bin/env bash
# @Lucian prime — Full system initialization
# Pulls all repos, rebuilds index, checks drift, syncs agents

set -e
ROOT="$(git rev-parse --show-toplevel)"
INTEL="$ROOT/.lucian/intelligence"

echo "[LUCIAN PRIME] Starting full system sync — $(date -u)"

# 1. Pull latest index from mirrornode-index if available
if [ -f "$ROOT/../mirrornode-index/canon/scripts/build_index.py" ]; then
  echo "[LUCIAN PRIME] Rebuilding repo index..."
  python3 "$ROOT/../mirrornode-index/canon/scripts/build_index.py"
  cp "$ROOT/../mirrornode-index/canon/repos.json" "$INTEL/index.json"
  echo "[LUCIAN PRIME] Index updated."
else
  echo "[LUCIAN PRIME] WARN: mirrornode-index not found locally. Using cached index."
fi

# 2. Run sweep
bash "$ROOT/.lucian/commands/sweep.sh"

# 3. Run status
bash "$ROOT/.lucian/commands/status.sh"

echo "[LUCIAN PRIME] Complete — $(date -u)"
