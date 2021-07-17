#!/bin/bash

top_dir_name=$(dirname ../..)
for _file in $(ls *.py)
do
	echo "running test - $_file"
	#python3 -m ${top_dir_name}.test.$_file
	python3 $_file
done
