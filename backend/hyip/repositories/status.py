# coding=utf-8
import logging
from hyip import models
from sqlalchemy import desc

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def update_status_project(**kwargs):
    status_project = models.StatusProject(**kwargs)
    models.db.session.add(status_project)
    models.db.session.commit()
    return status_project