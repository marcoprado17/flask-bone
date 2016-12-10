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

# TODO: Update r.py template


class NavbarResources:
    def __init__(self):
        self.string = self.__Strings()
        self.id = self.__Ids()

    class __Strings:
        def __init__(self):
            self.micro_blog = "Micro Blog"
            self.home = "Home"
            self.posts = "Posts"
            self.add_post = "Adicionar Post"
            self.view_posts = "Visualizar Posts"
            self.categories = "Categorias"
            self.add_category = "Adicionar Categoria"
            self.subcategories = "Subcategorias"
            self.add_subcategory = "Adicionar Subcategoria"
            self.enter = "Entrar"
            self.register = "Cadastrar"
            self.leave = "Sair"

    class __Ids:
        def __init__(self):
            self.home = "home"
            self.posts = "posts"
            self.categories = "categories"
            self.subcategories = "subcategories"

R = NavbarResources()
navbar_R = NavbarResources()
