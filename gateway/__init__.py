#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway
    ~~~~~~~

    This module implements the Gateway service.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask

from gateway.extensions import db
from gateway.extensions import bootstrap
from gateway.extensions import babel

from gateway.config import DefaultConfig

from rq import Queue, Connection

from gateway.bp_gateway import blueprint
from gateway.dashboard import dashboard as blueprint_dashboard


__all__ = ['Gateway']


class Gateway(Flask):
    """The Gateway object implements a WSGI application and acts
    as the central object. It is passed the name of the module or package
    of the application.  Once it is created it will act as a central registry
    for the converter functions, the URL rules and much more.

    The name of the package is used to resolve resources from inside the
    package or the folder the module is contained in depending on if the
    package parameter resolves to an actual python package (a folder with
    an `__init__.py` file inside) or a standard module (just a `.py` file).

    Usually you create a :class:`Gateway` instance in your main module or
    in the `__init__.py` file of your package like this::

        from gateway import Gateway
        app = Gateway(__name__)

    .. admonition:: About the First Parameter

        The idea of the first parameter is to give Flask an idea what
        belongs to your application.  This name is used to find resources
        on the file system, can be used by extensions to improve debugging
        information and a lot more.

    """
    def __init__(self, *args, **kwargs):
        config = kwargs.pop('config', None)
        Flask.__init__(self, *args, **kwargs)

        self.config.from_object(DefaultConfig())

        if config is None:
            self.config.from_object(config)

        with Connection():
            self.queue = Queue()

        self.configure_extensions()

        self.register_blueprint(blueprint)
        self.register_blueprint(blueprint_dashboard, url_prefix="/rq")

    def configure_extensions(self):
        """
        configure the extensions for the Gateway app
        """
        db.init_app(self)
        bootstrap.init_app(self)
        babel.init_app(self)
