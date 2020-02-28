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

@ns.route('/check-exists/<domain>', methods=['GET'])
class CheckDomain(flask_restplus.Resource):
    @ns.marshal_with(responses.exist_domain_res(ns))
    def get(self, domain):
        return services.domain.check_exists_domain(domain)

@ns.route('/search', methods=['GET'])
class GetAllDomain(flask_restplus.Resource):
    @ns.expect(requests.search_domain_parser, validate=True)
    @ns.marshal_with(responses.search_domain(ns))
    def get(self):
        return services.domain.search_domains(**request.args)