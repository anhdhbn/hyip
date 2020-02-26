# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import Resource, fields
from flask import request, redirect
from hyip.extensions.exceptions import BadRequestException
__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('projects', description='Project operations')

@ns.route('/create', methods=['POST'])
class Create(flask_restplus.Resource):
    @ns.expect(requests.create_project_req(ns), validate=True)
    @ns.marshal_with(responses.project_res(ns))
    def post(self):
        data = request.args or request.json
        result = services.project.create_project(
            **data)
        return result

@ns.route('/<projectId>', methods=['GET'])
class GetProjectInfo(flask_restplus.Resource):
    @ns.marshal_with(responses.project_res(ns))
    def get(self, projectId):
        return services.project.get_project_info_by_id(projectId)

@ns.route('', methods=['GET'])
class GetAllProjectInfo(flask_restplus.Resource):
    @ns.expect(requests.get_projects_parser, validate=True)
    @ns.marshal_with(responses.project_res(ns))
    def get(self):
        type_get = request.args.get("type").lower()
        if type_get == "all":
            return services.project.get_all_projects_info()
        elif type_get == "easy":
            return services.project.get_easy_projects_info()
        elif type_get == "diff":
            return services.project.get_diff_projects_info()
        elif type_get == "notscam":
            return services.project.get_not_scam_projects_info()
        elif type_get == "verified":
            return services.project.get_verified_projects()
        elif type_get == "unverified":
            return services.project.get_unverified_projects()
        else:
            raise BadRequestException