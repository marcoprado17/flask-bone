# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import Flask

def create_app(configs):
    static_folder = None
    for config in configs:
        if hasattr(config, 'STATIC_FOLDER'):
            static_folder = config.STATIC_FOLDER
    app = Flask(__name__, instance_relative_config=True, static_folder=static_folder)
    for config in configs:
        app.config.from_object(config)
    return app