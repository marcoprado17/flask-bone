#!/usr/bin/env bash



if ! [[ -n ${FLASK_PROJECT_ROOT} ]]
then
    echo "Run .../scripts/project/setup.sh first! If you already run it, restart your bash session to apply the changes."
    exit
fi

BLUEPRINT_ROOT=${FLASK_PROJECT_ROOT}/src/blueprints
BLUEPRINT_NAME="$1"

if ! [[ -n ${BLUEPRINT_NAME} ]]
then
    echo "What is the name of the blueprint: "
    read BLUEPRINT_NAME
fi

echo "The blueprint will be created at ""<${BLUEPRINT_ROOT}>"" with the name <"${BLUEPRINT_NAME}">."

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
    touch js/zzz_empty.js
    mkdir css
    touch css/zzz_empty.css
    mkdir img
    touch img/zzz_empty.png
    mkdir fonts
    touch fonts/zzz_empty.ttf
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


@"""${BLUEPRINT_NAME}"""_blueprint.route()
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


    #
    # data_provider.py
    #
    touch data_provider.py
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-


class """${BLUEPRINT_NAME^}"""DataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return {

        }


"""${BLUEPRINT_NAME}"""_data_provider = """${BLUEPRINT_NAME^}"""DataProvider()""" >> data_provider.py


    echo "New blueprint created."
    echo -e "\e[93mWARNING!!! Don't forget to mark the template directory."
    echo -e "\e[93mWARNING!!! Don't forget to register the blueprint in .../src/__init__.py with an url prefix (to use blueprint static folder it's necessary define the url prefix).\e[0m"
else
    echo "Creation of blueprint aborted."
fi