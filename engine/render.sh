#!/usr/bin/env bash
# usage: engine/render.sh videos/<slug> [snap times e.g. 0.5,5,12]   -> lint, snapshots (if given), render, final.mp4
set -e
V=$(cd "$1" && pwd); export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)
cd "$V/build"
npx -y hyperframes@0.8.92 lint 2>&1 | grep -E "✗|◇" || true
npx -y hyperframes@0.8.92 validate 2>&1 | grep -E "✗|◇" || true
if [ -n "$2" ]; then rm -rf snaps; npx -y hyperframes@0.8.92 snapshot --at "$2" --no-end -o snaps >/dev/null 2>&1; echo "snapshots: $V/build/snaps/contact-sheet-*.jpg"; exit 0; fi
npx -y hyperframes@0.8.92 render -o renders/out.mp4 > render.log 2>&1
ffmpeg -y -loglevel error -i renders/out.mp4 -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "$V/final.mp4"
ffprobe -v error -show_entries format=duration,size -of compact "$V/final.mp4"
