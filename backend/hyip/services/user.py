# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import RegisterBeforeException, UserExistsException
from hyip.extensions.exceptions import BadRequestException
from hyip.helpers import encode_token
from hyip.helpers import validate_register, hash_password

from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from hyip.helpers import validator, get_max_age, verify_password

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


def create_user(username, email, fullname, password, **kwargs):
    if validate_register(username, email, fullname, password):
        existed_user = repo.user.find_one_by_email_or_username_ignore_case(
            email, username)
        # check if user existed
        if existed_user:
            message = ("User with username {username} " +
                       "or email {email} already existed!").format(
                username=username,
                email=email
            )
            raise UserExistsException(message)

        # save pending register to database
        register = repo.user.save_user_to_database(
            username=username,
            email=email,
            fullname=fullname,
            password=hash_password(password)
        )
        return register

    else:
        raise BadRequestException("Invalid user data specified!")

def check_username_and_password(username, password):
    if (validator.validate_username(username) and
            validator.validate_password(password)):
        user = repo.user.find_one_by_username(username)
        if (not user):
            raise UserNotFoundException()
        if not verify_password(user.password, password):
            raise BadRequestException(message.INVALID_USERNAME_OR_PASSWORD)
        return user
    else:
        raise BadRequestException(message.INVALID_USERNAME_OR_PASSWORD)


def login(username, password, **data):
    user = check_username_and_password(username, password)

    resp = jsonify({
        **user.to_display_dict(),
        # 'notifications': services.notification.get_notification(user.id)
    })
    access_token = create_access_token(identity=user.email)
    set_access_cookies(resp, access_token, max_age=get_max_age())
    return resp


def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp

def check_exists_user(user_id):
    return repo.user.check_exists_user(user_id)