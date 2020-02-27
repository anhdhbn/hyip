# coding=utf-8
import logging

from flask_mail import Mail

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

from . import crawldata
from . import project
from . import status
from . import domain
from . import tracking

my_mail = Mail()


def init_app(app):
    my_mail.init_app(app)
