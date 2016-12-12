# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
#
"""
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

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

    from flask import redirect

    @app.route("/")
    def home_redirect():
        return redirect("home")

    # Registering blueprints
    from build.blueprints.routers.home.views import home_blueprint
    app.register_blueprint(home_blueprint, url_prefix="/home")
    from build.blueprints.wrappers.base import base_blueprint
    app.register_blueprint(base_blueprint, url_prefix="/base")
    from build.blueprints.components.lightly_route_dependent.navbar import navbar_blueprint
    app.register_blueprint(navbar_blueprint, url_prefix="/navbar")

    # Registering jinja filters
    from build.flask_bombril.jinja.filters import assert_defined, assert_callable, call, if_filter
    app.jinja_env.filters['assert_defined'] = assert_defined
    app.jinja_env.filters['assert_callable'] = assert_callable
    app.jinja_env.filters['call'] = call
    app.jinja_env.filters['if'] = if_filter

    # Registering lightly route dependent components context_processors
    from build.blueprints.components.lightly_route_dependent.navbar.data import NavbarData

    @app.context_processor
    def _():
        return dict(
            get_navbar_data=lambda: NavbarData(),
        )

    return app
