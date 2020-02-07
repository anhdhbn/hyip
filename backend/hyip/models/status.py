# coding=utf-8
from sqlalchemy import func
from hyip.models import TimestampMixin, db

from sqlalchemy_utils import ChoiceType
import enum

class StatusType(enum.IntEnum):
    PAYING = 0
    WAITING = 1
    PROBLEM = 2
    SCAM = 3

class StatusProject(db.Model, TimestampMixin):
    __tablename__ = 'status_projects'
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)

    status_project = db.Column(ChoiceType(StatusType, impl=db.Integer()), default=1, nullable=False)
    created_date = db.Column(db.Date(), default=func.current_date(), nullable=False)
