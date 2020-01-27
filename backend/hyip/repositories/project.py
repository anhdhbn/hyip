# coding=utf-8
import logging
from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def save_project_to_database(hosting, domain_info, ip_info, ssl_info, **kwargs):
    name, registrar, from_date, to_date =  domain_info
    domain =  models.Domain(name=name, registrar=registrar, from_date=from_date, to_date=to_date)

    ev, from_date, to_date, description = ssl_info
    ssl = models.SSL(ev=ev, from_date=from_date, to_date=to_date, description=description)

    address, domains_of_this_ip = ip_info
    ip = models.IP(address=address, domains_of_this_ip=domains_of_this_ip)
    project = models.Project(hosting=hosting,ssl=ssl,domain=domain,ip=ip, **kwargs)
    
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