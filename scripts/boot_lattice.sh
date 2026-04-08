#!/bin/bash
# ── MIRRORNODE Lattice Boot Script ────────────────────────────────────────────
# Boots all available agent runtimes in the background.
# Usage: bash scripts/boot_lattice.sh

set -e
cd "$(dirname "$0")/.."

echo ""
echo "  ███╗   ███╗██╗██████╗ ██████╗  ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗ ███████╗"
echo "  ████╗ ████║██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗████╗  ██║██╔═══██╗██╔══██╗██╔════╝"
echo "  ██╔████╔██║██║██████╔╝██████╔╝██║   ██║██████╔╝██╔██╗ ██║██║   ██║██║  ██║█████╗"
echo "  ██║╚██╔╝██║██║██╔══██╗██╔══██╗██║   ██║██╔══██╗██║╚██╗██║██║   ██║██║  ██║██╔══╝"
echo "  ██║ ╚═╝ ██║██║██║  ██║██║  ██║╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝██████╔╝███████╗"
echo "  ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝"
echo ""
echo "  Lattice Boot — $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
echo "─────────────────────────────────────────────────────────────────────────────────────"

# Activate venv if present
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
  echo "  ✅ venv activated"
fi

# Boot Lucian
if [ -f "lucian/runtime.py" ]; then
  echo "  🟢 Booting Lucian (port 7700)..."
  python lucian/runtime.py &
  LUCIAN_PID=$!
  echo "  Lucian PID: $LUCIAN_PID"
else
  echo "  ⚠️  Lucian runtime not found"
fi

# Boot Osiris
if [ -f "osiris/runtime.py" ]; then
  echo "  🟢 Booting Osiris (port 7701)..."
  python osiris/runtime.py &
  OSIRIS_PID=$!
  echo "  Osiris PID: $OSIRIS_PID"
else
  echo "  ⚠️  Osiris runtime not found"
fi

# Boot Hermes
if [ -f "hermes/runtime.py" ]; then
  echo "  🟢 Booting Hermes (port 7702)..."
  python hermes/runtime.py &
  HERMES_PID=$!
  echo "  Hermes PID: $HERMES_PID"
else
  echo "  ⚠️  Hermes runtime not found"
fi

echo ""
echo "  Lattice online. Waiting 2s for agents to initialize..."
sleep 2

# Health checks
echo ""
echo "  Health checks:"
curl -s http://localhost:7700/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"  Lucian  — {d.get('status','?')} | boot: {d.get('boot_time','?')[:19]}\")" 2>/dev/null || echo "  Lucian  — not responding"
curl -s http://localhost:7701/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"  Osiris  — {d.get('status','?')} | stripe: {d.get('stripe_connected','?')}\")" 2>/dev/null || echo "  Osiris  — not responding"
curl -s http://localhost:7702/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"  Hermes  — {d.get('status','?')} | queue: {d.get('queue_depth','?')}\")" 2>/dev/null || echo "  Hermes  — not responding"

echo ""
echo "  MIRRORNODE lattice is live. Press Ctrl+C to shut down all agents."
echo "─────────────────────────────────────────────────────────────────────────────────────"
wait
