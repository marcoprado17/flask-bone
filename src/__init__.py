# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from src.apps_holder import app
from flask import redirect


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
from src.blueprints.components.lightly_route_dependent.navbar import navbar_blueprint
app.register_blueprint(navbar_blueprint, url_prefix="/navbar")
#
# Routers
#
from src.blueprints.routers.home.views import home_blueprint
app.register_blueprint(home_blueprint, url_prefix="/home")
from src.blueprints.routers.register.views import register_blueprint
app.register_blueprint(register_blueprint, url_prefix="/cadastrar")
#
# Wrappers
#
from src.blueprints.wrappers.base import base_blueprint
app.register_blueprint(base_blueprint, url_prefix="/base")
# ==================================================================================================================
#
#
#
#
# Registering jinja filters
# ==================================================================================================================
from src.flask_bombril.jinja.filters import assert_defined, assert_callable, call, if_filter
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
from src.blueprints.components.lightly_route_dependent.navbar.data import NavbarData

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
# ==================================================================================================================
#
#
#
#
# Creating instances of auxiliar packages
# ==================================================================================================================
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
# ==================================================================================================================