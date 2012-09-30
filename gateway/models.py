#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.models
    ~~~~~~~~~~~~~~

    This module implements the models

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
import datetime
from gateway.extensions import db


class Converter(db.Model):
    """
    Stores the converters, for the relationship with the message model defined
    below.
    """
    id = db.Column(db.Integer, primary_key=True)

    #: the date when the converter has been inserted in the table
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )

    #: name of the converter, have to be unique and non nullable
    name = db.Column(
        db.String(256),
        unique=True,
        nullable=False
    )


class Message(db.Model):
    """
    Stores the messages for the history of the application.
    """
    id = db.Column(db.Integer, primary_key=True)

    #: the creation date of the message
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )

    #: where the file is stored
    file_path = db.Column(
        db.String(256),
        nullable=False
    )

    #: the digital signature of the message (SHA-256)
    sha256 = db.Column(
        db.String(64),
        nullable=False,
        unique=True
    )

    #: Json Field
    #: the system is agnostic with the connection parameters, so, we store 
    #: the information in the database to replay it if there is a problem.
    connection = db.Column(
        db.Text,
        nullable=False
    )

    #: the relation to the converter
    converter_id = db.Column(
        db.Integer,
        db.ForeignKey('converter.id'),
        nullable=False
    )
    converter = db.relationship(
        'Converter',
        backref=db.backref('messages', lazy='dynamic')
    )
