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
