#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import app

if app.config["DEBUG"]:
    app.run(host='0.0.0.0', port=5000, threaded=True)
else:
    app.run()
