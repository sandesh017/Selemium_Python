import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class ParametrizeDemo:
    pass


class TestLogin(ParametrizeDemo):
    @pytest.mark.parametrize(
        "username,password",
        [
            ("sandesh@gmail.com", "123456"),
            ("poudel@gmail.com", "78910")
        ]
    )
    def test_login(self, username, password):
        self.driver.get("https://www.sharesansar.com/login")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
