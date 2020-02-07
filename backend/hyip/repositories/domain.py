# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def check_exists_domain(domain):
    domain = models.Domain.query.filter(
        models.Domain.name == domain,
    ).first()
    return {
        "is_exists": domain is not None
    }

def get_all_domain():
    return models.Domain.query.all()