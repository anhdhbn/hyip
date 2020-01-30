# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def save_project_to_database(domain_info, ip_info, ssl_info, project_info, status_info):
    domain =  models.Domain(**domain_info)
    ssl = models.SSL(**ssl_info)
    ip = models.IP(**ip_info)
    project = models.Project(ssl=ssl,domain=domain,ip=ip, **project_info)
    status_project = models.StatusProject(**status_info)
    project.project_statuses.append(status_project)
    models.db.session.add(project)
    models.db.session.commit()
    return project

def check_exists_domain(domain):
    project = models.Project.query.filter(
        models.Domain.name == domain,
    ).first()
    return project is not None

def get_project_by_id(idProject):
    project = models.Project.query.get(idProject)
    return project

def check_exists_project_id(idProject):
    project = models.Project.query.filter(
        models.Project.id == idProject,
    ).first()
    return project is not None

def get_all_project():
    return models.Project.query.all()

def get_easy_project_info():
    return models.Project.query.filter(
        models.Project.easy_crawl == True,
    ).all()