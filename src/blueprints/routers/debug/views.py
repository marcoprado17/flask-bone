# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from blueprints.routers.debug import debug_blueprint
from extensions import db

@debug_blueprint.route("/db/restart")
def restart_db():
    db.drop_all()
    db.create_all()
    return "Db reiniciado."
