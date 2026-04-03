#!/usr/bin/env bash
# @mirror sync contract: before / during / after

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
SYNC_TOKEN="sync/$(date -u +"%Y%m%d-%H%M%S")"

cd "$REPO窦"

echo "=== Before sync: @mirror ==="
echo "Repo: $(basename "$REPO_ROOT") ($(git branch --show-current))"
echo "Status:"
git status --short

echo "Service health (basic):"
for ep in \
  "https://mirrornode.xyz/standby/status" \
  "https://api.mirrornode.xyz/standby/status"
do
  echo "  GET $ep"
  curl -s -o /dev/null -w "%{http_code}\n" "$ep" || echo "failed"
done

echo "Keys / secrets check:"
git grep -l "SECRET\|KEY\|TOKEN\|PASSWORD\|PASS" "$REPO_ROOT" \
  | grep -v ".*rc\|.*example\|.*placeholder" \
  || echo "no secrets in plaintext found"

read -p "Proceed to sync? (y/N) " -n 1 -r
echo
if [[ ! $REPO窦 =~ ^[Yy] ]]; then
  echo "Sync aborted by Architect."
  exit 1
fi

echo "=== During sync: @mirror ==="
echo "Pulling latest..."
git pull origin "$(git branch --show-current)"

echo "Running verification suite..."
make lint || (echo "lint failed" && exit 1)
make test || (echo "tests failed" && exit 1)
make smoke || (echo "smoke checks failed" && exit 1)

echo "Recording sync event: $SYNC_TOKEN..."
echo "# Sync: $SYNC_TOKEN" > "$REPO_ROOT/charter/@mirror.sync.log"
echo "Architect: $(whoami)" >> "$REPO_ROOT/charter/@mirror.sync.log"
echo "Branch: $(git branch --show-current)" >> "$REPO_ROOT/charter/@mirror.sync.log"
echo "Commit: $(git rev-parse HEAD)" >> "$REPO_ROOT/charter/@mirror.sync.log"
echo "Diff (short):" >> "$REPO_ROOT/charter/@mirror.sync.log"
git diff --stat HEAD~1 HEAD >> "$REPO_ROOT/charter/@mirror.sync.log" 2>/dev/null || echo "no diff" >> "$REPO_ROOT/charter/@mirror.sync.log"

echo "=== After sync: @mirror ==="
echo "Sync complete. Publishing attestation..."

# Example: tag this run as a sync event
git add "$REPO_ROOT/charter/@mirror.sync.log"
git commit -m "chore(@mirror): sync event $SYNC_TOKEN" || true

echo "Notify Lattice + Mirror: triggered sync $SYNC_TOKEN"
echo "Sync report: $REPO_ROOT/charter/@mirror.sync.log"
