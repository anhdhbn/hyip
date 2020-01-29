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

    def execute_script(self, link_user: str):
        raise NotImplementedError

    def init_selenium(self):
        raise NotImplementedError

    def get_options(self):
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




from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from fake_useragent import UserAgent

from jobqueue.driver.download import download_driver
from jobqueue import app_info

class ChromeDriver(Selenium):
    def getUA(self):
        ua = UserAgent()
        userAgent = ua.random
        return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

    def get_options(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        if app_info.headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            
        options.add_argument(f'user-agent={self.getUA()}')
        # options.setBinary("/path/to/other/chrome/binary")
        return options
    
    def init_selenium(self):
        def readJSFile(scriptFile):
            with open(scriptFile, 'r') as fileHandle:  
                script=fileHandle.read()
            return script
        from jobqueue  import get_path
        injectedJavascript = readJSFile(get_path("bypass.js"))      

        download_driver()
        options = self.get_options()
        try:
            # if app_info.headless:
            #     self.driver = webdriver.Chrome(options=options)
            # else:
            #     executable_path = os.path.join(os.getcwd(), "chromedriver")
            #     self.driver = webdriver.Chrome(executable_path=executable_path, options=options)
            
            executable_path = os.path.join(os.getcwd(), "chromedriver")
            self.driver = webdriver.Chrome(executable_path=executable_path, options=options)

            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": injectedJavascript
            })
            self.driver.implicitly_wait(10)
        except Exception as e:
            print(e.with_traceback())
            self.quit(True)

class Driver(ChromeDriver):
    def __init__(self):
        self.driver = None
        self.total_scrolls = 50
        self.scroll_time = 5
        self.old_height = 0
        self.init_selenium()

    def crawl(self):
        raise NotImplementedError
    def post_data(self):
        raise NotImplementedError

    def check_height(self):
        new_height = self.driver.execute_script("return document.body.scrollHeight")
        return new_height != self.old_height