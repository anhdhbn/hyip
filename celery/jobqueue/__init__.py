from easydict import EasyDict as edict
from pathlib import Path
import os
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration

from dotenv import load_dotenv
env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path=env_path, verbose=True)

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_PORT = os.getenv("REDIS_PORT")

HEADLESS = os.getenv("HEADLESS")
BACKEND_HOST = os.getenv("BACKEND_HOST")

SENTRY_DSN=os.getenv("SENTRY_DSN")


app_info = edict({
    'redis': {
        'host': REDIS_HOST,
        'password': REDIS_PASSWORD,
        'port': REDIS_PORT,
        'redis_url': f'redis://h:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'
    },
    'headless': True if HEADLESS == "1" else False,
    'host': BACKEND_HOST,
    'sentry_dsn': SENTRY_DSN,
    'path': os.path.join(os.getcwd(), "jobqueue"),
    'env': os.getenv('ENV'),
    'is_production': os.getenv('ENV') == "prod",
    'url_get_easy_project': "{}api/project/easy".format(BACKEND_HOST),
    'url_post_data_crawled': lambda id: "{}api/crawldata/{}".format(BACKEND_HOST, id)
})


sentry_sdk.init(app_info.sentry_dsn, integrations=[CeleryIntegration()])