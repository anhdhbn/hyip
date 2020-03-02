# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def search_domains(inputValue, page, ipp):
    items = models.Project.query.filter(
        models.Project.domain.like(inputValue + '%')
    ).paginate(int(page), int(ipp), error_out=False).items

    if len(items) == 0:
        return models.Project.query.filter(
        models.Project.domain.like('%' + inputValue + '%')
    ).paginate(int(page), int(ipp), error_out=False).items
    else:
        return items