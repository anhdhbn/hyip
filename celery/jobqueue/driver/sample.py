import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
# def all_subclasses(cls):
#     return set(cls.__subclasses__()).union(
#         [s for c in cls.__subclasses__() for s in all_subclasses(c)])

# def get_class_by_name(class_):
#     return getattr(sys.modules[__name__], class_)

from .base import Driver
import re
import requests
from bs4 import BeautifulSoup
import html as html_cvt

class Sites(Driver):
    def safe_get_element_by_css_selector_filter(self, selector):
        result = self.safe_get_element_by_css_selector(selector)
        if result == None: return None
        txt = self.preprocess_data(result.text)
        return txt

    def crawl(self, *args):
        try:
            id, investment_selector, paid_out_selector, member_selector, url =  args
            self.idProject = id
            self.url = url
            self.driver.get(url)
            html = html_cvt.unescape(self.driver.page_source)
            self.quit()

            soup = BeautifulSoup(html, "lxml")
            total_investment = soup.select_one(investment_selector)
            total_paid_out = soup.select_one(paid_out_selector)
            total_member = None
            if member_selector:
                total_member =  soup.select_one(member_selector)

            if total_investment is not None: 
                print(total_investment.text) 
            print(total_investment, total_paid_out, total_member)
            return None

        except:
            print(self.url)
            self.quit()
            return None
    
    def get_alexa_rank(self):
        from bs4 import BeautifulSoup
        from urllib.parse import urlparse
        parsed_uri = urlparse(self.url)
        domain = parsed_uri.netloc
        txt = requests.get("http://data.alexa.com/data?cli=10&dat=s&url="+ domain).text
        return BeautifulSoup(txt, "xml").find("REACH")['RANK']
    
    def save_data(self, *args):
        total_investment, total_paid_out, total_account, alexa_rank = args
        try:
            data = {
                "total_investment": float(total_investment),
                "total_paid_out": float(total_paid_out),
                "total_member": 0 if total_account is None else int(total_account),
                "alexa_rank": int(alexa_rank)
            }
            from jobqueue import app_info
            res = requests.post("{}api/crawldata/{}".format(app_info.host, self.idProject), json=data)
            print(res.text)
        except:
            print("Data error {}".format(self.url))

    def preprocess_data(self, data):
        return re.sub("[^0-9\.]", "", data)