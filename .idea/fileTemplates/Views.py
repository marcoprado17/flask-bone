#parse("header.py")

${BLUEPRINT_NAME}_blueprint = Blueprint("${BLUEPRINT_NAME}", __name__, static_folder="static", template_folder="templates")


@${BLUEPRINT_NAME}_blueprint.route("/")
def index():
    return render_template("${BLUEPRINT_NAME}/${BLUEPRINT_NAME}.html")
