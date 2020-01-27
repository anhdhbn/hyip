import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
# def all_subclasses(cls):
#     return set(cls.__subclasses__()).union(
#         [s for c in cls.__subclasses__() for s in all_subclasses(c)])

# def get_class_by_name(class_):
#     return getattr(sys.modules[__name__], class_)

from .driver import Driver
import re
import requests

class Sites(Driver):
    def safe_get_element_by_css_selector_filter(self, selector):
        result = self.safe_get_element_by_css_selector(selector)
        if result == None: return None
        txt = self.preprocess_data(result.text)
        return txt

    def crawl(self, *args):
        id, investment_selector, paid_out_selector, member_selector, url =  args
        # url, investment_selector, paid_out_selector, member_selector = args
        self.idProject = id
        self.url = url
        self.driver.get(url)
        self.current_scrolls = 0

        while (True):
            total_investment,total_paid_out, total_member = self.get_data(investment_selector, paid_out_selector,  member_selector)
            if total_investment and total_paid_out:
                return total_investment, total_paid_out, None if total_member is None else total_member
            if(self.scroll()):
                break
                
        total_investment,total_paid_out, total_member = self.get_data(investment_selector, paid_out_selector,  member_selector)

        if total_investment != None and total_paid_out != None:
            return total_investment, total_paid_out, None if total_member is None else total_member
        return None, None, None
    
    def get_alexa_rank(self):
        from bs4 import BeautifulSoup
        from urllib.parse import urlparse
        parsed_uri = urlparse(self.url)
        domain = parsed_uri.netloc
        txt = requests.get("http://data.alexa.com/data?cli=10&dat=s&url="+ domain).text
        return BeautifulSoup(txt, "xml").find("REACH")['RANK']
    
    def save_data(self, *args):
        total_investment, total_paid_out, total_account, alexa_rank = args
        data = {
            "total_investment": float(total_investment),
            "total_paid_out": float(total_paid_out),
            "total_member": 0 if total_account is None else int(total_account),
            "alexa_rank": int(alexa_rank)
        }
        from jobqueue import app_info
        res = requests.post("{}api/crawldata/{}".format(app_info.host, self.idProject), json=data)
        print(res.text)
        
    def get_data(self, investment_selector, paid_out_selector, member_selector):
        total_investment = self.safe_get_element_by_css_selector_filter(investment_selector)
        total_paid_out = self.safe_get_element_by_css_selector_filter(paid_out_selector)
        total_member = self.safe_get_element_by_css_selector_filter(member_selector) if member_selector is not None else None
        return total_investment, total_paid_out, total_member

    def scroll(self):
        try:
            if self.current_scrolls == self.total_scrolls:
                return True
            self.old_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(self.driver, self.scroll_time, 0.05).until(lambda driver: self.check_height())
            self.current_scrolls += 1
            return False
        except TimeoutException:
            return True

    def preprocess_data(self, data):
        return re.sub("[^0-9\.]", "", data)