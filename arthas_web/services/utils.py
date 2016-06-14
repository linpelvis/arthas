#!/usr/bin/python
# coding=utf-8

import simplejson as simplejson

def get_request_data(request_data):
    data = {}
    for key in request_data.keys():
        data[key.lower()] = request_data.get(key)
    return simplejson.dumps(data)


def check_get_method(method):
    if method != 'GET':
        return 'request method error'