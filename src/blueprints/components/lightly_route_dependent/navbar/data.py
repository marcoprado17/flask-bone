# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import url_for, g
from r import R


# TODO: After implement user management and user permissions, provide navbar data according to the user in question
class NavbarData:
    def __init__(self):
        self.title = R.string.navbar.micro_blog
        self.left_items = [
            NavbarItemData(R.string.navbar.home, url_for("home.index"), self.is_active(R.id.navbar.home)),
            # TODO: Add correct href after declaring the blueprints
            NavbarItemData(R.string.navbar.posts, "#", self.is_active(R.id.navbar.posts)),
        ]
        self.right_items = [
            NavbarItemData(R.string.navbar.login, "#", self.is_active(R.id.navbar.login)),
            NavbarItemData(R.string.navbar.register, url_for("register.index"), self.is_active(R.id.navbar.register)),
        ]

    # noinspection PyMethodMayBeStatic
    def is_active(self, id_):
        return True if id_ == g.active_navbar_item_id else False


class NavbarItemData:
    def __init__(self, text, href, active=False):
        self.text = text
        self.href = href
        self.active = active
