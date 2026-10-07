#!/usr/bin/env bash
# One-time setup per fresh session. Installs everything into ~/.sf
set -e
SF="$(cd "$(dirname "$0")/.." && pwd)/.cache/sfdeps"; mkdir -p "$SF"; cd "$SF"
pip install --break-system-packages -q sherpa-onnx soundfile scipy numpy pillow 2>/dev/null; pip install --break-system-packages -q --no-deps num2words 2>/dev/null
if [ ! -f kokoro-en-v0_19/model.onnx ]; then
  curl -sL -o kokoro.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/kokoro-en-v0_19.tar.bz2
  tar xjf kokoro.tar.bz2 && rm kokoro.tar.bz2
fi
if [ ! -d node_modules/@fontsource/space-mono ]; then
  npm init -y >/dev/null; npm i -s gsap @fontsource/anton @fontsource/inter @fontsource/instrument-serif @fontsource/jetbrains-mono @fontsource-variable/archivo @fontsource/space-mono >/dev/null 2>&1
fi
mkdir -p assets/fonts
cp node_modules/gsap/dist/gsap.min.js assets/
cp node_modules/@fontsource/anton/files/anton-latin-400-normal.woff2 assets/fonts/anton.woff2
cp node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2 assets/fonts/inter700.woff2
cp node_modules/@fontsource/inter/files/inter-latin-500-normal.woff2 assets/fonts/inter500.woff2
F=node_modules/@fontsource
cp $F/inter/files/inter-latin-800-normal.woff2 assets/fonts/inter800.woff2
cp $F/instrument-serif/files/instrument-serif-latin-400-normal.woff2 assets/fonts/iserif.woff2
cp $F/instrument-serif/files/instrument-serif-latin-400-italic.woff2 assets/fonts/iserif-italic.woff2
cp $F/jetbrains-mono/files/jetbrains-mono-latin-500-normal.woff2 assets/fonts/mono500.woff2
cp $F/jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2 assets/fonts/mono700.woff2
cp node_modules/@fontsource-variable/archivo/files/archivo-latin-wdth-normal.woff2 assets/fonts/archivo-wdth.woff2
cp $F/space-mono/files/space-mono-latin-400-normal.woff2 assets/fonts/spacemono400.woff2
cp $F/space-mono/files/space-mono-latin-700-normal.woff2 assets/fonts/spacemono700.woff2
echo "SF setup OK"
