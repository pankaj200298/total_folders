import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@id='userName'])[1]").send_keys("pankaj chanekar")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("demo@gamil.com")
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(" at cp , maharashtra")
driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys(" at navegaon , maharashtra")
driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()




time.sleep(5)