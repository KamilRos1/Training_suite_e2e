from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(self.url)
