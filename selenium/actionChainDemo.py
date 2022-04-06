import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.alert import Alert


class ActionChainDemo:
    def mouse_hover(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get('https://www.daraz.com.np/#')
        achains = ActionChains(driver)
        firsthover = driver.find_element(By.XPATH, "//span[normalize-space()='Home & Lifestyle']")

        achains.move_to_element(firsthover).perform()
        time.sleep(3)
        secondhover = driver.find_element(By.XPATH, "//span[normalize-space()='Lighting']")
        achains.move_to_element(secondhover).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Outdoor Lighting']").click()
        driver.close()

    def right_click(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get('http://demo.guru99.com/test/simple_context_menu.html')
        achains = ActionChains(driver)
        rightClick = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        achains.context_click(rightClick).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
        time.sleep(2)
        Alert(driver).accept()
        driver.quit()

    def double_click(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get('http://demo.guru99.com/test/simple_context_menu.html')
        achains = ActionChains(driver)
        doubleClick = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(doubleClick).perform()
        time.sleep(2)
        Alert(driver).accept()
        time.sleep(2)
        driver.close()


demoActionChain = ActionChainDemo()
demoActionChain.mouse_hover()
demoActionChain.right_click()
demoActionChain.double_click()
