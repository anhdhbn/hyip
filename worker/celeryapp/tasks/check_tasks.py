from celeryapp import celery
import logging

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

@celery.task(name="easy.check_easy")
def check_easy(**kwargs):
    from celeryapp.crawl_data import EasyCrawl
    temp = EasyCrawl(**kwargs)
    return temp.get_only_info_project()