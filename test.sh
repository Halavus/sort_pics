#!/bin/bash

input=$(realpath $1)

script_dir="$( dirname $0)"

if [[ -f "$script_dir/.conf" ]] ; then
    echo "Read the configuration file"
    # define vars here
fi

./main.py $input $out_source
#! /bin/bash

