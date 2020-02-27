# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException, UserNotFoundException, TrackingExistsException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def post_project_tracked_by_user(project_id):
    if repo.project.check_exists_project_id(project_id):
        repo.tracking.post_project_tracked_by_user(project_id)
        return get_project_tracked_by_user()
    else:
        raise ProjectNotFoundException()

def delete_project_tracked_by_user(project_id):
    if repo.project.check_exists_project_id(project_id):
        return repo.tracking.delete_project_tracked_by_user(project_id)
    else:
        raise ProjectNotFoundException()

def get_project_tracked_by_user():
    return [data for data in repo.project.get_all_projects() if data.tracked]

def check_exists_tracked(project_id):
    if repo.project.check_exists_project_id(project_id):
        return {
            'tracked': repo.tracking.check_exists_tracked(project_id)
        } 
    else:
        raise ProjectNotFoundException()