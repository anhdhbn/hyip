# coding=utf-8
from hyip.models import db, TimestampMixin
from sqlalchemy.orm import relationship

class IP(db.Model, TimestampMixin):
    __tablename__ = 'ips'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    projects = db.relationship("Project", back_populates="ip", cascade="all, delete")
    address = db.Column(db.String(64), nullable=False)
    domains_of_this_ip = db.Column(db.Text(), nullable=False)