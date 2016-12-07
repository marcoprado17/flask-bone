#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

home_blueprint = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@home_blueprint.route("/")
def home():
    return render_template("home/home.html")
