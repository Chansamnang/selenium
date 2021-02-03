from selenium import webdriver

remote_app = webdriver.remote.webdriver.WebDriver(
    command_executor='http://localhost:8765',
    desired_capabilities={'chromeOptions': {'binary': '/home/chansamnang/Downloads/WhatsAppSetup.exe'}},
    browser_profile=None,
    proxy=None,
    keep_alive=False)
