#!/bin/bash

find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} \;

git fetch
git add .

git status

if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

DM=$(date +"%Y-%m-%d %H:%M:%S")
PC=$(hostname)
USER_NAME=$(whoami)

git commit -m "Update from ${USER_NAME}@${PC} at ${DM}"
git push -u origin main
