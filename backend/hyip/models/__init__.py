
# coding=utf-8
import logging

import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs
from dotenv import load_dotenv
from flask_redis import FlaskRedis
from mockredis import MockRedis
from datetime import datetime, timedelta
from hyip.helpers.env import get_environ

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from config import _DOT_ENV_PATH

load_dotenv(_DOT_ENV_PATH)

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()
redis_client = FlaskRedis()
# Create mock redis for unit test
if get_environ('IS_TESTING_ENV') == 'True':
    redis_client = FlaskRedis.from_custom_provider(MockRedis)


def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)

    _logger.info('Start app in {env} environment with database: {db}'.format(
        env=app.config['ENV_MODE'],
        db=app.config['SQLALCHEMY_DATABASE_URI']
    ))

    redis_client.init_app(app)

def get_day_vn():
    return (datetime.utcnow() + timedelta(hours=7)).date()

def get_time_vn():
    return str((datetime.utcnow() + timedelta(hours=7)))

from .base import TimestampMixin
from .crawl_data import CrawlData
from .domain import Domain
from .ip import IP
from .project import Project
from .ssl import SSL
from .status import StatusProject
# from .tracking import tracking_project
from .user import User
# from .pending_register import Pending_register
# from .password import Password
# from .log import Log
# from .notification import Notification