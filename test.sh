#! /bin/bash

input=($(find . -type f))

python -i test.py $input
