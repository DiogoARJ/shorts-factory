#!/usr/bin/env bash
# One-time setup per fresh session. Installs everything into ~/.sf
set -e
SF="$(cd "$(dirname "$0")/.." && pwd)/.cache/sfdeps"; mkdir -p "$SF"; cd "$SF"
pip install --break-system-packages -q sherpa-onnx soundfile scipy numpy pillow num2words 2>/dev/null
if [ ! -f kokoro-en-v0_19/model.onnx ]; then
  curl -sL -o kokoro.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/kokoro-en-v0_19.tar.bz2
  tar xjf kokoro.tar.bz2 && rm kokoro.tar.bz2
fi
if [ ! -d node_modules/gsap ]; then
  npm init -y >/dev/null; npm i -s gsap @fontsource/anton @fontsource/inter >/dev/null 2>&1
fi
mkdir -p assets/fonts
cp node_modules/gsap/dist/gsap.min.js assets/
cp node_modules/@fontsource/anton/files/anton-latin-400-normal.woff2 assets/fonts/anton.woff2
cp node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2 assets/fonts/inter700.woff2
cp node_modules/@fontsource/inter/files/inter-latin-500-normal.woff2 assets/fonts/inter500.woff2
echo "SF setup OK"
