from celeryapp.utils import get_domain
from celeryapp import celery
import requests

class Project:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    def save_to_db(self):
        if self.check_have_all_attr():
            if not self.is_exists():
                r = requests.post(celery.conf.URL['post_create_project'], json=self.__dict__)

    def is_exists(self):
        domain = get_domain(self.url_crawl)
        r = requests.get(celery.conf.URL['get_check_exists_domain'](domain)).json()
        return r['data']['is_exists']

    def check_have_all_attr(self):
        arr_attrs = ['url_crawl']
        for attr in arr_attrs:
            if not hasattr(self, attr):
                return False
        return True

    def __repr__(self):
        return self.url_crawl

    def __hash__(self):
        return hash(self.url_crawl)

# from .isp import Isp
from .hyiplogs import HyipLogs
from .isp import Isp
from .hstat import HStat
arr_class = [HyipLogs, Isp, HStat]

class CrawlProjects:
    def crawl(self):
        projects = []
        for func in arr_class:
            crawler = func()
            projects += crawler.crawl()
        projects = [project for project in projects if project is not None]
        projects = list(set(projects))
        for project in projects:
            project.save_to_db()
        return len(projects)