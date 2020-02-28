# coding=utf-8
import logging

import flask_restx
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restx import Resource, reqparse, fields

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('crawldata', description='Crawldata operations')

@ns.route('/<project_id>', methods=['GET', 'POST'])
class GetDataCrawledOfProject(flask_restx.Resource):
    @ns.expect(requests.crawl_data_parser, validate=True)
    @ns.marshal_with(responses.crawl_data_res(ns))
    def get(self, project_id):
        return services.crawldata.get_data_crawled(project_id, **request.args)

    @ns.expect(requests.post_data_crawled_req(ns), validate=True)
    @ns.marshal_with(responses.crawl_data_res(ns))
    def post(self, project_id):
        data = request.args or request.json
        return services.crawldata.create_crawldata(project_id=project_id, **data) 