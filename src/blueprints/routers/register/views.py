# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import render_template, g
from src.r import R
from src.blueprints.routers.register.index_data import RegisterData
from src.blueprints.routers.register import register_blueprint


@register_blueprint.route("/")
def index():
    g.active_navbar_item_id = R.id.navbar.register
    return render_template("register/index.html")


@register_blueprint.context_processor
def _():
    return dict(
        get_register_index_data=lambda: RegisterData(),
    )
