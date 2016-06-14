#!/usr/bin/python
#coding=utf-8

__author__ = 'linpelvis'

import logging

from arthas_web.services.business.utils import _get_normalization_data

logger = logging.getLogger(__name__)

def switch(type):
    return {
        'default' :  '*',
    }[type]

class TestApp(object):
    NAME = 'test'

    def _get_user(self, type):
        if type is None:
            type = 'default'
        fields = switch(type)
        SQL = 'select %s from test.user ' % (fields)
        return _get_normalization_data(SQL)



