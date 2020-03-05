#!/usr/bin/env bash

input=$1
output=$2
structured=.${input}.py

cat $input | python entries.py > $structured

python $structured > $output
