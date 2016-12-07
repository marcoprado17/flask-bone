#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

jquery_blueprint = Blueprint("jquery", __name__, static_folder="static", template_folder="templates")
