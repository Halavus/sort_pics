#!/bin/bash

script_dir="$(realpath $0)"
input="$(realpath $1)"
out_root="$(realpath $2)"

if [[ -f "$script_dir/.conf" ]] ; then
    echo "Read the configuration file"
    # define vars here
fi

./main.py $input $out_root $script_dir
#! /bin/bash

