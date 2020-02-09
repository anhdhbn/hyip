# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException, UserNotFoundException, TrackingExistsException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def post_project_tracked_by_user(project_id, user_id):
    if repo.project.check_exists_project_id(project_id):
        if repo.user.check_exists_user(user_id):
            if not repo.tracking.check_exists_tracked(project_id, user_id):
                return repo.tracking.post_project_tracked_by_user(project_id, user_id)
            else:
                raise TrackingExistsException()
        else:
            raise UserNotFoundException()
    else:
        raise ProjectNotFoundException()

def delete_project_tracked_by_user(project_id, user_id):
    if repo.project.check_exists_project_id(project_id):
        if repo.user.check_exists_user(user_id):
            return repo.tracking.delete_project_tracked_by_user(project_id, user_id)
        else:
            raise UserNotFoundException()
    else:
        raise ProjectNotFoundException()

def get_project_tracked_by_user(user_id):
    if repo.user.check_exists_user(user_id):
        return repo.tracking.get_project_tracked_by_user(user_id)
    else:
        raise UserNotFoundException()

def check_exists_tracked(project_id, user_id):
    if repo.project.check_exists_project_id(project_id):
        if repo.user.check_exists_user(user_id):
            return {
                'tracked': repo.tracking.check_exists_tracked(project_id, user_id)
            } 
        else:
            raise UserNotFoundException()
    else:
        raise ProjectNotFoundException()