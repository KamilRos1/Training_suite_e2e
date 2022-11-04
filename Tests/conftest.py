from pytest import fixture
from selenium import webdriver
from ..src.page_objects.loginPage import LoginPage
from ..src.test_data.login_data import correct_user


@fixture(scope="class")
def chrome_driver(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@fixture(scope="class")
def login(chrome_driver):
    login_page = LoginPage(driver=chrome_driver)
    login_page.go_to()
    login_page.log_in(correct_user.username, correct_user.password)
