# В conftest-е все фикстуры

from selenium import webdriver
import pytest
import time

@pytest.fixture(name="WDI", autouse=True) # Фикстура по примеру урока от Александра
def webdriver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(name="auth") # Другой вариант фикстуры
def auth_traf():

    driver = webdriver.Chrome()

    driver.get("https://lk.staging.appgrade.pro/login")

    login_field = driver.find_element("xpath", "//input[@type='text']")
    password_field = driver.find_element("xpath", "//input[@type='password']")
    login_button = driver.find_element("xpath", "//button[@type='submit']")

    login_field.send_keys("kleisky")
    password_field.send_keys("V1asek!00700")
    login_button.click()

    time.sleep(2)

    assert driver.current_url == "https://lk.staging.appgrade.pro/campaign"

    yield driver

    driver.quit()
