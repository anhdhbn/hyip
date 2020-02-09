# coding=utf-8
import logging

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from hyip.extensions.exceptions import HTTPException
from hyip.constant import message

class UserExistsException(HTTPException):
    def __init__(self, message='user exists', errors=None):
        super().__init__(code=409, message=message, errors=errors, custom_code='user_exists')

class InvalidLoginTokenException(HTTPException):
    def __init__(self, message=message.INVALID_LOGIN_TOKEN, errors=None):
        super().__init__(code=401, message=message, errors=errors, custom_code='invalid_login_token')

class EncodeErrorException(HTTPException):
    def __init__(self, message=message.ENCODE_ERR, errors=None):
        super().__init__(code=401, message=message, errors=errors, custom_code='encode_err')

class RegisterBeforeException(HTTPException):
    def __init__(self, message='registed before', errors=None):
        super().__init__(code=409, message=message, errors=errors, custom_code='registed_before')

class DomainExistsException(HTTPException):
    def __init__(self, message='Domain was exists', errors=None):
        super().__init__(code=400, message=message, errors=errors, custom_code='domain_was_exists')
class TrackingExistsException(HTTPException):
    def __init__(self, message='Tracking was exists', errors=None):
        super().__init__(code=400, message=message, errors=errors, custom_code='tracking_was_exists')
class ProjectNotFoundException(HTTPException):
    def __init__(self, message='Project not found', errors=None):
        super().__init__(code=400, message=message, errors=errors, custom_code='project_not_found')

class UserNotFoundException(HTTPException):
    def __init__(self, message='User not found', errors=None):
        super().__init__(code=400, message=message, errors=errors, custom_code='user_not_found')