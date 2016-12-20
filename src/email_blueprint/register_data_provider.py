# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import g


class EmailRegisterDataProvider:
    def __init__(self):
        pass

    def get_data(self):
        return dict(
            confirm_url=g.confirm_url,
            email=g.email
        )


email_register_data_provider = EmailRegisterDataProvider()
