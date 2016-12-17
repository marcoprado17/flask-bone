# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import render_template, g, request, redirect, url_for

from forms import RegisterForm
from r import R
from index_data import RegisterData
from blueprints.routers.register import register_blueprint
from emails import email_manager


@register_blueprint.route("/", methods=["GET", "POST"])
def index():
    g.active_navbar_item_id = R.id.navbar.register
    g.form = RegisterForm()

    # GET
    if request.method == "GET":
        return render_template("register/index.html")
    # POST
    else:
        if not g.form.validate_on_submit():
            return render_template("register/index.html")

        email_manager.send_register_email()
        return redirect(url_for("home.index"))

@register_blueprint.context_processor
def _():
    return dict(
        get_register_index_data=lambda: RegisterData(),
    )
