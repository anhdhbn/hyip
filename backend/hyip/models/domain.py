# coding=utf-8
import datetime

from hyip.models import db, TimestampMixin
from sqlalchemy.orm import relationship

class Domain(db.Model, TimestampMixin):
    __tablename__ = 'domains'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    projects = db.relationship("Project", back_populates="domain", cascade="all, delete")

    name = db.Column(db.String(64), nullable=False)
    registrar = db.Column(db.String(64), nullable=False)
    from_date = db.Column(db.Date(), nullable=False)
    to_date = db.Column(db.Date(), nullable=False)