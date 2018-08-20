from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Constants
line_item_id = '6098417762938'


# Home page
driver.get('http://dev.unified.com:9000/')
driver.maximize_window()
driver.implicitly_wait(10)

# Login
driver.find_element(By.ID, 'email-login').send_keys('duy.nguyen@unified.com')
driver.find_element(By.NAME, 'password').send_keys('Unified@123')
driver.find_element(By.ID, 'submit').click()


# Access to test page
driver.get('http://dev.unified.com:9000/app/advertising/#/details/lineitem/fb36c4b1-2e06-4bdf-8205-b42a44a9c6b4')
wait = WebDriverWait(driver, 15)
wait.until(EC.invisibility_of_element_located((By.ID, 'loadingIcon')))
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[class="fa fa-spinner fa-spin"], .spinner')))

# # Verify status
# driver.find_element(By.CSS_SELECTOR,
#                     '#statusSwitch_{line_item_id_param}[disabled]'.format(line_item_id_param=line_item_id))
# if True:
#     print("Status is disabled")
# else:
#     print("Status is enabled")
#
#
# # Get Effective status value
# print(driver.find_element(By.CSS_SELECTOR,
#                           '#CampaignEffectiveStatus_{line_item_id_param}'.format(line_item_id_param=line_item_id)).text)
#
#
# # Get Campaign name
# print(driver.find_element(By.CSS_SELECTOR,
#                           '#campaignNameContainer_6098417762938 span span:not(.fa-external-link-square)').text)


# Get Adset number
adset_element = driver.find_element(By.CSS_SELECTOR,'[data-reactid*="adset_count_6098417762938"] span')

action = ActionChains(driver)
action.move_to_element(adset_element).perform()

print(adset_element.text)
