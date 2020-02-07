# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import Resource, reqparse, fields

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('crawldata', description='Project operations')

_crawl_data_res = ns.model('crawl_data_res', responses.crawl_data_res)
_post_datacrawled_req = ns.model('post_datacrawled_req', requests.post_datacrawled_req)

_crawl_data_parser = reqparse.RequestParser()
_crawl_data_parser.add_argument('limit', required=True)
@ns.route('/<project_id>', methods=['GET', 'POST'])
class GetDataCrawledOfProject(flask_restplus.Resource):
    @ns.expect(_crawl_data_parser, validate=True)
    @ns.marshal_with(_crawl_data_res)
    def get(self, project_id):
        return services.crawldata.get_data_crawled(project_id, **request.args)

    @ns.expect(_post_datacrawled_req, validate=True)
    @ns.marshal_with(_crawl_data_res)
    def post(self, project_id):
        data = request.args or request.json
        return services.crawldata.create_crawldata(project_id=project_id, **data) 