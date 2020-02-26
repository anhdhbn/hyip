# coding=utf-8
import logging

from flask import Blueprint
from flask_restplus import Api
import config

from hyip.extensions.exceptions import global_error_handler

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__, url_prefix=config.API_PREFIX)

api = Api(
    app=api_bp,
    version='1.0',
    title='Hyip Management API',
    validate=False,
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    from .project import ns as project_ns
    from .crawldata import ns as crawldata_ns
    from .process import ns as process_ns
    from .status import ns as status_ns
    from .domain import ns as domain_ns
    
    api.add_namespace(crawldata_ns)
    api.add_namespace(process_ns)
    api.add_namespace(domain_ns)
    api.add_namespace(project_ns)
    api.add_namespace(status_ns)

    app.register_blueprint(api_bp)

    api.error_handlers[Exception] = global_error_handler


from .schema import requests, responses
