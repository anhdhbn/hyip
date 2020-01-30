# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def get_status_project_by_id(project_id):
    return models.StatusProject.query.filter(
        models.StatusProject.project_id == project_id,
    ).all()

def update_project_status(**kwargs):
    status_project = models.StatusProject(**kwargs)
    models.db.session.add(status_project)
    models.db.session.commit()
    return status_project