# coding=utf-8
import logging
import flask_restplus
from flask import request

from hyip.celery import cele
from hyip.extensions import Namespace
from celery.result import AsyncResult
from flask_restplus import Resource, reqparse, fields
from . import responses, requests

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('celery', description='Celery operations')

# @ns.route('/<id>', methods=['GET'], endpoint="processing_celery")
@ns.route('/result/<id>', methods=['GET'])
class GetProjectInfo(flask_restplus.Resource):
    def get(self, id):
        result = AsyncResult(id=id, app=cele)
        return result.get()

_check_selector_parser = reqparse.RequestParser()
_check_selector_parser.add_argument('url', required=True)
_check_selector_parser.add_argument('investment_selector', required=True)
_check_selector_parser.add_argument('paid_out_selector', required=True)
_check_selector_parser.add_argument('member_selector', required=True)

_check_selector_res = ns.model('check_selector_res', responses.check_selector_res)
@ns.route('/check-selector', methods=['GET'])
class CheckSelectorInfo(flask_restplus.Resource):
    @ns.expect(_check_selector_parser, validate=True)
    @ns.marshal_with(_check_selector_res)
    def get(self):
        import celery
        result = cele.send_task("jobqueue.tasks.check_selector", kwargs=request.args)
        result = AsyncResult(id=result.id, app=cele)
        return result.get()

_check_easy_parser = reqparse.RequestParser()
_check_easy_parser.add_argument('url', required=True)

@ns.route('/check-easy', methods=['GET'])
class CheckEasyInfo(flask_restplus.Resource):
    @ns.expect(_check_easy_parser, validate=True)
    @ns.marshal_with(_check_selector_res)
    def get(self):
        import celery
        result = cele.send_task("jobqueue.tasks.check_easy", kwargs=request.args)
        result = AsyncResult(id=result.id, app=cele)
        return result.get()

@ns.route('/check-diff', methods=['GET'])
class Test(flask_restplus.Resource):
    @ns.expect(_check_selector_parser, validate=True)
    @ns.marshal_with(_check_selector_res)
    def get(self):
        import celery
        result = cele.send_task("jobqueue.tasks.check_diff", kwargs=request.args)
        result = AsyncResult(id=result.id, app=cele)
        return result.get()