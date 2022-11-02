from ..Base.base_element import BaseElement
from ..Base.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = "https://training-suite.ppro.dev/login/"

    @property
    def user_name_input(self):
        return BaseElement(driver=self.driver, by=By.ID, value='id_username')

    @property
    def user_password_input(self):
        return BaseElement(driver=self.driver, by=By.ID, value='id_password')

    @property
    def sign_in_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//button[normalize-space()='Sign in']")

    @property
    def login_error_alert(self):
        return BaseElement(driver=self.driver, by=By.CSS_SELECTOR, value="div[role=alert]")
