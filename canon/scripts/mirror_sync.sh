#!/usr/bin/env bash
# @mirror sync contract: before / during / after
# Migrated from charter/sync.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
SYNC_TOKEN="sync/$(date -u +"%Y%m%d-%H%M%S")"

cd "$REPO_ROOT"

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
if [[ ! $REPLY =~ ^[Yy] ]]; then
  echo "Sync aborted by Architect."
  exit 1
fi

echo "=== During sync: @mirror ==="
echo "Pulling latest..."
git pull origin "$(git branch --show-current)"

echo "Running verification suite..."
make lint  || (echo "lint failed" && exit 1)
make test  || (echo "tests failed" && exit 1)
make smoke || (echo "smoke checks failed" && exit 1)

LOG_PATH="$REPO_ROOT/canon/dossiers/mirror_sync_${SYNC_TOKEN//\//_}.log"
mkdir -p "$(dirname "$LOG_PATH")"

echo "Recording sync event: $SYNC_TOKEN..."
{
  echo "# Sync: $SYNC_TOKEN"
  echo "Architect: $(whoami)"
  echo "Branch: $(git branch --show-current)"
  echo "Commit: $(git rev-parse HEAD)"
  echo "Diff (short):"
  git diff --stat HEAD~1 HEAD 2>/dev/null || echo "no diff"
} > "$LOG_PATH"

echo "=== After sync: @mirror ==="
git add "$LOG_PATH"
git commit -m "chore(@mirror): sync event $SYNC_TOKEN" || true

echo "Sync complete. Log: $LOG_PATH"
echo "Notify Lattice + Mirror: triggered $SYNC_TOKEN"
