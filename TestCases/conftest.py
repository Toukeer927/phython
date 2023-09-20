from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config import config
class setUpAutomation:
    def _init_(self):
        self.driver=None

    def open_browser(self):
       # global driver

        if config.mode.lower() == "non-headless":
            if config.browser.lower() == 'chrome':
                self.driver = webdriver.Chrome(config.Chrome_driver_location)
            elif config.browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                print("Browser name in config is invalid")

        elif config.mode.lower() == "headless":
            if config.browser.lower() == 'chrome':
                options = Options()
                options.headless == True
                self.driver = webdriver.Chrome(config.Chrome_driver_location, options=options)
            elif config.browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                print("Browser name in config is invalid")

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(config.baseurl)

        return self.driver

    def closeBrowser(self):

        print("Closing the browser")
        self.driver.close()