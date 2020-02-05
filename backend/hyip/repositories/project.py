# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def save_project_to_database(domain_info, ip_info, ssl_info, project_info, status_info, script_info):
    domain =  models.Domain(**domain_info)
    ssl = models.SSL(**ssl_info)
    ip = models.IP(**ip_info)
    script = models.Script(**script_info)
    project = models.Project(ssl=ssl,domain=domain,ip=ip, script=script, **project_info)
    status_project = models.StatusProject(**status_info)
    project.project_statuses.append(status_project)
    models.db.session.add(project)
    models.db.session.commit()
    return project

def check_exists_domain(domain):
    domain = models.Domain.query.filter(
        models.Domain.name == domain,
    ).first()
    return domain is not None

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

def get_not_scam_project_info():
    status_projects = models.StatusProject.query.filter(
        models.StatusProject.status_project == 3,
    ).all()
    ids = [item.id for item in status_projects]
    projects = models.Project.query.filter(models.Project.id.notin_(ids)).all()
    return projects

def get_unverified_projects():
    return models.Project.query.filter(
        models.Project.is_verified == False,
    ).all()

def get_verified_projects():
    return models.Project.query.filter(
        models.Project.is_verified == True,
    ).all()

def verify_project(id_project):
    project = models.Project.query.get(id_project)
    project.is_verified = True
    models.db.session.commit()
    return project

def remove_project(id_project):
    # models.Project.query.filter(
    #     models.Project.id == id_project,
    # ).delete()
    models.db.session.delete(get_project_by_id(id_project))
    models.db.session.commit()
    return models.Project.query.all()