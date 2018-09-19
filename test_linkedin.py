from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import *

driver = Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://www.linkedin.com/')
driver.maximize_window()

# Locator
login_field = (By.ID, 'login-email')
pwd_field = (By.ID, 'login-password')
submit_btn = (By.ID, 'login-submit')
profile_btn = (
By.XPATH, '//a[start-with(.,"tap-target"])')

name_field = (By.XPATH, '//h1[@class="pv-top-card-section__name Sans-26px-black-85%"]')
# Input Email Address
driver.find_element(login_field[0], login_field[1]).send_keys('bctuan271095@gmail.com')
# Input Password
driver.find_element(pwd_field[0], pwd_field[1]).send_keys('Weareoneso0')
# click submit
driver.find_element(submit_btn[0], submit_btn[1]).click()
# click onl Welcome Tuan to go to profile
profile = wait.until(EC.element_to_be_clickable((profile_btn[0], profile_btn[1])))
profile.click()

# Verify name
actual_name = wait.until(EC.presence_of_element_located((name_field[0], name_field[1]))).text
expected_name = 'Tuan Bui'

# actual_name= driver.find_element(name_field[0],name_field[1]).text
assert_that(actual_name, equal_to(expected_name), 'Verify the full name is correct')

