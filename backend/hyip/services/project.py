# coding=utf-8
import logging
import os

from flask import jsonify
from flask import request
from hyip import repositories as repo
from hyip.helpers import get_domain
from hyip.extensions.custom_exception import DomainExistsException, ProjectNotFoundException
from hyip.extensions.exceptions import BadRequestException

from celery.result import AsyncResult
from hyip.celery import cele

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


def create_project(**kwargs):
    domain = get_domain(kwargs.get('url_crawl'))
    if not repo.project.check_exists_domain(domain):
        return repo.project.create_project(
            domain=domain,
            **kwargs
        )
    else:
        raise DomainExistsException(message=domain)

def get_project_info_by_id(idProject):
    if repo.project.check_exists_project_id(idProject):
        return repo.project.get_project_by_id(idProject)
    else:
        raise ProjectNotFoundException()

def get_all_projects_info():
    return repo.project.get_all_projects()

def get_easy_projects_info():
    return repo.project.get_easy_projects_info()

def get_diff_projects_info():
    return repo.project.get_diff_projects_info()

def get_not_scam_projects_info():
    return repo.project.get_not_scam_projects_info()

def get_verified_projects():
    return repo.project.get_verified_projects()

def get_unverified_projects():
    return repo.project.get_unverified_projects()