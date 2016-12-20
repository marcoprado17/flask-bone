# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import Blueprint
from index_data_provider import register_index_data_provider


register_blueprint = Blueprint("register", __name__, static_folder="static", template_folder="templates")


@register_blueprint.context_processor
def _():
    return dict(
        get_register_index_data=lambda: register_index_data_provider.get_data(),
    )

import views
