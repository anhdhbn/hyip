# coding=utf-8
from sqlalchemy import func
from hyip.models import db, TimestampMixin

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

    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    last_login = db.Column(db.TIMESTAMP, nullable=False, default=func.now())

    # from hyip.models import tracking_project as tp
    # tracking_projects = db.relationship('Project', secondary="tracking_projects")
    tracking_projects = db.relationship("TrackingProject", uselist=True, cascade="all, delete-orphan", backref="projects")
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'avatarUrl': self.avatar_url,
            'isAdmin': self.is_admin,
            'isActive': self.is_active,
            'password': self.password,
        }

    def to_display_dict(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'is_admin': self.is_admin,
            'is_active': self.is_active,
            'created_at': datetime.datetime.timestamp(self.created_at),
            'updated_at': datetime.datetime.timestamp(self.updated_at)
        }
