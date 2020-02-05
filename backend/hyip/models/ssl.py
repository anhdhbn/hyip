# coding=utf-8
import datetime

from hyip.models import TimestampMixin, db
from sqlalchemy.orm import relationship

class SSL(db.Model, TimestampMixin):
    __tablename__ = 'ssls'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    

    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    # project = db.relationship("Project", back_populates="ssl", cascade="all, delete")

    ev = db.Column(db.Boolean(False), default=False, nullable=False)
    from_date = db.Column(db.Date(), nullable=True)
    to_date = db.Column(db.Date(), nullable=True)
    description = db.Column(db.String(256), nullable=True, default='http')