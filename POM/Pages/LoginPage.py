from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """By locator"""
    EMAIL = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.XPATH, "//button[@id='loginBtn']")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions for login Page"""

    """this is used to get the page title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """This is used to check sign up link"""

    def is_sign_up_link_exit(self):
        return self.is_visible(self.SIGNUP_LINK)

    """this is used to login application """

    def do_login(self, username, password):
        self.do_send_key(self.EMAIL, username)
        self.do_send_key(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)
