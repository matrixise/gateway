#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.extensions
    ~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.babel import Babel

db = SQLAlchemy()
bootstrap = Bootstrap()
babel = Babel()
