#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import url_for, g

from blueprints.navbar.r import R


class NavbarDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return dict(
            title=R.string.flask_bone,
            items=[
                self.get_item(R.id.home, R.string.home, url_for("home.index"), self.is_active(R.id.home)),
                self.get_item(R.id.home, R.string.home, url_for("home.index"), self.is_active(R.id.home)),
                self.get_item(R.id.home, R.string.home, url_for("home.index"), self.is_active(R.id.home))
            ]
        )

    def get_item(self, id, text, href, active):
        return dict(
            id=id,
            text=text,
            href=href,
            active=active
        )

    def is_active(self, id):
        return True if id == g.active_navbar_item_id else False