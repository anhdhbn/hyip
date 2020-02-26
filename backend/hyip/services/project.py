# coding=utf-8
import logging
import os

from flask import jsonify
from flask import request
from hyip import repositories as repo
from hyip.helpers import get_domain
from hyip.extensions.custom_exception import DomainExistsException, ProjectNotFoundException
from hyip.extensions.exceptions import BadRequestException

from celery.result import AsyncResult
from hyip.celery import cele

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


