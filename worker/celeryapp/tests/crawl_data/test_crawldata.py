# coding=utf-8
import json
import logging
import unittest
import requests
from celeryapp import celery
from celeryapp.tests import Base

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CheckCrawlData(Base):
    def test_crawl_easy_project_every_day(self):
        result = requests.get(celery.conf.URL['get_easy_project'])
        if not result.json()['success']:
            print(result.json()['message'])
            result.raise_for_status()
        result = result.json()
        self.assertGreaterEqual(len(result['data']), 0)

    def test_crawl_diff_project_every_day(self):
        result = requests.get(celery.conf.URL['get_diff_project'])
        if not result.json()['success']:
            print(result.json()['message'])
            result.raise_for_status()
        result = result.json()
        self.assertGreaterEqual(len(result['data']), 0)

    def test_crawl_easy_project(self):
        from celeryapp.crawl_data import EasyCrawl
        for testcase in self.data['check_easy']:
            result = EasyCrawl(url_crawl = testcase['url_crawl'], id=testcase["id"]).crawl()
            assert_ = testcase['assert']
            for k, v in assert_.items():
                if assert_[k] == -1:
                    self.assertEqual(v, result[k])
                else:
                    self.assertLessEqual(v, result[k])

    def test_crawl_diff_project(self):
        from celeryapp.driver import Wrapper
        from celeryapp.crawl_data import DiffCrawl

        for testcase in self.data['check_diff']:
            result = Wrapper(DiffCrawl(
                id = testcase["id"],
                url_crawl = testcase['url_crawl'], 
                investment_selector=testcase['investment_selector'],
                paid_out_selector=testcase['paid_out_selector'],
                member_selector=testcase['member_selector'],
                )).get_only_info_project()
            assert_ = testcase['assert']
            for k, v in assert_.items():
                if assert_[k] == -1:
                    self.assertEqual(v, result[k])
                else:
                    self.assertLessEqual(v, result[k])