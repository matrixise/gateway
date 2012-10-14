#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.examples.worker
    ~~~~~~~~~~~~~~~~~~~~~~~

    This module implements the worker.

    :copyright: (c) 2012 by Stephane Wirtel <stephane@wirtel.be>.
    :license: BSD, see LICENSE for more details.
"""
from rq import Queue, Worker, Connection
from main import SendByMailConverter


def main():
    """
    call the Redis Queue connection and run the worker
    """
    with Connection():
        q = Queue()
        Worker(q).work()


if __name__ == '__main__':
    main()
