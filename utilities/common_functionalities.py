from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Common(object):
    def __init__(self, context):
        self.driver = context
        self.wait = WebDriverWait(self.driver, 10)

    # def find_single_element(self, tuple_locator):
    #     return self.driver.find_element(tuple_locator)

    def input_text(self, tuple_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(tuple_locator))
        element.clear()
        element.send_keys(text)
        # if element is True:
        #     self.clear_text(tuple_locator)
        #     element.send_keys(text)
        # else:
        #     print('Element is NOT visible')

    def clear_text(self, tuple_locator):
        element = self.wait.until(EC.visibility_of_element_located(tuple_locator))
        element.clear()
        # if element is True:
        #     element.clear()
        # else:
        #     print('Element is NOT visible')

    def click(self, tuple_locator):
        element = self.wait.until(EC.element_to_be_clickable(tuple_locator))
        element.click()
        # if element is True:
        #     element.click()
        # else:
        #     print('Element is NOT visible')

    def get_text(self, tuple_locator):
        element = self.wait.until(EC.visibility_of_element_located(tuple_locator))
        return element.text
