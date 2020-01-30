# coding=utf-8
from flask_restplus import fields
from hyip.api import api

register_user_req = {
    'email': fields.String(required=True, description='user email address'),
    'username': fields.String(required=True, description='user username'),
    'fullname': fields.String(required=True, description='fullname of user'),
    'password': fields.String(required=True, description='user password'),
}

login_req = {
    'username': fields.String(required=True, description='username'),
    'password': fields.String(required=True, description='password'),
}

create_project_req = {
    'url': fields.String(required=True),
    'script': fields.Integer(required=True),
    'investment_selector': fields.String(required=False),
    'paid_out_selector': fields.String(required=False),
    'member_selector': fields.String(required=False),
    'start_date': fields.Date(required=True),
    'plans': fields.String(required=True),
    'easy_crawl': fields.Boolean(required=False),
}

post_datacrawled_req = {
    'total_investment': fields.Float(required=True),
    'total_paid_out': fields.Float(required=True),
    'total_member': fields.Integer(required=True),
    'alexa_rank': fields.Integer(required=True),
}

project = api.model('project_sub', {
    'url' : fields.String(required=True),
    'script' : fields.Integer(required=True),
    'start_date' : fields.Date(required=True),
    'plans' : fields.String(required=True),
    'easy_crawl' : fields.Boolean(required=True),
    'hosting' : fields.String(required=True),
})

domain = api.model('domain_sub', {
    'name': fields.String(required=True),
    'registrar':  fields.String(required=True),
    'from_date':  fields.Date(required=True),
    'to_date':  fields.Date(required=True),
})

ip = api.model('ip_sub', {
    'ev' : fields.Boolean(required=True),
    'from_date':  fields.Date(required=True),
    'to_date':  fields.Date(required=True),
    'description' : fields.String(required=False),
})

ssl = api.model('ssl_sub', {
    'address' : fields.String(required=True),
    'domains_of_this_ip': fields.String(required=True),
})

create_project_by_crawler_req = api.model('create_project_by_crawler_req', {
    'project': fields.Nested(project, allow_null=False),
    'domain': fields.Nested(domain, allow_null=False),
    'ip': fields.Nested(ip, allow_null=False),
    'ssl': fields.Nested(ssl, allow_null=False),
})