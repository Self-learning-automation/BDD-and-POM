from selenium.webdriver import Chrome


def before_all(context):
   pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context.driver = Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()


def after_all(context):
    """
    Placeholder for any before feature hooks needed
    """
    pass
