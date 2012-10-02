#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    gateway.examples.client
    ~~~~~~~~~~~~~~~~~~~~~~~

    Here is an example, how to implement the client who push the data via 
    a JSON serializer to the Gateway
"""
import sys
import datetime
import requests

try:
    import simplejson as json
except ImportError:
    import json

def main():
    GATEWAY_URL = 'http://localhost:5000/converters/send_by_mail'
    jsoned_values = json.dumps({
        'connection' : {
            'host' : 'localhost',
            'port' : '5000',
        }, 
        'data' : {
            'text' : 'this is a test', 
            'timestamp' : datetime.datetime.now(),
        }
    })

    headers = {
        'Content-Type' : 'application/json',
    }

    query = requests.post(GATEWAY_URL,
                          data=jsoned_values,
                          headers=headers,
                          config={'verbose' : sys.stderr}
                         )

if __name__ == '__main__':
    main()
