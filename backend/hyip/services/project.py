# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.helpers import get_hosting_info_from_domain, get_info_from_domain, get_ip_info_from_domain, get_ssl_info_from_domain, get_domain
from hyip.extensions.custom_exception import DomainExistsException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


# Check exists domain

def create_project(url, **kwargs):
    domain = get_domain(url)

    if not repo.project.check_exists_domain(domain):
        hosting = get_hosting_info_from_domain(url)
        domain_info = get_info_from_domain(url)
        ip_info = get_ip_info_from_domain(url)
        ssl_info = get_ssl_info_from_domain(url)
        project = repo.project.save_project_to_database(
            hosting=hosting,
            domain_info=domain_info,
            ip_info=ip_info,
            ssl_info=ssl_info,
            url=url,
            **kwargs
        )
        return project
    else:
        raise DomainExistsException(errors=domain)

def get_project_info_by_id(idProject):
    return repo.project.get_project_by_id(idProject)

def get_all_project_info():
    return repo.project.get_all_project()