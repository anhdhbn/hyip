# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def check_exists_domain(domain):
    domain_obj = repo.project.check_exists_domain(domain)
    return {
        "is_exists": domain_obj is not None
    }

def search_domains(input='', page=1, ipp=10):
    return repo.domain.search_domains(input, page, ipp)