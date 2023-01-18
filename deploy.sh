# !/usr/bin/env bash
#
# I don't recommend doing something like this for any other repo!!
#

python3 generate_and_update_pdfs.py

git add .
git comment -m "automatic deploy"
git push
