from ..PageObjects.loginPage import LoginPage
from ..TestData.login_data import *
from pytest import mark


@mark.skip
def test_sign_in_positive(chrome_driver):
    driver = chrome_driver
    login_page = LoginPage(driver=driver)
    login_page.go_to()
    login_page.user_name_input.sendText(correct_user.username)
    login_page.user_password_input.sendText(correct_user.password)
    login_page.sign_in_button.click()
    assert driver.current_url == 'https://training-suite.ppro.dev/', "Url didn't change, log in failed"


def test_sign_in_negative(chrome_driver):
    driver = chrome_driver
    login_page = LoginPage(driver=driver)
    login_page.go_to()
    login_page.user_name_input.sendText(incorrect_user.username)
    login_page.user_password_input.sendText(incorrect_user.password)
    login_page.sign_in_button.click()
    assert login_page.login_error_alert.checkVisibility()
