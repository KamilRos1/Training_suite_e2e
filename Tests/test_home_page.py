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
        home_page.sessions_button.click()
        action = ActionChains(chrome_driver)
        action.move_to_element(
            home_page.find_session(TE_subsection).web_element
        ).perform()

        action.move_to_element(
            home_page.find_session(section).web_element
        ).click().perform()
        assert home_page.page_title.text() == section
