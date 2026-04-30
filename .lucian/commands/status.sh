#!/usr/bin/env bash
# @ops status — Health check: CI status, last commits, open PRs, agent sync lag

ROOT="$(git rev-parse --show-toplevel)"
INTEL="$ROOT/.lucian/intelligence"

echo "=============================="
echo " MIRRORNODE SYSTEM STATUS"
echo " $(date -u)"
echo "=============================="

echo ""
echo "--- INTELLIGENCE LAYER ---"
if [ -f "$INTEL/index.json" ]; then
  echo "index.json: $(python3 -c "
import json
raw = json.load(open('$INTEL/index.json'))
if isinstance(raw, list):
    print('repos=' + str(len(raw)) + ' (list format)')
elif isinstance(raw, dict):
    print('generated_at=' + str(raw.get('generated_at','unknown')) + ' repos=' + str(len(raw.get('repos',[]))))
else:
    print('unknown format')
" 2>/dev/null)" 2>/dev/null || echo "index.json: present (parse error)"
else
  echo "index.json: MISSING"
fi

if [ -f "$INTEL/agent_states.json" ]; then
  echo "agent_states.json: present"
else
  echo "agent_states.json: MISSING — agents not synced"
fi

if [ -f "$INTEL/drift_log.json" ]; then
  echo "drift_log.json: $(python3 -c "
import json
d = json.load(open('$INTEL/drift_log.json'))
swept = d.get('swept_at') or 'not yet swept'
drifted = len(d.get('drifted_repos', []))
print('swept_at=' + swept + ' drifted=' + str(drifted))
" 2>/dev/null)" 2>/dev/null || echo "drift_log.json: present"
else
  echo "drift_log.json: MISSING — run sweep first"
fi

echo ""
echo "--- LUCIAN RUNTIME ---"
if [ -f "$ROOT/lucian/runtime.py" ]; then
  echo "runtime.py: present"
fi

echo ""
echo "--- PROTOCOLS ---"
for p in ROTAN TRISM INOESSO NUMERAETHE; do
  if [ -f "$ROOT/protocols/$p.md" ]; then
    echo "$p: OK"
  else
    echo "$p: MISSING"
  fi
done

echo ""
echo "============================== END"
