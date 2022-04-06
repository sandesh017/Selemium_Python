import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser_name = "firefox"
if browser_name == "chrome":
    driver = webdriver.Chrome(executable_path="C:\\browserdriver\\chromedriver.exe")


elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path="C:\\browserdriver\\geckodriver.exe")

elif browser_name == "edge":
    driver = webdriver.Edge(executable_path="C:\\browserdriver\\msedgedriver.exe")
else:
    print("Please pass the correct browser name : " + browser_name)
    raise Exception('driver is not found')

driver.implicitly_wait(10)
driver.get("https://www.sharesansar.com/login")

driver.find_element(By.XPATH, "//input[@id='email']").send_keys('sandeshpoudel017@sxc.edu.np')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('helloworld')
driver.find_element(By.XPATH, "//input[@value='Login']").click()

time.sleep(10)

driver.quit()