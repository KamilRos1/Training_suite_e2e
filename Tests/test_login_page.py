from ..PageObjects.loginPage import LoginPage
from ..TestData.login_data import *
import pytest
import time


@pytest.mark.usefixtures("chrome_driver")
@pytest.mark.login
class LoginTests:
    def test_sign_in_positive(self):
        login_page = LoginPage(driver=self.driver)
        login_page.go_to()
        login_page.log_in(correct_user.username, correct_user.password)
        assert (
            self.driver.current_url == after_login_url
        ), "Url didn't change, log in failed"

    def test_sign_in_negative(self):
        login_page = LoginPage(driver=self.driver)
        login_page.go_to()
        login_page.log_in(incorrect_user.username, incorrect_user.password)
        assert (
            login_page.login_error_alert.checkVisibility()
        ), "Login error alert didn't appear"
