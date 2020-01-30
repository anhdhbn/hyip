from jobqueue import app_info
import requests
from urllib.parse import urlparse

class CheckStatusProject:
    def check(self, obj):
        url = obj['url']
        id = obj['id']
        setattr(self, "project_id", id)
        setattr(self, "status_project", 3)
        parsed_uri = urlparse(url)
        self.domain = parsed_uri.netloc
        is_scam = self.get_status_project()
        if is_scam:
            self.update_scam_project()
            return True
        else:
            return False
    
    def get_status_project(self):
        from .get_status_project  import arr_func
        for func in arr_func:
            if not func(self.domain):
                return False
        return True

    def update_scam_project(self):
        del self.domain
        r = requests.post(app_info.url.post_status, json=self.__dict__)