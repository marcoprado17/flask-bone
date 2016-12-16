# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField

from build.r import R
from flask_bombril.wtforms.validators.validators import Required, Email, Unique, Length, EqualTo
from models.user.user import User


class RegisterForm(FlaskForm):
    # TODO: After create login blueprint, set the correct url
    email = StringField(
        'Email',
        validators=[
            Required(),
            Email(),
            Unique(model=User, field=User.email,
                   message=lambda: R.string.register.email_already_registered % dict(href=url_for("home.index")))
        ])
    password = PasswordField(
        "Senha",
        validators=[
            Required(),
            Length(
                min_length=R.dimen.register.min_password_length,
                max_length=R.dimen.register.max_password_length,
                message=R.string.register.password_length % dict(
                    min_length=R.dimen.register.min_password_length,
                    max_length=R.dimen.register.max_password_length
                )
            ),
            EqualTo("password_confirmation", message=R.string.register.password_mismatch)
        ])
    password_confirmation = PasswordField(
        "Confirmação da senha",
        validators=[
            Required()
        ])
    submit = SubmitField("Cadastrar")
