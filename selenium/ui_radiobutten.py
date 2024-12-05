import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
radiobutens = driver.find_elements(By.XPATH, "//input[@type='radio']")

print(len(radiobutens))

for butten in radiobutens:
    if butten.get_attribute("value") == "radio2":
        butten.click()
        assert butten.is_selected()
        break
time.sleep(2)