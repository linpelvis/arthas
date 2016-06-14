#!/usr/bin/python
#coding=utf-8
__author__ = 'linpelvis'

import httplib
import json

from arthas_web.settings import DEBUG
from arthas_web.utils import json_encode_datetime
from django.http import HttpResponse


def json_response(func):
    '''
    Wraps the return value of the parent as a JSON response.
    '''
    def json_responsed(*args, **kwargs):
        retval = func(func.__name__, *args, **kwargs)
        if not isinstance(retval, HttpResponse):
            status_code = httplib.OK
            if isinstance(retval, dict) and 'http_status' in retval:
                status_code = retval['http_status']
                del retval['http_status']
            if not DEBUG and status_code >= 400:
                content = ''
            else:
                content = json.dumps(retval, default=json_encode_datetime)
            response = HttpResponse(content, content_type='application/json; charset=utf-8', status=status_code)
        else:
            response = retval
        return response
    return json_responsed