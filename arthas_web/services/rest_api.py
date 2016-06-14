#!/usr/bin/python
# coding=utf-8

__author__ = 'linpelvis'

import logging

from core.decorators import json_response
from arthas_web.services import invokeBusinessHandler

logger = logging.getLogger(__name__)


@json_response
def user(func_name, request, app_name):
    return invokeBusinessHandler(app_name, func_name, request)




