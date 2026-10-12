#!/bin/bash

source ~/jb-env/bin/activate

RUN_DIR="$(pwd)"

# Build using cached Sphinx/Jupyter Book state
jupyter book build ./ --builder pdflatex --path-output .

# Copy the generated PDF only if it exists
PDF=$(find ./_build/latex -maxdepth 1 -type f -name "*.pdf" | head -n 1)

if [ -n "$PDF" ]; then
    cp -u "$PDF" "$RUN_DIR/"
    echo "PDF copied to: $RUN_DIR/$(basename "$PDF")"
else
    echo "PDF file was not found."
fi

deactivate
