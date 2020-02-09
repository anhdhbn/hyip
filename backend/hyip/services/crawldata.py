# coding=utf-8
import logging
import os

from flask import jsonify
from hyip import repositories as repo
from hyip.extensions.custom_exception import ProjectNotFoundException

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

def create_crawldata(project_id, **kwargs):
    if repo.project.check_exists_project_id(project_id):
        return repo.crawldata.create_crawldata(project_id=project_id, **kwargs)
    else:
        raise ProjectNotFoundException()

def parse_number(s):
    try:
        return int(s)
    except ValueError:
        return 100000000

def get_data_crawled(project_id, limit='7'):
    limit = parse_number(limit)
    if repo.project.check_exists_project_id(project_id):
        return repo.crawldata.get_data_crawled(project_id, limit)
    else:
        raise ProjectNotFoundException()