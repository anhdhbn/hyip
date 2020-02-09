# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def post_project_tracked_by_user(project_id, user_id):
    if repo.project.check_exists_project_id(project_id):
        return repo.tracking.post_project_tracked_by_user(project_id, user_id)
    else:
        raise ProjectNotFoundException()

def delete_project_tracked_by_user(project_id, user_id):
    if repo.project.check_exists_project_id(project_id):
        return repo.tracking.delete_project_tracked_by_user(project_id, user_id)
    else:
        raise ProjectNotFoundException()

def get_project_tracked_by_user(user_id):
    return repo.tracking.get_project_tracked_by_user(user_id)