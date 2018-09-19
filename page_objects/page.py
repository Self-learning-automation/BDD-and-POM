from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))

    def type_text(self, tuple_selector, value):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        element.send_keys(value)

    def click_element(self, tuple_selector, timeout=15):
        element = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
        element.click()

    def get_element_text(self, tuple_selector, timeout=15):
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        return element.text
