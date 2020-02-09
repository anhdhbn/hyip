# coding=utf-8
from sqlalchemy import func
from hyip.models import db, TimestampMixin
import datetime

class User(db.Model, TimestampMixin):
    """
    Contains information of users table
    """
    __tablename__ = 'users'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    fullname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256))

    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # from hyip.models import tracking_project as tp
    # tracking_projects = db.relationship('Project', secondary="tracking_projects")
    tracking_projects = db.relationship("TrackingProject", uselist=True, cascade="all, delete", back_populates="project_tracked_by_users")
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'isAdmin': self.is_admin,
            'password': self.password,
        }

    def to_display_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'is_admin': self.is_admin,
            'created_at': datetime.datetime.timestamp(self.created_at),
            'updated_at': datetime.datetime.timestamp(self.updated_at)
        }
