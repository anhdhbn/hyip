from celeryapp.crawl_data.base import CrawlBase

class EasyCrawl(CrawlBase):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_info_project(self):
        pass