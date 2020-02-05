
# coding=utf-8
import json
import logging
import unittest

import pytest

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


@pytest.mark.usefixtures('client_class')
@pytest.mark.usefixtures('app_class')
class APITestCase(unittest.TestCase):
    def get(self, url):
        res = self.client.get(url).get_json()
        return res

    def post(self, url, data):
        content_type = 'application/json'
        data = json.dumps(data)

        res = self.client.post(url, data=data, content_type=content_type).get_json()
        return res