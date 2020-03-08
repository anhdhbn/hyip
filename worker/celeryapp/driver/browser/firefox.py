from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from celeryapp import celery
from celeryapp.driver.browser.base import Selenium

class FirefoxDriver(Selenium):
    def get_options(self):
        options = Options()
        if celery.conf.HEADLESS:
            options.add_argument("--headless")
        return options

    def init_selenium(self):
        try:
            self.driver = webdriver.Remote(command_executor=celery.conf.HUB_URL, desired_capabilities=self.get_options().to_capabilities())
        except Exception as e:
            self.quit()
            raise(e)