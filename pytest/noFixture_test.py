from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = None


def setup_module(module):
    global driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.daraz.com.np/")


def teardown_module(module):
    driver.quit()


def test_google_title():
    assert driver.title == "Daraz"


def test_google_url():
    assert driver.current_url == "https://www.daraz.com.np/"
