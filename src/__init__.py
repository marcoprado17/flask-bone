from flask import Flask

from blueprints.home.views import home_blueprint


app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(home_blueprint)
