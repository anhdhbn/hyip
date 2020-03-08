# coding=utf-8
import json
import logging
import unittest
from os import path
import requests

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


class Base(unittest.TestCase):
    def setUp(self):
        filename = "test.json"
        if path.exists(filename):
            import json
            with open(filename) as json_file:
                self.data = json.load(json_file)
        else:
            pass
            # url = ""
            # self.data = requests.get(url).json()