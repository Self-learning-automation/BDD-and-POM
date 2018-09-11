from behave import *

@given('User is in the php_travel page')
def go_to_homepage(context):
    context.browser.get("https://www.phptravels.net/")


# @step('the user click on My Account in the homepage')
# def click_my_account(context):
#     pass
#
#
# @step('the user click on Sign Up in My Account')
# def click_signup(context):
#     pass
#
#
# @step('the user input first name as "{first_name}" in the sign up page')
# def input_first_name(context, first_name):
#     pass
#
# # from behave import given, when, then, use_step_matcher
# # # use_step_matcher("re")
# @step('the user input last name as "{last_name}" in the sign up page')
# def input_last_name(context, last_name):
#     pass
#
#
# @step('the user input phone as "{phone}" in the sign up page')
# def input_phone(context, phone):
#     pass
#
#
# @step('the user input email in the sign up page')
# def input_email(context):
#     pass
#
# @step('')
# def input_password(context, password):
#     pass
#
# @step('')
# def input_confirm_password(context, confirm_password):
#     pass
#
# @when('')
# def click_signup_button(context):
#     pass
#
#
# @then('')
# def verify_signup_successfully(context, first_name, last_name):
#     pass