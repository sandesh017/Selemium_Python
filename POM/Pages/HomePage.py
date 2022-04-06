from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.XPATH, "//h1[normalize-space()='User Guide']")
    ACCOUNT_ICON = (By.XPATH, "//button[@id='account-menu']//img[contains(@class,'nav-avatar')]")
    ACCOUNT_NAME = (By.CLASS_NAME, "user-info-name")
    SETTING_ICON = (By.XPATH, "//a[@id='navSetting']//*[name()='svg']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_visible(self.SETTING_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        self.do_click(self.ACCOUNT_ICON)
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)
