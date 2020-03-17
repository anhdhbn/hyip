# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import Resource, reqparse, fields, marshal

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('crawldata', description='Crawldata operations')

@ns.route('/<project_id>', methods=['GET', 'POST'])
class GetDataCrawledOfProject(flask_restplus.Resource):
    @ns.expect(requests.crawl_data_parser, validate=True)
    @ns.marshal_with(responses.crawl_data_res(ns))
    def get(self, project_id):
        return services.crawldata.get_data_crawled(project_id, **request.args)

    @ns.expect(requests.post_data_crawled_req(ns), validate=True)
    @ns.marshal_with(responses.pos_crawl_data_res(ns))
    def post(self, project_id):
        data = marshal(request.args or request.json, requests.post_data_crawled_req(ns))
        if data['total_investments'] == -1 and data['total_paid_outs'] == -1:
            result = services.baddata.create_bad_data(project_id)
            setattr(result, 'is_bad_data', True)
            return result
        else:
            result = services.crawldata.create_crawldata(project_id=project_id, **data)
            setattr(result, 'is_bad_data', False)
            return result