#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

navbar_blueprint = Blueprint("navbar", __name__, static_folder="static", template_folder="templates")