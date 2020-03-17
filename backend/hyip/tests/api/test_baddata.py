# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services
from hyip.tests.api import APITestCase

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def setUp(self):
        self.id_project = self.init_project().id

    def create_bad_data(self):
        data = {
            'project_id' : self.id_project
        }
        result = self.post('/api/baddata', data=data)
        return result['data']['id']

    def test_get_bad_data(self):
        self.create_bad_data()
        result = self.get('/api/baddata')
        self.assertEqual(len(result['data']), 1)

    def test_solve_bad_data(self):
        id = self.create_bad_data()
        data = {
            'id': id,
            'project_id' : self.id_project
        }
        self.put('/api/baddata', data=data)
        result = self.get('/api/baddata')
        self.assertEqual(len(result['data']), 0)