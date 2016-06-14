from django.test import TestCase

import logging
from django.test.utils import override_settings

logger = logging.getLogger('arthas_web')

@override_settings(DEBUG=True)
class TestServiceBase(TestCase):
    def i(self, msg, *args, **kwargs):
        logger.info(msg, *args, **kwargs)


    def d(self, msg, *args, **kwargs):
        logger.debug(msg, *args, **kwargs)


    def w(self, msg, *args, **kwargs):
        logger.warn(msg, *args, **kwargs)

    def exp(self, msg, *args, **kwargs):
        logger.exception(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        logger.error(msg, *args, **kwargs)
