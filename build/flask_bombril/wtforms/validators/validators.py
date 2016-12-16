# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import gettext
import re

from wtforms.validators import InputRequired, Regexp, HostnameValidation, ValidationError, StopValidation

from flask_bombril.exceptions import InvalidFieldError
from flask_bombril.r import R


def raise_with_stop(validator, message=None):
    if validator.stop:
        if message:
            raise StopValidation(message)
        else:
            raise StopValidation(validator.message)
    else:
        if message:
            raise ValidationError(message)
        else:
            raise ValidationError(validator.message)


class Required(InputRequired):
    def __init__(self):
        self.message = R.string.validators.required_field
        super(Required, self).__init__(message=self.message)


class Email(Regexp):
    def __init__(self, stop=True):
        self.message = R.string.validators.invalid_email_format
        self.stop = stop
        self.validate_hostname = HostnameValidation(
            require_tld=True,
        )
        super(Email, self).__init__(r"^.+@([^.@][^@]+)$", re.IGNORECASE, self.message)

    def __call__(self, form, field, message=None):
        try:
            match = super(Email, self).__call__(form, field)
            if not self.validate_hostname(match.group(1)):
                raise_with_stop(self)
        except (ValidationError, StopValidation):
            raise_with_stop(self)


class Unique(object):
    def __init__(self, model, field, message=R.string.validators.unique_field, stop=True):
        self.message = message
        self.model = model
        self.field = field
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise_with_stop(self)


class Length(object):
    def __init__(self, min_length=-1, max_length=-1, message=None, stop=True):
        assert min_length >= -1 and max_length >= -1
        assert min_length != -1 or max_length != -1
        assert max_length == -1 or min_length <= max_length
        self.min = min_length
        self.max = max_length
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            message = self.message
            if message is None:
                if self.max == -1:
                    message = gettext.ngettext(
                        R.string.validators.field_min_length_singular,
                        R.string.validators.field_min_length_plural,
                        self.min) % dict(min_length=self.min)
                elif self.min == -1:
                    message = gettext.ngettext(
                        R.string.validators.field_max_length_singular,
                        R.string.validators.field_max_length_plural,
                        self.max) % dict(max_length=self.max)
                else:
                    message = R.string.validators.field_length_range % dict(min_length=self.min, max_length=self.max)

            raise_with_stop(self, message=message)


class EqualTo(object):
    def __init__(self, field_name, message=None, stop=True):
        self.field_name = field_name
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        try:
            other = form[self.field_name]
        except KeyError:
            message = R.string.validators.invalid_field_name % dict(field_name=self.field_name)
            raise InvalidFieldError(message)
        if field.data != other.data:
            message = self.message
            if message is None:
                message = R.string.validators.field_must_be_equal_to % dict(other_name=self.field_name)
            raise_with_stop(self, message=message)
