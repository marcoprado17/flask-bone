# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from app_contexts import Blueprint, render_template, g, current_app as app
from build.blueprints.components.lightly_route_dependent.navbar.r import navbar_R

home_blueprint = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@home_blueprint.route("/")
def index():
    app.logger.critical("Welcome!")
    app.logger.debug("Oi!")
    app.logger.error("Olá!")
    app.logger.info("Hi!")
    g.active_navbar_item_id = navbar_R.id.home
    return render_template("home/home.html")