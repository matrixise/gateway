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
from gateway.exceptions import UnknownFormat

__all__ = [
    'ConverterRegistry',
    'BaseConverter',
    'run_converter',
]


class ConverterRegistry(object):
    """
    The ConverterRegistry will be used as a singleton object in which one 
    we add all the registered converters 
    """

    #: The __converters is a dictionary where we store the name of the converter 
    #: with its class.
    __converters = dict()

    @classmethod
    def converters(cls):
        """
        return the name list of the registered converters
        """
        return cls.__converters.keys()

    @classmethod
    def add(cls, name, klass, options=None):
        """
        Add the converter in the registry

        :param klass: a subclass of the :class:`BaseConverter`

        :returns: the subclass of the :class:`BaseConverter`
        """
        if name in cls.__converters:
            raise AlreadyExistsConverter()

        if options is None:        
            options = dict()

        cls.__converters[name] = (klass, options)
        return klass

    @classmethod
    def get(cls, name):
        """
        Return the associated Converter

        :param name: The name of a converter
        :raises: :class:`~gateway.exceptions.NotFoundConverter` if the given name is not in the register
        """
        if not name in cls.__converters:
            raise NotFoundConverter()
        return cls.__converters[name][0]

    @classmethod
    def get_options(cls, name):
        if not name in cls.__converters:
            raise NotFoundConverter()
        return cls.__converters[name][1]

class ConverterMeta(type):
    """
    :param __name__: The name of the Converter
    :type __format__: string

    :param __format__: The format of the request (native, json)
    :type __format__: string

    :raises: Exception If there is no name for the converter
    :raises: :class:`gateway.exceptions.UnknownFormat` if the format of the converter is unknown.

    .. versionadded:: 0.2
        The param `__format__` has been introduced to use `curl <http://curl.org>`_ 
        or `httpie <http://httpie.org>`_.

    """

    FORMATS = ['json', 'native']
    def __new__(mcs, classname, bases, classdict):
        if classname == 'BaseConverter':
            return type.__new__(mcs, classname, bases, classdict)

        options = dict(
            name=classdict.get('__name__', False) or False,
            format=classdict.get('__format__', 'native') or 'native'
        )

        if not options['name']:
            raise Exception("There is no name for this converter")

        if options['format'] not in ConverterMeta.FORMATS:
            raise UnknownFormat(name, format)

        thisKlass = type.__new__(mcs, classname, bases, classdict)

        #: We add the new class in the registry
        ConverterRegistry.add(options['name'], thisKlass, options)
    
        return thisKlass


class BaseConverter(object):
    """
    The BaseConverter object implements the concept of Converter

    Here is an example::

        class MyConverter(BaseConverter):
            "This converter is very useful to convert from XXX to YYY."

            __name__ = 'my_converter'
            __format__ = 'json'
            def run(self, converter, request, data):
                return True
    """
    __metaclass__ = ConverterMeta


def run_converter(converter, request, data):
    """
    call the converter and pass the request and the data

    :param converter: the converter name 
    :param request: the request dictionnary (routing)
    :param data: the data to process
    :rtype: a subclass of :class:`~gateway.converters.Converter`
    """
    klass = ConverterRegistry.get(converter)
    return klass().run(converter, request, data)
