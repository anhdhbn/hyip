# coding=utf-8
import datetime
from sqlalchemy import func
from hyip.models import db, TimestampMixin
from sqlalchemy_utils import ChoiceType
import enum

from sqlalchemy.orm import backref

class LicensedType(enum.IntEnum):
    PAYING = 0
    WAITING = 1
    PROBLEM = 2
    SCAM = 3

class Project(db.Model, TimestampMixin):
    __tablename__ = 'projects'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    hosting = db.Column(db.String(64), nullable=False)
    script = db.Column(ChoiceType(LicensedType, impl=db.Integer()), default=1, nullable=False)
    url = db.Column(db.String(64), nullable=False)
    
    investment_selector = db.Column(db.String(1024), nullable=False,  default='')
    paid_out_selector = db.Column(db.String(1024), nullable=False,  default='')
    member_selector = db.Column(db.String(1024), nullable=False,  default='')
    start_date = db.Column(db.Date(), nullable=False)
    plans = db.Column(db.String(1024), nullable=True, default='')
    easy_crawl = db.Column(db.Boolean, nullable=False, default=False)
    create_date = db.Column(db.Date(), default=func.current_date(), nullable=False)

    ssl =  db.relationship("SSL", uselist=False, back_populates="projects", cascade="all, delete")
    domain =  db.relationship("Domain", uselist=False, back_populates="projects", cascade="all, delete")
    ip =  db.relationship("IP", uselist=False, back_populates="projects", cascade="all, delete")

    project_statuses = db.relationship("StatusProject", uselist=True, back_populates="projects", cascade="all, delete")
    crawl_data = db.relationship("CrawlData", uselist=True, back_populates="projects", cascade="all, delete")

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'hosting': self.hosting,
    #         'script': self.script,
    #         'url': self.url,
    #         'investment_selector': self.investment_selector,
    #         'paid_out_selector': self.paid_out_selector,
    #         'member_selector': self.member_selector,
    #         'start_date': self.start_date,
    #         'plans': self.plans,
    #         'ssl': self.ssl,
    #     }    