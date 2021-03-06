# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from r import R
from extensions import bcrypt, db

from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    email = db.Column(db.String(R.dimen.models.user.email_max_length), primary_key=True, unique=True)
    _password = db.Column(db.String(R.dimen.models.user.password_max_length))
    email_confirmed = db.Column(db.Boolean, default=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)