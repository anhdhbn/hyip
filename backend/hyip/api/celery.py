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

@ns.route('/check-easy', methods=['GET'])
class CheckEasyInfo(flask_restplus.Resource):
    @ns.expect(requests.check_easy_parser, validate=True)
    @ns.marshal_with(responses.check_selector_res(ns))
    def get(self):
        result = cele.send_task("celeryapp.tasks.check_easy", queue='default', kwargs=request.args)
        result = AsyncResult(id=result.id, app=cele)
        return result.get()

@ns.route('/check-diff', methods=['GET'])
class Test(flask_restplus.Resource):
    @ns.expect(requests.check_selector_parser, validate=True)
    @ns.marshal_with(responses.check_selector_res(ns))
    def get(self):
        result = cele.send_task("celeryapp.tasks.check_diff", queue='diff', kwargs=request.args)
        result = AsyncResult(id=result.id, app=cele)
        return result.get()