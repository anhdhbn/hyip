  
# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services
from hyip.tests.api import APITestCase
from datetime import datetime
from time import sleep

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def setUp(self):
        self.id_project = self.init_project().id

    def generate_status(self, id_project, status_project=3):
        return {
            'project_id': id_project,
            'status_project': status_project
        }

    def test_get_all_status_project(self):
        data = self.generate_status(self.id_project)
        services.status.update_status_project(**data)
        result = self.get('/api/status/all/'+ self.id_project)
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_get_status_project(self):
        data = self.generate_status(self.id_project, status_project=1)
        services.status.update_status_project(**data)
        result = self.get('/api/status/'+self.id_project)
        self.assertEqual(result['data']['status_project'], 1)

        sleep(0.5)
        data = self.generate_status(self.id_project, status_project=3)
        services.status.update_status_project(**data)
        result = self.get('/api/status/'+self.id_project)
        self.assertEqual(result['data']['status_project'], 3)

    def test_post_status_project(self):
        data = self.generate_status(self.id_project)
        result = self.post('/api/status', data)
        self.assertEqual(result['success'], True)