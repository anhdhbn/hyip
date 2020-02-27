# coding=utf-8
import logging
from hyip import models
from sqlalchemy import desc

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def check_exists_domain(domain):
    result = models.Project.query.filter(
        models.Project.domain == domain,
    ).first()
    return result is not None

def create_project(**kwargs):
    project = models.Project(**kwargs)
    models.db.session.add(project)
    models.db.session.commit()
    return project

def get_project_by_id(idProject):
    project = models.Project.query.get(idProject)
    return project

def check_exists_project_id(idProject):
    project = models.Project.query.filter(
        models.Project.id == idProject,
    ).first()
    return project is not None

def get_projects_id_scam():
    status_projects = models.StatusProject.query.filter(
        models.StatusProject.status_project == 3,
    ).all()
    return [item.project_id for item in status_projects]

def get_all_projects():
    return models.Project.query.all()

def get_easy_projects_info():
    # is easy and not scam
    ids = get_projects_id_scam()
    return models.Project.query.filter(
        models.Project.crawlable == True,
        models.Project.easy_crawl == True,
        models.Project.is_verified == True,
        models.Project.id.notin_(ids)
    ).all()

def get_diff_projects_info():
    ids = get_projects_id_scam()
    return models.Project.query.filter(
        models.Project.is_verified == True,
        models.Project.easy_crawl == False,
        models.Project.crawlable == True,
        models.Project.id.notin_(ids),
    ).all()

def get_not_scam_projects_info():
    ids = get_projects_id_scam()
    projects = models.Project.query.filter(models.Project.id.notin_(ids)).all()
    return projects

def get_unverified_projects():
    return models.Project.query.filter(
        models.Project.is_verified == False,
    ).order_by(models.Project.easy_crawl.desc()).all()

def get_verified_projects():
    return models.Project.query.filter(
        models.Project.is_verified == True,
    ).all()

def update_project(id_project, **kwargs):
    project = get_project_by_id(id_project)
    project.is_verified  = True
    for k, v in kwargs.items():
        tmp = kwargs.get(k, getattr(project, k, v))
        setattr(project, k, tmp)
    models.db.session.commit()
    return project

def remove_project(id_project):
    models.db.session.delete(get_project_by_id(id_project))
    models.db.session.commit()
    return models.Project.query.all()

def verify_project(id_project):
    project = get_project_by_id(id_project)
    project.is_verified = True
    models.db.session.commit()
    return project