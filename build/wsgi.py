# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from build.app_factory import create_app
from configs import default_app_config
from configs.instance import instance_app_config

app = create_app(
    default_app_config=default_app_config,
    instance_app_config=instance_app_config
)
