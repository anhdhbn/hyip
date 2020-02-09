# coding=utf-8
import logging
from hyip import models
from sqlalchemy import desc

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def get_project_tracked_by_user(user_id):
    return models.TrackingProject.query.filter(
        models.TrackingProject.user_id == user_id,
    ).all()


def post_project_tracked_by_user(project_id, user_id):
    tracking = models.TrackingProject(project_id=project_id, user_id=user_id)
    models.db.session.add(tracking)
    models.db.session.commit()
    return tracking

def delete_project_tracked_by_user(project_id, user_id):
    tracking = models.TrackingProject.query.filter(
        models.TrackingProject.user_id == user_id,
        models.TrackingProject.project_id == project_id,
    ).first()
    if tracking is not None:
        models.db.session.delete(tracking)
        models.db.session.commit()
    return get_project_tracked_by_user(user_id)