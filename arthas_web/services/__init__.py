#!/usr/bin/python
#coding=utf-8
from arthas_web.services.business.businessServiceHandler import BusinessServiceHandler
from arthas_web.services.utils import get_request_data, check_get_method

__author__ = 'linpelvis'

import logging

logger = logging.getLogger(__name__)


DISPATCH = ['user']

handler = BusinessServiceHandler(DISPATCH)

def business_base(get, app_name, func_name, type='json', ext=''):
    logger.info("business_base, data: %s app_name: %s, "
                "function_name: %s, ext: %s", get, app_name, func_name, ext)
    try:
        data = get_request_data(get)
        result = handler.dispatch[func_name](app_name, data, ext)
    except Exception as err:
        logger.error('execute error, err: %s', err.message)
        result = err.message

    logger.debug("business_base, result: %s", result)
    return result

def invokeBusinessHandler(app_name, func_name, request):
    logger.info("method: %s, request: %s app_name: %s", func_name, request, app_name)
    check_get_method(request.method)
    app_name = app_name.lower()
    return business_base(request.GET, app_name, func_name, 'json')
