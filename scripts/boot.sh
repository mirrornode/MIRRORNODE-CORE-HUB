#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# MIRRORNODE Lattice Boot Script
# Boots all agents in order: Lucian → Osiris → Hermes → Thoth → Theia → Ptah → Eve
# Usage: ./scripts/boot.sh
# ─────────────────────────────────────────────────────────────────────────────
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
cd "$REPO_ROOT"

# ── Load .env ────────────────────────────────────────────────────────────────
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
  echo "[BOOT] .env loaded"
else
  echo "[WARN] No .env found — copy .env.example to .env and fill in values"
fi

# ── Activate venv ────────────────────────────────────────────────────────────
if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
  echo "[BOOT] venv activated"
else
  echo "[WARN] No .venv found — run: python3 -m venv .venv && pip install -r requirements.txt"
  exit 1
fi

# ── Create logs dir ──────────────────────────────────────────────────────────
mkdir -p logs

# ── Boot function ────────────────────────────────────────────────────────────
boot_agent() {
  local NAME=$1
  local MODULE=$2
  local PORT=$3
  echo "[BOOT] Starting $NAME on port $PORT..."
  PYTHONPATH="$REPO_ROOT" uvicorn "$MODULE" \
    --host 0.0.0.0 \
    --port "$PORT" \
    --log-level info \
    > "logs/${NAME,,}.log" 2>&1 &
  echo "[BOOT] $NAME PID $! → logs/${NAME,,}.log"
  sleep 1
}

# ── Lattice boot sequence ─────────────────────────────────────────────────────
boot_agent LUCIAN  lucian.runtime:app   ${LUCIAN_PORT:-7700}
boot_agent OSIRIS  osiris.runtime:app   ${OSIRIS_PORT:-7701}
boot_agent HERMES  hermes.runtime:app   ${HERMES_PORT:-7702}
boot_agent THOTH   thoth.runtime:app    ${THOTH_PORT:-7703}
boot_agent THEIA   theia.runtime:app    ${THEIA_PORT:-7704}
boot_agent PTAH    ptah.runtime:app     ${PTAH_PORT:-7705}
boot_agent EVE     eve.runtime:app      ${EVE_PORT:-7706}

echo ""
echo "[BOOT] ✅ All agents launched. Checking Lucian manifest..."
sleep 3
curl -s http://localhost:${LUCIAN_PORT:-7700}/manifest | python3 -m json.tool 2>/dev/null || true
echo ""
echo "[BOOT] Run: curl http://localhost:7700/lattice/status to see full lattice health"
echo "[BOOT] Logs: tail -f logs/lucian.log"
