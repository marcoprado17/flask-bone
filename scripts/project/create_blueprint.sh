#!/usr/bin/env bash

ABORTED_MSG="Creation of blueprint module aborted"
BLUEPRINT_ROOT=${BLUEPRINT_ROOT}

echo "To define/change the environment variable BLUEPRINT_ROOT, use: export BLUEPRINT_ROOT=<path/to/blueprint/directory>"

if [[ -n ${BLUEPRINT_ROOT} ]]
then
    echo "BLUEPRINT_ROOT=""${BLUEPRINT_ROOT}"
else
    echo "Environment variable BLUEPRINT_ROOT must be defined"
    echo ${ABORTED_MSG}
    exit
fi

BLUEPRINT_NAME="$1"

if ! [[ -n ${BLUEPRINT_NAME} ]]
then
    echo "What is the name of the blueprint: "
    read BLUEPRINT_NAME
fi

echo "BLUEPRINT_NAME="${BLUEPRINT_NAME}
echo "The blueprint module will be created at ""<${BLUEPRINT_ROOT}>"" with the name <"${BLUEPRINT_NAME}">"

read -p "Are you sure? Press Y or y to continue: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    cd ${BLUEPRINT_ROOT}
    mkdir ${BLUEPRINT_NAME}
    cd ${BLUEPRINT_NAME}
    mkdir static
    cd static
    mkdir js
    mkdir css
    mkdir img
    cd ..
    mkdir templates
    cd templates
    mkdir ${BLUEPRINT_NAME}
    cd ${BLUEPRINT_NAME}
    touch ${BLUEPRINT_NAME}.html
    echo "<p>Welcome to "${BLUEPRINT_NAME}"!</p>" >> ${BLUEPRINT_NAME}.html
    cd ../..


    #
    # __init__.py
    #
    touch __init__.py
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> __init__.py


    #
    # views.py
    #
    touch views.py
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

"""${BLUEPRINT_NAME}"""_blueprint = Blueprint(\""""${BLUEPRINT_NAME}"""\", __name__, static_folder=\"static\", template_folder=\"templates\")


@"""${BLUEPRINT_NAME}"""_blueprint.route(\"route-suffix\")
def """${BLUEPRINT_NAME}"""():
    return render_template(\""""${BLUEPRINT_NAME}"""/"""${BLUEPRINT_NAME}""".html\")""" >> views.py


    #
    # forms.py
    #
    touch forms.py
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> forms.py


    #
    # field_validators.py
    #
    touch field_validators.py
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> field_validators.py


    #
    # url_arg_validators.py
    #
    touch url_arg_validators.py
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> url_arg_validators.py


    echo "New blueprint module created"
    echo "WARNING!!! Don't forget to register the blueprint with an url prefix (to use blueprint static folder it's necessary define the url prefix)"
else
    echo ${ABORTED_MSG}
fi