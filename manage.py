#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    manage.py
    ~~~~~~~~~

    This module implements the management interface.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app
from flask.ext.script import Manager
from gateway import create_app
from gateway.extensions import db
import gateway.models

def main():
    """
    create a CLI with some options
    """
    manager = Manager(create_app)

    @manager.command
    def db_create():
        db.create_all()

    @manager.command
    def db_drop():
        db.drop_all()

    @manager.command
    def routes():
        print current_app.url_map

    manager.run()


if __name__ == '__main__':
    main()
