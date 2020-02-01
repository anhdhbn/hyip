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
        services.project.create_project_by_crawler(**{
            'project': {
                "url": "https://keeper-money.com/",
                "investment_selector": "investment_selector asdasd ",
                "paid_out_selector": "paid_out_selector asdsa",
                "member_selector": "",
                "start_date": datetime.strptime("2020-01-07", "%Y-%m-%d"),
                "plans": "planss asdasdasd",
                "easy_crawl": True,
                "hosting": "Google LLC"
            },
            'domain': {
                "name": "google.com",
                "registrar": "MarkMonitor Inc.",
                "from_date": datetime.strptime("2020-01-07", "%Y-%m-%d"),
                "to_date": datetime.strptime("2020-01-07", "%Y-%m-%d")
            },
            'ip': {
                "address": "172.217.194.113",
                "domains_of_this_ip": "iad30s07-in-f14.1e100.net,iad30s07-in-f238.1e100.net"
            },
            'ssl': {
                "ev": False,
                "from_date": datetime.strptime("2020-01-07", "%Y-%m-%d"),
                "to_date": datetime.strptime("2020-01-07", "%Y-%m-%d"),
                "description": "GTS CA 1O1"
            },
            'script' :  {
                'source_page' : "ahihi source"
            }
        })

        projects = services.project.get_all_project_info()

        self.id = projects[0].id
        services.crawldata.create_crawldata(self.id, **{
            'total_investment' : 213321,
            'total_paid_out': 2313213,
            'total_member': 31,
            'alexa_rank': 30
        })

    def test_get_data_crawled(self):
        result = self.get('/api/crawldata/' + self.id)
        self.assertEqual(result['success'], True)

    def test_post_data_crawled(self):
        data = {
            'total_investment' : 213321,
            'total_paid_out': 2313213,
            'total_member': 31,
            'alexa_rank': 30
        }
        result = self.post('/api/crawldata/' + self.id, data=data)
        print(result)
        self.assertEqual(result['success'], True)
        