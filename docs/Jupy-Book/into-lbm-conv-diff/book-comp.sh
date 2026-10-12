#!/bin/bash
set -euo pipefail

source ~/jb-env/bin/activate

RUN_DIR="$(pwd)"

# Remove cached build files and rebuild.
jupyter book clean . --all
jupyter book build . --builder pdflatex --path-output .

# Copy the newly generated PDF.
PDF=$(find ./_build/latex -maxdepth 1 -type f -name "*.pdf" -print -quit)

if [[ -z "$PDF" ]]; then
    echo "PDF file was not found."
    exit 1
fi

cp -f "$PDF" "$RUN_DIR/"
echo "PDF copied to: $RUN_DIR/$(basename "$PDF")"

deactivate
