#!/usr/bin/env bash

FLASK_PROJECT_ROOT="$1";

if ! [[ -n ${FLASK_PROJECT_ROOT} ]]
then
    echo "What is the directory of the flask project: ";
    read FLASK_PROJECT_ROOT;
fi

echo "export FLASK_PROJECT_ROOT="${FLASK_PROJECT_ROOT}>>~/.bashrc;
echo "export PATH=\$PATH:"${FLASK_PROJECT_ROOT}/scripts>>~/.bashrc;
echo "export PATH=\$PATH:"${FLASK_PROJECT_ROOT}/scripts/project>>~/.bashrc;
echo "export PATH=\$PATH:"${FLASK_PROJECT_ROOT}/scripts/server_setups>>~/.bashrc;
echo "export PATH=\$PATH:"${FLASK_PROJECT_ROOT}/scripts/start_server>>~/.bashrc;

echo -e "\e[93mWARNING!!! Restart your bash session to apply the changes.\e[0m";