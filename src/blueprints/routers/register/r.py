# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================


class RegisterResources:
    def __init__(self):
        self.string = self.__Strings()
        self.id = self.__Ids()
        self.dimen = self.__Dimen()

    class __Strings:
        def __init__(self):
            self.email_already_registered = \
                "Email já cadastrado. Para entrar com este email, clique <a href='%(href)s'>aqui</a>."
            self.password_mismatch = "As senhas digitadas não são iguais."
            self.password_length = "A senha deve possuir entre %(min_length)d e %(max_length)d caracteres."

    class __Ids:
        def __init__(self):
            self.example = "example"

    class __Dimen:
        def __init__(self):
            self.min_password_length = 6
            self.max_password_length = 32


R = RegisterResources()
register_R = RegisterResources()
