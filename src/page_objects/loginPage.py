from ..base.base_element import BaseElement
from ..base.base_page import BasePage
from selenium.webdriver.common.by import By
from ..test_data.login_data import before_login_url


class LoginPage(BasePage):
    url = before_login_url

    @property
    def user_name_input(self):
        return BaseElement(driver=self.driver, by=By.ID, value="id_username")

    @property
    def user_password_input(self):
        return BaseElement(driver=self.driver, by=By.ID, value="id_password")

    @property
    def sign_in_button(self):
        return BaseElement(
            driver=self.driver,
            by=By.XPATH,
            value="//button[normalize-space()='Sign in']",
        )

    @property
    def login_error_alert(self):
        return BaseElement(
            driver=self.driver, by=By.CSS_SELECTOR, value="div.alert-danger[role=alert]"
        )

    @property
    def login_to_see_page_alert(self):
        return BaseElement(
            driver=self.driver, by=By.CSS_SELECTOR, value="div.alert-info[role=alert]"
        )

    def log_in(self, username, password):
        self.user_name_input.sendText(username)
        self.user_password_input.sendText(password)
        self.sign_in_button.click()
