from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

# type="file"
driver.find_element(By.NAME, 'upfile').send_keys('C:\\Users\\DELL\\Desktop\\testing\\zLatest\\selenium\\fileUpload.py')

driver.find_element(By.XPATH, "//input[@type='submit']").click()
