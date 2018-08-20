
from selenium.webdriver.common.by import By
from page_objects.page import Page



class HomePage(Page):

    #Locator
    login_field = (By.ID, 'login-email')
    pwd_field = (By.ID, 'login-password')
    submit_btn = (By.ID, 'login-submit')

    def __init__(self,driver):
        Page.__init__(self,driver)

    def input_username(self,username,locator):
        self.input(locator,username)

    def input_password(self,password,locator):
        self.input(locator,password)

    def click_login(self,locator):
        self.click(locator)