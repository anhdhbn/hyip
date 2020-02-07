# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def update_project_status(**kwargs):
    project_id = kwargs.get("project_id")
    if repo.project.check_exists_project_id(project_id):
        return repo.status.update_project_status(**kwargs)
    else:
        raise ProjectNotFoundException()

def get_status_project_by_id(project_id):
    if repo.project.check_exists_project_id(project_id):
        return repo.status.get_status_project_by_id(project_id)
    else:
        raise ProjectNotFoundException()

def get_all_status_project_by_id(project_id):
    if repo.project.check_exists_project_id(project_id):
        return repo.status.get_all_status_project_by_id(project_id)
    else:
        raise ProjectNotFoundException()