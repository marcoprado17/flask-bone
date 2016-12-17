# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import unittest

from flask_bombril.utils import get_test_suite_from_test_cases
from build.flask_bombril.wtforms.validators.email_format.test_case import TestCase as EmailFormatTestCase
from build.flask_bombril.wtforms.validators.equal_to.test_case import TestCase as EqualToTestCase
from length.test_case import TestCase as LengthTestCase
from required.test_case import TestCase as RequiredTestCase
from unique.test_case_invalid_inputs import TestCaseInvalidInputs as UniqueTestCaseInvalidInputs
from unique.test_case_valid_inputs import TestCaseValidInputs as UniqueTestCaseValidInputs

test_suite = get_test_suite_from_test_cases([
    EmailFormatTestCase,
    EqualToTestCase,
    LengthTestCase,
    RequiredTestCase,
    UniqueTestCaseInvalidInputs,
    UniqueTestCaseValidInputs
])

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(test_suite)
