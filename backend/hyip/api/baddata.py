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

ns = Namespace('baddata', description='Bad data operations')

@ns.route('', methods=['GET', 'POST', 'PUT'])
class BadData(flask_restplus.Resource):
    @ns.marshal_with(responses.baddata_res(ns))
    def get(self):
        return services.baddata.get_all_bad_data()
    
    @ns.expect(requests.post_bad_data_req(ns), validate=True)
    @ns.marshal_with(responses.baddata_res(ns))
    def post(self):
        data = marshal(request.args or request.json, requests.post_bad_data_req(ns))
        return services.baddata.create_bad_data(data['project_id'])

    @ns.expect(requests.put_bad_data_req(ns), validate=True)
    @ns.marshal_with(responses.baddata_res(ns))
    def put(self):
        data = marshal(request.args or request.json, requests.put_bad_data_req(ns))
        return services.baddata.solve_bad_data(data['id'], data['project_id'])