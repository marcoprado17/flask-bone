#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect
from blueprints.bootstrap.views import bootstrap_blueprint
from blueprints.components.lightly_route_dependent.navbar.data import NavbarData
from blueprints.components.lightly_route_dependent.navbar.views import navbar_blueprint
from blueprints.jquery.views import jquery_blueprint
from blueprints.routers.home.views import home_blueprint
from blueprints.wrappers.base.views import shared_blueprint
from configs import default_flask_app_config
from configs.instance import instance_flask_app_config
from flask_bombril.jinja.filters import assert_defined, assert_callable, call, if_filter

app = Flask(__name__, instance_relative_config=True)

app.config.from_object(default_flask_app_config)
app.config.from_object(instance_flask_app_config)


@app.route("/")
def home_redirect():
    return redirect("home")


# Registering blueprints
app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(shared_blueprint, url_prefix="/base")
app.register_blueprint(navbar_blueprint, url_prefix="/navbar")
app.register_blueprint(bootstrap_blueprint, url_prefix="/bootstrap")
app.register_blueprint(jquery_blueprint, url_prefix="/jquery")

# Registering filters to Jinja env
app.jinja_env.filters['assert_defined'] = assert_defined
app.jinja_env.filters['assert_callable'] = assert_callable
app.jinja_env.filters['call'] = call
app.jinja_env.filters['if'] = if_filter


# Registering functions in Jinja env to get the data of the lightly route dependent components
@app.context_processor
def _():
    return dict(
        get_navbar_data=lambda: NavbarData(),
    )
