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
from r import R
from flask_bombril.form_validators import Required, EmailFormat, Unique, Length, EqualTo
from models import User


class RegisterForm(FlaskForm):
    # TODO: After create login blueprint, set the correct url
    email = StringField(
        R.string.register.email_label,
        validators=[
            Required(),
            EmailFormat(),
            Unique(model=User, field=User.email,
                   message=lambda: R.string.register.email_already_registered % dict(href=url_for("home.index"))),
            Length(max_length=R.dimen.models.user.email_max_length)
        ])
    password = PasswordField(
        R.string.register.password_label,
        validators=[
            Required(),
            Length(
                min_length=R.dimen.models.user.password_min_length,
                max_length=R.dimen.models.user.password_max_length,
                message=R.string.register.password_length % dict(
                    min_length=R.dimen.models.user.password_min_length,
                    max_length=R.dimen.models.user.password_max_length
                )
            ),
            EqualTo("password_confirmation", message=R.string.register.password_mismatch)
        ])
    password_confirmation = PasswordField(
        R.string.register.password_confirmation_label,
        validators=[
            Required()
        ])
    submit = SubmitField(R.string.register.register)
