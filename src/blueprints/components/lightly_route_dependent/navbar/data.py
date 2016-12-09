#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import url_for, g

from blueprints.components.lightly_route_dependent.navbar.r import R


class NavbarData:
    def __init__(self):
        self.title = R.string.flask_bone
        self.items = [
            self.__ItemData(R.id.home, R.string.home, url_for("home.index"), self.is_active(R.id.home)),
            self.__ItemData(R.id.home, R.string.home, url_for("home.index"), self.is_active(R.id.home)),
            self.__ItemData(R.id.home, R.string.home, url_for("home.index"), self.is_active(R.id.home))
        ]

    class __ItemData:
        def __init__(self, id_, text, href, active):
            self.id = id_
            self.text = text
            self.href = href
            self.active = active

    # noinspection PyMethodMayBeStatic
    def is_active(self, id_):
        return True if id_ == g.active_navbar_item_id else False
