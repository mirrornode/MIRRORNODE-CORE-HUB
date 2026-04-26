#!/usr/bin/env bash
# @mirror sweep — Scan all repos for drift, uncommitted changes, anomalies

set -e
ROOT="$(git rev-parse --show-toplevel)"
DRIFT_LOG="$ROOT/.lucian/intelligence/drift_log.json"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "[SWEEP] Starting repository scan — $TIMESTAMP"

DRIFTS=()

for dir in $(find "$ROOT/.." -maxdepth 1 -type d -name 'mirrornode*' -o -name 'osiris*' -o -name 'theia*' -o -name 'Mirror_surface' 2>/dev/null); do
  if [ -d "$dir/.git" ]; then
    REPO=$(basename "$dir")
    cd "$dir"
    DIRTY=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    LAST=$(git log -1 --format='%ci' 2>/dev/null || echo 'unknown')
    if [ "$DIRTY" -gt "0" ]; then
      echo "[SWEEP] DRIFT: $REPO has $DIRTY uncommitted changes"
      DRIFTS+=("$REPO")
    fi
    cd "$ROOT"
  fi
done

# Write drift log
python3 -c "
import json, sys
log = {'swept_at': '$TIMESTAMP', 'drifted_repos': $(python3 -c "import json; print(json.dumps($([[ ${#DRIFTS[@]} -eq 0 ]] && echo '[]' || printf '%s\n' "${DRIFTS[@]}" | python3 -c 'import sys,json; print(json.dumps([l.strip() for l in sys.stdin]))')"))")}
with open('$DRIFT_LOG', 'w') as f:
    json.dump(log, f, indent=2)
print('[SWEEP] Drift log written.')
"
