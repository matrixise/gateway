#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.tools
    ~~~~~~~~~~~~~

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
import os
import hashlib


def save_to_disk(directory, filename, stream):
    if not os.path.exists(directory):
        os.makedirs(directory)

    absolute_path = os.path.join(directory, filename)

    with open(absolute_path, 'w') as f:
        f.write(stream)

    return absolute_path


def compute_sha(data):
    sha = hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()
