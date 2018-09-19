from selenium.webdriver.common.by import By

from pages.signup_page import SignupPage
from utilities.common_functionalities import Common


class HomePage(Common):
    myAccount_drop_down = (By.XPATH, "//*[@id='collapse']//*[@id='li_myaccount']")
    signUp_link = (By.XPATH, "//*[@id='collapse']//*[contains(text(),' Sign Up')]")

    def click_my_account(self):
        self.click((self.myAccount_drop_down[0], self.myAccount_drop_down[1]))

    def click_register(self):
        self.click((self.signUp_link[0], self.signUp_link[1]))
        # return SignupPage()








