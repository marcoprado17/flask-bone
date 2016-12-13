#parse("header.py")

from flask import Blueprint

${BLUEPRINT_NAME}_blueprint = Blueprint("${BLUEPRINT_NAME}", __name__, static_folder="static", template_folder="templates")
