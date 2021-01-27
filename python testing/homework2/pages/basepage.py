import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.page_url = ''
        self.BASE_URL = os.environ['URL']

    def current_url(self):
        return self.driver.current_url

    def load(self):
        with allure.step(f"Load the '{self.page_url}' page."):
            self.driver.get(self.correct_url())

    def correct_url(self):
        return self.BASE_URL + self.page_url

    def is_loaded(self):
        if not self.at_page():
            raise RuntimeError(f"The {self.page_url} page is not loaded properly")

    def get(self):
        if not self.at_page():
            self.load()
        self.is_loaded()
        return self

    def at_page(self) -> bool:
        return self.current_url() == self.correct_url()

    def refresh_page(self):
        self.driver.refresh()

    SEARCH_INPUT = (By.NAME, 'sSearch')

    @allure.step("Searching")
    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        self.driver.find_element(By.CLASS_NAME, "main-search--button").click()

    def link_button(self, button_locat_xpath):
        self.get()
        elm = self.driver.find_element(By.XPATH, button_locat_xpath)
        elm.click()
