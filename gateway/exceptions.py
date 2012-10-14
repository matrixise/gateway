#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.exceptions
    ~~~~~~~~~~~~~~~~~~

    This module implements the interface for the specific Exceptions.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""

# Use this exception if the asked converted does not exists
# in the ConverterRegistry
class UnknownConverter(Exception):
    """
    This exception is used by the ConverterRegistry and will be raised if the converter does not exists
    """
    def __init__(self, name=None):
        text = name if name else "UnknownConverter"
        super(UnknownConverter, self).__init__(text)


class AlreadyExistsConverter(Exception):
    pass


class NotFoundConverter(Exception):
    pass

class UnknownFormat(Exception):
    def __init__(self, name, format):
        super(UnknownFormat, self).__init__("Unknown format (%s) for the (%s) converter" % 
                                            (format, name))
