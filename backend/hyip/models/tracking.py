# coding=utf-8
import datetime

from hyip.models import db, TimestampMixin

from sqlalchemy_utils import ChoiceType
import enum

class StatusType(enum.Enum):
    Playing = 1
    Tracking = 2

# class TrackingProject(db.Model, TimestampMixin):    
#     __tablename__ = 'tracking_projects'

#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             setattr(self, k, v)

#     id = db.Column(db.String(64), primary_key=True, default=uuid4())
#     status_tracking = db.Column(ChoiceType(StatusType, impl=sa.Integer()), default=1, nullable=False)

tracking_project = db.Table('tracking_project', 
    db.Column('project_id', db.String(64), db.ForeignKey('projects.id'), nullable=False),
    db.Column('user_id',db.String(64), db.ForeignKey('users.id'),nullable=False),
    db.Column(ChoiceType(StatusType, impl=db.Integer()), default=1, nullable=False),
    db.PrimaryKeyConstraint('project_id', 'user_id') )