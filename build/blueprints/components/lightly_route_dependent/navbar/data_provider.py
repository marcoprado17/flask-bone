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
class NavbarDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return dict(
            title=R.string.navbar.micro_blog,
            left_items=[
                dict(
                    text=R.string.navbar.home,
                    href=url_for("home.index"),
                    active=self.is_active(R.id.navbar.home)
                ),
                dict(
                    text=R.string.navbar.posts,
                    href="#",
                    active=self.is_active(R.id.navbar.posts)
                )
            ],
            right_items=[
                dict(
                    text=R.string.navbar.login,
                    href="#",
                    active=self.is_active(R.id.navbar.login)
                ),
                dict(
                    text=R.string.navbar.register,
                    href=url_for("register.index"),
                    active=self.is_active(R.id.navbar.register)
                )
            ]
        )

    # noinspection PyMethodMayBeStatic
    def is_active(self, id_):
        return True if id_ == g.active_navbar_item_id else False


navbar_data_provider = NavbarDataProvider()
