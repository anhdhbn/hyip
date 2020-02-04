from bs4 import BeautifulSoup
from urllib.parse import urlparse

from jobqueue.driver.chrome import ChromeDriver
from jobqueue.driver.firefox import FirefoxDriver
from jobqueue import app_info

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import re


def handle_exceptions(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(self, *args, **kw):
        try:
            return fn(self, *args, **kw)
        except Exception as e:
            try:
                self.quit()
            except:
                pass
            print(f"Exception was raise in {self.__class__.__name__}->{fn.__name__}")
            raise(e)

class Driver(ChromeDriver):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.driver = None
        self.init_selenium()   


    def crawl(self):
        alexa_rank = int(self.get_alexa_rank())
        total_investment, total_paid_out, total_member = self.get_info_project()
        self.quit()
        return self.save_data(alexa_rank=alexa_rank, total_investment=total_investment, total_member=total_member, total_paid_out=total_paid_out)

    @handle_exceptions
    def get_info_project(self):
        raise NotImplementedError

    @handle_exceptions
    def save_data(self, **kwargs):
        res = requests.post(app_info.url.post_data_crawled(self.id), json=kwargs)
        res.raise_for_status()
        return True

    def get_alexa_rank(self):
        parsed_uri = urlparse(self.url)
        domain = parsed_uri.netloc
        txt = requests.get("http://data.alexa.com/data?cli=10&dat=s&url="+ domain).text
        return BeautifulSoup(txt, "xml").find("REACH")['RANK']
    
    def preprocess_data(self, data):
        return re.sub("[^0-9\.]", "", data)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def safe_get_element_by_css_selector_filter(self, selector, num_type=float):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

        if result is None: return None
        txt = self.preprocess_data(result.text)
        return num_type(txt)