#!/usr/bin/python
#coding=utf8

__author__ = 'linpelvis'

import logging

from arthas_web.services.business.app import testApp

logger = logging.getLogger(__name__)

APP_PROVIDER = {
        testApp.TestApp.NAME.lower() : testApp.TestApp(),
}
