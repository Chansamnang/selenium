import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class LoginTestCase1(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.browser = webdriver.Chrome(executable_path='/home/chansamnang/Downloads/chromedriver')
        self.browser.maximize_window()
        # navigate to application home page
        self.browser.get('https://www.phptravels.net/login')
        self.email = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div[1]/section/div/div[1]/div[2]/form/div[3]/div[1]/label/input')
        self.password = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div[1]/section/div/div[1]/div[2]/form/div[3]/div[2]/label/input')
        self.login_button = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div[1]/section/div/div[1]/div[2]/form/button')

    def tearDown(self):
        # close browser session
        time.sleep(5)
        self.browser.close()

    # login with valid email and invalid password
    def test_login1(self):
        self.email.send_keys('test1@gmail.com')
        self.password.send_keys('test')
        self.login_button.click()
        self.login_button.click()
        print(self.browser.title)
        assert self.browser.title == 'Login'

    # login with wrong email and password
    def test_login2(self):
        self.email.send_keys('test_admin@gmail.com')
        self.password.send_keys('1111')
        self.login_button.click()
        print(self.browser.title)
        # self.assertTrue(self.browser.title, 'My Account')
        assert self.browser.title == 'Login'

    # login with valid email and password
    def test_login3(self):
        self.email.send_keys('oneplus@gmail.com')
        self.password.send_keys('123123')
        self.login_button.click()
        print(self.browser.title)
        # self.assertTrue(self.browser.title, 'My Account')
        assert self.browser.title == 'Login'


if __name__ == '__main__':
    unittest.TextTestRunner()
