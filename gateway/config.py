#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.config
    ~~~~~~~~~~~~~~

    This module implements the default configuration.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
import os


class DefaultConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gateway.db'
    SQLALCHEMY_ECHO = True
    DEBUG = True

    STORAGE_PATH = os.path.abspath(os.path.join(os.getcwd(), 'filestore'))

    BABEL_DEFAULT_LOCALE = 'en_US'

    PROJECT_URL = 'http://localhost:5000'


#class ProductionConfig(DefaultConfig):
#    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://localhost:5432/gateway'
#    SQLALCHEMY_ECHO = False
#    DEBUG = False
