from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


def test_facebook():
    pathService = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=pathService)
    driver.get("https://www.facebook.com/")
    assert driver.title == 'Facebook - Log In or Sign Up'
    driver.quit()


def test_google():
    pathService = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=pathService)
    driver.get("https://www.google.com/")
    assert driver.title == 'Google'
    driver.quit()
