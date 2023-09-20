
from unittest import TestCase

from selenium.webdriver.common.by import By

from Config import config
from Pages import email
from TestCases.conftest import setUpAutomation


class emailTest(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()


    def testEmail(self):
        driver = self.obj.open_browser()
        print(driver.title)
        driver.implicitly_wait(15)
        # For Email
        driver.find_element(By.XPATH,email.ContactUs).click()
        driver.find_element(By.NAME,email.EmailName).send_keys("mohd")
        driver.find_element(By.NAME, email.Email).send_keys("md1@gmail.com")
        driver.find_element(By.NAME,email.EmailPhone).send_keys("99090090")
        driver.find_element(By.NAME,email.EmailMessage).send_keys("just checking")
        driver.find_element(By.XPATH,email.EmailSend).click()
        actual_title = driver.title
        print(actual_title)
        try:
            assert actual_title == config.expected_title_email
            print("The title of the email page is " + actual_title)
        except Exception as e:
            print(repr(e))
            print("the title of the page is not as expected")

