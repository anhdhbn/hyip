# coding=utf-8
import json
import logging
from unittest.mock import patch

from hyip import services
from hyip.tests.api import APITestCase
from datetime import datetime, timedelta
from random import uniform, randint

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class CrawlDataApiTestCase(APITestCase):
    def setUp(self):
        self.id_project = self.init_project().id
        self.init_crawldata(self.id_project)

    def init_data_crawldata(self, **kwargs):
        return {
            'total_investments' : uniform(100, 100000),
            'total_paid_outs': uniform(100, 100000),
            'total_members': randint(1, 1000),
            'alexa_rank': randint(1, 1000),
            **kwargs
        }

    def init_bad_data(self, **kwargs):
        return {
            'total_investments' : -1,
            'total_paid_outs': -1,
            'total_members': randint(1, 1000),
            'alexa_rank': randint(1, 1000),
            **kwargs
        }

    def init_crawldata(self, id_project, **kwargs):
        return services.crawldata.create_crawldata(id_project, **self.init_data_crawldata(**kwargs))

    def test_get_data_crawled(self):
        self.init_crawldata(self.id_project, created_at=datetime.now() - timedelta(2), created_date=datetime.now() - timedelta(2))
        self.init_crawldata(self.id_project, created_at=datetime.now() - timedelta(1), created_date=datetime.now() - timedelta(1))
        self.init_crawldata(self.id_project)
        self.init_crawldata(self.id_project)

        result = self.get('/api/crawldata/' + self.id_project + '?limit=all')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 3)

        result = self.get('/api/crawldata/' + self.id_project + '?limit=1')
        self.assertEqual(result['success'], True)
        self.assertEqual(len(result['data']), 1)

    def test_post_data_crawled(self):
        data = self.init_data_crawldata()
        result = self.post('/api/crawldata/' + self.id_project, data=data)
        self.assertEqual(result['data']['is_bad_data'], False)
        bad_data = self.init_bad_data()
        result = self.post('/api/crawldata/' + self.id_project, data=bad_data)
        self.assertEqual(result['data']['is_bad_data'], True)