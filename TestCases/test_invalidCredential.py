import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from Config import config
from Pages import loginPage
from TestCases.conftest import setUpAutomation


class login(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()


    def testInvalilogin(self):
        driver = self.obj.open_browser()
        print(driver.title)
        driver.implicitly_wait(15)
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()

        driver.find_element(By.XPATH, loginPage.loginUserName).send_keys("md112")
        driver.find_element(By.XPATH,loginPage.loginPassword).send_keys("12313")
        driver.find_element(By.XPATH,loginPage.loginClick).click()

        actual_title = driver.title
        print(actual_title)
        try:
            assert actual_title == config.expected_title_invalid
            print("The title of the page is " + actual_title)
        except Exception as e:
            print(repr(e))
            print("the title of the page is not as expected")
