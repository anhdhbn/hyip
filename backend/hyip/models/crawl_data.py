# coding=utf-8
from sqlalchemy import func
import sqlalchemy  as sq
from hyip.models import db, TimestampMixin

class CrawlData(TimestampMixin, db.Model):
    __tablename__ = 'crawldata'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    project_id = db.Column(db.String(64), db.ForeignKey('projects.id'), nullable=False)
    projects = db.relationship("Project", back_populates="crawl_data")
    
    tracking_day = db.Column(db.Date(), default=func.now(), nullable=False)
    total_investment = db.Column(db.REAL(), nullable=False)
    total_paid_out = db.Column(db.REAL(), nullable=False)
    total_member = db.Column(db.Integer(), nullable=False, default=0)
    alexa_rank =  db.Column(db.Integer(), nullable=False, default=0)

    create_date = db.Column(db.Date(), default=func.current_date(), nullable=False)
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