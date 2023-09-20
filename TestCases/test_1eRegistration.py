import time
from selenium.webdriver.common.by import By

from Config import config

from Pages import Registration
# from Config import configpy
from conftest import setUpAutomation
from unittest import TestCase

class register(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()


    def test_addNewAccount(self):
        driver = self.obj.open_browser()
        print(driver.title)
        driver.implicitly_wait(15)
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()
        actual_title=driver.title
        print(actual_title)
        driver.find_element(By.ID,Registration.Firstname).send_keys("mohd")
        driver.find_element(By.ID, Registration.lastName).send_keys("toukeer")
        driver.find_element(By.ID,Registration.street ).send_keys("indira")
        driver.find_element(By.ID, Registration.city).send_keys("luckpytnow")
        driver.find_element(By.ID, Registration.state).send_keys("uttarPradesh")
        driver.find_element(By.ID, Registration.zipCode).send_keys("226000")
        driver.find_element(By.ID, Registration.phoneNumber).send_keys("909090")
        driver.find_element(By.ID, Registration.ssn).send_keys("8989")
        driver.find_element(By.ID, Registration.userName).send_keys("mohd1")
        driver.find_element(By.ID, Registration.password).send_keys("1233")
        driver.find_element(By.ID, Registration.repeatePass).send_keys("1233")
        driver.find_element(By.XPATH,"//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input").click()

        try:
            assert actual_title==config.expected_title_login
            print("The title of the login page is " + actual_title)
        except Exception as e:
            print(repr(e))
            print("the title of the page is not as expected")

    def tearDown(self) -> None:
        self.obj.closeBrowser()