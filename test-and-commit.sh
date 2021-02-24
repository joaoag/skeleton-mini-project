#!/bin/bash
set -eu

project_dir="$HOME/projects/generation/mini-project-tests"

if [[ $(pwd) != ${project_dir} ]];
then
	echo -e "Not in project directory.Changing directory to ${project_dir}\n"
	cd ${project_dir}
fi
if python3 -m pytest tests/tests.py; 
then
	git commit -am "${1}"
fi