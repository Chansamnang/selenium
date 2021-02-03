from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

from selenium.webdriver.remote.webelement import WebElement


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/chansamnang/Downloads/geckodriver')
        self.driver.get('http://192.168.7.78/login')
        self.username = self.driver.find_element(By.ID, 'username_login')
        self.password = self.driver.find_element(By.ID, 'pwd_login')
        self.login_button = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[1]/div/div[2]/section/form/div[3]/button')

    def tearDown(self):
        self.driver.quit()

    # Login with valid username and valid passoword
    def test_Login001(self):
        self.username.send_keys('Lim Chansamnang')
        self.password.send_keys('Samnang123')
        self.login_button.click()
        time.sleep(2)
        assert self.driver.title == 'KIT Point System! | Dashboard'

    # Login with valid username and invalid password
    def test_Login002(self):
        self.username.send_keys('Lim Chansamnang')
        self.password.send_keys('test1')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        # print(self.err_msg.text)
        assert self.err_msg.text == '"The password is incorrect"'

    # Login with invalid username and valid password
    def test_Login003(self):
        self.username.send_keys('Chansamnang')
        self.password.send_keys('Samnang123')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        assert self.err_msg.text == '"The username does not exist"'

    # Login with invalid username and invalid password
    def test_Login004(self):
        self.username.send_keys('InvalidUsr')
        self.password.send_keys('InvalidPass')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        assert self.err_msg.text == '"The username does not exist"'

    # Click login without input username and password
    def test_Login005(self):
        self.username.send_keys('')
        self.password.send_keys('')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        assert self.err_msg.text == '"The username does not exist"'

    # Input the valid username and without input password
    def test_Login006(self):
        self.username.send_keys('Lim Chansamnang')
        self.password.send_keys('')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        print(self.err_msg.text)
        assert self.err_msg.text == '"The password is incorrect"'

    # Input the invalid username and without input password
    def test_Login007(self):
        self.username.send_keys('Lim Chan')
        self.password.send_keys('')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        print(self.err_msg)
        assert self.driver.title == 'KIT Point System! | Login'
        assert self.err_msg.text == '"The username does not exist"'

    # Input the valid passowrd and without input username
    def test_Login008(self):
        self.username.send_keys('')
        self.password.send_keys('Samnang123')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        assert self.err_msg.text == '"The username does not exist"'

    # Input the invalid password and without input username
    def test_Login009(self):
        self.username.send_keys('Samnang1999')
        self.password.send_keys('')
        self.login_button.click()
        time.sleep(2)
        self.err_msg = self.driver.find_element_by_class_name('ui-pnotify-text')
        assert self.err_msg.text == '"The username does not exist"'

    # Create Account
    def test_Login010(self):
        try:
            self.create_acc = self.driver.find_element_by_id('signup-link').click()
        except:
            print('Element is not click able')

    # Inputting username
    def test_Login011(self):
        self.create_acc = self.driver.find_element_by_id('signup-link').click()
        self.driver.find_element_by_id('username_create').send_keys('Testing')
        time.sleep(2)
        self.cr_usr = self.driver.find_element_by_id('username_create').get_attribute("value")  # get the value of the input
        print(self.cr_usr)
        assert len(self.cr_usr) > 0

    # Inputting username that have with another existing account
    def test_Login012(self):
        self.create_acc = self.driver.find_element_by_id('signup-link').click()
        self.driver.find_element_by_id('username_create').send_keys('Lim Chansamnang')
