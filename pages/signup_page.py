from selenium.webdriver.common.by import By
from utilities.common_functionalities import Common


class SignupPage(Common):
    first_name_input = (By.CSS_SELECTOR, "input[name = 'firstname']")
    last_name_input = (By.CSS_SELECTOR, "input[name = 'lastname']")
    phone_input = (By.CSS_SELECTOR, "input[name = 'phone']")
    email_input = (By.CSS_SELECTOR, "input[name = 'email']")
    password_input = (By.CSS_SELECTOR, "input[name = 'password']")
    confirm_password_input = (By.CSS_SELECTOR, "input[name = 'confirmpassword']")
    signUp_button = (By.CSS_SELECTOR, ".form-group button[type='submit']")
    fullname = (By.CSS_SELECTOR, "h3.RTL")

    def input_first_name(self, first_name):
        self.input_text((self.first_name_input[0], self.first_name_input[1]), first_name)

    def input_last_name(self, last_name):
        self.input_text((self.last_name_input[0], self.last_name_input[1]), last_name)

    def input_phone(self, phone):
        self.input_text((self.phone_input[0], self.phone_input[1]), phone)

    def input_email(self, email):
        self.input_text((self.email_input[0], self.email_input[1]), email)

    def input_password(self, password):
        self.input_text((self.password_input[0], self.password_input[1]), password)

    def input_confirm_password(self, confirm_password):
        self.input_text((self.confirm_password_input[0], self.confirm_password_input[1]), confirm_password)

    def click_sign_up(self):
        self.click((self.signUp_button[0], self.signUp_button[1]))

    def verify_fullname(self):
        return self.get_text(self.fullname)

