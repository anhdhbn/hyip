# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import Resource, reqparse, fields
from flask import request, redirect
from hyip.extensions.exceptions import BadRequestException
__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('project', description='Project operations')

_create_project_by_crawler_req = ns.model('create_project_by_crawler_req', requests.create_project_by_crawler_req)
_create_project_crawler_res = ns.model('project_crawler_res', responses.project_crawler_res)

_create_project_req = ns.model('create_project_req', requests.create_project_req)
_create_project_res = ns.model('project_res', responses.project_res)
_get_project_res = ns.model('get_project_res', responses.project_res)

@ns.route('/create', methods=['POST'])
class Create(flask_restplus.Resource):
    @ns.expect(_create_project_req, validate=True)
    @ns.marshal_with(_create_project_res)
    def post(self):
        data = request.args or request.json
        result = services.project.create_project(
            **data)
        return result



@ns.route('/<projectId>', methods=['GET'])
class GetProjectInfo(flask_restplus.Resource):
    @ns.marshal_with(_create_project_crawler_res)
    def get(self, projectId):
        return services.project.get_project_info_by_id(projectId)

_get_projects_parser = reqparse.RequestParser()
_get_projects_parser.add_argument('type', required=True, help="type can be all, easy, notscam")

@ns.route('', methods=['GET'])
class GetAllProjectInfo(flask_restplus.Resource):
    @ns.expect(_get_projects_parser, validate=True)
    @ns.marshal_with(_create_project_crawler_res)
    def get(self):
        type_get = request.args.get("type").lower()
        if type_get == "all":
            return services.project.get_all_project_info()
        elif type_get == "easy":
            return services.project.get_easy_project_info()
        elif type_get == "notscam":
            return services.project.get_not_scam_project_info()
        else:
            raise BadRequestException


@ns.route('/create-by-crawler', methods=['POST'])
class CreateByCrawler(flask_restplus.Resource):
    # @ns.expect(_create_project_by_crawler_req, validate=True)
    @ns.marshal_with(_create_project_crawler_res)
    def post(self):
        data = request.args or request.json
        project = services.project.create_project_by_crawler(
            **data)
        return project