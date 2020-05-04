#!/bin/bash
> oldFiles.txt
files=$(grep  ' jane ' ../data/list.txt| cut -d ' ' -f3 | cut -d'/' -f3)
for f in $files;do
        if test -e ~/data/$f; then
         echo ~/data/$f >> oldFiles.txt
        fi
done