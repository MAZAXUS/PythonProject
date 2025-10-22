import time
from selenium import webdriver
from selenium.webdriver import Keys

# ДЗ по передаче ключей в поля через локаторы

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

firstName_field_input = driver.find_element("xpath", "//input[@id='userName']")
firstName_field_input.clear()
firstName_field_input.send_keys("Maga")
time.sleep(3)
assert firstName_field_input.get_attribute("value") == "Maga", "Error in first name field"

userEmail_field = driver.find_element("xpath", "//input[@id='userEmail']")
userEmail_field.clear()
userEmail_field.send_keys("maga@mail.ru")
time.sleep(3)
assert userEmail_field.get_attribute("value") == "maga@mail.ru", "Error in user email field"

address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
address_field.clear()
address_field.send_keys("gagarina dom 10")
time.sleep(3)
assert address_field.get_attribute("value") == "gagarina dom 10", "Error in address field"

permanent_adress = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_adress.send_keys(Keys.CONTROL+"A")
time.sleep(3)
permanent_adress.send_keys(Keys.BACKSPACE)
permanent_adress.send_keys("Grozny")
time.sleep(3)
assert permanent_adress.get_attribute("value") == "Grozny", "Error in permanent address field"