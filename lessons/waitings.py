import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

wait = WebDriverWait(driver, 6, poll_frequency=1) # Объект ожидания, где я использую модуль WebDriverWait, прокидываю для него аргументы, это: сам объект драйвера, таймаут (сколько буду ждать) и частоту опроса элемента

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']") # Константа переменной для элемента который будет виден через какое-то время, для нее прокидываю локатор элемента, далее буду использовать переменную без использования findElement

wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)) # Вызываю объект ожидания, использую метод until который означает что "жду пока...", прокидываю модуль expected_conditions (ожидаемые условия) как EC для удобства, и вызываю метод visibility_of_element_located и для него прокидываю константу локатора

#Такое же ожидание только для того что элемент будет кликабелен через какое-то время

# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/dynamic-properties")

# wait = WebDriverWait(driver, 6, poll_frequency=1)

# ENABLE_AFTER_BUTTON = ("xpath", "//button[@id='enableAfter']")

# wait.until(EC.element_to_be_clickable(ENABLE_AFTER_BUTTON))

# Документ где есть все нужные явные ожидания: https://docs.google.com/document/d/1Bjt5Q_5If458o-UbKlgEnAMmfx_RKC4GGsBm9zpk0Ts/edit?usp=sharing

