import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

FILE_UPLOAD_FIELD = ("xpath", "//input[@id='uploadFile']")

file_field = driver.find_element(*FILE_UPLOAD_FIELD)
file_field.send_keys(r"C:\Users\ttt\PycharmProjects\PythonProject\images\768х1024.jpg")
time.sleep(5)