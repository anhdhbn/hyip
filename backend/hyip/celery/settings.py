from celery.schedules import crontab
import os

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = f'redis://h:{os.getenv("REDIS_PASSWORD")}@{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}'
CELERY_ACCEPT_CONTENT = ['json']

# CELERY_IMPORTS = ('jobqueue.tasks')

CELERY_TASK_RESULT_EXPIRES = 30
# CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CELERY_RESULT_BACKEND = f'mongodb://{os.getenv("MONGO_USER")}:{os.getenv("MONGO_PASS")}@{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}/{os.getenv("MONGO_DB")}'
CELERY_RESULT_BACKEND = f'redis://h:{os.getenv("REDIS_PASSWORD")}@{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}'

CELERYBEAT_SCHEDULE = {
  'auto-crawl-data-every-day': {
    'task': 'jobqueue.tasks.crawl_easy_project_every_day',
    # 'schedule': crontab(minute='*'),
    'schedule': crontab(minute=0, hour=0),
  },
}
