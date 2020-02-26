# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import Resource, reqparse, fields
from flask import request, redirect
from hyip.extensions.exceptions import BadRequestException
__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('project', description='Project operations')