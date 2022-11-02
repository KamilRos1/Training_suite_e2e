from pytest import fixture
from selenium import webdriver


@fixture
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
