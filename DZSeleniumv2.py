import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com")

USER_NAME_FIELD = driver.find_element("xpath", "//input[@id='user-name']")
PASSWORD_FIELD = driver.find_element("xpath", "//input[@id='password']")
LOGIN_BUTTON = driver.find_element("xpath", "//input[@id='login-button']")
ADD_BACKPACK_ITEM = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
INVENTORY_BUTTON = driver.find_element("xpath", "//a[@data-test='shopping-cart-link']")
CHECKOUT_BUTTON = driver.find_element("xpath", "//button[@id='checkout']")
FIRST_NAME_CHECKOUT = driver.find_element("xpath", "//input[@id='first-name']")
LAST_NAME_CHECKOUT = driver.find_element("xpath", "//input[@id='last-name']")
POSTAL_CODE_CHECKOUT = driver.find_element("xpath", "//input[@id='postal-code']")
CONTINUE_BUTTON = driver.find_element("xpath", "//input[@id='continue']")
FINISH_BUTTON = driver.find_element("xpath", "//button[@id='finish']")

USER_NAME_FIELD.send_keys("standard_user")
PASSWORD_FIELD.send_keys("secret_sauce")
LOGIN_BUTTON.click()
assert driver.current_url == "https://www.saucedemo.com/inventory.html"

ADD_BACKPACK_ITEM.click()
INVENTORY_BUTTON.click()
assert driver.current_url == "https://www.saucedemo.com/cart.html"

CHECKOUT_BUTTON.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

FIRST_NAME_CHECKOUT.send_keys("Maga")
assert FIRST_NAME_CHECKOUT.get_attribute("value") == "Maga", "Error in first name field"

LAST_NAME_CHECKOUT.send_keys("Eld")
assert LAST_NAME_CHECKOUT.get_attribute("value") == "Eld", "Error in last name field"

POSTAL_CODE_CHECKOUT.send_keys("7777")
assert POSTAL_CODE_CHECKOUT.get_attribute("value") == "7777", "Error in postal code field"

CONTINUE_BUTTON.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

FINISH_BUTTON.click()

time.sleep(5)

driver.quit()