# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import render_template, g, current_app as app
from r import R
from __init__ import home_blueprint


@home_blueprint.route("/")
def index():
    app.logger.critical("Welcome!")
    app.logger.debug("Oi!")
    app.logger.error("Olá!")
    app.logger.info("Hi!")
    g.active_navbar_item_id = R.id.navbar.home
    return render_template("home/index.html")
