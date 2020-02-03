# coding=utf-8
import datetime

from hyip.models import db, TimestampMixin

class TrackingProject(db.Model, TimestampMixin):    
    __tablename__ = 'tracking_projects'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.String(64), db.ForeignKey('users.id'),nullable=False)

    is_playing = db.Column(db.Boolean, default=0, nullable=False)

    # db.PrimaryKeyConstraint('project_id', 'user_id')
    # users = db.relationship("User", backref=db.backref("tracking_projects", cascade="all, delete-orphan", uselist=True))
    project_tracked_by_users = db.relationship("User", uselist=True, cascade="all, delete", backref="tracking_projects")

# tracking_project = db.Table('tracking_project', TimestampMixin.metadata,
#     db.Column('project_id', db.String(64), db.ForeignKey('projects.id'), nullable=False),
#     db.Column('user_id',db.String(64), db.ForeignKey('users.id'),nullable=False),
#     db.Column('is_playing', db.Boolean, default=0, nullable=False),
#     db.PrimaryKeyConstraint('project_id', 'user_id') )