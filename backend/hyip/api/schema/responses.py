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
    # 'url': fields.Url(endpoint="api.processing_celery")
}


project_crawler_res = {
    'id': fields.String(),
    'hosting': fields.String(),
    'url': fields.String(),
    'investment_selector': fields.String(),
    'paid_out_selector': fields.String(),
    'member_selector': fields.String(),
    'created_at': fields.Date(),
    'start_date': fields.Date(),
    'plans': fields.String(),
}

check_selector_res  = {
    'total_investment': fields.Float(),
    'total_paid_out': fields.Float(),
    'total_member': fields.Integer(),
}

crawl_data_res = {
    'id': fields.String(),
    'project_id': fields.String(),
    **check_selector_res,
    'alexa_rank': fields.Integer(),
    'created_date': fields.Date(),
}

status_project_res = {
    'id': fields.String(),
    'project_id': fields.String(),
    'status_project': fields.Integer(),
    'created_date': fields.Date(),
}

exist_domain_res = {
    'is_exists': fields.Boolean(),
}

get_all_domain = {
    'id': fields.String(),
    'project_id': fields.String(),
    'name': fields.String(),
    'registrar': fields.String(),
    'from_date': fields.Date(),
    'to_date': fields.Date(),
}