#!/bin/bash

# Requirements:
# bash: md5deep


script_dir="$(realpath $(dirname $0))"
input="$(realpath $1)"
out_root="$(realpath $2)"
debug_options="$3"

# not in use...
if [[ -f "$script_dir/.conf" ]] ; then
    echo "Read the configuration file"
    # define vars here
fi

python $debug_options $script_dir/main.py $input $out_root $script_dir
