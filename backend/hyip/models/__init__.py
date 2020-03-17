
# coding=utf-8
import logging

import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs
from datetime import datetime, timedelta

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from config import _DOT_ENV_PATH


db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()


def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)

    _logger.info('Start app in {env} environment with database: {db}'.format(
        env=app.config['APP_ENV'],
        db=app.config['SQLALCHEMY_DATABASE_URI']
    ))


from .base import TimestampMixin
from .crawl_data import CrawlData
from .project import Project
from .status import StatusProject
from .baddata import BadData
# from .pending_register import Pending_register
# from .password import Password
# from .log import Log
# from .notification import Notification