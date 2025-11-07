#!/bin/bash

find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} 

git fetch

git add .

git status

DM=date

git commit -m "$DM"

git push -u origin main
