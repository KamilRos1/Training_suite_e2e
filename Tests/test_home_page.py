from ..src.page_objects.homePage import HomePage
from ..src.test_data.home_page_data import *
from pytest import mark
import time
from selenium.webdriver.common.action_chains import ActionChains


@mark.homePage
@mark.usefixtures("login")
class HomePageTests:
    @mark.parametrize("section", sections)
    def test_sessions(self, section):
        home_page = HomePage(driver=self.driver)
        action = ActionChains(self.driver)
        home_page.sessions_button.click()
        action.move_to_element(
            home_page.find_element_in_dropdown(TE_subsection).web_element
        ).perform()

        action.move_to_element(
            home_page.find_element_in_dropdown(section).web_element
        ).click().perform()
        assert home_page.page_title.text() == section

    @mark.parametrize("section, title", materials_param)
    def test_materials(self, section, title):
        action = ActionChains(self.driver)
        home_page = HomePage(driver=self.driver)
        home_page.materials_button.click()
        action.move_to_element(
            home_page.find_element_in_dropdown(section).web_element
        ).click().perform()
        assert home_page.page_title.text() == title
