#!/bin/bash
set -eu

read message

project_dir="$HOME/projects/generation/mini-project-tests"

if [[ $(pwd) != ${project_dir} ]];
then
	echo -e "Not in project directory.Changing directory to ${project_dir}\n"
	cd ${project_dir}
fi
if python3 -m pytest tests/tests.py -v; 
then
	echo $message
	git commit -am "$message"
	git push
fi