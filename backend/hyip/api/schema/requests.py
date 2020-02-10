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
script_fields = api.model('script_fields', {
    'script_type': fields.Integer(),
})

status_fields = api.model('status_fields', {
    'status_project': fields.Integer(),
})

project_fields = api.model('project_fields', {
    'url': fields.String(required=True),
    'investment_selector': fields.String(required=False),
    'paid_out_selector': fields.String(required=False),
    'member_selector': fields.String(required=False),
    'start_date': fields.Date(required=False),
    'plans': fields.String(required=True),
    'easy_crawl': fields.Boolean(required=False),
})

# create_project_req = {
#     'project': fields.Nested(project_fields),
#     'script': fields.Nested(script_fields),
#     'status': fields.Nested(status_fields)
# }

create_project_req = {
    'url': fields.String(required=True),
    'script_type': fields.Integer(required=False),
    'investment_selector': fields.String(required=False),
    'paid_out_selector': fields.String(required=False),
    'member_selector': fields.String(required=False),
    'start_date': fields.Date(required=False),
    'plans': fields.String(required=True),
    'easy_crawl': fields.Boolean(required=False),
    'status_project': fields.Integer(required=False)
}

post_datacrawled_req = {
    'total_investments': fields.Float(required=True),
    'total_paid_outs': fields.Float(required=True),
    'total_members': fields.Integer(required=True),
    'alexa_rank': fields.Integer(required=True),
}

project = api.model('project_sub', {
    'url' : fields.String(required=True),
    'script_type' : fields.Integer(required=False),
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

create_project_by_crawler_req = api.model('project.create_project_by_crawler_req', {
    'project': fields.Nested(project, allow_null=False),
    'domain': fields.Nested(domain, allow_null=False),
    'ip': fields.Nested(ip, allow_null=False),
    'ssl': fields.Nested(ssl, allow_null=False),
})

update_status_project = api.model('project.update_status_project', {
    'project_id': fields.String(required=True),
    'status_project': fields.Integer(required=True),
})

update_selector_project = api.model('project.update_selector_project', {
    'investment_selector': fields.String(required=False),
    'paid_out_selector': fields.String(required=False),
    'member_selector': fields.String(required=False),
    'plans': fields.String(required=False),
    'easy_crawl': fields.Boolean(required=False),
    'crawlable': fields.Boolean(required=False),
})

update_projects_tracked_by_user = api.model('tracking.update_projects_tracked_by_user', {
    'project_id': fields.String(required=True),
    'user_id': fields.String(required=True),
})