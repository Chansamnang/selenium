from behave import given, when, then
from selenium import webdriver


@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Firefox(executable_path='/home/chansamnang/Downloads/geckodriver')


@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@then(u'verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/img').is_displayed()
    assert status == True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
