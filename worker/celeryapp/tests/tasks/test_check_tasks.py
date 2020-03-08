# coding=utf-8
import json
import logging
import unittest

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from celeryapp.tests.tasks import Base

class CheckTestCase(Base):
    def test_check_easy(self):
        from celeryapp.tasks import check_easy
        for testcase in self.data[check_easy.__name__]:
            result = check_easy(url = testcase['url'])
            assert_ = testcase['assert']
            for k, v in result.items():
                if assert_[k] == -1:
                    self.assertEqual(v, assert_[k])
                else:
                    self.assertGreaterEqual(v, assert_[k])

    def test_check_diff(self):
        from celeryapp.tasks import check_diff
        for testcase in self.data[check_diff.__name__]:
            result = check_diff(url = testcase['url'], 
                investment_selector=testcase['investment_selector'],
                paid_out_selector=testcase['paid_out_selector'],
                member_selector=testcase['member_selector'],
                )
            assert_ = testcase['assert']
            for k, v in result.items():
                if assert_[k] == -1:
                    self.assertEqual(v, assert_[k])
                else:
                    self.assertGreaterEqual(v, assert_[k])