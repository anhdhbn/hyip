from celery.schedules import crontab
import os
import sys
from dotenv import load_dotenv

__author__ = 'AnhDH'

_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)

APP_ENV = os.environ.get('APP_ENV', 'DEV').upper()
os.environ['APP_ENV'] = APP_ENV

for k, v in os.environ.items():
    if APP_ENV in k:
        k = k.replace(f"{APP_ENV}_", "")
        os.environ[k] = v

import settings

_current = getattr(sys.modules['settings'], '{0}'.format(APP_ENV))()
# copy attributes to the module for convenience
for atr in [f for f in dir(_current) if not '__' in f]:
    # environment can override anything
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)

def _env(name, default):
    """ Get configuration from environment in priorities:
      1. the env var with prefix of $APP_ENV
      2. the env var with the same name (in upper case)
      3. the default value
    :param str name: configuration name
    :param default: default value
    """

    def _bool(val):
        if not val:
            return False
        return val not in ('0', 'false', 'no')

    # make sure configuration name is upper case
    name = name.upper()

    # try to get value from env vars
    val = default
    for env_var in ('%s_%s' % (APP_ENV, name), name):
        try:
            val = os.environ[env_var]
            break
        except KeyError:
            pass
    else:
        env_var = None

    # convert to the right types
    if isinstance(default, bool):
        val = _bool(val)
    return env_var, val


__IGNORED_CONFIG = (
    'ROOT_DIR',
    'STATIC_DIR',
    'APP_ENV',
)

# rewrite all configuration with environment variables
_vars = list(locals().keys())
for name in _vars:
    if name in __IGNORED_CONFIG:
        continue
    if not name.startswith('_') and name.isupper():
        env_var, val = _env(name, locals()[name])
        locals()[name] = val


CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = REDIS_URL
CELERY_ACCEPT_CONTENT = ['json']

# CELERY_IMPORTS = ('jobqueue.tasks')

CELERY_TASK_RESULT_EXPIRES = 30

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "Europe/Paris"
CELERYBEAT_SCHEDULE = {
  'auto-crawl-project-every-day': {
    'task': 'celeryapp.tasks.crawl_project',
    'schedule': crontab(minute=0, hour=0),
    'options': {'queue': 'default'}
  },
  'auto-check-scam-every-day': {
    'task': 'celeryapp.tasks.check_scam_all',
    'schedule': crontab(minute=0, hour=2),
    'options': {'queue': 'default'}
  },
  'crawl-easy-project-every-day': {
    'task': 'celeryapp.tasks.crawl_easy_project_every_day',
    'schedule': crontab(minute=0, hour=3),
    'options': {'queue': 'default'}
  },
  'crawl-diff-project-every-day': {
    'task': 'celeryapp.tasks.crawl_diff_project_every_day',
    'schedule': crontab(minute=0, hour=4),
    'options': {'queue': 'diff'}
  },
}



from kombu import Queue

TASKS_QUEUES = (
    Queue('default', exchange='default', routing_key='default'),
    Queue('diff', exchange='diff', routing_key='diff')
)

CELERY_CREATE_MISSING_QUEUES = True

TASK_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'

# CELERY_TASK_ROUTES = {
#   'diff.tasks.*': 'diff',
#   'easy.tasks.*': 'easy',
# }