# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services
from hyip.tests.api import APITestCase
from datetime import datetime, timedelta
from random import uniform, randint

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def setUp(self):
        self.data = []
        for i in range(6):
            domain = self.generate_domain()
            project = self.init_project(domain=domain)
            self.data.append((project.id, domain))

    def test_check_exists(self):
        for id, domain in self.data:
            result = self.get('/api/domain/check-exists/'+ domain)
            self.assertEqual(result['data']['is_exists'], True)
        result = self.get('/api/domain/check-exists/' + self.generate_domain())
        self.assertEqual(result['data']['is_exists'], False)