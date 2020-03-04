# coding=utf-8
import logging
import flask_restplus

from hyip.extensions import Namespace
from . import responses, requests
from hyip import services
from flask import request

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


ns = Namespace('status', description='Status operations')

@ns.route('/<project_id>', methods=['GET'])
class GetStatus(flask_restplus.Resource):
    @ns.marshal_with(responses.status_project_res(ns))
    def get(self, project_id):
        return services.status.get_status_project_by_id(project_id)

@ns.route('/all/<project_id>', methods=['GET'])
class GetAllStatus(flask_restplus.Resource):
    @ns.marshal_with(responses.status_project_res(ns))
    def get(self, project_id):
        return services.status.get_all_status_project_by_id(project_id)

@ns.route('', methods=['POST'])
class UpdateStatus(flask_restplus.Resource):
    @ns.expect(requests.update_status_project(ns), validate=True)
    @ns.marshal_with(responses.status_project_res(ns))
    def post(self):
        data = flask_restplus.marshal(request.args or request.json, requests.update_status_project(ns))
        return services.status.update_status_project(**data)