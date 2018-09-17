from selenium.webdriver.common.by import By
from page_objects.page import Page
from hamcrest import assert_that, equal_to


class HomePage(Page):
    # Locator
    login_field = (By.ID, 'login-email')
    pwd_field = (By.ID, 'login-password')
    submit_btn = (By.ID, 'login-submit')
    name_field = (By.XPATH, '//*[@id="ember2196"]/span')

    def input_username(self, username):
        self.input((HomePage.login_field[0], HomePage.login_field[1]), username)

    def input_password(self, password):
        self.input((self.pwd_field[0], self.pwd_field[1]), password)

    def click_login(self):
        self.click((self.submit_btn[0], self.submit_btn[1]))

    def verify_login(self, name):
        expected_result = name
        actual_result = self.get_text((self.name_field[0], self.name_field[1]))
        assert_that(actual_result, equal_to(expected_result), "Verify User name")
