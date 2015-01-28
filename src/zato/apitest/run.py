# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# Originally part of Zato - open-source ESB, SOA, REST, APIs and cloud integrations in Python
# https://zato.io

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import os
import sys
import re

global extra_behave_options
extra_behave_options = ''
args_parsed = []
for idx, arg in enumerate(sys.argv):
    if re.match("--behave_options", arg):
	extra_behave_options += " " + re.sub(r'--behave_options=', '', arg)
	args_parsed.append(arg)
    if re.match("-b", arg):
	extra_behave_options += " " + sys.argv[idx + 1]
	args_parsed.append(arg)
	args_parsed.append(sys.argv[idx + 1])

for arg in args_parsed:
    sys.argv.remove(arg)

# Behave
from behave.configuration import Configuration
from behave.runner import Runner

# ConfigObj
from configobj import ConfigObj

def handle(path):
    file_conf = ConfigObj(os.path.join(path, 'features', 'config.ini'))
    behave_options = file_conf['behave']['options'] + extra_behave_options

    conf = Configuration(behave_options)
    conf.paths = [os.path.join(path, 'features')]
    runner = Runner(conf)
    runner.run()
