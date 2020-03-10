from celeryapp import celery
import logging

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

@celery.task(name="celeryapp.tasks.check_easy", queue='default')
def check_easy(**kwargs):
    from celeryapp.crawl_data import EasyCrawl
    temp = EasyCrawl(**kwargs)
    return temp.get_only_info_project()

@celery.task(name="celeryapp.tasks.check_diff", queue='diff')
def check_diff(**kwargs):
    from celeryapp.driver import Wrapper
    from celeryapp.crawl_data import DiffCrawl
    temp = Wrapper(DiffCrawl(**kwargs))
    return temp.get_only_info_project()