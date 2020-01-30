# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import fields
from flask import request, redirect

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


@ns.route('/all', methods=['GET'])
class GetAllProjectInfo(flask_restplus.Resource):
    @ns.marshal_with(_create_project_crawler_res)
    def get(self):
        return services.project.get_all_project_info()

@ns.route('/easy', methods=['GET'])
class GetProjectEasyInfo(flask_restplus.Resource):
    @ns.marshal_with(_create_project_crawler_res)
    def get(self):
        return services.project.get_easy_project_info()

@ns.route('/notscam', methods=['GET'])
class GetProjectNotScamInfo(flask_restplus.Resource):
    @ns.marshal_with(_create_project_crawler_res)
    def get(self):
        return services.project.get_not_scam_project_info()


@ns.route('/create-by-crawler', methods=['POST'])
class CreateByCrawler(flask_restplus.Resource):
    # @ns.expect(_create_project_by_crawler_req, validate=True)
    @ns.marshal_with(_create_project_crawler_res)
    def post(self):
        data = request.args or request.json
        project = services.project.create_project_by_crawler(
            **data)
        return project