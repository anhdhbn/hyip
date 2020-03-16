from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from celeryapp import celery
from celeryapp.driver.browser.base import Selenium

class ChromeDriver(Selenium):
    def get_options(self):
        options = Options()
        if celery.conf.HEADLESS:
            options.add_argument("--headless")

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        # options.add_argument("--width=1920")
        # options.add_argument("--height=10800")
        options.add_argument("--window-size=1920,10800")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        return options
    
    def init_selenium(self):
        try:
            self.driver = webdriver.Remote(command_executor=celery.conf.HUB_URL, desired_capabilities=self.get_options().to_capabilities())
            self.driver.set_window_size(1920, 10800)
        except Exception as e:
            self.quit()
            raise(__name__, e)