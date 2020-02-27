# coding=utf-8
import logging
from hyip import models, repositories as repo
from sqlalchemy import desc

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


def post_project_tracked_by_user(project_id):
    project = repo.project.get_project_by_id(project_id)
    project.tracked = True
    models.db.session.commit()
    return project

def delete_project_tracked_by_user(project_id):
    project = repo.project.get_project_by_id(project_id)
    project.tracked = not project.tracked
    models.db.session.commit()
    return project

def check_exists_tracked(project_id):
    project = repo.project.get_project_by_id(project_id)
    return project.tracked