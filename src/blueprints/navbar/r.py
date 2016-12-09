#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NavbarResources:
    def __init__(self):
        self.string = self.Strings()
        self.id = self.Ids()

    class Strings:
        def __init__(self):
            self.flask_bone = "Flask-Bone"
            self.home = "Home"
            self.page_1 = "Page 1"
            self.page_2 = "Page 2"

    class Ids:
        def __init__(self):
            self.title = "title"
            self.items = "items"
            self.home = "home"
            self.page_1 = "page-1"
            self.page_2 = "page-2"


R = NavbarResources()
navbar_R = NavbarResources()