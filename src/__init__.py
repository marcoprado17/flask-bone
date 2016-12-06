#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect

from blueprints.home.views import home_blueprint
from configs import default_flask_app_config
from configs.instance import instance_flask_app_config


app = Flask(__name__, instance_relative_config=True)

app.config.from_object(default_flask_app_config)
app.config.from_object(instance_flask_app_config)

@app.route("/")
def home_redirect():
    return redirect("home")
app.register_blueprint(home_blueprint, url_prefix="/home")