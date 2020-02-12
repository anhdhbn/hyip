from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from fake_useragent import UserAgent

from jobqueue import app_info

from jobqueue.driver.sele import Selenium

class ChromeDriver(Selenium):
    def getUA(self):
        ua = UserAgent()
        userAgent = ua.random
        return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        # return userAgent

    def get_options(self):
        options = Options()
        options.add_argument("--disable-notifications")
        # options.add_argument("--disable-infobars")
        # options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        # options.add_argument("--width=1920")
        # options.add_argument("--height=1080")
        if app_info.headless:
            options.add_argument("--headless")
            
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        # options.add_argument("--disable-impl-side-painting")
        # options.add_argument("--disable-gpu-sandbox")
        # options.add_argument("--disable-accelerated-2d-canvas")
        # options.add_argument("--disable-accelerated-jpeg-decoding")
        # options.add_argument('--test-type=ui')
        # options.add_argument(f'user-agent={self.getUA()}')
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        # options.setBinary("/path/to/other/chrome/binary")
        return options
    
    def init_selenium(self):
        def readJSFile(scriptFile):
            with open(scriptFile, 'r') as fileHandle:  
                script=fileHandle.read()
            return script
        injectedJavascript = readJSFile(os.path.join(app_info.path, "driver", "bypass.js"))      
        
        try:
            self.driver = webdriver.Remote(command_executor=app_info.hub.url, desired_capabilities=self.get_options().to_capabilities())
        except:
            self.quit()
            raise(e)
        # try:
            
        #     # print(help(self.driver))
        #     # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     #     "source": injectedJavascript
        #     # })
        #     # self.driver.implicitly_wait(10)
        # except Exception as e:
        #     self.quit()
        #     raise(e)