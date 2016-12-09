#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app_factory import create_app
from configs import default_app_config
from configs.instance import instance_app_config

app = create_app(
    default_app_config=default_app_config,
    instance_app_config=instance_app_config
)