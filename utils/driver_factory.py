from selenium import webdriver
from config.config import *

def get_driver():
    config1 = ConfigReader()
    browser = config1.get_browser()

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver