# coding=utf-8
import logging
import flask_restplus

from hyip.extensions import Namespace
from . import responses, requests
from hyip import services
from flask import request
from flask_restplus import Resource, reqparse, fields

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


ns = Namespace('domain', description='Domain operations')
