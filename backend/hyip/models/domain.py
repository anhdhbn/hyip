# coding=utf-8
from sqlalchemy import func
from hyip.models import db, TimestampMixin
from sqlalchemy.orm import relationship

class Domain(db.Model, TimestampMixin):
    __tablename__ = 'domains'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    # project = db.relationship("Project", back_populates="domain", cascade="all, delete")

    name = db.Column(db.String(64), nullable=False)
    registrar = db.Column(db.String(64), nullable=True)
    from_date = db.Column(db.Date(), nullable=True)
    to_date = db.Column(db.Date(), nullable=True)