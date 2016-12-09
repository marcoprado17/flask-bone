#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


def create_app(default_app_config, instance_app_config):
    static_folder = None
    if hasattr(default_app_config, 'STATIC_FOLDER'):
        static_folder = default_app_config.STATIC_FOLDER
    if hasattr(instance_app_config, 'STATIC_FOLDER'):
        static_folder = instance_app_config.STATIC_FOLDER
    app = Flask(__name__, instance_relative_config=True, static_folder=static_folder)

    app.config.from_object(default_app_config)
    app.config.from_object(instance_app_config)

    from flask import redirect

    @app.route("/")
    def home_redirect():
        return redirect("home")

    # Registering blueprints
    from src.blueprints.routers.home.views import home_blueprint
    app.register_blueprint(home_blueprint, url_prefix="/home")
    from src.blueprints.wrappers.base import base_blueprint
    app.register_blueprint(base_blueprint, url_prefix="/base")
    from src.blueprints.components.lightly_route_dependent.navbar import navbar_blueprint
    app.register_blueprint(navbar_blueprint, url_prefix="/navbar")

    # Registering jinja filters
    from src.flask_bombril.jinja.filters import assert_defined, assert_callable, call, if_filter
    app.jinja_env.filters['assert_defined'] = assert_defined
    app.jinja_env.filters['assert_callable'] = assert_callable
    app.jinja_env.filters['call'] = call
    app.jinja_env.filters['if'] = if_filter

    # Registering lightly route dependent components context_processors
    from src.blueprints.components.lightly_route_dependent.navbar.data import NavbarData

    @app.context_processor
    def _():
        return dict(
            get_navbar_data=lambda: NavbarData(),
        )

    return app
