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

_exists_domain = ns.model("exists-doamin", responses.exist_domain_res)

@ns.route('/check-exists/<domain>', methods=['GET'])
class CheckDomain(flask_restplus.Resource):
    @ns.marshal_with(_exists_domain)
    def get(self, domain):
        return services.domain.check_exists_domain(domain)

_search_domain_parser = reqparse.RequestParser()
_search_domain_parser.add_argument('input', required=True)
_search_domain_parser.add_argument('page', type=int)
_search_domain_parser.add_argument('ipp', type=int)

@ns.route('/search', methods=['GET'])
class GetAllDomain(flask_restplus.Resource):
    @ns.expect(_search_domain_parser, validate=True)
    @ns.marshal_with(responses.search_domain)
    def get(self):
        return services.domain.search_domains(**request.args)
