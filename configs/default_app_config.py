# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================

DEBUG = False

STATIC_FOLDER = None

LOGGING_FORMAT = '[ %(levelname)8s | %(asctime)s ] - [ %(pathname)64s | %(funcName)16s | %(lineno)4d ] - %(message)s'
LOGGING_FILENAME = '/vagrant/logs/log'
LOGGING_WHEN = 'D'
LOGGING_INTERVAL = 7
LOGGING_BACKUP_COUNT = 4

SQLALCHEMY_TRACK_MODIFICATIONS = False
