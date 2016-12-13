# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

from flask import url_for, g

from build.blueprints.components.lightly_route_dependent.navbar.r import R

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
