#!/usr/bin/env bash

FLASK_PROJECT_ROOT="$1"

if ! [[ -n ${FLASK_PROJECT_ROOT} ]]
then
    echo "What is directory of the flask project: "
    read FLASK_PROJECT_ROOT
fi

echo "export FLASK_PROJECT_ROOT="${FLASK_PROJECT_ROOT}>>~/.bashrc

sudo rm -r /usr/local/bin/create_blueprint
sudo ln -s ${FLASK_PROJECT_ROOT}/scripts/project/create_blueprint.sh /usr/local/bin/create_blueprint

echo -e "\e[93mWARNING!!! Restart your bash session to apply the changes.\e[0m"