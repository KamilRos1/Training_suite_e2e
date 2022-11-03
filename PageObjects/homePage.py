from ..Base.base_element import BaseElement
from ..Base.base_page import BasePage
from selenium.webdriver.common.by import By
from ..TestData.login_data import after_login_url


class HomePage(BasePage):
    ulr = after_login_url

    @property
    def training_suite_button(self):
        return BaseElement(
            driver=self.driver, by=By.CSS_SELECTOR, value=".navbar-header"
        )

    @property
    def sessions_button(self):
        return BaseElement(
            driver=self.driver,
            by=By.CSS_SELECTOR,
            value="a[data-original-title='Courses/Sessions']",
        )

    @property
    def materials_button(self):
        return BaseElement(
            driver=self.driver,
            by=By.CSS_SELECTOR,
            value="a[data-original-title='Materials']",
        )

    def find_element_in_dropdown(self, element):
        return BaseElement(
            driver=self.driver,
            by=By.XPATH,
            value=f"//li/a[contains(text(),'{element}')]",
        )

    @property
    def page_title(self):
        return BaseElement(
            driver=self.driver,
            by=By.CSS_SELECTOR,
            value="h2",
        )
