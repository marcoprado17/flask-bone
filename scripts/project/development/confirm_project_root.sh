#!/usr/bin/env bash

FLASK_PROJECT_ROOT=${FLASK_PROJECT_ROOT}

if ! [[ -n ${FLASK_PROJECT_ROOT} ]]
then
    echo "First, run scripts/project/setup.sh passing the root directory of the project. If you already run it, restart your bash session to apply the changes.";
    exit 1;
fi

YES="";

while getopts ":y" opt; do
  case ${opt} in
    y)
      YES="true";
      ;;
  esac
done

echo -e "The root directory of the project is: \e[100m"${FLASK_PROJECT_ROOT}"\e[49m";

if ! [[ ${YES} ]]
then
    read -p "Are you sure you want to continue? Press Y or y to continue: " -n 1 -r;
    echo;
fi

if ! [[ $REPLY =~ ^[Yy]$ || ${YES} ]]
then
    echo "Aborting...";
    exit 1;
fi