# coding=utf-8
import logging
import flask_restplus

from hyip.celery import cele
from hyip.extensions import Namespace
from celery.result import AsyncResult

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


ns = Namespace('celery', description='Celery operations')


@ns.route('/<id>', methods=['GET'], endpoint="processing_celery")
class GetProjectInfo(flask_restplus.Resource):
    def get(self, id):
        result = AsyncResult(id=id, app=cele)
        return result.get()