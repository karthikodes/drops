#!/usr/bin/env bash
# fusion_panel.sh — run the "panel" (Codex + Gemini) IN PARALLEL on a prompt,
# using the subscription CLIs you already pay for. Claude (the running session)
# is the third panelist + the judge + the synthesizer, so it is NOT called here.
#
# Usage:  fusion_panel.sh <prompt_file> [out_dir]
# Writes: <out_dir>/codex.md , <out_dir>/gemini.md  (whichever CLIs exist)
#
# Cost: $0 in API credits — both run on flat-fee subscriptions. (Burns sub quota.)

set -uo pipefail
Q="${1:?usage: fusion_panel.sh <prompt_file> [out_dir]}"
OUT="${2:-/tmp/fusion}"
mkdir -p "$OUT"
rm -f "$OUT/codex.md" "$OUT/gemini.md"
prompt="$(cat "$Q")"

pids=()

if command -v codex >/dev/null 2>&1; then
  (
    codex exec --skip-git-repo-check -c approval_policy=never -c sandbox_mode=read-only \
      -o "$OUT/codex.md" - < "$Q" >/dev/null 2>&1 || echo "[codex failed]" > "$OUT/codex.md"
  ) &
  pids+=($!)
else
  echo "[codex CLI not installed]" > "$OUT/codex.md"
fi

if command -v gemini >/dev/null 2>&1; then
  (
    gemini --skip-trust -p "$prompt" > "$OUT/gemini.md" 2>/dev/null || echo "[gemini failed]" > "$OUT/gemini.md"
  ) &
  pids+=($!)
else
  echo "[gemini CLI not installed]" > "$OUT/gemini.md"
fi

for p in "${pids[@]}"; do wait "$p"; done

echo "panel done -> $OUT"
for f in codex gemini; do
  if [ -s "$OUT/$f.md" ]; then
    echo "  $f.md: $(wc -c < "$OUT/$f.md") bytes"
  fi
done
