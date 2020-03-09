from celeryapp import celery
import logging
import requests

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

@celery.task(name='celeryapp.tasks.check_scam_all')
def check_scam_all():
    result = requests.get(celery.conf.URL['get_not_scam_project'])
    result.raise_for_status()
    result = result.json()
    for item in result['data']:
        check_scam.delay(item)
    return len(result['data'])

@celery.task(name='celeryapp.tasks.check_scam', max_retries=3, exponential_backoff=2, retry_jitter=False, autoretry_for=(Exception,))
def check_scam(project):
    from celeryapp.check_scam import CheckScam
    temp = CheckScam()
    result = temp.check(project)
    return "{} status: {}".format(project['url_crawl'], result)