# coding=utf-8
from flask_restplus import fields

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
