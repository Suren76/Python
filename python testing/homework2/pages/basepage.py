import os

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.page = ''
        self.BASE_URL = os.environ['URL']

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

    def link_button(self, buttons_locat_xpath,time=10):
        self.get()
        elm = WebDriverWait(self.driver,time).until(EC.presence_of_element_located(By.XPATH , button_locat_xpath),'no element')
        elm.click()