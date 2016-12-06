#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, url_for

home_blueprint = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@home_blueprint.route("/")
def home():
    data = dict(img_src=url_for("home.static", filename="img/let_the_adventure_begin.jpg"))
    return render_template("home/home.html", data=data)
