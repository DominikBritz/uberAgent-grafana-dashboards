#!/usr/bin/env bash
set -euo pipefail

mapping_file="$1"   # e.g. mapping.json
shift

# Loop over every templated JSON (am + adx)
for src in "$@"; do
  name=$(basename "$src")

  # look up the real UID for this filename
  uid=$(jq -r --arg f "$name" '.[$f] // empty' "$mapping_file")
  if [[ -z "$uid" ]]; then
    echo "ERROR: no entry for $name in $mapping_file" >&2
    exit 1
  fi

  # inject .uid and write to folder dist in repo root
  jq --arg uid "$uid" '
    .uid = $uid
  ' "$src" > "dist/$name"
done
