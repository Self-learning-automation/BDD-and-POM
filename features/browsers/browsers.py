from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Browsers:
    @staticmethod
    def select_browser(browser):
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        return driver

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #
    # def get_driver(self):
    #     return self.driver
    #
    # def go_to_homepage(self):
    #     self.driver.get("https://www.phptravels.net/")
