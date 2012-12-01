#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    bp_gateway
    ~~~~~~~~~~

    This module implements the Gateway Blueprint (Flask).

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
import time
from flask import render_template
from flask import request
from flask import jsonify
from flask import Blueprint
from flask import current_app

from sqlalchemy.exc import IntegrityError

import simplejson as json

from gateway.extensions import db
from gateway.exceptions import UnknownConverter

from gateway.converters import ConverterRegistry
from gateway.converters import run_converter

from gateway.models import Message
from gateway.models import Converter

from gateway.tools import save_to_disk
from gateway.tools import compute_sha

__all__ = ['blueprint']

blueprint = Blueprint('gateway', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    return render_template(
        'index.html',
        converters=ConverterRegistry.converters()
    )


def log_request(converter_name, sha, information):
    converter = Converter.query.filter_by(name=converter_name).first()
    if converter is None:
        converter = Converter(name=converter_name)
        db.session.add(converter)

    file_path = save_to_disk(current_app.config['STORAGE_PATH'],
                             sha,
                             request.data)

    msg = Message(file_path=file_path,
                  sha256=sha,
                  converter=converter,
                  connection=json.dumps(information['connection']))
    db.session.add(msg)
    db.session.commit()


def compute_all(converter_name, request):
    converter = ConverterRegistry.get(converter_name)

    sha = compute_sha(request.data)

    if converter.__format__ == 'json':
        if request.json is not None:
            information = request.json
        else:
            raise Exception("No data for a JSON Converter")
    elif converter.__format__ == 'native':
        information = dict(
            connection=dict(),
            data=request.data
        )

    return (sha, information,)


@blueprint.route('/converters/<string:converter_name>', methods=['GET', 'POST'])
def call_converter(converter_name):
    """
    :param converter_name: The Converter name
    """

    sync = 'sync' in request.args

    if converter_name not in ConverterRegistry.converters():
        raise UnknownConverter()

    if request.method == 'POST':
        sha, information = compute_all(converter_name, request)

        try:
            log_request(converter_name, sha, information)
        except IntegrityError:
            return jsonify(result='job already done'), 200

        # store in the Redis Queue
        job = current_app.queue.enqueue(run_converter,
                                        converter_name,
                                        information['connection'],
                                        information['data'])

        if sync:
            while job.result is None:
                time.sleep(0.1)

        return jsonify(result='job accepted'), 200
    else:
        query = Converter.query.filter_by(name=converter_name)
        converter = query.first()

        if not converter:
            messages = []
        else:
            messages = converter.messages

        return render_template(
            'converter_show.html',
            converter=converter_name,
            messages=messages
        )
