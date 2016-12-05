from flask import Blueprint

home_blueprint = Blueprint("home", "home", static_folder="static", template_folder="templates")


@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    return "Hello World!"
