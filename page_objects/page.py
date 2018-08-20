from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def input(self, tuple_locator, message):
        element = self.wait.until(EC.visibility_of_element_located(tuple_locator))
        element.send_keys(message)

    def click(self, tuple_locator):
        self.wait = WebDriverWait(self.driver, 2)
        element = self.wait.until((EC.element_to_be_clickable(tuple_locator)))
        element.click()

    def get_text(self, locator):
        self.driver.find_element(locator).text

    def wait_for_page_load(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator))
