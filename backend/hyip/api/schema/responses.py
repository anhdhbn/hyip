# coding=utf-8
from flask_restx import fields

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

exist_domain_res = lambda ns: ns.model('crawl_data_res', {
    'is_exists': fields.Boolean(),
})

search_domain  = lambda ns: ns.model('crawl_data_res', {
    'value': fields.String(attribute='id'),
    'label': fields.String(attribute='domain')
})

status_project_res =  lambda ns: ns.model('status_project_res', {
    'id': fields.String(),
    'project_id': fields.String(),
    'status_project': fields.Integer(),
    'created_date': fields.Date(),
})

projects_tracked_by_user_res = lambda ns: ns.model("projects_tracked_by_user_res", {
    'project_id': fields.String(attribute='id'),
})

check_projects_tracked = lambda ns: ns.model("check_projects_tracked", {
    'tracked': fields.Boolean(),
})

check_selector_res =  lambda ns: ns.model('check_selector_res', {
    'total_investments': fields.Float(),
    'total_paid_outs': fields.Float(),
    'total_members': fields.Integer(),
})