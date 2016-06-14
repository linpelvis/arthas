#!/usr/bin/python
#coding=utf-8

import simplejson

from arthas_web.services.business.app import APP_PROVIDER

__author__ = 'linpelvis'

import logging

logger = logging.getLogger(__name__)

class BusinessServiceHandler(object):

    def __init__(self, conf):
        self.dispatch = {}
        for key in conf:
            self.dispatch[key.lower()] = getattr(self, 'get_' + key)

    def get_user(self, app_name, data, ext=''):
        logger.info('get_user . '
                    'app_name: %s, data: %s, ext: %s', app_name, data, ext)
        try:
            params = simplejson.loads(data)
            app = APP_PROVIDER[app_name]
            ret = app._get_user(params.get('type'))
        except Exception as e:
            logger.error('get user failed. err: %s', e.message)
            raise e.message
        return ret