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

crawl_data_res = lambda ns: ns.model('crawl_data_res', {
    'id': fields.String(),
    'project_id': fields.String(),
    'total_investments': fields.Float(),
    'total_paid_outs': fields.Float(),
    'total_members': fields.Integer(),
    'alexa_rank': fields.Integer(),
    'created_date': fields.Date(),
})