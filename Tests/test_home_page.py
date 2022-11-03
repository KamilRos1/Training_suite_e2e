from ..PageObjects.homePage import HomePage
from ..TestData.home_page_data import *
from pytest import mark
import time
from selenium.webdriver.common.action_chains import ActionChains


@mark.homePage
class HomePageTests:
    @mark.parametrize("section", sections)
    def test_sessions(self, chrome_driver, login, section):
        home_page = HomePage(driver=chrome_driver)
        action = ActionChains(chrome_driver)
        home_page.sessions_button.click()
        action.move_to_element(
            home_page.find_element_in_dropdown(TE_subsection).web_element
        ).perform()

        action.move_to_element(
            home_page.find_element_in_dropdown(section).web_element
        ).click().perform()
        assert home_page.page_title.text() == section

    @mark.parametrize("section, title", materials_param)
    def test_materials(self, chrome_driver, login, section, title):
        action = ActionChains(chrome_driver)
        home_page = HomePage(driver=chrome_driver)
        home_page.materials_button.click()
        action.move_to_element(
            home_page.find_element_in_dropdown(section).web_element
        ).click().perform()
        assert home_page.page_title.text() == title
