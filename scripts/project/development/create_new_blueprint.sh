#!/usr/bin/env bash

confirm_project_root.sh -y;
RESULT=$?
if [[ ${RESULT} -ne 0 ]]
then
    exit ${RESULT}
fi
FLASK_PROJECT_ROOT=${FLASK_PROJECT_ROOT};

BLUEPRINT_ROOT=${FLASK_PROJECT_ROOT}/src/blueprints;

YES="";
BLUEPRINT_NAME="";

while getopts ":y :n:" opt; do
  case ${opt} in
    y)
      YES="true";
      ;;
    n)
      BLUEPRINT_NAME=$OPTARG;
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2;
      exit 1;
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2;
      exit 1;
      ;;
  esac
done

if ! [[ -n ${BLUEPRINT_NAME} ]]
then
    echo "What is the name of the blueprint: ";
    read BLUEPRINT_NAME;
fi

echo -e "The blueprint will be created at \e[100m"${BLUEPRINT_ROOT}"\e[49m with the name \e[100m"${BLUEPRINT_NAME}"\e[49m.";

if ! [[ ${YES} ]]
then
    read -p "Are you sure? Press Y or y to continue: " -n 1 -r;
    echo;
fi

if [[ $REPLY =~ ^[Yy]$ || ${YES} ]]
then
    cd ${BLUEPRINT_ROOT};
    mkdir ${BLUEPRINT_NAME};
    cd ${BLUEPRINT_NAME};
    mkdir static;
    cd static;
    mkdir js;
    touch js/zzz_empty.js;
    mkdir css;
    touch css/zzz_empty.css;
    mkdir img;
    touch img/zzz_empty.png;
    mkdir fonts;
    touch fonts/zzz_empty.ttf;
    cd ..;
    mkdir templates;
    cd templates;
    mkdir ${BLUEPRINT_NAME};
    cd ${BLUEPRINT_NAME};
    rm -f ${BLUEPRINT_NAME}.html;
    touch ${BLUEPRINT_NAME}.html;
    echo "<p>Welcome to "${BLUEPRINT_NAME}"!</p>" >> ${BLUEPRINT_NAME}.html;
    cd ../..;


    #
    # __init__.py
    #
    rm -f __init__.py;
    touch __init__.py;
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> __init__.py;


    #
    # views.py
    #
    rm -f views.py;
    touch views.py;
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

"""${BLUEPRINT_NAME}"""_blueprint = Blueprint(\""""${BLUEPRINT_NAME}"""\", __name__, static_folder=\"static\", template_folder=\"templates\")


@"""${BLUEPRINT_NAME}"""_blueprint.route()
def """${BLUEPRINT_NAME}"""():
    return render_template(\""""${BLUEPRINT_NAME}"""/"""${BLUEPRINT_NAME}""".html\")""" >> views.py;


    #
    # forms.py
    #
    rm -f forms.py;
    touch forms.py;
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> forms.py;


    #
    # field_validators.py
    #
    rm -f field_validators.py;
    touch field_validators.py;
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> field_validators.py;


    #
    # url_arg_validators.py
    #
    rm -f url_arg_validators.py;
    touch url_arg_validators.py;
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-""" >> url_arg_validators.py;


    #
    # data_provider.py
    #
    rm -f data_provider.py;
    touch data_provider.py;
    echo """#!/usr/bin/env python
# -*- coding: utf-8 -*-


class """${BLUEPRINT_NAME^}"""DataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return {

        }


"""${BLUEPRINT_NAME}"""_data_provider = """${BLUEPRINT_NAME^}"""DataProvider()""" >> data_provider.py;


    echo "New blueprint created.";
    echo -e "\e[93mWARNING!!! Don't forget to mark the template directory.";
    echo -e "\e[93mWARNING!!! Don't forget to register the blueprint in src/__init__.py with an url prefix (to use blueprint static folder it's necessary define the url prefix).\e[0m";
else
    echo "Creation of blueprint aborted.";
fi