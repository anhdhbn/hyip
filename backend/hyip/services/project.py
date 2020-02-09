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


# Check exists domain

def create_project(**kwargs):
    domain = get_domain(kwargs.get('url'))

    if not repo.project.check_exists_domain(domain):
        result = cele.send_task("jobqueue.tasks.crawl_info_project", kwargs=kwargs)
        return result
    else:
        raise DomainExistsException(errors=domain)


def create_project_by_crawler(**kwargs):
    project_info = kwargs.get('project', {})

    domain = get_domain(project_info.get('url'))
    if not repo.project.check_exists_domain(domain):
        domain_info = kwargs.get('domain', {})
        ip_info = kwargs.get('ip', {})
        ssl_info = kwargs.get('ssl', {})
        status_info  =  kwargs.get('status', {})
        script_info  =  kwargs.get('script', {})

        project = repo.project.save_project_to_database(
            domain_info=domain_info,
            ip_info=ip_info,
            ssl_info=ssl_info,
            project_info=project_info,
            status_info=status_info,
            script_info=script_info
        )
        return project
    else:
        raise DomainExistsException(message=domain)

def get_project_info_by_id(idProject):
    if repo.project.check_exists_project_id(idProject):
        return repo.project.get_project_by_id(idProject)
    else:
        raise ProjectNotFoundException()

def get_all_project_info():
    return repo.project.get_all_project()

def get_easy_project_info():
    return repo.project.get_easy_project_info()

def get_not_scam_project_info():
    return repo.project.get_not_scam_project_info()

def verify_project(id_project):
    if repo.project.check_exists_project_id(id_project):
        return repo.project.verify_project(id_project)
    else:
        raise ProjectNotFoundException()

def get_verified_projects():
    return repo.project.get_verified_projects()

def get_unverified_projects():
    return repo.project.get_unverified_projects()

def remove_project(id_project):
    if repo.project.check_exists_project_id(id_project):
        return repo.project.remove_project(id_project)
    else:
        raise ProjectNotFoundException()

def update_selector(id_project, **kwargs):
    if repo.project.check_exists_project_id(id_project):
        return repo.project.update_selector(id_project, **kwargs)
    else:
        raise ProjectNotFoundException()