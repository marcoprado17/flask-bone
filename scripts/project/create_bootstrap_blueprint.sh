#!/usr/bin/env bash

confirm_project_root.sh;
RESULT=$?
if [[ ${RESULT} -ne 0 ]]
then
    exit ${RESULT}
fi
FLASK_PROJECT_ROOT=${FLASK_PROJECT_ROOT};

BLUEPRINT_ROOT=${FLASK_PROJECT_ROOT}/src/blueprints
BLUEPRINT_NAME=bootstrap

cd ${BLUEPRINT_ROOT};
mkdir ${BLUEPRINT_NAME};
cd ${BLUEPRINT_NAME};
mkdir static;
cd static;
mkdir js;
cp ${FLASK_PROJECT_ROOT}/bower_components/bootstrap/dist/js/bootstrap.js ${BLUEPRINT_ROOT}/${BLUEPRINT_NAME}/static/js
mkdir css;
cp ${FLASK_PROJECT_ROOT}/bower_components/bootstrap/dist/css/bootstrap.css ${BLUEPRINT_ROOT}/${BLUEPRINT_NAME}/static/css
mkdir fonts;
cp -a ${FLASK_PROJECT_ROOT}/bower_components/bootstrap/dist/fonts/. ${BLUEPRINT_ROOT}/${BLUEPRINT_NAME}/static/fonts