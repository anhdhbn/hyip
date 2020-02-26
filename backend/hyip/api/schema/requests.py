# coding=utf-8
from flask_restplus import fields, reqparse

create_project_req = lambda ns: ns.model('create_project_req', {
    'url_crawl': fields.String(required=True),
    'investment_selector': fields.String(required=False, default=''),
    'paid_out_selector': fields.String(required=False, default=''),
    'member_selector': fields.String(required=False, default=''),
})

get_projects_parser = reqparse.RequestParser()
get_projects_parser.add_argument('type', required=True, help="type can be all, easy, notscam, verified, unverified")