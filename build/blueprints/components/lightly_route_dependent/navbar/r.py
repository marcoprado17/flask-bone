# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================


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
