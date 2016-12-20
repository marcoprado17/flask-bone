# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================


class Resources:
    def __init__(self):
        self.string = self.__Strings()
        self.id = self.__Ids()
        self.dimen = self.__Dimens()

    class __Strings:
        def __init__(self):
            self.navbar = self.__Navbar()
            self.register = self.__Register()
            self.email = self.__Email()
            self.micro_blog = "Micro Blog"

        class __Navbar:
            def __init__(self):
                self.home = "Home"
                self.posts = "Posts"
                self.add_post = "Adicionar Post"
                self.view_posts = "Visualizar Posts"
                self.categories = "Categorias"
                self.add_category = "Adicionar Categoria"
                self.subcategories = "Subcategorias"
                self.add_subcategory = "Adicionar Subcategoria"
                self.login = "Entrar"
                self.register = "Cadastrar"
                self.leave = "Sair"

        class __Register:
            def __init__(self):
                self.email_already_registered = \
                    "Email já cadastrado. Para entrar com este email, clique <a href='%(href)s'>aqui</a>."
                self.password_mismatch = "As senhas digitadas não são iguais."
                self.password_length = "A senha deve possuir entre %(min_length)d e %(max_length)d caracteres."
                self.email_label = "Email"
                self.password_label = "Senha"
                self.password_confirmation_label = "Confirmação da senha"
                self.register = "Cadastrar"
                self.already_has_account = "Já possui conta?"
                self.title = "Cadastro"

        class __Email:
            def __init__(self):
                self.register = self.__Register()

            class __Register:
                def __init__(self):
                    self.welcome = "Olá!"
                    self.confirm_email = "Deseja utilizar <u>%(email)s</u> como seu email principal na %(title)s?"
                    self.confirm_button_text = "Sim, desejo utilizar este email"
                    self.subject = "Confirme seu endereço de e-mail | %(title)s"

    class __Ids:
        def __init__(self):
            self.navbar = self.__Navbar()
            self.register = self.__Register()

        class __Navbar:
            def __init__(self):
                self.home = "home"
                self.posts = "posts"
                self.categories = "categories"
                self.subcategories = "subcategories"
                self.register = "register"
                self.login = "login"

        class __Register:
            def __init__(self):
                self.example = "example"

    class __Dimens:
        def __init__(self):
            self.navbar = self.__Navbar()
            self.register = self.__Register()
            self.models = self.__Models()

            self.default_password_field_max_length = 256
            self.default_string_field_max_length = 1024

        class __Navbar:
            def __init__(self):
                self.example = 42

        class __Register:
            def __init__(self):
                self.example = 42

        class __Models:
            def __init__(self):
                self.user = self.__User()

            class __User:
                def __init__(self):
                    self.email_max_length = 256
                    self.password_min_length = 6
                    self.password_max_length = 32


R = Resources()
