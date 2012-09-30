#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.examples.main
    ~~~~~~~~~~~~~~~~~~~~~

    Here is an example, how to implement a basic converter to send a JSON 
    request to a mail server

    :copyright: (c) 2012 - Stephane Wirtel <stephane@wirtel.be>
    :license: BSD, see LICENSE for more details.
"""
from gateway import Gateway
from gateway.converters import BaseConverter

class SendByMailConverter(BaseConverter):
    """
    This converter receives a JSON format and send it by mail
    """
    __name__ = 'send_by_mail'

    def run(self, converter, request, data):
        return True


def application(config=None):
    """
    used by a WSGI server (ex: gunicorn)
    """
    return Gateway(__name__, config=config)


def main():
    """Call the application function and execute the WSGI application"""
    app = application()
    app.run()

if __name__ == '__main__':
    """used by a standalone version"""
    main()
