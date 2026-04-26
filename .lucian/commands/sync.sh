#!/usr/bin/env bash
# @agent sync — Update agent_states.json with current sync timestamp

ROOT="$(git rev-parse --show-toplevel)"
STATES="$ROOT/.lucian/intelligence/agent_states.json"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
AGENT=${1:-"manual"}

python3 - <<EOF
import json, os

path = "$STATES"
timestamp = "$TIMESTAMP"
agent = "$AGENT"

if os.path.exists(path):
    with open(path) as f:
        states = json.load(f)
else:
    states = {"agents": {}}

states["agents"][agent] = {"last_sync": timestamp, "status": "active"}
states["last_updated"] = timestamp

with open(path, 'w') as f:
    json.dump(states, f, indent=2)

print(f"[SYNC] {agent} synced at {timestamp}")
EOF
