
# coding=utf-8
import json
import logging
import unittest
import random
import string
import pytest

from hyip import services

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
        res = self.client.post(url, data=data, content_type=content_type)
        return res.get_json()

    def put(self, url, data):
        content_type = 'application/json'
        data = json.dumps(data)
        res = self.client.put(url, data=data, content_type=content_type)
        return res.get_json()

    def delete(self, url, data):
        content_type = 'application/json'
        data = json.dumps(data)
        res = self.client.delete(url, data=data, content_type=content_type)
        return res.get_json()

    def patch(self, url, data):
        content_type = 'application/json'
        data = json.dumps(data)
        res = self.client.patch(url, data=data, content_type=content_type)
        return res.get_json()

    def post_json(self, url, data):
        return self.client.post(url, json=data).get_json()

    def delete(self, url, data):
        content_type = 'application/json'
        data = json.dumps(data)

        res = self.client.delete(url, data=data, content_type=content_type).get_json()
        return res

    def randomString(self, stringLength=5):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def generate_domain(self, domain=None):
        if domain is None:
            return f"{self.randomString()}.{self.randomString(3)}"
        else:
            return domain

    def init_data_project(self, domain=None):
        return {
            "url_crawl": f"https://{self.generate_domain(domain)}/",
            "investment_selector": "investment_selector 123",
            "paid_out_selector": "paid_out_selector 456",
            "member_selector": "member_selector 789",
        }

    def init_project(self, domain=None, **kwargs):
        return services.project.create_project(**self.init_data_project(domain=domain),**kwargs)