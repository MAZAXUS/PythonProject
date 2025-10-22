import time
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument("--incognito")
# options.add_argument("--ignore-certificate-errors")
options.add_argument("--window-size=1920,1080")
# options.page_load_strategy = "eager"
# options.page_load_strategy = "normal"

driver = webdriver.Chrome(options=options)
driver.get("https://lk.staging.appgrade.pro/login")
time.sleep(3)
print(driver.title)