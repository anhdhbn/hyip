# coding=utf-8
from flask_restplus import fields, reqparse

create_project_req = lambda ns: ns.model('create_project_req', {
    'url_crawl': fields.String(required=True),
    'investment_selector': fields.String(required=False, default=''),
    'paid_out_selector': fields.String(required=False, default=''),
    'member_selector': fields.String(required=False, default=''),
    'easy_crawl': fields.Boolean(required=False, default=False),
    'crawlable': fields.Boolean(required=False, default=False),
    'tracked': fields.Boolean(required=False, default=False),
    'type_currency': fields.String(required=False, max_length=3),
})

get_projects_parser = reqparse.RequestParser()
get_projects_parser.add_argument('type', required=True, help="type can be all, easy, notscam, verified, unverified")

update_project_req = lambda ns: ns.model('update_project_req', {
    'url_crawl': fields.String(required=True),
    'investment_selector': fields.String(required=False, default=''),
    'paid_out_selector': fields.String(required=False, default=''),
    'member_selector': fields.String(required=False, default=''),
    'easy_crawl': fields.Boolean(required=True, default=False),
    'crawlable': fields.Boolean(required=True, default=False),
    'tracked': fields.Boolean(required=False, default=False),
    'type_currency': fields.String(required=False, max_length=3),
})