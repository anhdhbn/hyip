from celeryapp import celery
import logging
import requests

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

@celery.task(name='celeryapp.tasks.crawl_easy_project_every_day', queue='default')
def crawl_easy_project_every_day():
    result = requests.get(celery.conf.URL['get_easy_project'])
    result.raise_for_status()
    result = result.json()
    for item in result['data']:
        crawl_easy_project.delay(**item)
    return len(result['data'])

@celery.task(name='celeryapp.tasks.crawl_diff_project_every_day', queue='default')
def crawl_diff_project_every_day():
    result = requests.get(celery.conf.URL['get_diff_project'])
    result.raise_for_status()
    result = result.json()
    for item in result['data']:
        crawl_diff_project.delay(**item)
    return len(result['data'])

@celery.task(name='celeryapp.tasks.crawl_easy_project', max_retries=3, exponential_backoff=2, retry_jitter=False, autoretry_for=(Exception,), queue='default')
def crawl_easy_project(**kwargs):
    from celeryapp.crawl_data import EasyCrawl
    temp = EasyCrawl(**kwargs)
    return temp.crawl()

@celery.task(name="celeryapp.tasks.crawl_diff_project", max_retries=3, exponential_backoff=2, retry_jitter=False, autoretry_for=(Exception,), queue='diff')
def crawl_diff_project(**kwargs):
    from celeryapp.driver import Wrapper
    from celeryapp.crawl_data import DiffCrawl
    temp = Wrapper(DiffCrawl(**kwargs))
    return temp.crawl()