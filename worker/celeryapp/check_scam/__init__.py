
from celeryapp.utils import get_domain
from celeryapp import celery
import requests

class CheckScam:
    def check(self, obj):
        url_crawl = obj['url_crawl']
        domain = get_domain(url_crawl)
        setattr(self, "project_id", obj['id'])
        setattr(self, "status_project", self.get_status_project(domain))

        current_status_project = self.get_current_Status()
        
        if self.status_project != current_status_project:
            self.update_scam_project()

        return self.status_project

    def get_current_Status(self):
        r = requests.get(celery.conf.URL['get_status'](self.project_id)).json()
        return r['data']['status_project']
    
    def get_status_project(self, domain):
        return 1
        # from .get_status_project  import arr_func
        # for func in arr_func:
        #     if not func(self.domain):
        #         return False
        # return True

    def update_scam_project(self):
        r = requests.post(celery.conf.URL['post_status'], json=self.__dict__)