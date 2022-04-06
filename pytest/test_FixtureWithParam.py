""""Using Conftest.py"""

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import pytest
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


import pytest


@pytest.mark.usefixtures("init_driver")
class Test_Google():

    def test_google_title(self):
        self.driver.get("https://www.daraz.com.np/")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("https://www.daraz.com.np/")
        assert self.driver.current_url == "https://www.daraz.com.np/"
