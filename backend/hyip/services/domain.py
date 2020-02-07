# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def check_exists_domain(domain):
    return repo.domain.check_exists_domain(domain)

def get_all_domain():
    return repo.domain.get_all_domain()