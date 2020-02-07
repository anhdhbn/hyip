# coding=utf-8
import logging
import flask_restplus

from hyip.extensions import Namespace
from . import responses, requests
from hyip import services
from flask import request

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


ns = Namespace('domain', description='Status operations')

_exists_domain = ns.model("exists-doamin", responses.exist_domain_res)

@ns.route('/check-exists/<domain>', methods=['GET'])
class CheckDomain(flask_restplus.Resource):
    @ns.marshal_with(_exists_domain)
    def get(self, domain):
        return services.domain.check_exists_domain(domain)

_get_all_domain = ns.model("get_all_domain", responses.get_all_domain)
@ns.route('/all', methods=['GET'])
class GetAllDomain(flask_restplus.Resource):
    @ns.marshal_with(_get_all_domain)
    def get(self):
        return services.domain.get_all_domain()
