# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import g


class RegisterIndexDataProvider:
    def __init__(self):
        pass


    def get_data(self):
        return dict(
            form=g.form
        )


register_index_data_provider = RegisterIndexDataProvider()
