from pytest import fixture
from selenium import webdriver
from .PageObjects.loginPage import LoginPage
from .TestData.login_data import correct_user


@fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@fixture()
def login(chrome_driver):
    login_page = LoginPage(driver=chrome_driver)
    login_page.go_to()
    login_page.log_in(correct_user.username, correct_user.password)
