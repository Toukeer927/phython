import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from Pages import loginPage
from TestCases.conftest import setUpAutomation


class login(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()


    def testlogin(self):
        driver = self.obj.open_browser()
        print(driver.title)
        driver.implicitly_wait(15)
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()

        # For login
        driver.find_element(By.XPATH, loginPage.loginUserName).send_keys("mohd1")
        driver.find_element(By.XPATH,loginPage.loginPassword).send_keys("1233")
        driver.find_element(By.XPATH,loginPage.loginClick).click()
