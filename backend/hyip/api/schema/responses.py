# coding=utf-8
from flask_restplus import fields

from hyip.api import api
from hyip import models

user_res = {
    'id': fields.String(),
    'email': fields.String(description='user email address'),
    'username': fields.String(description='user username'),
    'fullname': fields.String(description='fullname of user'),
    'is_admin': fields.Boolean(description='user is admin or not'),
    'updated_at': fields.DateTime(),
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
    'easy_crawl': fields.Boolean(),
    'crawlable': fields.Boolean(),
}

check_selector_res  = {
    'total_investments': fields.Float(),
    'total_paid_outs': fields.Float(),
    'total_members': fields.Integer(),
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

search_domain = api.model("search_domain", {
    'value': fields.String(attribute='project_id'),
    'label': fields.String(attribute='name')
})

ssl_fields = api.model('ssl_fields', {
    'ev': fields.Boolean(),
    'from_date': fields.Date(),
    'to_date': fields.Date(),
    'description': fields.String(),
})

domain_fields = api.model('ssl_fields', {
    'name': fields.String(),
    'registrar': fields.String(),
    'from_date': fields.Date(),
    'to_date': fields.Date(),
})

ip_fields = api.model('ip_fields', {
    'address': fields.String(),
    'domains_of_this_ip': fields.String(),
})

script_fields = api.model('script_fields', {
    'script_type': fields.String(),
})

details_project = api.model("details_project", {
    'hosting': fields.String(),
    'plans': fields.String(),
    'created_at': fields.Date(),
    'start_date': fields.Date(),
    'plans': fields.String(),
    'easy_crawl': fields.Boolean(required=False),
    'ssl': fields.Nested(ssl_fields),
    'domain': fields.Nested(domain_fields),
    'ip': fields.Nested(ip_fields),
    'script': fields.Nested(script_fields),
    'type_currency': fields.String(required=False),
})


projects_tracked_by_user = api.model("tracking.projects_tracked_by_user", {
    'project_id': fields.String(),
})

check_projects_tracked = api.model("tracking.check_projects_tracked", {
    'tracked': fields.Boolean(),
})