import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 5)

driver.get("https://lk.staging.appgrade.pro/login")

# Страница авторизации

USER_NAME_FIELD = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Login']")))
PASSWORD_FIELD = driver.find_element(By.XPATH, "//input[@type='password']")
SIGN_IN = driver.find_element(By.XPATH, "//button[@type='submit']")

USER_NAME_FIELD.send_keys("kleisky")
PASSWORD_FIELD.send_keys("V1asek!00700")
SIGN_IN.click()
assert driver.current_url == "https://lk.staging.appgrade.pro/campaigns", "Не смог перейти на страницу"

time.sleep(5)