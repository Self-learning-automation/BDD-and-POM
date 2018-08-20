from selenium.webdriver.common.by import By
from page_objects.page import Page


class HomePage(Page):
    email = (By.ID, 'email-login')
    password = (By.NAME, 'password')
    signIn = (By.ID, 'submit')
    welcome = (By.CSS_SELECTOR, "a[data-control-name='identity_welcome_message']")
    def input_username(self, username):
        self.input(self.email, username)

    def input_password(self, password):
        self.input(self.password, password)

    def click_signin(self):
        self.click_element(self.signIn)

    def wait_until_loading_is_completed(self):
        self.explicit_wait()