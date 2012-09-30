#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.py
    ~~~~~~~~~~

    This module implements the management interface.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys

from flask.ext.script import Manager, Server
from ..extensions import db
from ..models import Converter, Message


def import_app(module):
    parts = module.split(":", 1)
    if len(parts) == 1:
        module, obj = module, "application"
    else:
        module, obj = parts[0], parts[1]

    try:
        __import__(module)
    except ImportError:
        if module.endswith(".py") and os.path.exists(module):
            raise ImportError("Failed to find application, did "
                "you mean '%s:%s'?" % (module.rsplit(".", 1)[0], obj))
        else:
            raise

    mod = sys.modules[module]
    app = eval(obj, mod.__dict__)
    if app is None:
        raise ImportError("Failed to find application object: %r" % obj)
    if not callable(app):
        raise TypeError("Application object must be callable.")
    return app

# print "os.getcwd: %r" % (os.getcwd())
sys.path.append(os.getcwd())


class CustomManager(Manager):
    # def __init__(self, *args, **kwargs):
    #     super(CustomManager, self).__init__(*args, **kwargs)

    def create_app(self, **kwargs):
        if 'custom_app' in kwargs:
            module = kwargs.pop('custom_app')
            self.app = import_app(module)
        return super(CustomManager, self).create_app(**kwargs)


def main():
    """
    create a CLI with some options
    """

    manager = CustomManager(None)
    manager.add_option('-a', '--app', dest='custom_app', required=True)
    manager.add_command('run', Server())

    @manager.command
    def db_create():
        db.create_all()

    manager.run()

if __name__ == '__main__':
    main()
