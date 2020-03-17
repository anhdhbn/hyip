# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def create_bad_data(project_id, **kwargs):
    if repo.project.check_exists_project_id(project_id):
        return repo.baddata.create_bad_data(project_id=project_id, **kwargs)
    else:
        raise ProjectNotFoundException()

def get_all_bad_data():
    return repo.baddata.get_all_bad_data()

def solve_bad_data(id, project_id):
    if repo.project.check_exists_project_id(project_id):
        return repo.baddata.solve_bad_data(id)
    else:
        raise ProjectNotFoundException()