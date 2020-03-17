# coding=utf-8
import logging
from hyip import models
from sqlalchemy import desc

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def get_all_bad_data():
    return models.BadData.query.filter(
        models.BadData.solved == False,
    ).order_by(desc(models.BadData.created_at)).all()

def solve_bad_data(id):
    bad_data = models.BadData.query.get(id)
    bad_data.solved = True
    models.db.session.commit()
    return bad_data

def create_bad_data(**kwargs):
    bad_data = models.BadData(**kwargs)
    models.db.session.add(bad_data)
    models.db.session.commit()
    return bad_data