# coding=utf-8
import logging
import flask_restplus
from flask import request

from hyip.extensions import Namespace
from celery.result import AsyncResult
from flask_restplus import Resource, reqparse, fields
from . import responses, requests
import celery
from hyip.celery import cele

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('celery', description='Celery operations')