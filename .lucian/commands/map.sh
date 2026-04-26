#!/usr/bin/env bash
# @repo map — Generate architecture topology from index.json

ROOT="$(git rev-parse --show-toplevel)"
INTEL="$ROOT/.lucian/intelligence"
MAP="$INTEL/architecture_map.json"

python3 - <<EOF
import json, os
from datetime import datetime, timezone

index_path = "$INTEL/index.json"
if not os.path.exists(index_path):
    print("[MAP] ERROR: index.json not found. Run @Lucian prime first.")
    exit(1)

with open(index_path) as f:
    index = json.load(f)

tiers = {"REVENUE": [], "CORE": [], "SURFACE": [], "EXPERIMENT": []}
for repo in index.get("repos", []):
    tier = repo.get("tier", "EXPERIMENT")
    tiers.setdefault(tier, []).append(repo.get("name", "unknown"))

arch_map = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "tiers": tiers,
    "total_repos": len(index.get("repos", [])),
    "agents": ["Lucian", "Osiris", "Hermes", "Oracle"],
    "signature": {"prime": 137, "lattice_constant": "phi", "resonance_key": "1:1:2:3:5:8"}
}

with open("$MAP", 'w') as f:
    json.dump(arch_map, f, indent=2)

print("[MAP] Architecture map written to .lucian/intelligence/architecture_map.json")
for tier, repos in tiers.items():
    print(f"  {tier}: {repos}")
EOF
