# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from src.app_factory import create_app

if __name__ == "__main__":
    from configs import default_app_config
    from configs.instance import instance_app_config

    app = create_app(
        default_app_config=default_app_config,
        instance_app_config=instance_app_config
    )
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=app.config["DEBUG"]
    )
