#!/usr/bin/env bash
set -euo pipefail

CHARTER="${1:-}"
SIG_FILE="${2:-${CHARTER}.sig}"

if [[ -z "$CHARTER" || ! -f "$CHARTER" || ! -f "$SIG_FILE" ]]; then
  echo "Usage: ./verify_signature.sh <charter> [signature-file]" >&2
  exit 2
fi

for field in Charter Hash Signed Authority; do
  count=$(grep -c "^${field}:" "$SIG_FILE" || true)
  if [[ "$count" -ne 1 ]]; then
    echo "Invalid signature receipt: expected exactly one ${field} field" >&2
    exit 1
  fi
done

recorded_charter=$(sed -n 's/^Charter:[[:space:]]*//p' "$SIG_FILE")
recorded_hash=$(sed -n 's/^Hash:[[:space:]]*sha256://p' "$SIG_FILE")
recorded_authority=$(sed -n 's/^Authority:[[:space:]]*//p' "$SIG_FILE")

if [[ "$recorded_charter" != "$(basename "$CHARTER")" ]]; then
  echo "Charter name mismatch: receipt=${recorded_charter} file=$(basename "$CHARTER")" >&2
  exit 1
fi

if [[ ! "$recorded_hash" =~ ^[0-9a-fA-F]{64}$ ]]; then
  echo "Invalid SHA-256 value in signature receipt" >&2
  exit 1
fi

if command -v sha256sum >/dev/null 2>&1; then
  actual_hash=$(sha256sum "$CHARTER" | awk '{print $1}')
elif command -v shasum >/dev/null 2>&1; then
  actual_hash=$(shasum -a 256 "$CHARTER" | awk '{print $1}')
else
  echo "No SHA-256 utility available" >&2
  exit 2
fi

if [[ "${recorded_hash,,}" != "${actual_hash,,}" ]]; then
  echo "Charter hash mismatch" >&2
  echo "expected=${recorded_hash}" >&2
  echo "actual=${actual_hash}" >&2
  exit 1
fi

if [[ "$recorded_authority" != "MIRRORNODE Canon v1.0.0" ]]; then
  echo "Unexpected signature authority: ${recorded_authority}" >&2
  exit 1
fi

echo "Verified charter receipt: $(basename "$CHARTER") sha256:${actual_hash}"
