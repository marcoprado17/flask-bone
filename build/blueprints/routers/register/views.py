# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from flask import Blueprint, render_template, g

from build.r import R
from build.blueprints.routers.register.index_data import RegisterData

register_blueprint = Blueprint("register", __name__, static_folder="static", template_folder="templates")


@register_blueprint.route("/")
def index():
    g.active_navbar_item_id = R.id.navbar.register
    return render_template("register/index.html")

@register_blueprint.context_processor
def _():
    return dict(
        get_register_index_data=lambda: RegisterData(),
    )