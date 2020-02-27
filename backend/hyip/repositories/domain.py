# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def search_domains(inputValue, page, ipp):
    return models.Project.query.filter(
        models.Domain.name.like(inputValue + '%')
    ).paginate(int(page), int(ipp), error_out=False).items