from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.close()
