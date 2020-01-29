import os
import platform

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Selenium:
    def __init__(self):
        raise NotImplementedError

    def init_selenium(self):
        raise NotImplementedError
    
    def quit(self, e=False):
        self.driver.close()
        if(e): exit()

    def convert_to_dict(self, obj):
        return obj.__dict__

    def wait_css(self, css_selector):
        try:
            WebDriverWait(self.driver, self.timeout_second).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except Exception as e:
            print(e)
    
    def safe_get_element_by_css_selector(self, css_selector):
        try:
            return self.driver.find_element_by_css_selector(css_selector)
        except Exception as e:
            # print(e)
            pass
    
    def safe_get_elements_by_css_selector(self, css_selector):
        try:
            return self.driver.find_elements_by_css_selector(css_selector)
        except Exception as e:
            print(e)

    def safe_get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(e)
    
    def safe_get_elements_by_xpath(self, xpath):
        try:
            return self.driver.find_elements_by_xpath(xpath)
        except Exception as e:
            print(e)

    def safe_get_element_by_id(self, elem_id):
        try:
            return self.driver.find_element_by_id(elem_id)
        except NoSuchElementException:
            return None