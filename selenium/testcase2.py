import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class LoginTestCase2(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.browser = webdriver.Chrome(executable_path='/home/chansamnang/Downloads/chromedriver')
        self.browser.maximize_window()
        # navigate to application home page
        self.browser.get('http://192.168.7.78/login')
        self.username = self.browser.find_element_by_xpath('//*[@id="username_login"]')
        self.password = self.browser.find_element_by_xpath('//*[@id="pwd_login"]')
        self.login_button = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/form/div[3]/button')

    def tearDown(self):
        # close browser session
        time.sleep(5)
        self.browser.close()

    # login with valid email and invalid password
    def test_login1(self):
        self.username.send_keys('test1')
        self.password.send_keys('test1')
        self.login_button.click()
        print(self.browser.title)
        assert self.browser.title == 'KIT Point System! |  Login '

    # login with invalid username and password
    def test_login2(self):
        self.username.send_keys('test2')
        self.password.send_keys('test2')
        self.login_button.click()
        print(self.browser.title)
        # self.assertTrue(self.browser.title, 'My Account')
        assert self.browser.title == 'KIT Point System! |  Login '

    # login with valid username and password
    def test_login3(self):
        self.username.send_keys('Lim Chansamnang')
        self.password.send_keys('Samnang123')
        self.login_button.click()
        print(self.browser.title)
        # self.assertTrue(self.browser.title, 'My Account')
        assert self.browser.title == 'KIT Point System! |  Dashboard '


if __name__ == '__main__':
    unittest.TextTestRunner()