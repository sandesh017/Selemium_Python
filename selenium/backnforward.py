from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

driver = webdriver.Firefox(service=Service((GeckoDriverManager().install())))
driver.implicitly_wait(10)

driver.get('https://www.daraz.com.np/')

driver.find_element(By.CSS_SELECTOR, '.purple').click()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)

driver.refresh()

driver.quit()