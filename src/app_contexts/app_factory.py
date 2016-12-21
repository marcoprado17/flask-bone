# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import sys

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, redirect, request, url_for

from configs import default_app_config
from configs.instance import instance_app_config
from configs.instance import unit_test_app_config

from extensions import db

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
    from extensions import mail
    mail.init_app(app)

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
    from blueprints.components.lightly_route_dependent.navbar import navbar_blueprint
    app.register_blueprint(navbar_blueprint, url_prefix="/navbar")
    #
    # Routers
    #
    from blueprints.routers.home import home_blueprint
    app.register_blueprint(home_blueprint, url_prefix="/home")
    from blueprints.routers.register import register_blueprint
    app.register_blueprint(register_blueprint, url_prefix="/cadastrar")
    if app.config["DEBUG"]:
        from blueprints.routers.debug import debug_blueprint
        app.register_blueprint(debug_blueprint, url_prefix="/debug")
    #
    # Wrappers
    #
    from blueprints.wrappers.base import base_blueprint
    app.register_blueprint(base_blueprint, url_prefix="/base")
    #
    # Macros
    #
    from macros import macros_blueprint
    app.register_blueprint(macros_blueprint)
    #
    # Email
    #
    from email_blueprint import email_blueprint
    app.register_blueprint(email_blueprint)
    # ==================================================================================================================
    #
    #
    #
    #
    # Registering jinja filters
    # ==================================================================================================================
    from flask_bombril.jinja_filters import assert_defined, assert_callable, call, if_filter
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
    from blueprints.components.lightly_route_dependent.navbar.navbar_data_provider import navbar_data_provider
    from r import R

    @app.context_processor
    def _():
        return dict(
            get_navbar_data=lambda: navbar_data_provider.get_data(),
            R=R,
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
    # ==================================================================================================================
    #
    #
    #
    #
    # Registering error handler
    # ==================================================================================================================
    @app.errorhandler(500)
    def handle_error(error):
        db.session.rollback()
        app.logger.error("url: " + request.url)
        if request.method == "POST" and len(request.form) > 0:
            form_fields = dict(request.form)
            if "password" in form_fields:
                form_fields["password"] = "******"
            if "password_confirmation" in form_fields:
                form_fields["password_confirmation"] = "******"
            app.logger.error("form_fields: " + str(form_fields))
        return R.string.temp_error_html % dict(href=url_for("home.index")), 500

    return app


def create_unit_test_app():
    app = __create_app([default_app_config, instance_app_config, unit_test_app_config])

    return app
