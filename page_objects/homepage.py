from selenium.webdriver.common.by import By
from page_objects.page import Page


class HomePage(Page):
    # Locator
    login_field = (By.ID, 'login-email')
    pwd_field = (By.ID, 'login-password')
    submit_btn = (By.ID, 'login-submit')
    name_field = (By.CSS_SELECTOR, '[data-control-name="identity_welcome_message"]>span')

    def input_username(self, username):
        self.type_text(self.login_field, username)

    def input_password(self, password):
        self.type_text(self.pwd_field, password)

    def click_login(self):
        self.click_element(self.submit_btn)

    def get_user_name(self):
        return self.get_element_text(self.name_field)
