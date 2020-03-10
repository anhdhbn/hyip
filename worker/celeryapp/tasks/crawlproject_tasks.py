from celeryapp import celery
import logging
import requests

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

@celery.task(name='celeryapp.tasks.crawl_project')
def crawl_project():
    from celeryapp.crawl_projects import CrawlProjects
    temp = CrawlProjects()
    result = temp.crawl()
    return result