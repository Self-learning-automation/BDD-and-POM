from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Page:
    def __init__(self, driver):
        self.driver = Chrome()

    def input(self, tuple_locator, text):
        if EC.visibility_of_element_located(tuple_locator):
            self.driver.find_element(tuple_locator).sendKeys(text)
        else:
            print('Element Not Found')

    def explicit_wait(self, tuple_locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.invisibility_of_element_located(tuple_locator))

    def click_element(self, tuple_locator):
        Page.explicit_wait()
        self.driver.find_element(tuple_locator).click()

    def get_text(self, tuple_locator):
        if EC.visibility_of_element_located(tuple_locator):
            tuple_locator.getText()
        else:
            print('Element Not Found')




