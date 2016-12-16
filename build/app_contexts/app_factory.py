# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import Flask, redirect
from configs import default_app_config
from configs.instance import instance_app_config
from configs.instance import unit_test_app_config


def __create_app(configs):
    static_folder = None
    for config in configs:
        if hasattr(config, 'STATIC_FOLDER'):
            static_folder = config.STATIC_FOLDER

    app = Flask(__name__, instance_relative_config=True, static_folder=static_folder)

    for config in configs:
        app.config.from_object(config)

    # Initializing extensions
    from extensions import bcrypt
    bcrypt.init_app(app)
    from extensions import db
    db.init_app(app)

    return app


def create_app():
    app = __create_app([default_app_config, instance_app_config])

    @app.route("/")
    def home_redirect():
        return redirect("home")

    #
    #
    #
    # Registering blueprints
    # ==================================================================================================================
    #
    # Components
    #
    from build.blueprints.components.lightly_route_dependent.navbar import navbar_blueprint
    app.register_blueprint(navbar_blueprint, url_prefix="/navbar")
    #
    # Routers
    #
    from build.blueprints.routers.home.views import home_blueprint
    app.register_blueprint(home_blueprint, url_prefix="/home")
    from build.blueprints.routers.register.views import register_blueprint
    app.register_blueprint(register_blueprint, url_prefix="/cadastrar")
    #
    # Wrappers
    #
    from build.blueprints.wrappers.base import base_blueprint
    app.register_blueprint(base_blueprint, url_prefix="/base")
    # ==================================================================================================================
    #
    #
    #
    #
    # Registering jinja filters
    # ==================================================================================================================
    from build.flask_bombril.jinja.filters import assert_defined, assert_callable, call, if_filter
    app.jinja_env.filters['assert_defined'] = assert_defined
    app.jinja_env.filters['assert_callable'] = assert_callable
    app.jinja_env.filters['call'] = call
    app.jinja_env.filters['if'] = if_filter
    # ==================================================================================================================
    #
    #
    #
    #
    # Registering lightly route dependent components context_processors
    # ==================================================================================================================
    from build.blueprints.components.lightly_route_dependent.navbar.data import NavbarData

    @app.context_processor
    def _():
        return dict(
            get_navbar_data=lambda: NavbarData(),
        )
    # ==================================================================================================================
    #
    #
    #
    #
    # Configuring Logging
    # ==================================================================================================================
    import logging
    from logging.handlers import TimedRotatingFileHandler
    handler = TimedRotatingFileHandler(
        filename=app.config['LOGGING_FILENAME'],
        when=app.config['LOGGING_WHEN'],
        interval=app.config['LOGGING_INTERVAL'],
        backupCount=app.config['LOGGING_BACKUP_COUNT']
    )
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    return app


def create_unit_test_app():
    app = __create_app([default_app_config, instance_app_config, unit_test_app_config])

    return app
