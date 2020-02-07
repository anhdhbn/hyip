# coding=utf-8
import logging
from hyip import models
from sqlalchemy import desc

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def get_data_crawled(project_id, limit_):
    return models.CrawlData.query.filter(
        models.CrawlData.project_id == project_id,
    ).order_by(desc(models.CrawlData.created_date)).limit(limit_).all()

def create_crawldata(**kwargs):
    crawldata = models.CrawlData(**kwargs)
    models.db.session.add(crawldata)
    models.db.session.commit()
    return crawldata