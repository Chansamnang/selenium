from behave import *
from selenium import webdriver


@given('I launch firefox browser')
def step_impl(context):
    context.driver = webdriver.Firefox(executable_path="/home/chansamnang/Downloads/geckodriver")


@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").submit()


@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        Text = context.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/h1")
        print(Text.text)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if Text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
