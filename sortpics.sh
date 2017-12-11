#!/bin/bash

# Requirements:
# bash: md5deep

# Usage
# sort_pics [input] [out_root] [python debug options]

script_dir="$(realpath $(dirname $0))/sortpics"
input="$(realpath "$1")"
out_root="$(realpath "$2")"
debug_options="$3"

cache_dir="$out_root/.cache"

# mkdir -p creates only if not present
mkdir -p $cache_dir ;
touch $cache_dir/cached_images


# TODO add option to ignore the next step and run the script on current dir only
find "$input" -type f -name *.jpg > /tmp/finds.list
find "$input" -type f -name *.mp4 >> /tmp/finds.list
# Change $input value to the generated .list file. Probably not best pratices...
input="/tmp/finds.list"

# not in use...
if [[ -f "$script_dir/.conf" ]] ; then
    echo "Read the configuration file"
    # define vars here
fi

python $debug_options $script_dir/main.py $input $out_root $cache_dir $script_dir ;

# remove the tmp list
#rm $input
