from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

driver.get('https://www.daraz.com.np/')
driver.get_screenshot_as_file('daraz.png')

'''full screenshot'''
# make sure that you are running in headless mode

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('daraz1.png')
