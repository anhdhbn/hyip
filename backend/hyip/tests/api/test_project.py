# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services, app
from hyip.tests.api import APITestCase
from datetime import datetime

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def make_scam_project(self, project_id):
        data = {
            'project_id': project_id,
            'status_project': 3
        }
        services.status.update_status_project(**data)

    def generate_scam_project(self, **kwargs):
        project = self.init_project(**kwargs)
        self.make_scam_project(project.id)

    def test_post_create_project(self):
        domain = self.generate_domain()
        data = self.init_data_project(domain)
        result = self.post('/api/projects', data)
        self.assertEqual(result['success'], True)
        self.assertEqual(result['data']['domain'], domain)
        self.assertIsNotNone(result['data']['created_date'])

    def test_get_info_project(self):
        domain = self.generate_domain()
        project = self.init_project(domain=domain)
        result = self.get("/api/projects/" + project.id)
        self.assertEqual(result['success'], True)
        self.assertEqual(result['data']['domain'], domain)

    def test_get_all_projects(self):
        self.init_project()
        self.generate_scam_project()
        result = self.get("/api/projects?type=all")
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 2)

    def test_get_easy_projects(self):
        self.init_project(easy_crawl=True, crawlable=True, is_verified=True)
        self.generate_scam_project(easy_crawl=True, crawlable=True, is_verified=True)
        result = self.get("/api/projects?type=easy")
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_get_diff_projects(self):
        self.init_project(easy_crawl=False, crawlable=True, is_verified=True)
        self.generate_scam_project(easy_crawl=False, crawlable=True, is_verified=True)
        result = self.get("/api/projects?type=diff")
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_get_notscam_projects(self):
        self.init_project(easy_crawl=False, crawlable=True, is_verified=True)
        self.generate_scam_project(easy_crawl=False, crawlable=True, is_verified=True)
        result = self.get("/api/projects?type=notscam")
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_get_verified_projects(self):
        self.init_project(easy_crawl=False, crawlable=True, is_verified=True)
        self.generate_scam_project(easy_crawl=False, crawlable=True, is_verified=True)
        result = self.get("/api/projects?type=verified")
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 2)

    def test_get_unverified_projects(self):
        self.init_project(easy_crawl=False, crawlable=True, is_verified=False)
        self.generate_scam_project(easy_crawl=False, crawlable=True, is_verified=False)
        result = self.get("/api/projects?type=unverified")
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 2) 
        
    def test_update_project(self):
        project = self.init_project(easy_crawl=False, crawlable=True, is_verified=False)
        data = {
            'easy_crawl': True,
            'type_currency': "USD",
            "is_verified": False,
            "fucking": True,
            'url_crawl': self.generate_domain(),
            'crawlable': False,
        }
        result = self.put("/api/projects/" + project.id, data)
        print(result)
        self.assertEqual(result['data']['easy_crawl'], True)
        self.assertEqual(result['data']['is_verified'], True)

    def test_remove_project(self):
        project = self.init_project(easy_crawl=False, crawlable=True, is_verified=False)
        result = self.delete("/api/projects/" + project.id, {})
        self.assertEqual(len(result['data']), 0)

    def test_verify_project(self):
        project = self.init_project(easy_crawl=False, crawlable=True, is_verified=False)
        result = self.patch("/api/projects/" + project.id, {})
        self.assertEqual(result['data']['is_verified'], True)