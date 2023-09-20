import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from Config import config
from Pages import paybill, Registration, loginPage
from TestCases.conftest import setUpAutomation


class paytest(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()


    def testPay(self):
        driver = self.obj.open_browser()
        print(driver.title)
        driver.implicitly_wait(15)
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()



        # driver.find_element(By.XPATH, loginPage.loginUserName).send_keys("mohd1")
        # driver.find_element(By.XPATH, loginPage.loginPassword).send_keys("1233")
        # driver.find_element(By.XPATH, loginPage.loginClick).click()



        driver.find_element(By.ID, Registration.Firstname).send_keys("mohd")
        driver.find_element(By.ID, Registration.lastName).send_keys("toukeer")
        driver.find_element(By.ID, Registration.street).send_keys("indira")
        driver.find_element(By.ID, Registration.city).send_keys("lucnow")
        driver.find_element(By.ID, Registration.state).send_keys("uttarPradesh")
        driver.find_element(By.ID, Registration.zipCode).send_keys("226000")
        driver.find_element(By.ID, Registration.phoneNumber).send_keys("909090")
        driver.find_element(By.ID, Registration.ssn).send_keys("8989")
        driver.find_element(By.ID, Registration.userName).send_keys("mohd1934")
        driver.find_element(By.ID, Registration.password).send_keys("1233")
        driver.find_element(By.ID, Registration.repeatePass).send_keys("1233")
        driver.find_element(By.XPATH, "//*[@id='customerForm']/table/tbody/tr[13]/td[2]/input").click()

        driver.find_element(By.XPATH, paybill.payclick_on_BillPay).click()
        driver.find_element(By.XPATH, paybill.payEnter_PayeeName).send_keys("mohd")
        driver.find_element(By.XPATH,paybill.payEnter_Address).send_keys("indira Nagar")
        driver.find_element(By.XPATH, paybill.payEnter_City).send_keys("lucknow")
        driver.find_element(By.XPATH, paybill.payEnter_State).send_keys("uttarPradesh")
        driver.find_element(By.XPATH, paybill.payEnter_ZipCode).send_keys("78382")
        driver.find_element(By.NAME, paybill.payEnter_Phone).send_keys("909090")
        driver.find_element(By.XPATH, paybill.payEnter_AccountNo).send_keys("909767")
        driver.find_element(By.XPATH, paybill.payVerifyAccountNo).send_keys("909767")
        driver.find_element(By.XPATH, paybill.payEnter_Amount).send_keys("1000")
        driver.find_element(By.XPATH, paybill.paySubmit).click()

