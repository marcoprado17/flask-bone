#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect

from blueprints.home.views import home_blueprint
from blueprints.shared.views import shared_blueprint
from blueprints.bootstrap.views import bootstrap_blueprint
from blueprints.jquery.views import jquery_blueprint

from configs import default_flask_app_config
from configs.instance import instance_flask_app_config


app = Flask(__name__, instance_relative_config=True)

app.config.from_object(default_flask_app_config)
app.config.from_object(instance_flask_app_config)

@app.route("/")
def home_redirect():
    return redirect("home")
app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(shared_blueprint, url_prefix="/shared")
app.register_blueprint(bootstrap_blueprint, url_prefix="/bootstrap")
app.register_blueprint(jquery_blueprint, url_prefix="/jquery")