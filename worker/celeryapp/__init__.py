# coding=utf-8
from __future__ import absolute_import
import logging
import inspect
from celery import Celery

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

# instantiate Celery object
celery = Celery(include=[
                            'celeryapp.tasks',
                        ])

# import celery config file
celery.config_from_object('config')

import config as cf

for atr in [f for f in dir(cf) if not '__' in f and not 'CELERY' in f]:
    if atr.islower():
        continue
    val =  getattr(cf, atr)
    if isinstance(val, str) or atr == 'URL':
        setattr(celery.conf, atr, val)