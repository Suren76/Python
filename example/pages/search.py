from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from pages.basepage import BasePage


class DuckDuckGoSearchPage(BasePage):
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    page = 'search'

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Searching")
    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
