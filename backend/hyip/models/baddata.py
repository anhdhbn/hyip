# coding=utf-8
from sqlalchemy import func
from hyip.models import TimestampMixin, db

class BadData(db.Model, TimestampMixin):
    __tablename__ = 'bad_data'
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    solved = db.Column(db.Boolean(), default=False, nullable=False)