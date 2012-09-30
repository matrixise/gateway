#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gateway
-------

    :copyright: (c) 2012 - Stephane Wirtel <stephane@wirtel.be>
    :license: BSD, see LICENSE for more details

::
    
    from gateway import Gateway
    from gateway.converters import BaseConverter

    class SendByMailConverter(BaseConverter):
        __name__ = 'send_by_mail'

        def run(self, converter, request, data):
            return True


    def application(config=None):
        gateway = Gateway(__name__, config=config)
        return gateway


    def main():
        app = application()
        app.run()

    if __name__ == '__main__':
        main()

::

    $ pip install Gateway
    $ python gateway_server.py

"""
import sys
from setuptools import setup
from setuptools import find_packages

if not hasattr(sys, 'version_info') or sys.version_info < (2, 6, 0, 'final'):
    raise SystemExit("Gateway requires Python 2.6 or later.")

with open('README') as f:
    README = f.read()

with open('CHANGES') as f:
    CHANGES = f.read()

setup(
    name                 = 'Gateway',
    version              = '0.1dev',
    url                  = 'http://github.com/matrixise/gateway/',
    license              = 'BSD',
    description          = 'Gateway is a WSGI layer over Redis Queue with workers',
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
