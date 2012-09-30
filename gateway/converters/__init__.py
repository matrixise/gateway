#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.converters
    ~~~~~~~~~~~~~~~~~~

    This module implements the management interface.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
from gateway.exceptions import AlreadyExistsConverter
from gateway.exceptions import NotFoundConverter

__all__ = ['ConverterRegistry', 'run_converter']


class ConverterRegistry(object):
    __converters = dict()

    @classmethod
    def converters(cls):
        return cls.__converters.keys()

    @classmethod
    def add(cls, name, klass):
        """
        Add the converter in the registry
        """
        if name in cls.__converters:
            #"This converter is already defined in the registry")
            raise AlreadyExistsConverter()
        cls.__converters[name] = klass
        return klass

    @classmethod
    def get(cls, name):
        """
        Return the associated Converter
        """
        if not name in cls.__converters:
            raise NotFoundConverter()
        return cls.__converters[name]


class ConverterMetaClass(type):
    def __new__(cls, classname, bases, classdict):
        base_converter = classdict.get('_base_converter', False) or False

        if not base_converter:
            name = classdict.get('__name__', False) or False

            if not name:
                raise Exception("There is no name for this converter")

        thisKlass = type.__new__(cls, classname, bases, classdict)
        if not base_converter:
            ConverterRegistry.add(name, thisKlass)

        return thisKlass


class BaseConverter(object):
    _base_converter = True
    __metaclass__ = ConverterMetaClass


def run_converter(converter, request, data):
    """
    call the converter and pass the request and the data

    :param converter: the converter name 
    :param request: the request dictionnary (routing)
    :param data: the data to process
    """
    klass = ConverterRegistry.get(converter)
    return klass().run(converter, request, data)
