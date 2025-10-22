from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

driver.get("https://lk.staging.appgrade.pro/login")

# Страница авторизации

USER_NAME_FIELD = driver.find_element("xpath", "//input[@type='text']")
PASSWORD_FIELD = driver.find_element("xpath", "//input[@type='password']")
SIGN_IN = driver.find_element("xpath", "//button[@type='submit']")

USER_NAME_FIELD.send_keys("kleisky")
PASSWORD_FIELD.send_keys("V1asek!00700")
SIGN_IN.click()
assert driver.current_url == "https://lk.staging.appgrade.pro/campaigns"