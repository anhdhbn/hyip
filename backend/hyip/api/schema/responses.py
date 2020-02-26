# coding=utf-8
from flask_restplus import fields

project_res = lambda ns: ns.model('project_res', {
    'url_crawl': fields.String(),
    'domain': fields.String(),

    'investment_selector': fields.String(),
    'paid_out_selector': fields.String(),
    'member_selector': fields.String(),

    'easy_crawl': fields.Boolean(),
    'is_verified': fields.Boolean(),
    'crawlable': fields.Boolean(),
    'tracked': fields.Boolean(),
    'type_currency': fields.String(),

    'created_date': fields.Date()
})