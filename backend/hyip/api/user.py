# coding=utf-8
import logging

import flask_restplus
from flask import request

from hyip import services
from hyip.extensions import Namespace
from hyip.extensions.custom_exception import InvalidLoginTokenException
from . import responses, requests

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

ns = Namespace('user', description='User operations')




_login_req = ns.model('login_req', requests.login_req)

@ns.route('/login', methods=['GET', 'POST'])
class Login(flask_restplus.Resource):
    @ns.expect(_login_req, validate=True)
    # @ns.marshal_with(_user_res)
    def post(self):
        "check username and password and set jwt token to httponly cookies"
        data = request.args or request.json
        resp = services.user.login(**data)
        return resp


@ns.route('/logout', methods=['GET', 'POST'])
class Logout(flask_restplus.Resource):
    def post(self):
        "remove jwt token from httponly cookies"
        resp = services.user.logout()
        return resp


_register_req = ns.model('register_req', requests.register_user_req)
_register_res = ns.model('register_res', responses.register_res)


@ns.route('/register', methods=['GET', 'POST'])
class Registers(flask_restplus.Resource):
    @ns.expect(_register_req, validate=True)
    @ns.marshal_with(_register_res)
    def post(self):
        "validate register data, add data to pending register table and send confirm email"
        data = request.args or request.json
        return services.user.create_user(
            **data)