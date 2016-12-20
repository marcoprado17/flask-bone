# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import render_template, g, request, redirect, url_for

from forms import RegisterForm
from models import User
from r import R
from blueprints.routers.register import register_blueprint
from email_blueprint import email_manager
from extensions import db


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

        db.session.add(
            User(
                email=g.form.email.data
            )
        )
        db.session.commit()

        email_manager.send_register_email(g.form.email.data)
        return redirect(url_for("home.index"))

@register_blueprint.route("/email-confirmado", methods=["GET"])
def email_confirmed():
    return "Email confirmado."