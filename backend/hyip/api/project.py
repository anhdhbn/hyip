# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import fields

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('project', description='Project operations')


_create_project_req = ns.model('create_project_req', requests.create_project_req)
_create_project_res = ns.model('project_res', responses.project_res)

@ns.route('/create', methods=['POST'])
class Create(flask_restplus.Resource):
    @ns.expect(_create_project_req, validate=True)
    @ns.marshal_with(_create_project_res)
    def post(self):
        data = request.args or request.json
        project = services.project.create_project(
            **data)
        return project


_get_project_res = ns.model('get_project_res', responses.project_res)
@ns.route('/<projectId>', methods=['GET'])
class GetProjectInfo(flask_restplus.Resource):
    @ns.marshal_with(_get_project_res)
    def get(self, projectId):
        return services.project.get_project_info_by_id(projectId)


@ns.route('/all', methods=['GET'])
class GetAllProjectInfo(flask_restplus.Resource):
    @ns.marshal_with(_get_project_res)
    def get(self):
        return services.project.get_all_project_info()

@ns.route('/easy', methods=['GET'])
class GetAllProjectInfo(flask_restplus.Resource):
    @ns.marshal_with(_get_project_res)
    def get(self):
        return services.project.get_easy_project_info()