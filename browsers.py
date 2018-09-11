from selenium import webdriver


class Browsers:

    @staticmethod
    def select_browser(browser):
        if browser == "Chrome":
            driver = webdriver.Chrome("C:/Users/huyle/PycharmProjects/phptravels/features/browsers/chromedriver.exe")
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        return driver
