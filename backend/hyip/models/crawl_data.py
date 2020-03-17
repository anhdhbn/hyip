# coding=utf-8
from sqlalchemy import func
import sqlalchemy  as sq
from hyip.models import db, TimestampMixin
import json

class CrawlData(TimestampMixin, db.Model):
    __tablename__ = 'crawldata'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    
    tracking_day = db.Column(db.Date(), default=func.current_date(), nullable=False)
    total_investments = db.Column(db.REAL(), nullable=False)
    total_paid_outs = db.Column(db.REAL(), nullable=False)
    total_members = db.Column(db.Integer(), nullable=False, default=0)
    alexa_rank =  db.Column(db.Integer(), nullable=False, default=0)

    created_date = db.Column(db.Date(), default=func.current_date(), nullable=False)

    def __repr__(self):
        dic = {}
        keys = [key for key in self.__dict__.keys() if '__' not in key]
        for key in keys:
            dic[key] = self.__dict__[key]
        print(dic)
        return {
            'id': self.id
        }