from jobqueue import app_info, get_domain
import requests

class Project:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    def save_to_db(self):
        if  not self.is_exists():
            if self.check_have_all_attr():
                r = requests.post(app_info.url.post_create_project, json=self.__dict__)

    def is_exists(self):
        domain = get_domain(self.url)
        r = requests.get(app_info.url.get_check_exists_domain(domain)).json()
        return r['data']['is_exists']

    def check_have_all_attr(self):
        arr_attrs = ['url', 'script_type', 'plans']
        for attr in arr_attrs:
            if not hasattr(self, attr):
                return False
        return True

    # def __hash__(self):
    #     return self.url

from .isp import Isp
arr_class = [Isp]

class CrawlProjects:

    def crawl(self):
        projects = []
        for func in arr_class:
            crawler = func()
            projects += crawler.crawl()
        # projects = list(set(projects))
        for project in projects:
            project.save_to_db()
        return len(projects)
    
