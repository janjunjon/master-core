#!/bin/bash

files=($(ls ${1}))
execfile="execGrads.sh"

for file in ${files[@]}; do
    if [ $file != $execfile ]; then
        echo "grads -bcp ${file}"
        grads -bcp $file
        quit
    fi
done