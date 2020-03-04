# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests
from flask_restplus import Resource, reqparse, fields

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('tracking', description='Tracking operations')

@ns.route('/check', methods=['POST'])
class CheckTracking(flask_restplus.Resource):
    @ns.expect(requests.update_projects_tracked_by_user_req(ns), validate=True)
    @ns.marshal_with(responses.check_projects_tracked(ns))
    def post(self):
        data = flask_restplus.marshal(request.args or request.json, requests.update_projects_tracked_by_user_req(ns))
        return services.tracking.check_exists_tracked(**data)

@ns.route('', methods=['GET', 'POST', 'DELETE'])
class UpdateTrackingProject(flask_restplus.Resource):
    @ns.marshal_with(responses.projects_tracked_by_user_res(ns))
    def get(self):
        return services.tracking.get_project_tracked_by_user()

    @ns.expect(requests.update_projects_tracked_by_user_req(ns), validate=True)
    @ns.marshal_with(responses.projects_tracked_by_user_res(ns))
    def post(self):
        data = flask_restplus.marshal(request.args or request.json, requests.update_projects_tracked_by_user_req(ns))
        return services.tracking.post_project_tracked_by_user(**data)

    @ns.expect(requests.update_projects_tracked_by_user_req(ns), validate=True)
    @ns.marshal_with(responses.projects_tracked_by_user_res(ns))
    def delete(self):
        data = flask_restplus.marshal(request.args or request.json, requests.update_projects_tracked_by_user_req(ns))
        return services.tracking.delete_project_tracked_by_user(**data)