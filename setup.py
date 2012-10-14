#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gateway
-------

    :copyright: (c) 2012 - Stephane Wirtel <stephane@wirtel.be>
    :license: BSD, see LICENSE for more details
"""
import sys
from setuptools import setup
from setuptools import find_packages

if not hasattr(sys, 'version_info') or sys.version_info < (2, 6, 0, 'final'):
    raise SystemExit("Gateway requires Python 2.6 or later.")

with open('README.rst') as f:
    README = f.read()

with open('CHANGES') as f:
    CHANGES = f.read()

setup(
    name                 = 'Gateway',
    version              = '0.2dev',
    url                  = 'http://github.com/matrixise/gateway/',
    license              = 'BSD',
    description          = 'Gateway is a Converter tools based on Redis Queue and WSGI',
    long_description     = README + '\n' + CHANGES,
    author               = 'Stephane Wirtel',
    author_email         = 'stephane@wirtel.be',
    packages             = find_packages(),
    include_package_data = True,
    zip_safe             = False,
    platforms            = 'any',
    install_requires    = [
    'Flask',
    'Flask-Bootstrap',
    'Flask-Rq',
    'Flask-SQLAlchemy',
    'Flask-Babel',
    'Flask-Script',
    'rq',
    'rq-dashboard',
    ],
    entry_points      = """
    [console_scripts]
    gateway = gateway.scripts.gateway:main
    """,
    classifiers       = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
