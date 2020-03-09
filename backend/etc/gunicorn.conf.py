
# coding=utf-8
import logging
import multiprocessing
import os

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
))
_VAR = os.path.join(_ROOT, 'var')
_ETC = os.path.join(_ROOT, 'etc')

bind = '0.0.0.0:{}'.format(os.getenv('PORT', 5000))
workers = multiprocessing.cpu_count() * 2 + 1

timeout = 60 * 60  # 3 minutes
keepalive = 24 * 3600  # 1 day
worker_class = 'gevent'
max_requests = 1000
logconfig = os.path.join(_ETC, 'logging.ini')
