# coding=utf-8
from hyip.models import db, TimestampMixin
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType
import enum

class LicensedType(enum.IntEnum):
    LICENSED = 0
    UNKNOWN = 1
    NOTLICENSED = 2

class Script(db.Model, TimestampMixin):
    __tablename__ = 'scripts'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    # project = db.relationship("Project", back_populates="script", cascade="all, delete")
    source_page = db.Column(db.Text(4294000000), nullable=False)
    script_type = db.Column(db.Integer(), default=1, nullable=False)