# coding=utf-8
import datetime
from sqlalchemy import func
from hyip.models import db, TimestampMixin
from sqlalchemy_utils import ChoiceType
import enum

from sqlalchemy.orm import backref


class Project(db.Model, TimestampMixin):
    __tablename__ = 'projects'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    url_crawl = db.Column(db.String(64), nullable=False)
    domain = db.Column(db.String(64), nullable=False)
    
    investment_selector = db.Column(db.String(1024), nullable=False,  default='')
    paid_out_selector = db.Column(db.String(1024), nullable=False,  default='')
    member_selector = db.Column(db.String(1024), nullable=False,  default='')

    easy_crawl = db.Column(db.Boolean(), nullable=False, default=False)
    is_verified = db.Column(db.Boolean(), default=False, nullable=False)
    crawlable = db.Column(db.Boolean(), default=False, nullable=False)
    tracked = db.Column(db.Boolean(), default=False, nullable=False)
    type_currency = db.Column(db.String(3), nullable=True, default="")

    created_date = db.Column(db.Date(), default=func.current_date(), nullable=False)
    # USD
    # BTC
    # RUB nga

    # project_statuses = db.relationship("StatusProject", uselist=True, cascade="all, delete-orphan", backref="projects")
    project_statuses = db.relationship("StatusProject", uselist=True, cascade="all, delete-orphan")
    crawl_data = db.relationship("CrawlData", uselist=True, cascade="all, delete-orphan")