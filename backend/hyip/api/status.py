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

_status_project_res = ns.model('status_project_res', responses.status_project_res)
_update_status_project = ns.model('update_status_project', requests.update_status_project)

@ns.route('/<project_id>', methods=['GET'])
class GetStatus(flask_restplus.Resource):
    @ns.marshal_with(_status_project_res)
    def get(self, project_id):
        return services.status.get_status_project_by_id(project_id)

@ns.route('/all/<project_id>', methods=['GET'])
class GetStatus(flask_restplus.Resource):
    @ns.marshal_with(_status_project_res)
    def get(self, project_id):
        return services.status.get_all_status_project_by_id(project_id)


@ns.route('', methods=['POST'])
class UpdateStatus(flask_restplus.Resource):
    @ns.expect(_update_status_project, validate=True)
    @ns.marshal_with(_status_project_res)
    def post(self):
        data = request.args or request.json
        return services.status.update_project_status(**data)