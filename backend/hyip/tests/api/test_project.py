# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services,  app
from hyip import repositories as repo
from hyip.tests.api import APITestCase
from datetime import datetime

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def setUp(self):
        result = services.project.create_project_by_crawler(**{
            'project': {
                "url": "https://google.com/",
                "investment_selector": "investment_selector asdasd ",
                "paid_out_selector": "paid_out_selector asdsa",
                "member_selector": "",
                "start_date": datetime.strptime("2020-01-07", "%Y-%m-%d"),
                "plans": "planss asdasdasd",
                "easy_crawl": False,
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
                "name": "keeper-money.com",
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
        self.id = result.id

    def test_get_all_projects(self):
        result = self.get('/api/project?type=all')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 2)
        

    def test_post_create_project(self):
        data = {
            "url": "https://longinvest.biz/",
            "investment_selector": "#statistic > div > div > div:nth-child(2) > div > div.item.item3.aos-init.aos-animate > div.number > span",
            "paid_out_selector": "#statistic > div > div > div:nth-child(2) > div > div.item.item4.aos-init.aos-animate > div.number > span",
            "member_selector": "#statistic > div > div > div:nth-child(2) > div > div.item.item2.aos-init.aos-animate > div.number > span",
            "start_date": "2018-07-12",
            "plans": "1.0%-1.6% daily, 130%-240% after",
            "easy_crawl": True
        }
        result = self.post('/api/project/create', data)
        self.assertEqual(result['success'], True)

    # def test_post_create_project_by_crawler(self):
    #     data = {
    #         "project": {
    #             "url": "https://www.google.com/",
    #             "investment_selector": "investment_selector asdasd ",
    #             "paid_out_selector": "paid_out_selector asdsa",
    #             "member_selector": "",
    #             "start_date": datetime.strptime("2020-01-07", "%Y-%m-%d").date(),
    #             "plans": "planss asdasdasd",
    #             "easy_crawl": False,
    #             "hosting": "Google LLC"
    #         },
    #         "domain": {
    #             "name": "google.com",
    #             "registrar": "MarkMonitor Inc.",
    #             "from_date": "1997-09-15",
    #             "to_date": "2028-09-13"
    #         },
    #         "ip": {
    #             "address": "172.217.194.113",
    #             "domains_of_this_ip": "iad30s07-in-f14.1e100.net,iad30s07-in-f238.1e100.net"
    #         },
    #         "ssl": {
    #             "ev": False,
    #             "from_date": "2020-01-14",
    #             "to_date": "2020-04-07",
    #             "description": "GTS CA 1O1"
    #         },
    #         "script": {
    #             "source_page": "ahihihi"
    #         }
    #     }
    #     result = self.client.post('/api/project/create-by-crawler', json=data, content_type='application/json')
    #     print(result.data)
    #     self.assertEqual(result, True)
        
    def test_get_all_easy_project(self):
        result = self.get('/api/project?type=easy')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_get_all_not_scam_project(self):
        result = self.get('/api/project?type=notscam')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 2)

    def test_get_info_project(self):
        result = self.get('/api/project/' + self.id)
        self.assertEqual(result['success'], True)

    def test_make_a_project_was_verified(self):
        result = self.post('/api/project/verified/' + self.id, data={})
        print(result)
        self.assertEqual(result['success'], True)

        result = self.get('/api/project?type=verified')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_get_verified_project(self):
        result = self.get('/api/project?type=verified')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 0)

    def test_get_unverified_project(self):
        result = self.get('/api/project?type=unverified')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 2)

    def test_remove_project(self):
        result = self.post('/api/project/remove/' + self.id, {})
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)
        result = self.get('/api/domain/check-exists/google.com')
        self.assertEqual(result['data']['is_exists'], False)

    def test_update_selector_project(self):
        data = {
            "investment_selector": "test1",
            "paid_out_selector": "test2",
            "member_selector": "test3",
            "plans": "test4",
            "easy_crawl": False
        }
        result = self.post('/api/project/update/' + self.id, data=data)
        self.assertEqual(result['success'], True)
        self.assertEqual(result['data']['investment_selector'], data['investment_selector'])
        self.assertEqual(result['data']['paid_out_selector'], data['paid_out_selector'])
        self.assertEqual(result['data']['member_selector'], data['member_selector'])
        self.assertEqual(result['data']['plans'], data['plans'])
        self.assertEqual(result['data']['easy_crawl'], data['easy_crawl'])
