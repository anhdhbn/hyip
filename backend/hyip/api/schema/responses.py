# coding=utf-8
from flask_restplus import fields

from hyip.api import api

user_res = {
    'email': fields.String(description='user email address'),
    'username': fields.String(description='user username'),
    'fullname': fields.String(description='fullname of user'),
    'avatar_url': fields.String(description='avatar url of user'),
    'is_active': fields.Boolean(description='user is active or not'),
    'is_admin': fields.Boolean(description='user is admin or not')
}

register_res = {
    'username': fields.String(description="Username"),
    'email': fields.String(description="Email"),
    'fullname': fields.String(description="User full name"),
}

project_res = {
    'id': fields.String(),
    'url': fields.Url(endpoint="api.processing_celery")
    # 'hosting': fields.String(),
    # 'script': fields.Integer(),
    # 'url': fields.String(),
    # 'investment_selector': fields.String(),
    # 'paid_out_selector': fields.String(),
    # 'member_selector': fields.String(),
    # 'created_at': fields.Date(),
    # 'start_date': fields.Date(),
    # 'plans': fields.String(),
    # 'ssl': 
    # 'domain':
    # 'ip':
}


project_crawler_res = {
    'id': fields.String(),
    'hosting': fields.String(),
    'script': fields.Integer(),
    'url': fields.String(),
    'investment_selector': fields.String(),
    'paid_out_selector': fields.String(),
    'member_selector': fields.String(),
    'created_at': fields.Date(),
    'start_date': fields.Date(),
    'plans': fields.String(),
    # 'ssl': 
    # 'domain':
    # 'ip':
}

crawl_data_res = {
    'id': fields.String(),
    'project_id': fields.String(),
    'total_investment': fields.Float(),
    'total_paid_out': fields.Float(),
    'total_member': fields.Integer(),
    'alexa_rank': fields.Integer(),
}