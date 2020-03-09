# coding=utf-8
import json
import logging
import unittest

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from celeryapp.tests import Base

class CheckTestCase(Base):
    def test_check_easy(self):
        from celeryapp.crawl_data import EasyCrawl
        for testcase in self.data['check_easy']:
            result = EasyCrawl(url_crawl = testcase['url_crawl']).get_only_info_project()
            assert_ = testcase['assert']
            for k, v in result.items():
                if assert_[k] == -1:
                    self.assertEqual(v, assert_[k])
                else:
                    self.assertGreaterEqual(v, assert_[k])

    def test_check_diff(self):
        from celeryapp.driver import Wrapper
        from celeryapp.crawl_data import DiffCrawl

        for testcase in self.data['check_diff']:
            result = Wrapper(DiffCrawl(url_crawl = testcase['url_crawl'], 
                investment_selector=testcase['investment_selector'],
                paid_out_selector=testcase['paid_out_selector'],
                member_selector=testcase['member_selector'],
                )).get_only_info_project()
            assert_ = testcase['assert']
            for k, v in result.items():
                if assert_[k] == -1:
                    self.assertEqual(v, assert_[k])
                else:
                    self.assertGreaterEqual(v, assert_[k])