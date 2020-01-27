# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def get_data_crawled(project_id):
    return models.CrawlData.query.filter(
        models.CrawlData.project_id == project_id,
    ).all()

def create_crawldata(**kwargs):
    crawldata = models.CrawlData(**kwargs)
    models.db.session.add(crawldata)
    models.db.session.commit()
    return crawldata