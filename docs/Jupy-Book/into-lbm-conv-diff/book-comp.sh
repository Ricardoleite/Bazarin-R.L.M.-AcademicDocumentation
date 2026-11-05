#!/bin/bash
set -euo pipefail

source "$HOME/jb-env/bin/activate"
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"

OUTPUT_DIR="$HOME/static-web-pages/book"
mkdir -p -- "$OUTPUT_DIR"

jupyter book clean "$OUTPUT_DIR" --all
jupyter book build . --builder pdflatex --path-output "$OUTPUT_DIR"

cp -- "$OUTPUT_DIR"/_build/latex/*.pdf "$OUTPUT_DIR/"
printf 'PDF copied to: %s\n' "$OUTPUT_DIR"
