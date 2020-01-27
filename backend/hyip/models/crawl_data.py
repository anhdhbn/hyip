# coding=utf-8
from datetime import datetime, timedelta

from hyip.models import db, TimestampMixin, get_day_vn

import sqlalchemy  as sq

class CrawlData(TimestampMixin, db.Model):
    __tablename__ = 'crawldata'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    projects = db.relationship("Project", back_populates="crawl_data")
    
    tracking_day = db.Column(db.Date(), default =get_day_vn, nullable=False)
    total_investment = db.Column(db.REAL(), nullable=False)
    total_paid_out = db.Column(db.REAL(), nullable=False)
    total_member = db.Column(db.Integer(), nullable=False, default=0)
    alexa_rank =  db.Column(db.Integer(), nullable=False, default=0)

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'project_id': self.project_id,
    #         'tracking_day': self.tracking_day,
    #         'total_investment': self.fullname,
    #         'total_paid_out': self.total_paid_out,
    #         'total_member': self.total_member,
    #         'alexa_rank': self.alexa_rank,
    #     }