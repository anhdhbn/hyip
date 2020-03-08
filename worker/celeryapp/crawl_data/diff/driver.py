from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from celeryapp.driver.browser import ChromeDriver, FirefoxDriver
from celeryapp.crawl_data.base import CrawlBase

class Driver(ChromeDriver, CrawlBase):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.driver = None
        self.init_selenium()

    def crawl(self):
        result = super(CrawlBase, self).crawl()
        self.quit()
        return result

    def scroll(self):
        import time
        height = int(self.driver.execute_script("return window.innerHeight"))
        max_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        current_scroll_position = 0
        while current_scroll_position <= max_height:
            current_scroll_position += height
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))

    def safe_get_element_by_css_selector_filter(self, selector, num_type=float):
        wait = WebDriverWait(self.driver, 30, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

        if result is None: return None
        txt = self.preprocess_data(result.text)
        return num_type(float(txt))