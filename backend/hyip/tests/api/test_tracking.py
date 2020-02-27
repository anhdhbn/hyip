# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services
from hyip import repositories as repo
from hyip.tests.api import APITestCase
from datetime import datetime

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def setUp(self):
        self.id_project = self.init_project(tracked=True).id
        data = self.generate_data_tracking(self.id_project)
        result = self.post('/api/tracking', data=data)
        self.assertEqual(len(result['data']), 1)

    def generate_data_tracking(self, id_project):
        return {
            'project_id': id_project
        }

    def test_get_tracking_projects_by_user(self):
        project_id = self.init_project(tracked=True).id
        self.post('/api/tracking', data=self.generate_data_tracking(project_id))
        result = self.get('/api/tracking')
        self.assertEqual(len(result['data']), 2)

    def test_create_tracking_project(self):
        project_id = self.init_project(tracked=True).id
        result = self.post('/api/tracking', data=self.generate_data_tracking(project_id))
        self.assertEqual(len(result['data']), 2)

    def delete_create_tracking_project(self):
        data = self.generate_data_tracking(self.id_project)
        result = self.delete('/api/tracking' ,data=data)
        self.assertEqual(len(result['data']), 0)

    def test_check_exists_tracked(self):
        data = self.generate_data_tracking(self.id_project)
        result = self.post('/api/tracking/check', data=data)
        self.assertEqual(result['data']['tracked'], True)