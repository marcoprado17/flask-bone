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

from flask import url_for, g

from src.blueprints.components.lightly_route_dependent.navbar.r import R

# TODO: After implement user management and user permissions, provide navbar data according to the user in question


class NavbarData:
    def __init__(self):
        self.title = R.string.micro_blog
        self.left_items = [
            NavbarItemData(R.string.home, url_for("home.index"), self.is_active(R.id.home)),
            # TODO: Add correct href after declaring the blueprints
            NavbarItemData(R.string.posts, "#", self.is_active(R.id.posts)),
        ]
        self.right_items = [
            NavbarItemData(R.string.enter, "#"),
            NavbarItemData(R.string.register, "#"),
        ]

    # noinspection PyMethodMayBeStatic
    def is_active(self, id_):
        return True if id_ == g.active_navbar_item_id else False


class NavbarItemData:
    def __init__(self, text, href, active=False):
        self.text = text
        self.href = href
        self.active = active
