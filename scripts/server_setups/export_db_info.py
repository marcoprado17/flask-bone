# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

import sys
sys.path.insert(0, "/vagrant")
from configs.instance import instance_app_config

assert hasattr(instance_app_config, "DB_USERNAME"), "instance_app_config must have DB_USERNAME"
assert hasattr(instance_app_config, "DB_PASSWORD"), "instance_app_config must have DB_PASSWORD"
assert hasattr(instance_app_config, "TEST_DB_NAME"), "instance_app_config must have TEST_DB_NAME"
assert hasattr(instance_app_config, "PRODUCTION_DB_NAME"), "instance_app_config must have PRODUCTION_DB_NAME"

text_file = open("scripts/server_setups/export_db_info_result.txt", "w")
text_file.writelines([
    "DB_USERNAME='%s'\n" % instance_app_config.DB_USERNAME,
    "DB_PASSWORD='%s'\n" % instance_app_config.DB_PASSWORD,
    "TEST_DB_NAME='%s'\n" % instance_app_config.TEST_DB_NAME,
    "PRODUCTION_DB_NAME='%s'\n" % instance_app_config.PRODUCTION_DB_NAME])
text_file.close()
