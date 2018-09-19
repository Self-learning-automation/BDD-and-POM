from behave import *
from page_objects.homepage import HomePage


@given('I go to LinkedIn page')
def go_to_homepage(context):
    pass


@when('I input username as "{username}" in username field')
def input_username(context, username):
    context.home_page.input_username(username)


@when('I input password as "{password}" in password field')
def input_password(context, password):
    context.home_page.input_password(password)


@when('I click on login button')
def click_login(context):
    context.home_page.click_login()


@then('UserName of mine is displayed as "{name}"')
def verify_fullname(context, name):
    context.home_page.verify_login(name)
