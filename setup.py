"""
Package install information.
"""

import ast
import os
import re

from distutils.core import setup

prog = re.compile(r'__version__\s*=\s*(.+)')
with open(os.path.join('CloudAuthz', '__init__.py')) as file:
    for line in file:
        match_object = prog.match(line)
        if match_object:
            version = ast.literal_eval(match_object.group(1))
            break

REQ = [
    'requests == 2.18.4'
]

setup(
    name='CloudAuthz',
    version=version,
    description='Implements means of authorization delegation on cloud-based '
                'resource providers without sharing credentials.',
    author='Vahid Jalili',
    url='https://github.com/Genometric/CloudAuthz',
    install_requires=REQ,
    license='GPLv3'
)
