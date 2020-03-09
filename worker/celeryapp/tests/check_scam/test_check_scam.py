# coding=utf-8
import json
import logging
import unittest
import requests
from celeryapp import celery
from celeryapp.tests import Base

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class TestCheckScam(Base):
    def test_check_scam_all(self):
        result = requests.get(celery.conf.URL['get_not_scam_project'])
        if not result.json()['success']:
            print(result.json()['message'])
            result.raise_for_status()
        result = result.json()
        self.assertGreaterEqual(len(result['data']), 0)

    def test_check_scam(self):
        from celeryapp.check_scam import CheckScam
        for testcase in self.data['check_scam']:
            temp = CheckScam()
            result = temp.check(testcase)
            self.assertEqual(result, testcase['assert']['status_project'])