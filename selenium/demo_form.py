import time
from select import select
# from select import select_by
# from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#python locator
# ID, Xpath, CCSelector , classname , name , linktext

driver.find_element(By.NAME, "email").send_keys("hello@gamil.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456789")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# driver.find_element(By.ID, "exampleFormControlSelect1")
#tagname.find_element(By.xpath, "//input[@submit"]
#static dropdown
# time.sleep(3)
dropdown = select(driver.find_element(By.ID,"exampleFormControlSelect1"))

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("02-20-1998")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]" ).send_keys("helloo pc")
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
#  css -- tagname(by.csselector, "[attribute ='value']")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("pankaj chanekar")
time.sleep(20)
assert "Success" in message