import os

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.page = ''
        self.BASE_URL = os.environ['URL']
        self.driver.switch_to.frame()


    def current_url(self):
        return self.driver.current_url

    def load(self):
        with allure.step(f"Load the '{self.page}' page."):
            self.driver.get(self.correct_url())

    def correct_url(self):
        return self.BASE_URL + self.page

    def is_loaded(self):
        if not self.at_page():
            raise RuntimeError(f"The {self.page} page is not loaded properly")

    def get(self):
        try:
            if not self.at_page():
                self.load()
            self.is_loaded()
        except RuntimeError:
            self.load()
            self.is_loaded()
        return self

    def at_page(self) -> bool:
        return self.current_url() == self.correct_url()

    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Wait until the page url contains {1}")
    def wait_until_url_contains(self, url, time_out: int = 20):
        try:
            WebDriverWait(self.driver, time_out, 0.1).until(EC.url_contains(url))
        except TimeoutException:
            raise TimeoutException(f"After {time_out} seconds of wait the page url doens't contain {url}")