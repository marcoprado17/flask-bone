#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2.runtime import Undefined


def assert_defined(value):
    assert not isinstance(value, Undefined)
    return value


def assert_callable(value):
    assert callable(value)
    return value


def call(func, *args, **kwargs):
    return func(*args, **kwargs)


def if_filter(value, condition, default):
    if condition:
        return value
    return default
