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

crawl_data_parser = reqparse.RequestParser()
crawl_data_parser.add_argument('limit', required=True)

post_data_crawled_req = lambda ns: ns.model('post_data_crawled_req', {
    'total_investments': fields.Float(required=True),
    'total_paid_outs': fields.Float(required=True),
    'total_members': fields.Integer(required=True),
    'alexa_rank': fields.Integer(required=True),
})

search_domain_parser = reqparse.RequestParser()
search_domain_parser.add_argument('input', required=True)
search_domain_parser.add_argument('page', type=int)
search_domain_parser.add_argument('ipp', type=int)

update_status_project = lambda ns: ns.model('update_status_project', {
    'project_id': fields.String(required=True),
    'status_project': fields.Integer(required=True),
})

update_projects_tracked_by_user_req = lambda ns: ns.model('update_projects_tracked_by_user_req', {
    'project_id': fields.String(required=True),
})


check_selector_parser = reqparse.RequestParser()
check_selector_parser.add_argument('url', required=True)
check_selector_parser.add_argument('investment_selector', required=True)
check_selector_parser.add_argument('paid_out_selector', required=True)
check_selector_parser.add_argument('member_selector', required=True)

check_easy_parser = reqparse.RequestParser()
check_easy_parser.add_argument('url', required=True)