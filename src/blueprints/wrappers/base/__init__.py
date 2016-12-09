#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

base_blueprint = Blueprint("base", __name__, static_folder="static", template_folder="templates")
