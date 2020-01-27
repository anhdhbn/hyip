from celery.schedules import crontab
from . import app_info
CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = app_info.redis.redis_url
CELERY_ACCEPT_CONTENT = ['json']

CELERY_IMPORTS = ('jobqueue.tasks')

CELERY_TASK_RESULT_EXPIRES = 30
# CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'auto-crawl-data-every-day': {
      'task': 'jobqueue.tasks.crawl_data_every_day',
      # 'schedule': crontab(minute='*'),
      'schedule': crontab(minute=0, hour=0),
    },
}
