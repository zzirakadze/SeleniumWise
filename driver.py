import chromedriver_autoinstaller
from selenium import webdriver


class DriverFactory:
    chromedriver_autoinstaller.install()
    driver: webdriver = webdriver.Chrome()
