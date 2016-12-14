# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from flask import Flask


def create_app(default_app_config, instance_app_config):
    static_folder = None
    if hasattr(default_app_config, 'STATIC_FOLDER'):
        static_folder = default_app_config.STATIC_FOLDER
    if hasattr(instance_app_config, 'STATIC_FOLDER'):
        static_folder = instance_app_config.STATIC_FOLDER
    app = Flask(__name__, instance_relative_config=True, static_folder=static_folder)

    app.config.from_object(default_app_config)
    app.config.from_object(instance_app_config)

    return app
