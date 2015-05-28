# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Originally part of Zato - open-source ESB, SOA, REST, APIs and cloud integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from unittest import TestCase

# Zato
from zato.apitest import version

class TopLevelModuleTestCase(TestCase):
    def test_version(self):
        self.assertEquals('1.9', version)
