# coding=utf-8
import json
import logging
import unittest

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from celeryapp.tests import Base

class CheckCrawlProject(unittest.TestCase):
    def test_crawl_project(self):
        from celeryapp.crawl_projects import CrawlProjects
        temp = CrawlProjects()
        result = temp.crawl()
        self.assertGreater(result, 300)