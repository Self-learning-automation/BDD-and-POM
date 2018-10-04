from pages.homepage import HomePage
from pages.signup_page import SignupPage


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context.browser = init_browser_session()
    context.homepage = HomePage(context.browser)
    context.signup_page = SignupPage(context.browser)
    context.browser.maximize_window()


def init_browser_session():
    from features.browsers.browsers import Browsers
    browser = Browsers().select_browser("Chrome")
    return browser


def after_scenario(context, scenario):
    # context.browser.quit()
    pass


def after_all(context):
    """
    Placeholder for any before feature hooks needed
    """
    pass
