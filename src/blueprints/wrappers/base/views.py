#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

shared_blueprint = Blueprint("base", __name__, static_folder="static", template_folder="templates")
