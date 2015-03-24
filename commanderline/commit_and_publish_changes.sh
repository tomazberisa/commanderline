#!/bin/bash

./commander_line.py -h > ../README.md 
git add -u 
git commit -m "$1"
git push
