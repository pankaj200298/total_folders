import time
from select import select
# from select import select_by
# from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, "(//input[@id='autosuggest'])[1]").send_keys("ind")
time.sleep(1)
#plural find_elements by replacing find_element
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
time.sleep(3)

for contry in countries :
    if contry.text == "India" :
        contry.click()
        break
time.sleep(4)
print(driver.find_element(By.XPATH, "(//input[@id='autosuggest'])[1]").get_attribute("value"))
assert driver.find_element(By.XPATH, "(//input[@id='autosuggest'])[1]").get_attribute("value") == "India"
