from behave import *
from pages.homepage import HomePage
from hamcrest import *


@given('User is in the php_travel page')
def go_to_homepage(context):
    context.browser.get("https://phptravels.net")


@when('the user click on My Account in the homepage')
def click_myaccount(context):
    context.homepage.click_my_account()


@step('the user click on Register in My Account')
def click_register(context):
    context.homepage.click_register()


@step('the user input first name as "{first_name}" in the sign up page')
def input_first_name(context, first_name):
    context.signup_page.input_first_name(first_name)


@step('the user input last name as "{last_name}" in the sign up page')
def input_last_name(context, last_name):
    context.signup_page.input_last_name(last_name)


@step('the user input phone as "{phone}" in the sign up page')
def input_phone(context, phone):
    context.signup_page.input_phone(phone)


@step('the user input email as "{email}" in the sign up page')
def input_email(context, email):
    context.signup_page.input_email(email)


@step('the user input password as "{password}" in the sign up page')
def input_password(context, password):
    context.signup_page.input_password(password)


@step('the user input confirm password as "{confirm_password}" in the sign up page')
def input_confirm_password(context, confirm_password):
    context.signup_page.input_confirm_password(confirm_password)


@step('the user click on Sign up button in the sign up page')
def click_sign_up(context):
    context.signup_page.click_sign_up()

@then('Verify redirect user to profile page, first nam  e as "{first_name}" and last name as "{last_name}" displays correctly')
def verify_signup_successfully(context, first_name, last_name):
    actual_text = context.signup_page.verify_fullname()
    expected_text = "Hi, " + first_name + " " + last_name
    assert_that(actual_text, equal_to(expected_text))

