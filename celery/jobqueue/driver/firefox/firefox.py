from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
from fake_useragent import UserAgent

from jobqueue import app_info

from jobqueue.driver.sele import Selenium

class FirefoxDriver(Selenium):
    def getUA(self):
        ua = UserAgent()
        userAgent = ua.random
        return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        # return userAgent
    def get_options(self):
        options = Options()
        return options

    def init_selenium(self):
        def readJSFile(scriptFile):
            with open(scriptFile, 'r') as fileHandle:  
                script=fileHandle.read()
            return script
        injectedJavascript = readJSFile(os.path.join(app_info.path, "driver", "bypass.js"))      
        self.driver = webdriver.Remote(desired_capabilities=self.get_options().to_capabilities())
        # print(help(self.driver))
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": injectedJavascript
        # })
        # self.driver.implicitly_wait(10)