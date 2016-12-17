# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from flask import Blueprint, render_template, g, current_app as app
from build.r import R

home_blueprint = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@home_blueprint.route("/")
def index():
    app.logger.critical("Welcome!")
    app.logger.debug("Oi!")
    app.logger.error("Olá!")
    app.logger.info("Hi!")
    g.active_navbar_item_id = R.id.navbar.home
    return render_template("home/index.html")