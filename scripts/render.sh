#!/usr/bin/env bash
# Render a .pptx to PDF (LibreOffice) and per-slide PNG previews (pdftoppm) for visual QA.
# usage: scripts/render.sh path/to/deck.pptx  → deck.pdf next to it, PNGs in <dir>/qa/png/
set -euo pipefail
pptx="$1"; dir="$(dirname "$pptx")"; base="$(basename "$pptx" .pptx)"
soffice --headless --convert-to pdf --outdir "$dir" "$pptx" >/dev/null 2>&1
mkdir -p "$dir/qa/png"; rm -f "$dir/qa/png/${base}"-*.png
pdftoppm -r 60 -png "$dir/$base.pdf" "$dir/qa/png/$base"
ls -la "$dir/$base.pdf"; ls "$dir/qa/png" | wc -l
