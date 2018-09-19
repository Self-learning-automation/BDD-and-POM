from behave import *
from hamcrest.core import assert_that
from hamcrest import equal_to
from page_objects.homepage import HomePage


@given('I go to LinkedIn page')
def go_to_homepage(context):
    context.driver.get('https://www.linkedin.com/')


@when('I input username as "{username}" in username field')
def input_username(context, username):
    HomePage(context.driver).input_username(username)


@when('I input password as "{password}" in password field')
def input_password(context, password):
    HomePage(context.driver).input_password(password)


@when('I click on login button')
def click_login(context):
    HomePage(context.driver).click_login()


@then('UserName of mine is displayed as "{name}"')
def verify_fullname(context, name):
    assert_that(HomePage(context.driver).get_user_name(), equal_to(name), 'Verify username is correct')
