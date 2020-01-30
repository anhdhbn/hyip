from bs4 import BeautifulSoup
from urllib.parse import urlparse

from .chrome import ChromeDriver
from jobqueue import app_info

class Driver(ChromeDriver):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.driver = None
        self.init_selenium()   

    def crawl(self):
        alexa_rank = int(self.get_alexa_rank())
        total_investment, total_paid_out, total_member = self.get_info_project()
        self.save_data(alexa_rank=alexa_rank, total_investment=total_investment, total_member=total_member, total_paid_out=total_paid_out)

    def get_info_project(self):
        raise NotImplementedError

    def save_data(self, **kwargs):
        try:
            res = requests.post(app_info.url.post_data_crawled(self.id), json=kwargs)
            res.raise_for_status()
        except:
            print("Data error {}".format(self.url))

    def check_height(self):
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return new_height != self.old_height

    def get_alexa_rank(self):
        parsed_uri = urlparse(self.url)
        domain = parsed_uri.netloc
        txt = requests.get("http://data.alexa.com/data?cli=10&dat=s&url="+ domain).text
        return BeautifulSoup(txt, "xml").find("REACH")['RANK']